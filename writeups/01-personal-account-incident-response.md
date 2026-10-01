# Incident Response: Suspicious Activity Alert on a Personal Google Account

**Date:** 2026-10-01
**Type:** Account compromise investigation and hardening
**Scope:** My own Google account and devices
**Status:** Contained. Follow-up items open.

## Summary
Google raised a critical security alert reporting suspicious activity from one of my own Mac devices and automatically signed that session out. I ran a breach-exposure check, rotated credentials, audited active sessions and recovery settings, and checked the mailbox for attacker persistence. No evidence of ongoing unauthorized access was found.

## Detection
- **Alert:** "Suspicious activity in your account" (Google critical security alert)
- **Source:** Personal MacBook Pro, flagged as a device with suspicious activity
- **Automatic action:** Google signed the session out on that device
- **Date of alert:** 2026-09-04

## Investigation

| Check | Tool | Result |
|---|---|---|
| Email in known data breaches | Have I Been Pwned | 0 breaches found |
| Password exposure | `scripts/pwcheck.py` (HIBP Pwned Passwords API) | Tested; checker working |
| Active sessions | Google Account, Your devices | All sessions tied to my own devices and location |
| Recent security events | Google Account, Security activity | Reviewed |
| Mail forwarding rules | Gmail settings | No unauthorized forwarding |
| Mail filters | Gmail settings | No unauthorized filters |
| Second factor | Google Account, 2-Step Verification | Already enabled (authenticator app + passkey) |

## Containment and Remediation
1. Rotated the account password to a randomly generated one, stored in a password manager.
2. Reviewed every signed-in session across Mac, iPhone, and other devices.
3. Confirmed no forwarding addresses or filters that could silently exfiltrate mail.
4. Verified 2-Step Verification is enforced with an authenticator app and passkey rather than SMS.
5. Enabled HIBP breach notifications for the account email.

## Open Follow-ups
- [ ] Full malware scan of the flagged Mac
- [ ] Audit browser extensions on the flagged Mac
- [ ] Review third-party apps with Google account access
- [ ] Sign out stale sessions inactive for 60+ days
- [ ] Confirm both recovery phone numbers are current

## Lessons Learned
- **A clean breach check is not proof of safety.** HIBP returned 0 breaches, yet the account still triggered an alert. The threat came from the device, not a leaked password database.
- **Personal details make weak passwords.** Pet names, ages, and interests are easy to find through OSINT. Generated passwords remove that attack surface.
- **Attackers persist through mailbox rules.** Forwarding and filter checks belong in every account-compromise playbook.
- **Unused sessions are open doors.** Old logins should be signed out routinely.

## Skills Demonstrated
Incident triage · Credential rotation · Session auditing · Persistence checks · MFA verification · OSINT awareness · Documentation

*Identifying details such as phone numbers, email addresses, and exact device names are omitted.*
