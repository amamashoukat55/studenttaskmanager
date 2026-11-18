
import unittest
from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        result = self.manager.add_task("Complete assignment")

        self.assertTrue(result)
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(
            self.manager.tasks[0]["title"],
            "Complete assignment"
        )

    def test_add_empty_task(self):
        result = self.manager.add_task("")

        self.assertFalse(result)
        self.assertEqual(len(self.manager.tasks), 0)

    def test_complete_task(self):
        self.manager.add_task("Study Python")

        result = self.manager.complete_task(1)

        self.assertTrue(result)
        self.assertTrue(self.manager.tasks[0]["completed"])

    def test_delete_task(self):
        self.manager.add_task("Delete this task")

        result = self.manager.delete_task(1)

        self.assertTrue(result)
        self.assertEqual(len(self.manager.tasks), 0)


if __name__ == "__main__":
    unittest.main()
