from task import ToDoList
from colorama import Fore, Back, Style

todo = ToDoList()

while True:
    print(Fore.WHITE,"\nTodo List Menu:")
    print(Fore.BLUE, "1. Add Task")
    print(Fore.BLUE, "2. List Tasks")
    print(Fore.BLUE, "3. Mark Task as Completed")
    print(Fore.BLUE, "4. Quit")
    
    usr_input = int(input(Fore.RED + "Enter your choice:"))

    if usr_input == 1:
        task_input = input(Fore.RED + "Enter the task details:")
        todo.add_task(task_input)
    
    elif usr_input == 2:
        todo.list_task()

    elif usr_input == 3:
        todo.list_task()
        i = int(input(Fore.RED + "Enter task id:"))
        todo.delete_task(i)

    elif usr_input == 4:
        break