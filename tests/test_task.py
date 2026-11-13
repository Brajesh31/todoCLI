import sys
import unittest
from pathlib import Path
from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from task import Task
from status import Status, to_string


class TaskModelTests(unittest.TestCase):
    def test_task_serializes_expected_fields(self):
        task = Task(7, "Write tests", Status.InProgress.value)
        self.assertEqual(
            task.to_dict(),
            {"num": 7, "title": "Write tests", "status": 2},
        )

    def test_update_changes_status(self):
        task = Task(1, "Ship feature", Status.New.value)
        task.update(Status.Done.value)
        self.assertEqual(task.status, Status.Done.value)

    def test_status_labels_and_unknown_value(self):
        self.assertEqual(to_string(1).strip(), "New")
        self.assertEqual(to_string(2).strip(), "In Progress")
        self.assertEqual(to_string(3).strip(), "Done")
        self.assertEqual(to_string(99), "")

    def test_print_uses_status_label(self):
        task = Task(3, "Review PR", Status.Done.value)
        output = StringIO()
        with redirect_stdout(output):
            task.print()
        self.assertIn("3:", output.getvalue())
        self.assertIn("Done", output.getvalue())
        self.assertIn("Review PR", output.getvalue())


if __name__ == "__main__":
    unittest.main()
