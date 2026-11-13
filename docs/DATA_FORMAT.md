# todoCLI Data Format

## 1. Overview

todoCLI stores its task collection as JSON in a file named `tasks.json`. The filename is a relative path, so it is resolved against the process working directory rather than automatically against the repository root.

The file is the application's persisted task state. Treat it as user data.

## 2. Top-level structure

The expected top-level JSON value is an array. Each array element represents one task.

```json
[
  {
    "num": 1,
    "title": "Prepare weekly report",
    "status": 1
  },
  {
    "num": 2,
    "title": "Review pull request",
    "status": 2
  }
]
```

## 3. Field reference

| Field | Expected type | Purpose |
|---|---|---|
| `num` | Integer | Task identifier |
| `title` | String | Human-readable task title |
| `status` | Integer | Workflow state |

The current model reconstructs Task objects from dictionary keys. Renaming a key or changing its type can make existing data incompatible.

## 4. Status values

| Stored value | Meaning |
|---:|---|
| 1 | New |
| 2 | In Progress |
| 3 | Done |

Unknown values do not have a mapped display label in the current status helper. Avoid introducing new values without updating the enum, CLI validation, tests, and documentation together.

## 5. Identifier behavior

The manager computes the next identifier as one greater than the maximum existing ID. This is sufficient for a single process operating on one local file. It does not provide concurrency safety, distributed uniqueness, or protection against manually duplicated IDs.

## 6. Range selection behavior

The range filter uses Python range semantics. The upper bound is exclusive. This affects list, update, and delete operations that accept a range.

Example: a range from 2 to 6 selects IDs 2, 3, 4, and 5.

## 7. File lifecycle

On startup, the manager checks whether the relative data file exists. Existing records are loaded and converted into Task instances. After command dispatch, the current collection is serialized and written as formatted JSON.

This means read-oriented commands may also trigger a save in the current CLI lifecycle. A future persistence refactor could avoid writes for read-only operations.

## 8. Safe manual editing

If you edit the JSON file manually:

1. Stop all running todoCLI processes.
2. Copy the original file as a backup.
3. Use a JSON-aware editor.
4. Preserve the top-level array.
5. Keep all required keys and expected types.
6. Keep IDs unique.
7. Use only supported status values.
8. Validate the JSON before running the application again.

## 9. Known persistence limitations

- No file locking is implemented.
- No atomic temporary-file replacement is implemented.
- No automatic backup or version history is implemented.
- No schema version or migration system is implemented.
- No merge strategy exists for concurrent writers.
- Malformed JSON or missing fields can cause runtime errors.

## 10. Future compatibility guidance

If the task format changes, add a schema version and a migration path. Keep old files readable where practical, validate converted records, preserve backups, and test both the legacy and new formats. Do not silently discard unknown fields or records.
