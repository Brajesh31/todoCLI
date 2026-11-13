import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"


class CliSmokeTests(unittest.TestCase):
    def run_cli(self, *args, cwd):
        env = os.environ.copy()
        env["PYTHONPATH"] = str(SRC)
        return subprocess.run(
            [sys.executable, str(SRC / "main.py"), *args],
            cwd=cwd,
            env=env,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_help_exits_successfully(self):
        result = self.run_cli("--help", cwd=ROOT)
        self.assertEqual(result.returncode, 0)
        self.assertIn("Todo CLI manager", result.stdout)

    def test_add_then_list_persists_in_working_directory(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            added = self.run_cli("add", "CLI test task", cwd=temp_dir)
            self.assertEqual(added.returncode, 0, added.stderr)
            self.assertTrue((Path(temp_dir) / "tasks.json").exists())

            listed = self.run_cli("list", cwd=temp_dir)
            self.assertEqual(listed.returncode, 0, listed.stderr)
            self.assertIn("CLI test task", listed.stdout)

    def test_status_command_lists_supported_values(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            result = self.run_cli("status", cwd=temp_dir)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("1 - New", result.stdout)
        self.assertIn("2 - In Progress", result.stdout)
        self.assertIn("3 - Done", result.stdout)


if __name__ == "__main__":
    unittest.main()
