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
- **Action:** Used `cd inhere`, then `ls`. Found files `-file00` to `-file09`. Used `cat -- "-file07"` to find the ASCII text file.
- **Password:** `6C7h9GD8M6ai5nr7wo1RonrzFjj9yIrG`

## Level 5 → Level 6
**Goal:** Password is in a file under `inhere` that is human-readable, 1033 bytes, and not executable.
- **Action:** Used `find . -type f -size 1033c ! -executable` to filter all files in all subdirectories. 
- **Mistake to avoid:** I accidentally read `-file2` (a decoy with a dash) instead of `.file2` (the hidden file with a dot). The `find` command gave me the correct path, but I had to make sure I was in the right directory before running `cat`.
- **Password:** `pXa26xhMWaC2SvDotA4r9EgZkulOeSBW`

## Level 6 → Level 7
**Goal:** Password is stored in a file somewhere on the server, owned by user `bandit7`, owned by group `bandit6`, and exactly 33 bytes in size.
- **Action:** Used `find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null` to search the entire filesystem while hiding permission errors.
- **File Found:** `/var/lib/dpkg/info/bandit7.password`
- **Command to read:** `cat /var/lib/dpkg/info/bandit7.password`
- **Password:** `Bmnnvf82KzQlfxgAI2d1zYbr1u9pr3E3`

## Level 7 → Level 8
**Goal:** Password is stored in `data.txt` next to the word `millionth`.
- **Action:** Used `grep "millionth" data.txt` to filter the file and print only the line containing the target word.
- **Password:** `VR1ljMayciFxbnUokuQmJFw6QC9VKtub`

## Level 8 → Level 9
**Goal:** Password is in `data.txt` and is the only line that occurs only once.
- **Action:** Used `sort data.txt | uniq -u` to sort the lines and filter out duplicates, leaving only the unique line.
- **Password:** `EjmOSvuAu7sGAHqHVcBDPirRe9T03kxl`
