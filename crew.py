from process import Process

class Crew:
    def __init__(self, agents, tasks, process_mode=Process.SEQUENTIAL):
        self.agents = agents
        self.tasks = tasks
        self.process = Process(mode=process_mode)

    def kickoff(self, input_data):
        return self.process.execute(self.tasks, input_data)
