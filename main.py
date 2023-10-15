from task import ToDoList

todo = ToDoList()

while True:
    print("\nTodo List Menu:")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Completed")
    print("4. Quit")
    
    usr_input = int(input("Enter your choice"))

    if usr_input == 1:
        task_input = input("Enter the task details")
        todo.add_task(task_input)
    
    elif usr_input == 2:
        todo.list_task()

    elif usr_input == 3:
        i = int(input("Enter task id"))
        todo.delete_task(i)

    elif usr_input == 4:
        break