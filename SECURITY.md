# Security Policy

## Supported Versions

Sky Frogs is pre-release; only the latest commit on `main` is supported. Once stable releases are published, this section will be updated with a version table.

## Reporting a Vulnerability

If you discover a security vulnerability in the Sky Frogs pack, **please do not open a public issue.** Use one of these private channels:

1. **GitHub Security Advisories** (preferred): visit the repo's [Security tab](https://github.com/Flatts3000/sky-frogs/security/advisories/new) and submit a draft advisory. This routes directly to the maintainer.
2. **Direct contact**: message the maintainer via the GitHub profile at [@Flatts3000](https://github.com/Flatts3000).

## What Counts

A modpack's threat surface is small but non-empty. Realistic concerns:

- **Malicious KubeJS scripts** — pack-shipped scripts that exfiltrate data, abuse file system access, or execute commands beyond their intended sandbox.
- **Recipe injection / progression bypasses** — KubeJS overrides or datapack JSONs that unintentionally allow item duplication, creative-mode access in survival, or other exploit shortcuts that bypass the intended progression. (Treated as a security issue when the bypass affects multiplayer servers.)
- **Server crashes / denial of service** — pack content (configs, KubeJS, datapack overrides) that causes a server to crash or hang on specific player actions.
- **Resource exhaustion** — pack-introduced loops, infinite recipes, or unbounded data structures that exhaust memory or CPU.
- **Supply chain** — a bundled mod's `pack.toml` entry pointing to the wrong jar (CDN poisoning, typo-squatted slug, etc.).

### What is NOT in scope here

These belong upstream — file with the relevant project, not this repo:

- A vulnerability in a bundled mod's own code → that mod's issue tracker.
- A vulnerability in Productive Frogs → [productive-frogs/security/advisories/new](https://github.com/Flatts3000/productive-frogs/security/advisories/new).
- A NeoForge / Minecraft client or server vulnerability → NeoForge / Mojang.

If you're unsure whether something qualifies, report it privately to us and we'll route it.

## Response Timeline

- **Acknowledgement**: within 7 days of receiving the report.
- **Initial assessment**: within 14 days.
- **Fix + disclosure**: timing varies by severity. Critical issues get a hotfix release on Modrinth + CurseForge; lower-severity issues land in the next regular release.

This is a hobby OSS project — timelines are best-effort, not contractual.

## Disclosure

We follow coordinated disclosure: report privately, we work on the fix, and we publish the advisory + fix together. We'll credit the reporter unless you request anonymity.
