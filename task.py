from colorama import Fore, Back, Style
class ToDoList:
    # This is a todo list class
    # all methods related to the list will be in hre
    def __init__(self) -> None:
        self.task_details = {} # task_id: task_name pair
        # self.task_completed = {} # When completed it remove task from task details add it to task completed

    def add_task(self, task):
        # This function adds a task to the todo list
        key = len(self.task_details)
        self.task_details[key+1] = task
        print("Task added Successfully")

    def delete_task(self, task_id):
        # Deleting a particular key from the dictionary
        if task_id not in self.task_details.keys():
            print(Fore.YELLOW + "No Such task found")
            return
        del self.task_details[task_id]
        print(Fore.YELLOW + "Task deleted Successfully")

    def list_task(self):
        # This function lists all tasks in the todo list
        print(Fore.LIGHTGREEN_EX + "Task details")
        for i, task in self.task_details.items():
            print(Fore.GREEN + f"{i}. Title: {task}")