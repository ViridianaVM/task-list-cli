from task_list_cli.task_list import TaskList

becca = task_list()

new_task = becca.create_task(title="learn flask", description="learn it")
print(new_task)

becca.list_tasks()

