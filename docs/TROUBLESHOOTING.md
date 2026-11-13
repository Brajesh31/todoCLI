# Troubleshooting

## Python command is not found

Confirm Python is installed and available on PATH:

```bash
python --version
```

On systems where the executable is named `python3`, use `python3` in the commands.

## Module import errors

The current source uses local imports such as `from task_manager import TaskManager`. Run the entry point from the `src` directory:

```bash
cd todoCLI/src
python main.py --help
```

## Tasks appear to be missing

The data filename is the relative path `tasks.json`. It is resolved from the process working directory. Check the directory from which the command was run and search for multiple copies of the file.

## JSON decoding error

The manager loads the entire JSON file during startup. Invalid JSON prevents normal loading. Stop all running instances, make a backup, and validate the file with a JSON parser before editing it. The expected top-level value is an array of task objects.

## Task fields are missing

Each task object must contain `num`, `title`, and `status`, with values compatible with the Task constructor. The current code does not perform a migration or comprehensive schema validation.

## A task has no visible status label

Only numeric values 1, 2, and 3 have labels. The current helper returns an empty string for unknown values. Review the stored record and use the supported status vocabulary.

## Range excludes the last ID

The range helper follows Python semantics: the end value is exclusive. To include ID 5, use an end value of 6.

## Changes disappear after multiple commands or instances

The application rewrites the full JSON collection and does not lock the file. Multiple instances can overwrite one another. Use one process at a time and keep backups. Concurrent-write safety is not currently implemented.

## Permission denied while saving

Check filesystem permissions for both the current working directory and the data file. Do not run the utility with elevated privileges as a workaround unless there is a specific, understood reason.

## Recovery checklist

1. Stop all running todoCLI processes.
2. Copy the current JSON file before attempting repairs.
3. Confirm which working directory contains the active file.
4. Validate JSON syntax and required fields.
5. Restore from a known-good backup if records are missing or corrupted.
6. Re-run the application using a disposable copy before replacing the original.
