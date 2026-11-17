# Day 4 - File Sizes, Strings & Access Control

### November 17, 2026

## 1. Theory (Google Cybersecurity)
- **Topic:** Understanding Phishing.
- **Key Learnings:**
  - **Phishing Tactics (Social Engineering):** Psychological tricks designed to manipulate the user.
    - **1. Urgency:** "Act now!"
    - **2. Fear:** "Your account is locked!"
    - **3. Authority:** Impersonating a manager.
  - **Phishing Indicators (Red Flags):** Verifiable signs that a message is malicious.
    - **Technical Indicators:** Incorrect sender domains, malicious link addresses.
    - **Content Indicators:** Poor grammar, generic greetings, unusual requests.

## 2. Linux (OverTheWire Bandit)
- **Progress:** Level 5 completed, logged into Level 6.
- **Key Learnings:**
  - Learned to use `ls -lh` to view human-readable file sizes (K, M, G).
  - Used `find . -type f -size 1033c ! -executable` to locate a specific file.
  - Understood the difference between absolute paths (`/`) and relative paths (`.`).
  - Made a mistake by reading a decoy file (`-file2`, 2.5K) instead of the hidden file (`.file2`, 1033 bytes). Learned to check the dot and directory.
  - **Password:** `pXa26xhMWaC2SvDotA4r9EgZkulOeSBW`

## 3. Python (freeCodeCamp)
- **Progress:** Built the "Email Profile Validator" project.
- **Key Learnings:**
  - **`.find()`:** Returns the index position of a character (e.g., `email.find('@')`).
  - **Slicing:** Extracted the username from the email using `email[:at_position]`.
  - **`in` operator:** Checked if a substring exists (e.g., `'@' in email`).
  - **`.strip()`:** Removes whitespace from the beginning and end.
  - **`.title()`:** Capitalizes the first letter of each word.
  - **`.lower()`:** Converts all letters to lowercase.

## 4. Web Exploitation (PortSwigger)
- **Progress:** Solved Lab 4: User role controlled by request parameter.
- **Concept:** Parameter-based access control. The server determines the user's role based on a client-side value (like a cookie or URL parameter). If the user can change that value, they can escalate their privileges.
- **Execution:** Opened Developer Tools (F12) -> Application -> Cookies. Changed the `Admin` cookie from `false` to `true`. Navigated to `/admin` and deleted `carlos`.
- **Key Takeaway:** Never trust the client. The server must verify the user's role securely.
