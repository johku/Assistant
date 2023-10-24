from datetime import datetime

class Task:
    def __init__(self, task_id, task_text, task_datetime):
        self.task_id = task_id
        self.task_text = task_text
        self.task_datetime = task_datetime

    def __str__(self):
        return f"Task {self.task_id}: {self.task_text} (Due at {self.task_datetime})"

    # Getter methods
    def get_task_id(self):
        return self._task_id

    def get_task_text(self):
        return self._task_text

    def get_task_datetime(self):
        return self._task_datetime

    # Setter methods
    def set_task_id(self, task_id):
        self._task_id = task_id

    def set_task_text(self, task_text):
        self._task_text = task_text

    def set_task_datetime(self, task_datetime):
        self._task_datetime = task_datetime