# ------------------------------- Task Manager project ---------------------------------
# plan:
"""
1. - add task to list
2. - mark a task to complete
3. - view tasks
4. - Quit
pass ---> we use this when we build the program to don't display me error.
After you create this message you will create each function.
"""
# -----------------------------------------------------------------------------------
# Program:

def addTask():
    # get task from user.
    task = input("Enter task: ")
    # define task status.
    task_info = {"task": task, "completed": False}
    # add task to the list of tasks.
    if task_info not in tasks:
        tasks.append(task_info)
        print("Task added to list successfully")

# -------------------------------------------------
def mark_task_comlete():
    # get list of incomplete tasks.
    incomplete_tasks = [task for task in tasks if task["completed"] == False]
    if len(incomplete_tasks) == 0:
        print("No tasks to mark as complete")
        print(" ")
        return
    # show them to the user.
    for i, task in enumerate(incomplete_tasks):
        print(f"{i + 1}- {task['task']}")
        print('-'*30)
    try:    
        # get the task from the user.
        task_number = int(input("choose the task to complete: "))
        # I expect if user made  index error 
        if task_number < 1 or task_number > len(incomplete_tasks):
            print("Invalid Task Number")
            return
        # mark the task as completed
        incomplete_tasks[task_number-1]['completed'] = True   # this list contain a dictionary so, I write ['completed']
        # print(tasks)   # this list indicate to the same location in memory that incomplete list indicate it.
        print("Task marked completed")
    # # I expect if user made  value error     
    except ValueError:
        print("Invalid input, please enter a number.")  
        print(" ") 

# -------------------------------------------------       
def view_tasks():   
    if not tasks:
        print("No tasks to view")
        return 
    
    for i, task in enumerate(tasks):
        status = "✔" if task["completed"] else "❌"  # we use ternary operator 
        print(f"{i+1}. {task['task']} {status}")
        
# -------------------------------------------------
message = """1. - add task to list
2. - mark a task to complete
3. - view tasks
4. - Quit
"""
# list to store tasks
tasks = []

while True:
    print(message)
    choice = input("Enter your choice: ")

    if choice == "1":
        addTask()  # function calling
        
    elif choice == "2":
        mark_task_comlete()

    elif choice == "3":
        view_tasks()

    elif choice == "4":
        break
    else:
        print("Invalid choice, please enter a number between 1 and 4")