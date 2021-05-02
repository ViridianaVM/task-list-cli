from task_list_cli.task_list import TaskList

becca = TaskList()
print("*******")
print("Delete All Tasks")

all_tasks = becca.list_tasks()

for task in all_tasks:
    becca.get_task(id=task['id'])
    becca.delete_task()

print("*******")
print("Create 2 tasks")
print("*******")

new_task = becca.create_task(title="learn flask", description="learn it")
print("New Task 1: ", new_task)
new_task = becca.create_task(title="grade PSE 5", description="grade it")
print("New Task 2: ", new_task)

print("*******")
print("All tasks: ", becca.list_tasks())

print("*******")
print("Select task with title 'learn flask' ")
becca.get_task(title="learn flask")

print("*******")
print("Selected Task: ",becca.selected_task)


print("*******")
print("Delete Selected Task")

becca.delete_task()

print("*******")
print("All tasks: ", becca.list_tasks())