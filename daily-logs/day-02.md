# Day 2 - Access Control & Encoding
### November 12, 2026
## 1. Linux (OverTheWire Bandit)
- **Progress:** Levels 2 to 4 completed.
- **Key Learnings:**
  - Learned 4 different ways to handle filenames with spaces or dashes:
    1. Quotes: `cat "filename with spaces"`
    2. Escape: `cat filename\ with\ spaces`
    3. Option Ender: `cat -- "-filename"`
    4. Path: `cat ./filename`
  - Learned how to read the `ls -la` output format (Permissions, Links, Owner, Group, Size, Date, Filename).
  - Used `ls -la` to find hidden files (starting with a dot).
  - Learned to identify the correct filename column instead of grabbing the permissions column by mistake.

## 2. Python (freeCodeCamp)
- **Progress:** Strings module.
- **Key Learnings:**
  - Strings are immutable. You can't change them in place, but you can reassign variables.
  - Escape sequences: `\n` (newline), `\t` (tab), `\\` (backslash).
  - String Operations: Concatenation (`+`), Repetition (`*`).
  - String Interpolation: Using `f-strings` (e.g., `f'My name is {name}'`) to insert variables directly into strings without needing `str()`.
  - String Slicing: `string[start:stop:step]`. Learned how to reverse a string using `[::-1]`.
  - String Methods: `.upper()`, `.lower()`, `.strip()`, `.replace()`, `.split()`, `.join()`, `.startswith()`, `.endswith()`, `.find()`, `.count()`, `.capitalize()`, `.title()`.

## 3. Web Exploitation (PortSwigger)
- **Progress:** Solved Lab 2: Unprotected admin functionality.
- **Concept:** Access Control determines who is allowed to do what. Broken Access Control (Vertical Privilege Escalation) is when a normal user can access admin functionality.
- **Execution:** Checked `robots.txt`, found the `/administrator-panel` directory, accessed it directly, and deleted the user `carlos`.

## 4. CTF Practice (CyLab & picoCTF)
- **CyLab:** Solved the "Mod 26" challenge using CyberChef (ROT13 decoding).
- **picoCTF:**
  - Learned Base16 (Hexadecimal) math. Converted `0x3D` to decimal (61) and `42` to binary (`101010`).
  - Solved a Base64 challenge by decoding `bDNhcm5fdGgzX3IwcDM1` to `l3arn_th3_r0p35` (Leetspeak for "learn the ropes").
  - Realized that CyberChef's "Magic" wand is a powerful tool for identifying unknown encodings.
