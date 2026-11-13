# Roadmap

This roadmap separates current implementation from possible future work. An item listed here is not a shipped feature or a delivery commitment.

## Current baseline

- [x] Add, list, update, and delete tasks from the terminal.
- [x] Filter tasks by status and numeric ID range.
- [x] Store task records in a local JSON file.
- [x] Separate CLI, task model, status vocabulary, and task manager modules.
- [x] Add baseline unit and CLI smoke tests.

## Reliability improvements

- [ ] Validate task status values at the CLI and manager boundaries.
- [ ] Improve parser validation for mutually exclusive selection arguments.
- [ ] Handle malformed JSON and missing fields with actionable errors.
- [ ] Write updates through a temporary file and atomic replacement.
- [ ] Add optional backup rotation before overwriting task data.
- [ ] Make the data-file path configurable without changing the default unexpectedly.
- [ ] Define behavior for concurrent invocations or explicitly prevent them.

## Usability improvements

- [ ] Decide whether range endpoints should remain exclusive or become inclusive, then keep help and tests aligned.
- [ ] Add clearer feedback when an ID does not exist.
- [ ] Add title search if a concrete user need justifies the added CLI surface.
- [ ] Consider a confirmation option for bulk deletion.

## Packaging and distribution

- [ ] Add project metadata only when a supported installation workflow is selected.
- [ ] Provide a console-script entry point if system-wide installation is introduced.
- [ ] Declare the supported Python version range.
- [ ] Establish tagged releases and a support policy.

## Data compatibility

- [ ] Introduce a versioned JSON format before adding fields that require migration.
- [ ] Add migration tests using representative older task files.
- [ ] Document backup and recovery behavior.

## Non-goals unless product scope changes

The current project is a small local CLI. A hosted multi-user service, account system, cloud synchronization, reminders, recurring tasks, and graphical interface would materially change its architecture and security requirements. They should not be added merely to increase the feature list.
