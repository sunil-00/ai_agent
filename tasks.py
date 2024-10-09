import re
import yaml

class BaseTask:
    def __init__(self, task_config, agents):
        self.description = task_config['description']
        self.expected_output = task_config['expected_output']
        self.agents = agents

    def execute(self, input_data):
        agent_name = self.extract_agent_name()

        if agent_name not in self.agents:
            raise ValueError(f"Agent '{agent_name}' not found.")
        
        agent = self.agents[agent_name]

        task_input = self.description.format(game=input_data['game'])

        response = agent.act(task=task_input, context=input_data.get('context', ''))

        return response

    def extract_agent_name(self):
        if "check for errors" in self.description:
            return "qa_engineer_agent"
        elif "create" in self.description and "check for errors" not in self.description:
            return "senior_engineer_agent"
        elif "insure" in self.description:
            return "chief_qa_engineer_agent"
        else:
            raise ValueError("No suitable agent found for this task.")

def load_tasks(tasks_file, agents):
    with open(tasks_file, 'r', encoding='utf-8') as file:
        tasks_config = yaml.safe_load(file)

    tasks = {}
    for task_name, task_data in tasks_config.items():
        tasks[task_name] = BaseTask(task_data, agents)

    return tasks
