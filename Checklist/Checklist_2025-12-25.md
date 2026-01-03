Merry Christmas! It is **Thursday, December 25, 2025**.

Even on a holiday, a sophisticated engineer maintains their edge. Today's plan is designed to be **light but high-impact**, focusing on the "gift" of isolation (Docker) and the elegance of efficient lookups.

Here is your daily learning plan for **2025-12-25**.

---

# 📅 **2025-12-25 — Daily Learning Plan**

| **Category**                   | **Task**                                              | **Status** |
| ------------------------------ | ----------------------------------------------------- | ---------- |
| 🧠 LeetCode Practice           | **771. Jewels and Stones** (Hash Set Efficiency)      | ✅          |
| 🖥️ Server Building Essentials | **Lesson 6: The Container Revolution (Docker Setup)** | ✅          |
| 🐧 Linux Learning              | Command: **`tar`** (Archiving & Backups)              | ✅          |

---

## 🧠 LeetCode — **771. Jewels and Stones**

Tags: #HashTable #String #Optimization

Difficulty: Easy

Why chosen:

- It is a perfect holiday warmup: simple logic but clear performance distinctions.
    
- It reinforces the difference between a **Nested Loop Search** ($O(n \times m)$) and a **Hash Set Lookup** ($O(n + m)$).
    

### 🎯 **Concept to learn today: "The O(1) Lookup"**

You are given a string of "Jewels" (types you own) and "Stones" (all items). You must count how many stones are jewels.

- **The Naive Way:** For every stone, loop through the jewels string to check if it matches.
    
- **The Elegant Way:**
    
    1. Turn the `Jewels` string into a **Hash Set**.
        
    2. Iterate through `Stones` once.
        
    3. Check if `stone` is in `JewelSet`.
        
- **Why it matters:** Checking existence in a string is $O(n)$; checking existence in a Set is $O(1)$. This is the fundamental optimization for large-scale data processing.
    

---

## 🖥️ Server Building Essentials — **Lesson 6: The Container Revolution (Docker)**

Tags: #Docker #Containers #DevOps #Infrastructure

Goal: We are shifting paradigms. In the past, you installed applications (like Python, Node.js, or Nginx) directly onto the OS. This creates "Dependency Hell."

Today, we install Docker, and everything else runs inside isolated boxes. This keeps your server clean and portable.

### 1. **The Architecture: Host vs. Container**

- **Virtual Machines (VMs):** Virtualize the _Hardware_. Heavy, slow to boot (OS inside OS).
    
- **Containers:** Virtualize the _OS_. They share the Linux Kernel of the host but have their own filesystem. Lightweight, instant boot.
    

### 2. **The Setup (Ubuntu Server)**

Do not use `snap`. Use the official repository for the latest version.

- **Install:** `sudo apt install docker.io docker-compose-v2`
    
- The Permission Fix: By default, only root can run containers. To run them as you, add yourself to the group:
    
    sudo usermod -aG docker $USER
    
    (You must log out and log back in for this to take effect).
    

### 💡 **Actionable Task: The "Hello World" of DevOps**

1. Run the test container: `docker run hello-world`.
    
    - _What happens:_ Docker pulls the image from the cloud (Docker Hub), creates a container, runs the script, prints text, and shuts down.
        
2. List running containers: `docker ps`.
    
3. List stopped containers: `docker ps -a`.
    

---

## 🐧 Linux Learning — Command: **`tar`**

Tags: #Linux/Command/tar #Backups #Compression

Why chosen:

- In Lesson 5, you learned `crontab`. The most common use of `crontab` is running backups.
    
- `tar` (Tape Archive) is the standard tool for bundling many files into one package, preserving permissions and ownership (unlike standard zip).
    

### 🎯 **Core Uses & The "X-Z-F" Mnemonic**

| **Scenario**                    | **Command**                          | **Sophistication**                                                                                                        |
| ------------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| **Create a compressed backup**  | `tar -czvf backup.tar.gz /etc/nginx` | **c**: Create<br>**z**: Gzip compression (smaller size)<br>**v**: Verbose (show files)<br>**f**: Filename (must be last!) |
| **Extract an archive**          | `tar -xzvf archive.tar.gz`           | **x**: Extract.<br>Memorize `xzvf` — it is the "muscle memory" command of Linux admins.                                   |
| **List contents (Peek inside)** | `tar -tvf archive.tar.gz`            | **t**: List. Always check the contents of a backup before extracting it to avoid overwriting files.                       |

### 💡 **Practice Task: The Manual Backup**

1. Create a dummy folder `project` with 3 text files inside.
2. Compress it: `tar -czvf project_backup.tar.gz project`.
3. Delete the original folder: `rm -rf project`.
4. Restore it: `tar -xzvf project_backup.tar.gz`.
5. _Bonus Integration:_ Imagine putting this command into yesterday's `crontab` script to back up your web server configuration every night!