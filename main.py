from dotenv import load_dotenv
load_dotenv()

from agents import load_agents
from crew import Crew
from tasks import load_tasks
import yaml


def main():
    agents = load_agents('config/agents.yaml')

    tasks = load_tasks('config/tasks.yaml', agents)

    gamedesigns = load_gamedesign('config/gamedesign.yaml')

    input_data = {
        'game': gamedesigns['example2_pacman']
    }

    crew = Crew(agents, tasks)

    results = crew.kickoff(input_data)

    print("\nFinal Results:")
    for task_name, result in results.items():
        print(f"Result for '{task_name}':\n{result}\n")

def load_gamedesign(gamedesign_file):
    with open(gamedesign_file, 'r', encoding='utf-8') as file:
        gamedesign_config = yaml.safe_load(file)

    return gamedesign_config
    
if __name__ == "__main__":
    main()