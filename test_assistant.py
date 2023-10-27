import unittest
from datetime import datetime
from datetime import timedelta
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

        self.app.add_repeat_task(task)
        self.assertEqual(len(self.app.tasks), 1)

if __name__ == '__main__':
    unittest.main()
