# Contributing to todoCLI

Thank you for considering a contribution. The goal is to keep todoCLI understandable, reliable, and small enough that a developer can follow the complete command-to-storage flow without needing a large framework.

## Before opening a change

Read the main [README](README.md), the [architecture guide](docs/ARCHITECTURE.md), and the [development guide](docs/DEVELOPMENT.md). Check the existing implementation before proposing a new feature. In particular, understand that tasks are persisted to a relative `tasks.json` file and that ID ranges currently use Python's exclusive end boundary.

## Contribution principles

1. **Correctness before feature count.** Fix incorrect behavior and unclear edge cases before adding complexity.
2. **Keep the layers separate.** CLI parsing belongs in `main.py`; task collection and persistence belong in `task_manager.py`; per-task behavior belongs in `task.py`; status vocabulary belongs in `status.py`.
3. **Preserve user data.** Changes to JSON structure, IDs, or status values must include a compatibility plan.
4. **Document observable behavior.** Any change to a command, default, filter, or data path must be reflected in the README.
5. **Avoid unnecessary dependencies.** The current application relies on the Python standard library. Add dependencies only when they provide clear value.

## Local workflow

```bash
git clone https://github.com/Brajesh31/todoCLI.git
cd todoCLI
git switch -c docs-or-feature/short-description
cd src
python main.py --help
```

Run the application from `src/` so its local module imports resolve. Use a disposable directory or test data when validating persistence behavior.

## What to include in a pull request

A useful pull request description should explain:

- The problem or user need.
- The behavior before the change.
- The behavior after the change.
- Any command syntax or JSON format changes.
- Tests or manual verification performed.
- Compatibility risks for existing `tasks.json` files.
- Documentation updated.

Keep a pull request focused. A CLI feature, unrelated formatting changes, and a data migration should not be bundled together unless they are inseparable.

## Testing expectations

For changes to task operations, verify add, list, update, delete, status filtering, and range filtering. For persistence changes, verify that data survives a process restart and that malformed or inaccessible files fail in a clear way. For parser changes, inspect the generated help output and test missing or conflicting arguments.

Do not test against a personal task file. Use a temporary data location or disposable working copy.

## Reporting bugs

A useful bug report includes the Python version, operating system, exact command, current working directory, expected result, actual result, and a minimal example of the JSON data if persistence is involved. Remove private task titles or personal information before sharing logs or data.

## Security and privacy

Never commit API keys, passwords, personal task exports, machine-specific paths, or private data. If you discover a security issue, follow [SECURITY.md](SECURITY.md) rather than publishing exploit details in a public issue.

## Review standard

Contributions should be readable, narrowly scoped, and maintainable. A change is not complete merely because it works for one happy-path example. Consider empty lists, unknown IDs, invalid statuses, malformed JSON, range boundaries, and repeated runs.
