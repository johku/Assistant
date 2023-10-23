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
        self.tasks = {}
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
        date = input("Enter date dd:mm:yy: ")
        time = input("Enter time hh:mm: ")

        date_list = date.split(":")
        time_list = time.split(":")
        task_datetime = datetime(int(date_list[2]) + 2000, int(date_list[1]), int(date_list[0]), int(time_list[0]), int(time_list[1]))

        self.tasks[self.task_id] = (text, task_datetime)
        self.task_id += 1

        # Store task to tasks.csv
        self.handler.update_tasks(self.tasks)

    def delete_task(self):
        task_id = input("Enter task id: ")
        del self.tasks[task_id]
        self.handler.update_tasks(self.tasks)
        

    def print_tasks(self):
        if self.tasks == None:
            print("No tasks assigned")
            return

        for task in self.tasks:
            print(f'{task}: {self.tasks[task][0]} {self.tasks[task][1].strftime("%Y-%m-%d %H:%M")}')

    def load_tasks(self):
        tasks = self.handler.load_tasks()
        
        if tasks == None:
            return

        self.tasks = tasks

    def check_tasks(self):
        # format: (1, 'test', datetime.datetime(2023, 5, 15, 15, 0))

        while True:
            current_time = datetime.now()
            
            if self.tasks == None:
                return

            for id, values in self.tasks.items():
                if current_time.year == values[1].year and current_time.month == values[1].month and current_time.day == values[1].day and current_time.hour == values[1].hour and current_time.minute == values[1].minute:
                    self.engine.say(f"You have a task that requires your attention. The task is {values[0]}")
                    self.engine.runAndWait()
            
            time.sleep(45)

    def repeat_task():
        #create_next_task()
        pass

    def create_next_task():
        pass
        


    def main(self):
        # Load tasks from tasks.csv

        self.load_tasks()


        # Start a thread to continuously check tasks
        check_tasks_thread = threading.Thread(target=self.check_tasks)
        check_tasks_thread.daemon = True  # Allow the thread to exit when the main program exits
        check_tasks_thread.start()

        while True:
            print("Choose an option or use text to prompt ChatGPT")
            print("0: exit")
            print("1: add task")
            print("2: delete task")
            print("3: list tasks")
            print("-------------------------------------------")
            option = input("prompt: ")

            if option == "0":
                break
            elif option == "1":
                self.add_task()
            elif option == "2":
                self.delete_task()
            elif option == "3":
                self.print_tasks()
            else:
                self.get_response(option)

            # Check if there are any tasks that match current time here

            #time.sleep(30)




if __name__ == "__main__":
    assistant = AssistantApp()
    assistant.main()
