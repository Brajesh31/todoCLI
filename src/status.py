from enum import Enum

class Status(Enum):
    New = 1
    InProgress = 2
    Done = 3

def to_string(status):
    mapping = {
        Status.New.value:           "New        ",
        Status.InProgress.value:    "In Progress",
        Status.Done.value:          "Done       "
    }
    return mapping.get(status, "")

