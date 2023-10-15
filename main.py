from task import ToDoList

todolist = ToDoList()
while True:
    print("\nTodo List Menu:")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Completed")
    print("4. Quit")

    user_input = int(input("Enter option"))
    if user_input==2:
        todolist.list_task()
    pass