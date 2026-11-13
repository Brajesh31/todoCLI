# todoCLI User Guide

## 1. What this guide covers

This guide explains how to operate the current todoCLI command-line application, how task records are stored, and how to avoid common data and command-line mistakes. It describes existing behavior rather than proposed features.

## 2. Start from the correct directory

The application modules live in `src/` and use local module imports. Run the program from that directory:

```bash
cd todoCLI/src
python main.py --help
```

The task data path is the relative filename `tasks.json`. The file is therefore created in the current working directory. If you run the command from another directory, you may see a different task list.

## 3. Create tasks

Use the `add` subcommand followed by a title:

```bash
python main.py add "Prepare weekly report"
python main.py add "Review pull request" 2
```

The optional numeric argument sets the initial status. When omitted, the CLI uses status 1. Use the supported values:

- 1: New
- 2: In Progress
- 3: Done

Titles should be quoted when they contain spaces. The program does not currently provide a dedicated interactive editor or rich-text title format.

## 4. View tasks

```bash
python main.py list
python main.py list --status 1
python main.py list --range 1 10
python main.py list --range 1 10 --status 2
```

The list command can show all records or filter by status and ID range. The implementation uses Python's range behavior, where the upper endpoint is excluded. Therefore `--range 1 10` selects IDs 1 through 9.

## 5. Change task status

```bash
python main.py upd 3 2
python main.py upd --range 1 5 3
python main.py upd --status_from 1 2
```

The first example changes task 3 to In Progress. The second changes IDs in the selected range to Done. The third selects tasks currently in New and changes them to In Progress. Consult `python main.py upd --help` for the parser's exact argument requirements.

## 6. Delete tasks

```bash
python main.py del 3
python main.py del --status 3
python main.py del --range 1 5
```

Deletion removes records from the in-memory collection and the next save rewrites the JSON file. There is no recycle bin or built-in undo for deletion. Back up `tasks.json` before bulk operations.

## 7. Understand task IDs

The manager calculates the next ID from the highest ID currently loaded plus one. IDs are not guaranteed to be globally unique across separate copies of the data file. If all records are deleted, the next run can begin again at ID 1.

Do not manually assign duplicate IDs in the JSON file. The current implementation does not provide a database constraint to prevent collisions in manually edited data.

## 8. Back up and move your tasks

To back up tasks, copy `tasks.json` while the application is not writing to it. To move tasks to another machine, copy the file into the working directory from which you will run the program.

Before restoring a backup, stop other instances of todoCLI. The application does not lock the file or merge concurrent changes.

## 9. Common problems

### Tasks seem missing

Check the current working directory and locate the `tasks.json` file there. A second copy of the application or a different terminal directory can result in a different data file.

### The last ID in a range is not included

The range upper endpoint is exclusive. Supply an endpoint one greater than the last ID you want to include.

### A task displays no status label

The saved numeric status may not be 1, 2, or 3. Use the supported values unless you are deliberately changing the status model.

### JSON parsing fails

Make a backup first. Inspect the file for missing commas, unmatched braces, or invalid field types. The expected record contains `num`, `title`, and `status`.

### Permission denied

Ensure the current user can read and write the working directory and `tasks.json`.

## 10. Current feature boundaries

The current application is a local task list. It does not include due dates, priorities, tags, projects, recurring tasks, notifications, accounts, cloud sync, encryption, or a graphical interface. These should not be assumed when planning workflows around the tool.
