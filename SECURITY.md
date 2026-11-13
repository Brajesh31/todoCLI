# Security Policy

## Scope

todoCLI is a local command-line task manager. Its current design stores task records in a JSON file named `tasks.json` relative to the process working directory. It does not currently expose a network service or user authentication layer.

## Supported version

Security reports should identify the exact commit or version being used. The repository does not currently publish a formal release support matrix. Until releases are established, reports concerning the default branch should include the commit SHA where possible.

## Reporting a vulnerability

Please do not publish sensitive exploit details in a public issue. Contact the repository maintainer through the private security reporting option available on the GitHub repository. Include:

- A concise description of the issue.
- The affected commit or file.
- The Python version and operating system.
- Reproduction steps that do not expose private task data.
- The impact you believe an attacker or local user could achieve.
- Any suggested mitigation.

Allow reasonable time for investigation before public disclosure.

## Data and local security considerations

- Treat `tasks.json` as user data. It may contain personal task titles.
- Do not commit real task exports to the repository.
- Restrict filesystem permissions if the task file contains sensitive information.
- Back up the data file before manual edits or bulk operations.
- Avoid running the application with elevated privileges unless necessary.
- Do not load task files from untrusted sources without inspecting their contents.
- The current implementation does not provide encryption at rest, access control, audit logging, or concurrent-write protection.

## Dependency and supply-chain considerations

The current application code uses Python standard-library modules. If third-party dependencies are introduced, review their provenance, supported versions, update cadence, and security advisories. Pin or constrain dependencies appropriately and document the supported Python versions.

## Out-of-scope expectations

This project should not be represented as a secure multi-user task platform. It is a small local utility. Any future network, synchronization, account, or import/export feature will require a separate threat model and additional security controls.
