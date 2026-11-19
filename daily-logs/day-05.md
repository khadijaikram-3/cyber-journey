# Day 5 - Searching the Filesystem & Security Concepts

### November 18, 2026

## 1. Theory (Google Cybersecurity)
- **Role of a Security Analyst:** Monitor and protect information and systems.
  - Responsibilities: Protect computer/network systems, install prevention software, conduct periodic security audits.
  - Difference: **Analyst** focuses on detections; **Engineer** focuses on project-related works.
- **Key Concepts:**
  - **Compliance:** Adhering to internal standards and external regulations to avoid fines and breaches.
  - **Security Frameworks:** Guidelines for building plans to mitigate risks.
  - **Security Controls:** Safeguards designed to reduce specific security risks.
  - **Security Posture:** An organization's ability to manage its defense of critical assets and react to change.
  - **Threat Actor:** Any person or group who presents a security risk.
  - **Internal Threat:** A current/former employee, vendor, or partner who poses a risk (accidental or intentional).
  - **Network Security:** Keeping network infrastructure secure from unauthorized access.
  - **Cloud Security:** Ensuring cloud assets are properly configured and access is limited to authorized users.
  - **Programming in Cyber:** Automating repetitive tasks, reviewing web traffic, alerting suspicious activity.

## 2. Linux (OverTheWire Bandit)
- **Progress:** Level 6 completed. Logged into Level 7.
- **Key Learnings:**
  - Used `find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null` to search the entire filesystem for a specific file.
  - Understood the importance of `2>/dev/null` to suppress "Permission Denied" errors.
  - Located the file `/var/lib/dpkg/info/bandit7.password` and read it with `cat`.
  - **Password for Level 7:** `Bmnnvf82KzQlfxgAI2d1zYbr1u9pr3E3`

## 3. Python (freeCodeCamp)
- **Progress:** Continued the "Employee Profile Validator" project.
- **Key Learnings:**
  - `.replace(old, new)`: Replaces a substring with a new one.
  - `.find(substring)`: Returns the index position of a substring.
  - `.upper()`: Converts all characters to uppercase.
  - `.lower()`: Converts all characters to lowercase.

