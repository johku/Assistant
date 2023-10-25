import unittest
from unittest.mock import patch
from assistant import AssistantApp

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

        self.app.add_task()
        self.app.delete_task()
        self.assertEqual(len(self.app.tasks), 0)

if __name__ == '__main__':
    unittest.main()
