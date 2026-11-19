# Day 6 - Data Filtering & Horizontal Escalation

### November 19, 2026

## 1. Theory (Google Cybersecurity)
- **Core Concepts:** PII (Personally Identifiable Information), SPII (Sensitive PII), Security Posture, Threat Actor.
- **Transferable Skills:** Communication, Problem-solving, Time management, Growth mindset, Diverse perspectives.
- **Technical Skills:** Programming (automation), SIEM tools (log analysis), IDS (Intrusion Detection Systems), Threat landscape knowledge, Incident response.

## 2. Linux (OverTheWire Bandit)
- **Progress:** Level 7 completed.
- **Key Learnings:**
  - Used `grep "millionth" data.txt` to find a specific line inside a massive text file.
  - Reviewed essential data processing commands: `sort`, `uniq`, `strings`, `base64`, `tr`, `tar`, `gzip`, `xxd`, and `man`.
  - **Password for Level 8:** `VR1ljMayciFxbnUokuQmJFw6QC9VKtub`

## 3. Python (freeCodeCamp)
- **Progress:** Completed "Employee Profile Validator" and "Bill Splitter" workshops.
- **Key Learnings:**
  - `.split()`: Splits a string into a list based on a separator.
  - `.join()`: Joins a list of strings into one string.
  - `.startswith()` / `.endswith()`: Checks the beginning or end of a string.
  - `.count()`: Counts occurrences of a substring.
  - **Integers & Floats:** Floor division (`//`), Exponentiation (`**`), Infinity (`float('inf')`), `round()`, `abs()`, `pow()`.
  - **Augmented Assignment:** `my_var += 5`.

## 4. Web Exploitation (PortSwigger)
- **Progress:** Solved Lab 05 (Unpredictable User IDs) and Lab 06 (Password Disclosure).
- **Concept:** Horizontal Privilege Escalation (IDOR). Accessing another user's data at the same privilege level.
- **Execution (Lab 06):** 
  - Logged in as `wiener`, changed URL to `id=carlos` to get his masked password.
  - Changed URL to `id=administrator` to get the admin's masked password.
  - Opened Developer Tools (Inspect), changed `<input type="password">` to `type="text"` to unmask the password.
  - Logged in as `administrator` and deleted `carlos`.
