# Testing Guide

## Current test suite

The repository uses Python's built-in `unittest` framework. It does not require an external test dependency.

Run the suite from the repository root:

```bash
python -m unittest discover -s tests -v
```

The tests cover the Task model, status labels, task-manager persistence and selection behavior, and CLI smoke paths. Persistence tests use temporary working directories so they do not touch a developer's real `tasks.json`.

## Additional validation

```bash
python -m compileall -q src tests
cd src
python main.py --help
python main.py status
```

## Coverage map

| Area | Covered behavior |
|---|---|
| Task model | Dictionary serialization, status update, display output |
| Status mapping | Supported labels and unknown status behavior |
| Task manager | Empty store, load/save, next ID, status filter, range filter, update, delete |
| CLI | Help output, status output, add/list persistence across processes |
| File isolation | Tests use temporary directories |

## Important behavior captured by tests

- The task data file is relative to the process working directory.
- IDs start at 1 for an empty file and continue after the highest loaded ID.
- Range filters use Python's exclusive upper endpoint.
- Unknown status values currently map to an empty display label.
- The CLI writes task state to JSON after command dispatch.

These tests intentionally capture current behavior. If range semantics, validation, persistence location, or save behavior changes, update the tests and user documentation in the same change.

## Gaps to address

The current tests are a useful baseline, not exhaustive assurance. Future tests should cover malformed JSON, missing task fields, invalid status input, missing IDs, conflicting command arguments, permission errors, interrupted writes, and concurrent processes. Tests for file failures should use mocks or temporary directories.

## CI interpretation

The GitHub Actions workflow compiles the source, runs the unit tests, and exercises the CLI help and status commands. A passing workflow does not establish concurrency safety, data recovery, or correctness for every malformed input.
