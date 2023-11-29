import os
import time
import threading
from dotenv import load_dotenv
import pyttsx3
import data_handler
from datetime import datetime
from datetime import timedelta
from task import Task

class AssistantApp:
    def __init__(self):
        # Initialize text to speech
        self.engine = pyttsx3.init()

        # Initialize tasks
        self.tasks = []
        self.task_id = 1
        self.handler = data_handler.DataHandler()

    def get_response(self, message):
        response = self.handler.ChatGPT(message)

        # Say the response with TTS
        print(response)
        self.engine.say(response)
        self.engine.runAndWait()

    def add_task(self):
        text = input("Enter task: ")
        repeats = input("Generate repeating task? yes/no: ")

        repeat_interval = None

        if repeats == 'yes':
            repeat_interval = int(input("Enter repeat interval (days): "))
            repeats = True
        else:
            repeats = False

        for attempt in range(3):
            try:
                date = input("Enter date dd:mm:yy: ")
                time = input("Enter time hh:mm: ")

                date_list = date.split(":")
                time_list = time.split(":")
                task_datetime = datetime(int(date_list[2]) + 2000, int(date_list[1]), int(date_list[0]), int(time_list[0]), int(time_list[1]))
                break
            except Exception as e:
                print("Incorrect time format, try again.")
                continue

        
        if repeat_interval == None:
            self.tasks.append(Task(self.task_id, text, task_datetime, repeats))
        else:
            self.tasks.append(Task(self.task_id, text, task_datetime, repeats, repeat_interval))

        self.task_id += 1

        # Store task to tasks.csv
        self.handler.update_tasks(self.tasks)
        return self.task_id - 1

    def delete_task(self, delete_id):
        
        for task in self.tasks:
            if task.task_id == delete_id:
                self.tasks.remove(task)

        self.handler.update_tasks(self.tasks)
        

    def print_tasks(self):
        if self.tasks == None:
            print("No tasks assigned")
            return

        print('*******************************************')

        for task in self.tasks:
            if task.task_reminder_added == True:
                print(f'{task.task_id}: REMINDER: {task.task_text} {task.task_datetime.strftime("%Y-%m-%d %H:%M")}')
            else:
                print(f'{task.task_id}: {task.task_text} {task.task_datetime.strftime("%Y-%m-%d %H:%M")}')

        print('*******************************************')

    def load_tasks(self):
        tasks = self.handler.load_tasks()
        
        if tasks == None or len(tasks) == 0:
            return

        self.tasks = tasks
    
        last_id = tasks[len(tasks) - 1].task_id
        self.task_id = last_id + 1

    def check_tasks(self):
        # format: (1, 'test', datetime.datetime(2023, 5, 15, 15, 0))

        while True:
            current_time = datetime.now()
            
            if self.tasks == None:
                return

            for task in self.tasks:
                if current_time.year == task.task_datetime.year and current_time.month == task.task_datetime.month and current_time.day == task.task_datetime.day and current_time.hour == task.task_datetime.hour and current_time.minute == task.task_datetime.minute:
                    print(task.task_text)
                    self.engine.say(f"You have a task that requires your attention. The task is {task.task_text}")
                    self.engine.runAndWait()
                                        
                    if task.task_repeats == True and task.task_repeat_added == False:                        
                        self.add_repeat_task(task)
                        task.task_repeat_added = True

                    if task.task_reminder_added == False:
                        task.task_datetime = task.task_datetime + timedelta(hours=1)
                        task.task_reminder_added = True
            
            # Possibly reduntant update tasks
            self.handler.update_tasks(self.tasks)
            time.sleep(45)

    def add_repeat_task(self, task):
        task_datetime = task.task_datetime + timedelta(days=task.task_repeat_interval)

        self.tasks.append(Task(self.task_id, task.task_text, task_datetime, task.task_repeats, task.task_repeat_interval))
        self.task_id += 1

        self.handler.update_tasks(self.tasks)


    def add_reminder(self, task):
        #self.handler.add_reminder()
        pass

    
    def clear_reminders(self):
        #self.handler.clear_reminders()
        pass

    def main(self):
        # Load tasks from tasks.csv
        self.load_tasks()

        # Start a thread to continuously check tasks
        check_tasks_thread = threading.Thread(target=self.check_tasks)
        check_tasks_thread.daemon = True  # Allow the thread to exit when the main program exits
        check_tasks_thread.start()

        while True:

            self.print_tasks()

            print("Choose an option or use text to prompt ChatGPT")
            print("0: exit")
            print("1: add task")
            print("2: delete task")
            print("3: list tasks")
            print("-------------------------------------------")
            option = input("prompt: ")

            
            if option == "0":
                self.handler.update_tasks(self.tasks)
                break
            elif option == "1":
                self.add_task()
            elif option == "2":
                delete_id = int(input("Enter task id: "))
                self.delete_task(delete_id)
            elif option == "3":
                continue
            else:
                self.get_response(option)




if __name__ == "__main__":
    assistant = AssistantApp()
    assistant.main()
