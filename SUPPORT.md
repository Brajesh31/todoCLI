# Support

## Before requesting support

- Confirm the Python version and operating system.
- Run `python main.py --help` from the `src` directory.
- Check the current working directory because `tasks.json` is stored relative to it.
- Read the user guide and troubleshooting guide.
- Reproduce the issue with a disposable task file.

## Report a problem

Use the GitHub bug report template. Include the exact command, working directory, expected behavior, actual behavior, Python version, and sanitized error output.

Do not attach a personal `tasks.json` file without removing private task titles and other personal information.

## Data safety

Make a copy of `tasks.json` before bulk deletion or manual repair. The application does not include built-in undo, automatic backups, encryption, or concurrent-write protection.

## Security reports

For security concerns, follow [SECURITY.md](SECURITY.md). Do not publish private task data or exploit details in a public issue.
