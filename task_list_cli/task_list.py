import requests
import datetime

class TaskList:
    def __init__(self, url="http://localhost:5000", selected_task=None):
        self.url = url
        self.selected_task = selected_task
    
    def create_task(self,title="Default Task",description="Default Description",completed_at=None):
        query_params = {
            "title": title,
            "description": description,
            "completed_at": completed_at
        }
        response = requests.post(self.url+"/tasks",json=query_params)
        return response.json()

    def list_tasks(self):
        response = requests.get(self.url+"/tasks")
        return response.json()

    def get_task(self, title=None, id=None):
        
        for task in self.list_tasks():
            if title:
                if task["title"]==title:
                    id = task["id"]
                    self.selected_task = task
            elif id == task["id"]:
                self.selected_task = task

        if self.selected_task == None:
            return "Could not find task by that name or id"

        response = requests.get(self.url+f"/tasks/{id}")
        return response.json()

    def update_task(self,title=None,description=None,completed_at=None):
        if not title:
            title = self.selected_task["title"]
        if not description:
            description = self.selected_task["description"]
        # if not completed_at:
        #     completed_at = self.selected_task["is_complete"]

        query_params = {
        "title": title,
        "description": description,
        "completed_at": completed_at
        }
        response = requests.put(
            self.url+f"/tasks/{self.selected_task['id']}",
            json=query_params
            )
        return response.json()

    def delete_task(self):
        response = requests.delete(self.url+f"/tasks/{self.selected_task['id']}")
        self.selected_task = None
        return response.json()
    
    def mark_complete(self):
        response = requests.patch(self.url+f"/tasks/{self.selected_task['id']}/mark_complete")
        return response.json()

    def mark_incomplete(self):
        response = requests.patch(self.url+f"/tasks/{self.selected_task['id']}/mark_incomplete")
        return response.json()
