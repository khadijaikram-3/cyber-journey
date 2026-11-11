#  Linux Command Cheat Sheet

A detailed reference guide for essential Linux commands, including syntax, purpose, and real-world examples for cybersecurity.

---

##  Navigation & Directory Management

### `pwd` (Print Working Directory)
- **Purpose:** Shows the absolute path of the directory you are currently in.
- **Syntax:** `pwd`
- **Example:** `pwd` -> Output: `/home/kali/Desktop`
- **Why use it:** When you get lost in the terminal, this tells you exactly where you are.

### `ls` (List)
- **Purpose:** Lists files and directories.
- **Syntax:** `ls [options] [directory]`
- **Example:** `ls -la` 
- **Why use it:** `ls -la` shows hidden files (starting with a dot `.`) and gives details like permissions, owner, and file size.

### `cd` (Change Directory)
- **Purpose:** Moves you from one directory to another.
- **Syntax:** `cd [directory_path]`
- **Example:** `cd /var/www/html` (moves to the web server folder) or `cd ..` (moves up one folder).
- **Why use it:** To navigate the file system without a mouse.

### `mkdir` (Make Directory)
- **Purpose:** Creates a new folder.
- **Syntax:** `mkdir [folder_name]`
- **Example:** `mkdir hacking_notes`
- **Why use it:** To organize your scripts, tools, and notes.

---

##  Reading & Viewing Files

### `cat` (Concatenate)
- **Purpose:** Reads a file and prints its entire contents to the screen.
- **Syntax:** `cat [filename]`
- **Example:** `cat /etc/passwd`
- **Why use it:** Fastest way to read a short file (like a `readme` or a password file). 
- **Hacker Note:** If a file is named `-`, use `cat ./-` so the terminal doesn't treat it as a flag.

### `less`
- **Purpose:** Opens a file so you can scroll through it page by page.
- **Syntax:** `less [filename]`
- **Example:** `less /var/log/auth.log`
- **Why use it:** If a log file is 10,000 lines long, `cat` will flood your screen. `less` lets you read it slowly. (Press `q` to quit).

### `head` & `tail`
- **Purpose:** Shows the first 10 lines (`head`) or the last 10 lines (`tail`) of a file.
- **Syntax:** `head [filename]` or `tail [filename]`
- **Example:** `tail -n 20 /var/log/syslog` (shows the last 20 lines).
- **Why use it:** Great for checking the most recent errors in a log file without reading the whole thing.

---

##  Searching & Finding

### `find`
- **Purpose:** Searches for files and directories based on specific criteria.
- **Syntax:** `find [starting_directory] -name "[filename]"`
- **Example:** `find / -name "flag.txt" 2>/dev/null`
- **Why use it:** To locate a file when you don't know where it is. *(Note: `2>/dev/null` hides the "Permission Denied" errors).*

### `grep` (Global Regular Expression Print)
- **Purpose:** Searches for a specific word or pattern inside a file.
- **Syntax:** `grep "[word]" [filename]`
- **Example:** `grep "password" /var/log/auth.log`
- **Why use it:** When a file is massive, `grep` instantly finds the specific line you care about.

---

##  File Information & Manipulation

### `file`
- **Purpose:** Tells you what type of file it is (regardless of the file extension).
- **Syntax:** `file [filename]`
- **Example:** `file unknown_file`
- **Why use it:** A hacker might find a file with no extension. `file` will tell you if it's an image, a text file, or a compiled binary.

### `du` (Disk Usage)
- **Purpose:** Estimates the size of a file or directory.
- **Syntax:** `du -h [filename]`
- **Example:** `du -h backup.zip`
- **Why use it:** `-h` means "human-readable" (shows KB, MB, GB instead of raw bytes).

### `chmod` (Change Mode)
- **Purpose:** Changes the permissions of a file (read, write, execute).
- **Syntax:** `chmod +x [filename]`
- **Example:** `chmod +x exploit.sh`
- **Why use it:** Linux won't run a script unless it has "execute" permissions. This command makes it runnable.

---

##  Networking & Remote Access

### `ssh` (Secure Shell)
- **Purpose:** Logs into a remote computer securely.
- **Syntax:** `ssh username@host -p port`
- **Example:** `ssh bandit0@bandit.labs.overthewire.org -p 2220`
- **Why use it:** The primary way to access remote servers in cybersecurity.

### `nc` (Netcat)
- **Purpose:** The "Swiss Army Knife" of networking. Used to connect to ports, listen for connections, or transfer files.
- **Syntax:** `nc [host] [port]`
- **Example:** `nc 192.168.1.5 4444`
- **Why use it:** Hackers use this to grab banners (like in CyLab) or to spawn reverse shells (getting a terminal on a victim's machine).

### `ping`
- **Purpose:** Tests if a remote computer is reachable on the network.
- **Syntax:** `ping [host]`
- **Example:** `ping 8.8.8.8`
- **Why use it:** Quick check to see if a server is online before you try to hack it.

---

##  Important Special Characters
- `./` -> Means "the current directory."
- `../` -> Means "go up one directory."
- `~` -> Means "the home directory of the current user."
- `|` (Pipe) -> Takes the output of one command and passes it to another. 
  - *Example:* `cat /var/log/syslog | grep "error"` (Reads the file, then filters for the word "error").
