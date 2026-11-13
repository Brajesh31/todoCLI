# Release Checklist

## Product behavior

- [ ] Verify add, list, update, delete, and status commands.
- [ ] Verify status and range filters.
- [ ] Confirm command help matches actual parser arguments.
- [ ] Confirm range endpoint behavior is documented.
- [ ] Confirm missing IDs and invalid input behavior is understood.

## Data safety

- [ ] Test with a disposable `tasks.json`.
- [ ] Verify data survives process restart.
- [ ] Verify existing JSON records remain readable.
- [ ] Review any data format change and migration path.
- [ ] Confirm no personal task data is committed.
- [ ] Review backup and recovery instructions.

## Validation

- [ ] `python -m compileall -q src tests` succeeds.
- [ ] `python -m unittest discover -s tests -v` succeeds.
- [ ] CLI help and status smoke checks succeed.
- [ ] CI is green for the release commit.

## Repository maintenance

- [ ] README and docs reflect shipped behavior.
- [ ] CHANGELOG.md is updated.
- [ ] Security and contribution guidance is current.
- [ ] No unreviewed dependencies or generated artifacts are included.
- [ ] Release notes do not claim roadmap items as implemented.
