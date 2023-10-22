from datetime import datetime

class Task:
    def __init__(self, task_id, task_text, task_datetime):
        self.task_id = task_id
        self.task_text = task_text
        self.task_datetime = task_datetime

    def __str__(self):
        return f"Task {self.task_id}: {self.task_text} (Due at {self.task_datetime})"
