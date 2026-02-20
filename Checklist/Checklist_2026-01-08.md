It is **Thursday, January 8, 2026**.

With only **45 minutes** and **Medium** energy, today’s plan is optimized for **speed and synergy**. We will align the Server lesson directly with the Linux command so you learn the _theory_ and the _tool_ simultaneously, saving mental context-switching costs.

Here is your focused daily learning plan for **2026-01-08**.

---

# 📅 **2026-01-08 — Daily Learning Plan**

| **Category**                   | **Task**                                                    | **Status** |
| ------------------------------ | ----------------------------------------------------------- | ---------- |
| 🧠 LeetCode Practice           | **345. Reverse Vowels of a String** (Two Pointers)          | ✅          |
| 🖥️ Server Building Essentials | **Deep Dive: The Discretionary Access Control (DAC) Model** | ✅          |
| 🐧 Linux Learning              | Command: **`chmod`** (Applied Permission Management)        | ✅          |

---

## 🧠 LeetCode — **345. Reverse Vowels of a String**

Tags: #TwoPointers #String #Logic

Difficulty: Easy

Why chosen:

- **Time Efficient:** This problem can be solved in 10–15 minutes.
    
- **Skill Continuity:** It continues the "Converging Pointers" theme from _Is Subsequence_ (Jan 5) and _Squares of a Sorted Array_ (Dec 9), but adds a conditional check (is it a vowel?) inside the loop.
    

### 🎯 **Concept to learn today: "Conditional Swapping"**

You need to reverse only the vowels in a string while keeping consonants in place.

- **The Strategy:** Use `Left` (start) and `Right` (end) pointers.
    
- **The Flow:**
    
    1. Move `Left` forward until it hits a vowel.
        
    2. Move `Right` backward until it hits a vowel.
        
    3. **Swap** them.
        
    4. Repeat until `Left >= Right`.
        
- **Why efficient?** You touch every character exactly once ($O(N)$), performing swaps in-place.
    

---

## 🖥️ Server Building Essentials — **Deep Dive: The Permission Model (DAC)**

Tags: #Security #Filesystem #Inodes #Octal

Goal: Understanding why Linux uses "777" or "644". This is the Discretionary Access Control system. In Linux, permissions are not attached to the filename; they are stored in the Inode (the metadata structure on the disk).

### 1. The Trinity: Read, Write, Execute

Every file has three sets of permissions for three types of actors:

- **User (u):** The owner of the file.
    
- **Group (g):** Other users in the file's assigned group (e.g., `www-data` for web servers).
    
- **Others (o):** Everyone else (the public).
    

### 2. The Octal Math (The 4-2-1 Rule)

Computers see permissions as binary bits. Humans see them as octal numbers.

- **Read (r)** = `4` (Binary `100`)
    
- **Write (w)** = `2` (Binary `010`)
    
- **Execute (x)** = `1` (Binary `001`)
    

**The Calculation:**

- **7 (4+2+1):** Read, Write, and Execute. (Full control).
    
- **6 (4+2):** Read and Write. (Standard for files).
    
- **5 (4+1):** Read and Execute. (Standard for directories/scripts).
    
- **4 (4):** Read Only.
    

### 3. The Directory Trap

Sophisticated insight:

- **Read** on a directory means you can **list** files (`ls`).
    
- **Execute** on a directory means you can **enter** it (`cd`).
    
- _Critical:_ If a directory is `400` (Read only), you can list the files but **cannot** enter it to access them. You almost always need `5` (Read+Exec) for directories.
    

---

## 🐧 Linux Learning — Command: **`chmod`**

Tags: #Linux/Command/chmod #Permissions #Security

Why chosen:

- Directly applies the "Octal Math" theory from the Server lesson.
    
- Essential for fixing "Permission Denied" errors during server setup.
    

### 🎯 **Core Uses & The "Symbolic vs. Numeric" Style**

| **Scenario**               | **Command**              | **Sophistication**                                                                                                                        |
| -------------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Secure a Private Key**   | **`chmod 600 key.pem`**  | **Owner:** Read/Write (6). **Group:** None (0). **Others:** None (0). This is mandatory for SSH keys; the server will reject "open" keys. |
| **Make a script runnable** | **`chmod +x script.sh`** | **Symbolic Mode.** Adds `Execute` permission for everyone. Easier than calculating the exact number if you just want to "add" ability.    |
| **Fix Web Server Files**   | `chmod 644 index.html`   | **Owner:** RW. **Everyone else:** Read Only. Standard for web content.                                                                    |
| **Recursive Update**       | `chmod -R 755 /var/www`  | **Danger Zone:** Recursively applies permissions to every file inside. Use with caution.                                                  |

### 💡 **Practice Task: The "Locked Door" Experiment**

1. Create a folder: `mkdir vault`.
    
2. Create a file inside: `touch vault/secret.txt`.
    
3. **Lock the folder:** `chmod 000 vault`.
    
4. Try to list it: `ls vault`. (Result: `Permission denied`).
    
5. **Unlock only listing:** `chmod 400 vault`.
    
6. Try to list: `ls vault`. (Result: You see the name `secret.txt`, but likely with `????` metadata because you can't _enter_ to read the inode).
    
7. **Unlock entry:** `chmod 500 vault`.
    
8. Try again: `ls -l vault`. (Success).