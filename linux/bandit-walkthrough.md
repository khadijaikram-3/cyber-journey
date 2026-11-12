# OverTheWire: Bandit Walkthrough

## Level 0 → Level 1
**Goal:** Log in via SSH and find the password in the `readme` file.
- **Command:** `ssh bandit0@bandit.labs.overthewire.org -p 2220`
- **Password:** `bandit0`
- **Action:** Used `ls` to list files, found `readme`. Used `cat readme` to read the password.

## Level 1 → Level 2
**Goal:** Password is in a file named `-` (dash).
- **Action:** Used `cat ./-` because a dash alone means "standard input" and will freeze the terminal. `./` tells Linux to look in the current directory.
- **Password:** `PK8fYLZg2hnHSz83plBL1iEPKdD3QToB`

## Level 2 → Level 3
**Goal:** Password is in a file named `--spaces in this filename--`.
- **Action:** Used `cat -- "--spaces in this filename--"`. The `--` tells `cat` to stop looking for flags and treat the next argument as a filename.
- **Password:** `7ZZ2LFrykP2zEyvBl4m3clcL7tGYJPME`

## Level 3 → Level 4
**Goal:** Password is in a hidden file in the `inhere` directory.
- **Action:** Used `cd inhere` to enter the directory. Used `ls -la` to list all files, including hidden ones. Spotted `...Hiding-From-You` in the filename column (not the permissions column). Used `cat "...Hiding-From-You"` to read it.
- **Password:** `xzTXq1rDJQVVAzdv5cHq1TQytTWufAMq`

## Level 4 → Level 5
**Goal:** Password is in the only human-readable file in the `inhere` directory.
- **Action:** *(Write your own notes here after you solve it!)*
