import json
from pathlib import Path
from task import Task

DATA_FILE = "tasks.json"

def find(items, num):
    return next((i for i in items if i.num == num), None)

def filter_status(items, status):
    return [i for i in items if i.status == status]

def filter_range(items, num_range):
    return [i for i in items if i.num in num_range]

def print_items(collection):
    if len(collection) == 0:
        print("No Items")
        return

    for i in collection:
        i.print()


class TaskManager:

    def __init__(self):
        self.tasks = []
        self.index = 1

        if Path(DATA_FILE).is_file():
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                self.tasks = [Task(**t) for t in data]

            if self.tasks:
                self.index = max(t.num for t in self.tasks) + 1

    def save(self):
        tasks_data = [t.to_dict() for t in self.tasks]
        with open(DATA_FILE, "w") as f:
            json.dump(tasks_data, f, indent=2)

    def add(self, title, status):
        self.tasks.append(Task(self.index, title, status))
        self.index += 1

    def task_with_op(self, num, status, ranges, callback):
        if ranges is not None:
            items = filter_range(self.tasks, ranges)
            if status is not None:
                f_items = filter_status(items, status)
                for item in f_items:
                    callback(item)
                return

            for item in items:
                callback(item)
            return

        if status is not None:
            items = filter_status(self.tasks, status)
            for item in items:
                callback(item)
            return

        item = find(self.tasks, num)
        if item is not None:
            callback(item)

    def delete(self, num, status, ranges):
        self.task_with_op(num, status, ranges, lambda item: self.tasks.remove(item))

    def update(self, num, status, ranges, status_from):
       self.task_with_op(num, status_from, ranges, lambda item: item.update(status))

    def list(self, status, ranges):
        if ranges is not None:
            items = filter_range(self.tasks, ranges)
            if status is not None:
                f_items = filter_status(items, status)
                print_items(f_items)
                return

            print_items(items)
            return

        if status is not None:
            items = filter_status(self.tasks, status)
            print_items(items)
            return

        print_items(self.tasks)
