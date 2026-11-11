# Day 1 - The Foundation Begins                                                    
###                                                                                               November 11, 2026

## 1. Linux (OverTheWire Bandit)
- **Progress:** Levels 0 to 2 completed.
- **Key Concepts:** SSH, Linux file system navigation, handling special characters in filenames.
- **Commands Learned:**
  - `ssh`: Secure Shell. Used for remote login. Syntax: `ssh username@host -p port`
  - `ls`: Lists directory contents.
  - `cat`: Reads and outputs file contents. Used `cat ./-` to read a file named with a dash.
  - `cd`: Change directory.
  - `file`: Classifies a file (tests filesystem, magic, and language).
  - `du`: Estimates file space usage. (Supports wildcards like `*`).
  - `find`: Searches for files in a directory hierarchy.

## 2. Python (freeCodeCamp)
- **Progress:** 15/143 steps. Completed "Introduction to Python", Variables/Data Types Theory, and the "Build a Report Card Printer" Workshop.
- **Key Concepts:**
  - Python is used in cybersecurity for automation, threat analysis, and vulnerability detection.
  - Variables use `snake_case`.
  - Comments start with `#`.
  - `print()` outputs data. Commas add spaces.
- **Data Types:**
  - `int`: Whole numbers (10).
  - `float`: Decimals (4.50).
  - `str`: Text ('hello').
  - `bool`: True/False.
- **Functions:**
  - `type()`: Returns the data type of a variable.
  - `isinstance()`: Checks if a variable is a specific type.

## 3. Web Exploitation (PortSwigger)
- **Progress:** Solved Lab 1 - File path traversal, simple case.
- **Concept:** Path (or Directory) Traversal allows an attacker to read arbitrary files on the server by manipulating file paths. Using `../`, an attacker can move up directory levels to access sensitive files like `/etc/passwd`.
- **Execution:** Intercepted the image request in Burp Suite Repeater and modified the GET request to `filename=../../../etc/passwd`. Successfully retrieved the system user list.

## 4. CTF Practice (CyLab & picoCTF)
- **CyLab:** Completed Section 1 (Sanity). Used `ssh` to log into a remote server, downloaded a file to read a flag, and used `netcat (nc)` to connect to a specific port and retrieve a flag.
- **picoCTF:** Read the "Beginner's Guide to the Challenge Library" to understand CTF categories (General Skills, Crypto, Forensics, Web, Rev, Pwn).
