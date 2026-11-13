# todoCLI Development Guide

## 1. Audience

This guide is for developers who want to run, inspect, test, or extend todoCLI. It documents the repository's current Python source layout and the practical workflow for making safe changes.

## 2. Environment setup

The project currently uses Python standard-library modules. No dependency installation is required for the application as it exists today.

Recommended setup:

```bash
git clone https://github.com/Brajesh31/todoCLI.git
cd todoCLI
python --version
cd src
python main.py --help
```

Use a supported Python 3 release. If your operating system provides multiple Python versions, use `python3` instead of `python` in the commands.

## 3. Working-directory behavior

The data file is configured as the relative path `tasks.json`. This means the file is resolved from the current working directory. The source modules are under `src/`, and the current import style expects execution from that directory.

For normal local use:

```bash
cd todoCLI/src
python main.py add "First task"
python main.py list
```

Do not run the script from an unrelated directory unless you intentionally want the JSON file to be created there and have configured the Python import path accordingly.

## 4. Understanding the command interface

The command-line interface is built in `src/main.py`. Use `argparse` help rather than guessing the accepted argument combinations:

```bash
python main.py --help
python main.py add --help
python main.py del --help
python main.py upd --help
python main.py list --help
```

The current interface accepts numeric status values. The built-in mapping is 1 = New, 2 = In Progress, and 3 = Done.

## 5. Manual verification checklist

Until a dedicated automated test suite is included, use a disposable working directory and check the main user paths manually:

- Add a task without an explicit status.
- Add a task with each valid status.
- List all tasks.
- Filter by status.
- Filter by a range and confirm the exclusive upper bound.
- Update one task by ID.
- Update a group selected by current status.
- Update a group selected by ID range.
- Delete one task.
- Delete a group selected by status.
- Delete a group selected by range.
- Restart the application and confirm data persists.
- Run the status command and confirm labels are displayed.

Always test with disposable data. The application writes to `tasks.json` and can overwrite the file after each command.

## 6. Suggested automated test layout

A future test suite could use Python's built-in `unittest` or `pytest` if the project intentionally adopts that dependency. Suggested logical test groups:

| Test group | What to verify |
|---|---|
| Status | Enum values and text conversion |
| Task | Constructor, update, print formatting, dictionary output |
| Task manager | Loading, ID generation, add, update, delete, filters, save |
| CLI | Parser defaults, required subcommands, argument routing |
| Persistence | Valid JSON, empty file, malformed JSON, missing fields, permissions |

Persistence tests should patch or isolate the data path. They must not use a developer's real task file.

## 7. Code organization expectations

- Keep argument definitions and command routing in `main.py`.
- Keep task collection and persistence logic in `task_manager.py`.
- Keep per-task behavior in `task.py`.
- Keep status definitions and display mapping in `status.py`.
- Avoid introducing circular imports.
- Prefer small functions with explicit inputs and outputs.
- Validate user input before persisting it.
- Do not silently change JSON keys or status meanings.

## 8. Data compatibility

The current JSON representation stores `num`, `title`, and `status`. If a change modifies those keys or their types, existing user data may no longer load. Treat any data-shape change as a compatibility change.

A safe data migration should:

1. Identify the old schema.
2. Read the old data without modifying it in place.
3. Convert each record to the new schema.
4. Validate the converted collection.
5. Write the new file safely.
6. Preserve or recommend a backup of the original data.
7. Add tests for both old and new representations.

## 9. Performance expectations

The current list-based collection is appropriate for a small personal task list. Lookup and filtering operations scan the collection, so their cost grows linearly with the number of tasks. A database or indexed structure is unnecessary for the current scope unless the product requirements change materially.

## 10. Pull request checklist

Before proposing a change:

- [ ] The change has a clear user-facing or maintenance purpose.
- [ ] Existing commands continue to work unless a breaking change is intentional.
- [ ] Range semantics are tested.
- [ ] Persistence behavior is tested with temporary files.
- [ ] Error cases are considered.
- [ ] README command examples match the parser.
- [ ] Architecture documentation reflects any changed module responsibility.
- [ ] No personal task data, local JSON files, or secrets are committed.

## 11. Known constraints to preserve in documentation

Do not claim that todoCLI currently supports due dates, priorities, cloud sync, accounts, reminders, or a GUI. Do not claim that the project is packaged for installation as a system-wide command. These can be future goals, but the current source does not implement them.
