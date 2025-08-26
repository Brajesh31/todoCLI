from status import to_string

class Task:

    def __init__(self, num, title, status):
        self.num = num
        self.title = title
        self.status = status

    def print(self):
        print(f"{self.num}: [{to_string(self.status)}] '{self.title}'")

    def update(self, status):
        self.status = status

    def to_dict(self):
        return {
            "num": self.num,
            "title": self.title,
            "status": self.status
        }