import os
import csv
import openai
from dotenv import load_dotenv
from datetime import datetime
from datetime import timedelta
from task import Task

class DataHandler:
    def __init__(self):
        # Load enviroment variables from .env
        load_dotenv()
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    def ChatGPT(self, message):
        openai.api_key = self.OPENAI_API_KEY

        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ],
        max_tokens=500
        )

        return completion.choices[0].message.content
    

    def update_tasks(self, tasks):
        # original format: {1: ('test2', datetime.datetime(2023, 2, 14, 14, 0))}
        script_dir = os.path.dirname(__file__)
        file_name = os.path.join(script_dir, "tasks.csv")

        try:
            with open(file_name, mode='w', newline='') as file:
                pass
        except Exception as e:
            print(f"Error emptying the CSV file: {e}")

        for task in tasks:
            task_id = task.task_id

            task_text = task.task_text
            task_repeats = task.task_repeats
            task_repeat_interval = task.task_repeat_interval
            task_repeat_added = task.task_repeat_added
            task_reminder_added = task.task_reminder_added

            year = task.task_datetime.year
            month = task.task_datetime.month
            day = task.task_datetime.day
            hour = task.task_datetime.hour
            minute = task.task_datetime.minute

            data = [task_id, task_text, year, month, day, hour, minute, task_repeats, task_repeat_interval, task_repeat_added, task_reminder_added]

            try:
                with open(file_name, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(data)
            except Exception as e:
                print(f"Error writing to the CSV file: {e}")

    
    def load_tasks(self):
        # original format: (1, 'test', datetime.datetime(2023, 5, 15, 15, 0))
        try:
            script_dir = os.path.dirname(__file__)
            file_name = os.path.join(script_dir, "tasks.csv")

            tasks = []

            # Open the CSV file for reading
            with open(file_name, 'r') as file:
                # Create a CSV reader
                csv_reader = csv.reader(file)

                # Iterate through each row in the CSV file
                # Example row: ['1', 'test', '2023', '5', '15', '15', '0']
                for row in csv_reader:

                    task_datetime = datetime(int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6]))
                    task_id = row[0]
                    task_text = row[1]
                    task_repeats = row[7]
                    task_repeat_interval = row[8]
                    task_repeat_added = row[9]
                    task_reminder_added = row[10]

                    if task_repeat_added == 'True':
                        task_repeat_added = True
                    else:
                        task_repeat_added = False

                    if task_reminder_added == 'True':
                        task_reminder_added = True
                    else:
                        task_reminder_added = False

                    tasks.append(Task(int(task_id), task_text, task_datetime, task_repeats, int(task_repeat_interval), task_repeat_added, task_reminder_added))

            return tasks
        except Exception as e:
            print("No tasks to load")