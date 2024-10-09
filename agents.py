import yaml
from langchain.prompts.prompt import PromptTemplate
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools.render import render_text_description
from langchain_groq import ChatGroq
import tools
from langchain_core.tools.structured import StructuredTool
import os

MODEL = os.getenv("MODEL", "llama3-70b-8192")

class BaseAgent:
    def __init__(self, agent_config, tools_list=None):
        self.role = agent_config['role']
        self.goal = agent_config['goal']
        self.backstory = agent_config['backstory']
        self.llm = ChatGroq(model=MODEL)
        self.tools = tools_list or [getattr(tools, func_name) for func_name in dir(tools) if isinstance(getattr(tools, func_name), StructuredTool)]
        self.tool_names = render_text_description(list(self.tools))

        self.system_prompt = PromptTemplate.from_template("""
You are a {role}. Your goal is {goal}. 
{backstory}

Answer the following questions as best you can. You have access to the following tools:

{tool_names}

Use the following format:

Question: the input question you must answer
Thought: you should always think fast about what to do
Action: the action to take, should be one of [{tools}] (ignore if no tools are available or no action is needed)
Action Input: the input to the action
Observation: the result of the action
Note: if an action fails, do not repeat the same action more than 3 times

Example:
  Action: write_code_to_file
  Action Input: "def foo():\n    print('bar')\n"
  Observation: "Code successfully written to file."

... (this Thought/Action/Action Input/Observation can repeat up to 12 times) (if you can't come up with the answer within 12 attempts, just give the best answer you can)

Thought: I now know the final answer
Final Answer: the complete and correct answer to the input question, including full code, should be a self-contained single answer that is ready to be used in a codebase

Begin!

Context: {context}
Question: {task}
Thought: {agent_scratchpad}
        """)

        self.agent = create_react_agent(llm=self.llm, tools=self.tools, prompt=self.system_prompt)
        self.agent_executor = AgentExecutor(agent=self.agent, tools=self.tools, verbose=True, max_iterations=30, handle_parsing_errors=True)

    def act(self, task, context=''):
        agent_input = {
            "role": self.role,
            "goal": self.goal,
            "backstory": self.backstory,
            "tools": self.tools,
            "tool_names": self.tool_names,
            "task": task,
            "context": context
        }
        response = self.agent_executor.invoke(agent_input)
        return response['output'] if 'output' in response else ''
    
    def add_tool(self, tool):
        if isinstance(tool, list):
            self.tools.extend(tool)
        else:
            self.tools.append(tool)
        self.tool_names = render_text_description(list(self.tools))

def load_agents(agents_file):
    with open(agents_file, 'r', encoding='utf-8') as file:
        agents_config = yaml.safe_load(file)

    agents = {}
    for agent_name, agent_data in agents_config.items():
        agents[agent_name] = BaseAgent(agent_data)
    
    return agents
