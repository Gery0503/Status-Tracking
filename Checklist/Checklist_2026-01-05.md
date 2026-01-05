It is **Monday, January 5, 2026**.

Given your **Medium** energy level and **1-hour** constraint, today’s plan is designed for **high conceptual return with moderate execution intensity**. We will focus on "flow" (Two Pointers) and "architecture" (how software actually installs), avoiding heavy brute-force coding or complex kernel debugging.

Here is your daily learning plan for **2026-01-05**.

---

# 📅 **2026-01-05 — Daily Learning Plan**

| **Category**                   | **Task**                                                       | **Status** |
| ------------------------------ | -------------------------------------------------------------- | ---------- |
| 🧠 LeetCode Practice           | **392. Is Subsequence** (Two Pointers / Linear Scan)           | ✅          |
| 🖥️ Server Building Essentials | **Deep Dive: The Package Management Subsystem (APT vs. DPKG)** | ✅          |
| 🐧 Linux Learning              | Command: **`diff`** (Configuration Comparison)                 | ✅          |

---

## 🧠 LeetCode — **392. Is Subsequence**

Tags: #TwoPointers #String #Greedy

Difficulty: Easy

Why chosen:

- **Energy Match:** This problem is "logic-light" but "technique-heavy." It requires a smooth linear scan without complex math or recursion, fitting your medium energy perfectly.
    
- **Core Skill:** It reinforces the **Two Pointer** technique (one pointer for the source, one for the target), a pattern you will use constantly in server log parsing.
    

### 🎯 **Concept to learn today: "The Passive Follower"**

You have a small string `s` and a large string `t`. Does `s` exist inside `t` keeping the relative order?

- **The Logic:**
    
    - Pointer `i` tracks your progress in `s` (the goal).
        
    - Pointer `j` tracks your progress in `t` (the search space).
        
    - **Rule:** Always move `j`. Move `i` _only_ when characters match (`s[i] == t[j]`).
        
    - If `i` reaches the end of `s`, you found it.
        
- **Why efficient?** You process the long string exactly once ($O(N)$), with no backtracking.
    

---

## 🖥️ Server Building Essentials — **Deep Dive: The Package Management Subsystem**

Tags: #SystemArchitecture #APT #DPKG #Dependencies

Goal: Understanding how Linux manages software. Why is "installing" on Linux different from an .exe on Windows? It comes down to Shared Libraries and the Dependency Graph.

### 1. The "Why": Shared Libraries & Dependency Hell

In Windows, programs often bundle their own DLLs (libraries). In Linux, the OS provides a single shared library (e.g., `openssl`).

- **The Risk:** If Nginx needs `openssl v1.1` and Python needs `openssl v3.0`, you have a conflict.
    
- **The Solution:** The Package Manager is a **Constraint Solver**. It calculates a graph of dependencies to ensure no two programs break each other.
    

### 2. The Architecture: Backend (`dpkg`) vs. Frontend (`apt`)

New admins confuse these. They are distinct layers.

- **Layer 1: The Backend — `dpkg` (Debian Package)**
    
    - **Role:** The dumb worker. It installs _one_ `.deb` file from your disk.
        
    - **Limitation:** It knows nothing about the internet or dependencies. If you run `dpkg -i tool.deb` and it needs a library you don't have, `dpkg` simply fails.
        
    - **The Database:** It maintains the "State of the World" in `/var/lib/dpkg/status`. This text file lists every file owned by every package on your system.
        
- **Layer 2: The Frontend — `apt` (Advanced Package Tool)**
    
    - **Role:** The intelligent manager. It talks to **Repositories** (servers listed in `/etc/apt/sources.list`).
        
    - **The Magic:** When you type `apt install nginx`:
        
        1. `apt` downloads the package lists (catalogs).
            
        2. It calculates the dependency tree ("Nginx needs OpenSSL, do we have it? No? I will fetch it too").
            
        3. It downloads the `.deb` files.
            
        4. It hands them to `dpkg` to actually install.
            

### 3. The "Update" Mechanism

- `apt update`: This **does not** update software. It only updates the _catalog_ (the text lists of what versions exist in the repo).
    
- `apt upgrade`: This compares your installed versions (from `dpkg`) against the new catalog (from `apt update`) and calculates the upgrade path.
    

---

## 🐧 Linux Learning — Command: **`diff`**

Tags: #Linux/Command/diff #Configuration #Troubleshooting

Why chosen:

- **Scenario:** You change a server config file (`nginx.conf`), and suddenly the server won't start. You need to know: _"What exactly did I change?"_
    
- **Fit:** It requires low mental energy but yields high value for debugging.
    

### 🎯 **Core Uses & The "Unified" Standard**

| **Scenario**                    | **Command**                        | **Sophistication**                                                                                                                        |
| ------------------------------- | ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Compare two files**           | `diff file1.conf file2.conf`       | The default output is cryptic (`<` and `>`). Hard to read.                                                                                |
| **The "Human" Read (Standard)** | **`diff -u file1 file2`**          | **`-u` (Unified)**. This is the industry standard format (used by GitHub). It shows context lines and uses `+` (added) and `-` (removed). |
| **Compare directory contents**  | `diff -r /etc/nginx /backup/nginx` | **`-r` (Recursive)**. Tells you which files are missing or different between an entire backup folder and the live folder.                 |

### 💡 **Practice Task: The "Undo" Check**

1. Create a file `original.txt` with 3 lines of text.
    
2. Copy it: `cp original.txt new.txt`.
    
3. Edit `new.txt`: Change one word and add a new line at the bottom.
    
4. Run: `diff -u original.txt new.txt`.

**Observation:** Notice how it clearly marks the changes with `-` (old line) and `+` (new line). This is exactly what you see in a Git commit.