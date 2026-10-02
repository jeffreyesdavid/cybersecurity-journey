# Gahto | Cybersecurity

**Aspiring Security Analyst | Breach Response · IoT Security · AI Security**

Self-taught security practitioner focused on protecting individuals and small businesses from scams, data breaches, and insecure devices. I bring 10 years of digital marketing and e-commerce experience and an insider's view of how attackers exploit social platforms.

## Focus
- **Breach Response & Scam Defense:** account recovery and hardening after data exposure
- **IoT / Camera Security:** securing small-business surveillance systems
- **AI Security:** LLM risks, prompt injection, OWASP Top 10 for LLMs
- **Cloud Security:** AWS secure configuration

## Portfolio
| Project | Skills | Status |
|---------|--------|--------|
| [tx-guard: Crypto Transaction Safety Checker](https://github.com/jeffreyesdavid/tx-guard) | Python, Ethereum, threat detection, transaction simulation, unit testing | Complete |
| [Incident Response: Personal Google Account](writeups/01-personal-account-incident-response.md) | Triage, credential rotation, session audit, MFA | Complete |
| Breach Response: Client A | OSINT, account hardening, credit freeze | Planned |
| Camera Security Audit | IoT, network segmentation, access control | Planned |
| Scam Defense Kit | Social engineering, awareness training | Planned |
| Home Lab: SIEM | Wazuh, log analysis, detection | Planned |

## Certifications
- [ ] CompTIA Security+
- [ ] AWS Certified Cloud Practitioner
- [x] Google Analytics · Google Ads · Meta Blueprint · HubSpot

## Ethics
All testing is performed on systems I own or have written permission to assess. Personal data is redacted.

## Progress Log
- **2026-10-02:** Built [tx-guard](https://github.com/jeffreyesdavid/tx-guard), a Python tool that checks crypto transactions before signing: matches 2,500+ known scam addresses, detects wallet-draining approvals, and simulates transactions on live Ethereum to show exact losses and hidden approvals. 37 automated tests.
- **2026-10-02:** Audited and rebuilt my [interactive resume](https://github.com/jeffreyesdavid/interactive-resume): removed my publicly exposed phone number (PII), fixed a broken deployment, cleared leftover AI-generated text, and retargeted it for fraud and security analyst roles.
- **2026-10-02:** Scoped a least-privilege GitHub token to one repo, then revoked and rotated it immediately after accidental exposure.
- **2026-10-01:** Built a Python password breach checker using the HIBP Pwned Passwords API. Uses k-anonymity, so the real password never leaves the machine. See [`scripts/pwcheck.py`](scripts/pwcheck.py).
- **2026-10-01:** Investigated a Google critical security alert on my own account: rotated credentials, audited sessions, checked for mailbox persistence. See [write-up](writeups/01-personal-account-incident-response.md).

## Connect
[LinkedIn](https://www.linkedin.com/in/jeffreyisdavid/) · [TryHackMe](https://tryhackme.com/p/gahtomahiko)
