from task_list_cli.task_list import TaskList


options = {
    "1": "list tasks", 
    "2": "create task",
    "3": "select task", 
    "4": "update task", 
    "5": "delete task", 
    "6": "mark task complete",
    "7": "mark task incomplete",
    "8": "Delete All Tasks",
    "9": "list all options",
    "10": "Quit"
    }

def list_choices():
    print("What would you like to do?")
    print("**************************")
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    print("You must select a task before updating it, deleting it, marking it complete, or marking it incomplete.")

choice = None
valid_choices = options.keys()

task_list = TaskList(url="https://beccas-task-list-c15.herokuapp.com/")
play = True
list_choices()

while play==True:
    while choice not in valid_choices:
        print("What would you like to do? Select 9 to see all options again")
        choice = input("Make your selection using the option number: ")

    if choice in ['4','5','6','7'] and task_list.selected_task == None:
        print("You must select a task before updating it, deleting it, marking it complete, or marking it incomplete.")
        choice = "3"

    if choice=='1':
        print("Tasks:")
        print("**************************")
        for task in task_list.list_tasks():
            print(task)
    elif choice=='2':
        print("Great! Let's create a new task.")
        title=input("What is the title of your task? ")
        description=input("What is the description of your task? ")
        new_task = task_list.create_task(title=title, description=description)
        print("New task:", new_task)
    elif choice=='3':
        select_by = input("Would you like to select by title or id? ")
        if select_by=="title":
            title = input("Which task title would you like to select? ")
            task_list.get_task(title=title)
        elif select_by=="id":
            id = input("Which task id would you like to select? ")
            if isnumeric(id):
                id = int(id)
                task_list.get_task(id=id)
        else:
            print("Could not select. Please enter id or title.")
        
        if task_list.selected_task:
            print("Selected task: ", task_list.selected_task)

    elif choice=='4':
        print(f"Great! Let's update the task: {task_list.selected_task}")
        title=input("What is the new title of your task? ")
        description=input("What is the new description of your task? ")
        updated_task = task_list.update_task(title=title, description=description)
        print("Updated task:", updated_task)

    elif choice=='5':
        task_list.delete_task()
        print(task_list.list_tasks())
    elif choice=='6':
        response = task_list.mark_complete()
        print("Complete task: ", response)
    elif choice=='7':
        response = task_list.mark_incomplete()
        print("Incomplete task: ", response)
    elif choice=='8':
        for task in task_list.list_tasks():
            task_list.get_task(id=task['id'])
            task_list.delete_task()
        print("Deleted all tasks.")
    elif choice=='9':
        list_choices()
    elif choice=='10':
        play=False


    choice = None
    print("**************************")