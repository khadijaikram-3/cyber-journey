# Day 3 - Advanced Linux Searching & Web Exploitation

### November 13, 2026

## 1. Linux (OverTheWire Bandit)
- **Progress:** Levels 4 and 5 completed.
- **Key Learnings:**
  - Level 4: Found the human-readable file by testing files one by one with `cat -- "-file07"`.
  - Level 5: Used the `find` command to filter files by specific properties.
  - **Command learned:** `find . -type f -size 1033c ! -executable`
    - `.` = current directory
    - `-type f` = only files
    - `-size 1033c` = exactly 1033 bytes
    - `! -executable` = not executable
  - Successfully located the file path and read the password for Level 6.

## 2. Python (freeCodeCamp)
- **Progress:** Built the "Employee Profile Generator".
- **Key Learnings:**
  - String Concatenation: Using `+` and `str()` to combine strings and integers (e.g., `'I am ' + str(age)`).
  - String Slicing: Extracting specific parts of a string using `[start:stop]`. 
    - `employee_code[0:3]` extracts the first 3 characters.
    - `employee_code[-3:]` extracts the last 3 characters.
  - F-strings: Used `f'...'` to interpolate variables directly without needing `str()`.

## 3. Web Exploitation (PortSwigger)
- **Progress:** Solved Lab 3: Unprotected admin functionality with unpredictable URL.
- **Concept:** Security by Obscurity. Hiding a URL in JavaScript does not protect it.
- **Execution:** Opened "View Page Source", searched for "admin", found the hidden URL `/admin-tp0r3e`, appended it to the main URL, accessed the admin panel, and deleted `carlos`.

## 4. CTF Practice (CyLab)
- **Warm Challenge:** Downloaded a file using `wget`, made it executable with `chmod +x`, and found the flag using the `-h` flag. Flag: `academy{b1scu1ts_4nd_gr4vy_57d8c79}`
- **Tab Complete Challenge:** Unzipped a heavily nested folder structure using `unzip`. Navigated through the folders, made the binary executable, and ran it to get the flag. Flag: `academy{l3v3l_up!_t4k3_4_r35t!_9d928112}`
