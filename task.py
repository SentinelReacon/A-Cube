class ToDoList:
    def __init__(self) -> None:
        self.task_details = {} # task_id: task_name pair
        self.task_completed = {} # When completed it remove task from task details add it to task completed

    def add_task(self, task):
        pass

    def delete_task(self, task_id):
        pass

    def mark_complete(self, task_id):
        pass