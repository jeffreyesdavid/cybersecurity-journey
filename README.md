# Jeffrey David | Cybersecurity Journey

**Aspiring Fraud & Security Analyst | Scam defense · Incident response · Python**

Self-taught security practitioner focused on stopping fraud and scams, and protecting individuals and small businesses from data breaches and insecure devices. I bring 10 years of digital marketing and e-commerce experience and an insider's view of how attackers exploit social platforms.

## Focus
- **Fraud & Scam Defense:** spotting scams before money moves (see tx-guard), awareness for everyday users
- **Incident Response:** account recovery, credential rotation and hardening after data exposure
- **IoT / Camera Security:** securing small-business surveillance systems
- **AI Security:** LLM risks, prompt injection, OWASP Top 10 for LLMs
- **Cloud Security:** AWS secure configuration

## Portfolio
| Project | Skills | Status |
|---------|--------|--------|
| [tx-guard: Crypto Transaction Safety Checker](https://github.com/jeffreyesdavid/tx-guard) | Python, Ethereum, threat detection, transaction simulation, unit testing, Streamlit web app | Complete · [Try it live →](https://txguard-jeffrey.streamlit.app) |
| [beat-guard: Beat Fingerprinting & Theft Detection](https://github.com/jeffreyesdavid/beat-guard) | Python, audio fingerprinting, SHA-256, blockchain timestamps, evidence reporting | Complete |
| [VPN Guardian: Personal Security Agent](https://github.com/jeffreyesdavid/vpn-guardian) | Bash, network security, VPN/routing, leak detection, local AI (Ollama), GitHub Pages | v1.1 shipped · [Project site →](https://jeffreyesdavid.github.io/vpn-guardian/) |
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
- **2026-10-03:** Built and shipped [VPN Guardian](https://github.com/jeffreyesdavid/vpn-guardian) ([project site](https://jeffreyesdavid.github.io/vpn-guardian/)), a macOS agent that checks every 30 seconds that my VPN is actually working: it catches VPN drops, IP leaks and route leaks, alerts my laptop and phone, and has a local AI model (Ollama) explain each alert in plain English so no data leaves the machine. Wrote a v0→v6 roadmap toward a self-hosted WireGuard VPN and a home SOC.
- **2026-10-03:** Revoked and replaced a GitHub token after pasting it into a visible username prompt, then pushed again with the token only entered at the hidden password prompt.
- **2026-10-03:** Expanded a fine-grained GitHub token's access one repository at a time instead of granting it all repos, keeping automation access least-privilege.
- **2026-10-03:** Shipped a [live web demo of tx-guard](https://txguard-jeffrey.streamlit.app) so anyone can check a transaction or address in the browser with no install. Added an animated terminal demo to the README showing it catch three common wallet-draining scams, and fixed a broken clone URL in the setup instructions.
- **2026-10-02:** Hardened tx-guard's input validation after a mistyped test input produced misleading output: malformed transaction data is now rejected with a clear error instead of being silently misread.
- **2026-10-02:** Built [beat-guard](https://github.com/jeffreyesdavid/beat-guard) ([project page](https://jeffreyesdavid.github.io/beat-guard/)), a Python tool that fingerprints music producers' beats, timestamps them on Bitcoin, and finds them inside other songs, even under vocals, MP3 compression, or a sped-up disguise. Produces a shareable evidence report. 10 end-to-end tests.
- **2026-10-02:** Built [tx-guard](https://github.com/jeffreyesdavid/tx-guard), a Python tool that checks crypto transactions before signing: matches 2,500+ known scam addresses, detects wallet-draining approvals, and simulates transactions on live Ethereum to show exact losses and hidden approvals. 37 automated tests.
- **2026-10-02:** Audited and rebuilt my [interactive resume](https://github.com/jeffreyesdavid/interactive-resume): removed my publicly exposed phone number (PII) and purged it from git history (deleting it from the file alone leaves it in old commits), fixed a broken deployment, cleared leftover AI-generated text, and retargeted it for fraud and security analyst roles.
- **2026-10-02:** Scoped a least-privilege GitHub token to one repo, then revoked and rotated it immediately after accidental exposure.
- **2026-10-01:** Built a Python password breach checker using the HIBP Pwned Passwords API. Uses k-anonymity, so the real password never leaves the machine. See [`scripts/pwcheck.py`](scripts/pwcheck.py).
- **2026-10-01:** Investigated a Google critical security alert on my own account: rotated credentials, audited sessions, checked for mailbox persistence. See [write-up](writeups/01-personal-account-incident-response.md).

## Connect
[Resume](https://jeffreyesdavid.github.io/interactive-resume/) · [LinkedIn](https://www.linkedin.com/in/jeffreyisdavid/) · [TryHackMe](https://tryhackme.com/p/gahtomahiko)
