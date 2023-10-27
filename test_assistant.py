import unittest
from datetime import datetime
from datetime import timedelta
from io import StringIO
from unittest.mock import patch
from assistant import AssistantApp
from task import Task

class TestAssistant(unittest.TestCase):
    def setUp(self):
        self.app = AssistantApp()  # Create an instance of the AssistantApp for testing

    @patch('builtins.input', side_effect=['test1', 'no', '23:05:23', '15:00'])
    def test_add_task(self, mock_input):
        # Use assert methods to check if the results match your expectations

        self.app.add_task()
        self.assertEqual(len(self.app.tasks), 1)

    @patch('builtins.input', side_effect=['test1', 'no','23:05:23', '15:00', '1'])
    def test_delete_task(self, mock_input):

        task_id = self.app.add_task()
        self.app.delete_task(task_id)
        self.assertEqual(len(self.app.tasks), 0)

    def test_add_repeat_task(self):
        task_datetime = datetime(2023, 5, 15, 15, 00)
        task = Task(1, 'test', task_datetime, True, 1)

        # Test that new datetime is added
        self.app.add_repeat_task(task)
        self.assertEqual(len(self.app.tasks), 1)

        # Test that datetime has increased
        later_datetime = datetime(2023, 5, 16, 15, 00)
        self.assertEqual(self.app.tasks[0].task_datetime, later_datetime)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_tasks(self, mock_stdout):
        # Create some tasks in the app
        self.app.tasks = [
            Task(1, "Task 1", datetime(2023, 5, 15, 15, 0), False, 0),
            Task(2, "Task 2", datetime(2023, 5, 16, 10, 30), False, 0)
        ]

        # Call the print_tasks method
        self.app.print_tasks()

        # Capture the printed output
        printed_output = mock_stdout.getvalue()

        # Define the expected output
        expected_output = "1: Task 1 2023-05-15 15:00\n2: Task 2 2023-05-16 10:30\n"

        # Assert that the printed output matches the expected output
        self.assertEqual(printed_output, expected_output)

if __name__ == '__main__':
    unittest.main()
