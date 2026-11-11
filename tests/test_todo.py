import sys
import json
from pathlib import Path
import pytest

# Ensure src is on sys.path
SRC_DIR = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(SRC_DIR))

import task_manager
from task_manager import TaskManager
from status import Status, to_string


@pytest.fixture(autouse=True)
def isolated_data_file(tmp_path, monkeypatch):
    """Isolate tasks.json into a temporary path for each test."""
    temp_file = tmp_path / "tasks.json"
    monkeypatch.setattr(task_manager, "DATA_FILE", str(temp_file))
    yield temp_file


def test_task_manager_add_and_persistence(isolated_data_file):
    """Tests adding tasks with Unicode titles and saving to disk."""
    tm = TaskManager()
    tm.add("Buy groceries 🍎", Status.New.value)
    tm.add("Write clean code 🚀", Status.InProgress.value)
    tm.save()

    # Verify JSON content on disk
    assert isolated_data_file.exists()
    content = isolated_data_file.read_text(encoding="utf-8")
    data = json.loads(content)
    assert len(data) == 2
    assert data[0]["title"] == "Buy groceries 🍎"
    assert data[0]["num"] == 1
    assert data[1]["title"] == "Write clean code 🚀"
    assert data[1]["num"] == 2

    # Verify loading back from disk
    tm2 = TaskManager()
    assert len(tm2.tasks) == 2
    assert tm2.index == 3


def test_task_manager_update_status():
    """Tests updating a task's status."""
    tm = TaskManager()
    tm.add("First task", Status.New.value)
    assert tm.tasks[0].status == Status.New.value

    tm.update(num=1, status=Status.Done.value, ranges=None, status_from=None)
    assert tm.tasks[0].status == Status.Done.value


def test_task_manager_delete_task():
    """Tests deleting a task by ID."""
    tm = TaskManager()
    tm.add("Task 1", Status.New.value)
    tm.add("Task 2", Status.New.value)
    assert len(tm.tasks) == 2

    tm.delete(num=1, status=None, ranges=None)
    assert len(tm.tasks) == 1
    assert tm.tasks[0].num == 2


def test_status_to_string_mapping():
    """Tests status enum to human string representations."""
    assert "New" in to_string(Status.New.value)
    assert "In Progress" in to_string(Status.InProgress.value)
    assert "Done" in to_string(Status.Done.value)
    assert to_string(999) == ""
