# Day 8 - Authentication, Formatting & CTF Exploits

### November 23, 2026

## 1. Theory (Google Cybersecurity)
- **8 Domains of CISSP:**
  1. Security and Risk Management (goals/objectives)
  2. Asset Security (physical/digital assets)
  3. Security Architecture and Engineering (effective tools)
  4. Communications and Network Security (physical/wireless)
  5. Identity and Access Management (policies for assets)
  6. Security Assessment and Testing (control testing/analysis)
  7. Security Operations (investigations/prevention)
  8. Software Development Security (secure coding practices)
- **Attack Types & Domains:**
  - Password Attacks (Brute force, Rainbow table) -> Communication & Network Security.
  - Social Engineering (Phishing, Smishing, Vishing, Whaling, BEC, etc.) -> Security & Risk Management.
  - Physical Attacks (USB drop, Card cloning) -> Asset Security.
  - Adversarial AI -> Communication & Network Security + Identity and Access Management.
  - Supply-chain Attacks -> Multiple domains (Risk Management, Architecture, Operations).
  - Cryptographic Attacks (Birthday, Collision, Downgrade) -> Communication & Network Security.
- **Threat Actor Types:**
  - **APTs (Advanced Persistent Threats):** Highly skilled, research targets, remain undetected for long periods (goal: infrastructure damage, intellectual property).
  - **Insider Threats:** Abuse authorized access (sabotage, corruption, espionage).
  - **Hacktivists:** Driven by political agendas (propaganda, social change).
- **Hacker Types:**
  - **Authorized (Ethical):** Follow code of ethics/law to secure organizations.
  - **Semi-authorized:** Researchers who find but don't exploit vulnerabilities.
  - **Unauthorized (Unethical):** Malicious, break the law for financial gain.

## 2. Python (freeCodeCamp)
- **Progress:** Learned F-string formatting for numbers.
- **Key Learnings:**
  - `f"{value:.2f}"`: Displays a float with exactly two decimal places without changing the underlying value.
  - **Format Breakdown:** `:` (starts format), `.2` (two decimal places), `f` (fixed-point notation).
  - `round(value, 2)` returns a numeric value, while `f"{value:.2f}"` returns a string. Trailing zeros are guaranteed with f-strings but not with `round()`.
  - Floating-point math (e.g., `0.1 + 0.2 = 0.30000000000000004`) can be cleaned up for display using f-strings.

## 3. Linux (OverTheWire Bandit)
- **Progress:** Level 8 completed.
- **Key Learnings:**
  - Used the pipe (`|`) to chain commands: `sort data.txt | uniq -u`.
  - `sort` organizes lines alphabetically, and `uniq -u` filters out duplicates to find the unique line.
  - **Password for Level 9:** `EjmOSvuAu7sGAHqHVcBDPirRe9T03kxl`

## 4. Web Exploitation (PortSwigger)
- **Progress:** Started the "Authentication" learning path.
- **Key Learnings:**
  - **Authentication vs. Authorization:** Authentication is verifying *who* you are (identity). Authorization is verifying *what* you are allowed to do (permissions).
  - **Brute-force Attacks:** Using trial and error (often automated with wordlists) to guess valid credentials.
  - **Username Enumeration:** Usernames are often predictable (`admin`, `administrator`, `firstname.lastname@company.com`). They can be leaked through public profiles, HTTP responses, or emails.

## 5. CTF Practice (CyLab)
- **Challenge 1: Insp3ct0r**
  - **Objective:** Inspect the website to find a flag split into 3 parts.
  - **Execution:** Used Developer Tools (Inspect Element) -> Page Source for part 1. Found part 2 in `mycss.css` and part 3 in `myjs.js`.
  - **Flag:** `academy{tru3_d3t3ct1ve_0r_ju5t_lucky?d6c61154}`
- **Challenge 2: Strings**
  - **Objective:** Extract a flag hidden in a binary file.
  - **Execution:** Ran `strings strings | grep -i "academy"` to find the human-readable text.
  - **Flag:** `academy{5tRIng5_1T_DAEbE8bd}`
