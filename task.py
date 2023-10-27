from datetime import datetime

class Task:
    def __init__(self, task_id, task_text, task_datetime, task_repeats, task_repeat_interval=0):
        self.task_id = task_id
        self.task_text = task_text
        self.task_datetime = task_datetime
        self.task_repeats = task_repeats
        self.task_repeat_interval = task_repeat_interval
        self.task_repeat_added = False

    def __str__(self):
        return f"Task {self.task_id}: {self.task_text} (Due at {self.task_datetime})"

    def __eq__(self, other):
        # Define the equality comparison for Task objects
        if isinstance(other, Task):
            # Compare task_id
            return self.task_id == other.task_id and self.task_datetime == other.task_datetime
        return False

    # Getter methods
    def get_task_id(self):
        return self.task_id

    def get_task_text(self):
        return self.task_text

    def get_task_datetime(self):
        return self.task_datetime
    
    def get_task_repeats(self):
        return self.task_repeats

    # Setter methods
    def set_task_id(self, task_id):
        self.task_id = task_id

    def set_task_text(self, task_text):
        self.task_text = task_text

    def set_task_datetime(self, task_datetime):
        self.task_datetime = task_datetime

    def set_task_repeats(self, task_repeats):
        self.task_repeats = task_repeats