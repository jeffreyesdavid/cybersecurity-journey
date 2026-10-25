# Exposure Review: AI Coding-Session Links in Public Git History

**Date:** 2026-10-25
**Type:** Proactive exposure assessment and repository hardening
**Scope:** Eight of my own public GitHub repositories
**Status:** Remediated. Preventive controls in place.

## Summary
A security engineer publicly disclosed that Claude Code appends a link to the originating AI session in every commit by default. A session's visibility is controlled separately: once set to Public, any signed-in account can read the full transcript, including every command run and any secret printed along the way. Sharing does not mint a new link, so a link already sitting in commit history goes live the moment the session is made public.

My portfolio is built largely with AI coding agents and published in public repositories, so I assessed my own exposure, scanned every repository for leaked credentials, disabled the behavior at its source, and added a control that blocks secrets before they are ever committed.

## Threat Model
| Element | Detail |
|---|---|
| Asset | AI session transcripts: commands, file contents, tokens or keys printed during work |
| Exposure path | Session link in a public commit, combined with a session later set to Public |
| Who can exploit it | Anyone who reads the repository and holds a free account |
| Likelihood | Low per session, but cumulative across every commit, and permanent once in history |
| Impact | Credential theft, unauthorized access to connected accounts |

**Key insight:** neither feature is a vulnerability on its own. The risk lives in the combination and in the defaults, a pattern worth recognizing well beyond this one tool.

## Investigation

| Check | Method | Result |
|---|---|---|
| Session links in commit history | `git log --all --grep` across every repository | 29 commits across 5 repositories carry session links |
| Secrets in full git history | gitleaks 8.30.1 on all eight repositories | 1 finding, triaged below |
| Sharing visibility | Session sharing settings | Repository-access requirement already enabled |

### Triage of the single finding
gitleaks flagged a `generic-api-key` match in a test file for tx-guard. Investigation showed the string was the **public USDC token contract address** used as test data, information published on every blockchain explorer. Classified as a **false positive**, then suppressed by fingerprint in `.gitleaksignore` with a documented justification, so the exception is auditable rather than silent.

## Remediation
1. **Disabled session links at the source.** Set `attribution.sessionUrl` to `false` (and cleared commit and PR attribution) in the global settings and in each repository's `.claude/settings.json`, which governs cloud sessions.
2. **Verified rather than assumed.** Public bug reports show the session trailer has persisted for some users despite the setting, so commit output is checked after the change.
3. **Kept historical sessions private.** Links already in history are harmless while their sessions remain private, so rewriting history was weighed against the cost of force-pushing and deliberately not pursued.
4. **Resolved diverged branches** (rebased onto remote commits made by cloud sessions) and pushed the fix to all eight repositories.

## Prevention
- **Pre-commit secret scanning.** Installed a gitleaks pre-commit hook in all eight repositories. Any staged key or token now blocks the commit before it can reach GitHub, including commits made by AI agents working locally.
- **Persistent tooling.** Moved the scanner out of a temporary directory so the control survives restarts.

## Residual Risk
- The hook only runs on my own machine. Commits made by cloud sessions rely on the repository-level settings rather than local scanning; adding gitleaks to CI would close that gap.
- Historical links remain in commit history. The control is that their sessions are never made public.

## Lessons Learned
- **Defaults are policy.** An attribution feature and a sharing feature, each reasonable alone, combine into a permanent exposure path when left at their defaults.
- **Treat anything an AI agent sees as potentially published.** Short-lived, least-privilege tokens limit the damage if a transcript ever leaks.
- **Triage before you panic.** A scanner hit is a lead, not a verdict. Confirming the false positive avoided an unnecessary key rotation and produced a documented, auditable exception.
- **Prevention beats detection.** Scanning history finds yesterday's leaks; a pre-commit hook stops tomorrow's.

## Skills Demonstrated
Threat modeling · Exposure assessment · Secret scanning (gitleaks) · False-positive triage · Secure configuration · Preventive controls · Git operations · Documentation

*Session identifiers, local paths and account details are omitted.*
