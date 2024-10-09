class Process:
    SEQUENTIAL = 'sequential'
    PARALLEL = 'parallel'

    def __init__(self, mode=SEQUENTIAL):
        self.mode = mode

    def execute(self, tasks, input_data):
        if self.mode == self.SEQUENTIAL:
            results = {}
            for task_name, task in tasks.items():
                try:
                    print(f"Executing task: {task_name}")
                    result = task.execute(input_data)
                    results[task_name] = result
                    input_data['context'] = result
                    print(f"Task '{task_name}' completed successfully.")
                except Exception as e:
                    print(f"Error executing task '{task_name}': {e}")
            return results
        else:
            raise NotImplementedError("Parallel execution is not implemented yet.")
