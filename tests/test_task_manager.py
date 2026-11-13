import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from task_manager import TaskManager


class TaskManagerTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.previous_cwd = os.getcwd()
        os.chdir(self.temp_dir.name)

    def tearDown(self):
        os.chdir(self.previous_cwd)
        self.temp_dir.cleanup()

    def test_empty_store_starts_with_first_id(self):
        manager = TaskManager()
        self.assertEqual(manager.tasks, [])
        self.assertEqual(manager.index, 1)

    def test_add_save_and_reload(self):
        manager = TaskManager()
        manager.add("First task", 1)
        manager.add("Second task", 2)
        manager.save()

        with open("tasks.json", encoding="utf-8") as data_file:
            saved = json.load(data_file)

        self.assertEqual(saved[0], {"num": 1, "title": "First task", "status": 1})
        self.assertEqual(saved[1], {"num": 2, "title": "Second task", "status": 2})

        reloaded = TaskManager()
        self.assertEqual([task.num for task in reloaded.tasks], [1, 2])
        self.assertEqual(reloaded.index, 3)

    def test_next_id_uses_highest_existing_id(self):
        with open("tasks.json", "w", encoding="utf-8") as data_file:
            json.dump([
                {"num": 2, "title": "Two", "status": 1},
                {"num": 9, "title": "Nine", "status": 3},
            ], data_file)

        manager = TaskManager()
        self.assertEqual(manager.index, 10)

    def test_list_filters_by_status(self):
        manager = TaskManager()
        manager.add("New item", 1)
        manager.add("Done item", 3)
        output = StringIO()
        with redirect_stdout(output):
            manager.list(3, None)
        self.assertIn("Done item", output.getvalue())
        self.assertNotIn("New item", output.getvalue())

    def test_range_uses_exclusive_end(self):
        manager = TaskManager()
        for title in ("one", "two", "three", "four"):
            manager.add(title, 1)
        output = StringIO()
        with redirect_stdout(output):
            manager.list(None, range(2, 4))
        self.assertIn("two", output.getvalue())
        self.assertIn("three", output.getvalue())
        self.assertNotIn("four", output.getvalue())

    def test_update_by_id_and_delete_by_id(self):
        manager = TaskManager()
        manager.add("Keep", 1)
        manager.add("Change then remove", 1)
        manager.update(2, 3, None, None)
        self.assertEqual(manager.tasks[1].status, 3)
        manager.delete(2, None, None)
        self.assertEqual([task.title for task in manager.tasks], ["Keep"])

    def test_delete_by_status(self):
        manager = TaskManager()
        manager.add("Open", 1)
        manager.add("Finished", 3)
        manager.delete(None, 3, None)
        self.assertEqual([task.title for task in manager.tasks], ["Open"])

    def test_list_empty_collection(self):
        manager = TaskManager()
        output = StringIO()
        with redirect_stdout(output):
            manager.list(None, None)
        self.assertIn("No Items", output.getvalue())


if __name__ == "__main__":
    unittest.main()
