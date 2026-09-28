# Security Policy

## Supported versions

| Version | Supported |
| ------- | --------- |
| `main`  | Yes       |

## Reporting a vulnerability

Please **do not** open a public GitHub issue for security problems.

Report privately via:

- [GitHub private security advisory](https://github.com/YukaC/ArtGraph/security/advisories/new) for this repository, or
- Email: **agusyuk25@gmail.com**

Include steps to reproduce and impact if known. We aim to acknowledge reports within a few business days.

## Scope

ArtGraph is a local Python script that runs `git` subprocesses and modifies global Git identity settings. Reports about unsafe command invocation, path traversal, or unintended modification of user Git config are in scope. Abuse of contribution-graph patterns on third-party services is a policy matter for those platforms, not this repo’s code alone.
