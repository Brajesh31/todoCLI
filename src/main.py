import argparse

from task_manager import TaskManager


def setup():
    parser = argparse.ArgumentParser(prog="todoCLI", description="Todo CLI manager")
    sub = parser.add_subparsers(dest="cmd", required=True)

    add = sub.add_parser("add", help="Add new task, optionally with status")
    add.add_argument("title", help="Task title")
    add.add_argument("status", type=int, nargs="?", default=1, help="Optional status (default 1)")

    delete = sub.add_parser("del", help="Delete task(s)")
    delete.add_argument("index", type=int, nargs="?", help="ID of task to delete")
    delete.add_argument("--status", type=int, help="Delete tasks with this status")
    delete.add_argument("--range", type=int, nargs=2, metavar=("START", "END"), help="Delete tasks in this ID range")

    upd = sub.add_parser("upd", help="Update task status")
    upd.add_argument("index", type=int, nargs="?", help="ID of task to update")
    upd.add_argument("status", type=int, nargs="*", help="New status (1 or 2 integers for range)")
    upd.add_argument("--range", type=int, nargs=2, metavar=("START", "END"), help="Range of IDs to update")
    upd.add_argument("--status_from", type=int, help="Update tasks with this current status")

    lst = sub.add_parser("list", help="List tasks")
    lst.add_argument("--status", type=int, help="Filter by status")
    lst.add_argument("--range", type=int, nargs=2, metavar=("START", "END"), help="Filter by ID range")

    sub.add_parser("status", help="Show available statuses")

    return parser


def show_statuses():
    print("1 - New")
    print("2 - In Progress")
    print("3 - Done")


def main():
    parser = setup()
    args = parser.parse_args()

    task_manager = TaskManager()

    if args.cmd == "add":
        task_manager.add(args.title, args.status)
    elif args.cmd == "del":
        task_manager.delete(args.index, args.status, args.range)
    elif args.cmd == "upd":
        new_status = args.status[0] if args.status else None
        task_manager.update(args.index, new_status, args.range, args.status_from)
    elif args.cmd == "list":
        task_manager.list(args.status, args.range)
    elif args.cmd == "status":
        show_statuses()

    task_manager.save()

if __name__ == "__main__":
    main()