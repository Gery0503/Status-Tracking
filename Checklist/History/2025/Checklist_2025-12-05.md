
---

# 📅 **2025-12-05 — Daily Learning Plan**

| **Category**                   | **Task**                                                     | **Status** |
| ------------------------------ | ------------------------------------------------------------ | ---------- |
| 🧠 LeetCode Practice           | **189. Rotate Array** (Array Manipulation, Space Complexity) | ✅          |
| 🖥️ Server Building Essentials | **Lesson 1: Initial Post-OS Setup and SSH Security**         | ✅          |
| 🐧 Linux Learning              | Command: **`systemctl`** (Service Management & Control)      | ✅          |

---

## 🧠 LeetCode — **189. Rotate Array**

Tags: #Arrays #TwoPointers #Optimization

Difficulty: Medium

Why chosen today:

- This problem challenges your thinking on **In-Place Array Manipulation** and requires careful consideration of **Space Complexity** (aim for $O(1)$ extra space).
    
- It introduces a powerful technique: the **"Reverse" method**, which is non-obvious and highly prized in interviews for array problems.
    

### 🎯 **Concept to learn today: "The Three-Step Reverse"**

The most efficient, $O(n)$ time and $O(1)$ space solution involves three reversals:

1. **Reverse the entire array.**
    
2. **Reverse the first $k$ elements.**
    
3. **Reverse the remaining $n-k$ elements.**
    

**Example:** Array `[1, 2, 3, 4, 5, 6, 7]`, rotate $k=3$.

1. **Reverse All:** `[7, 6, 5, 4, 3, 2, 1]`
    
2. **Reverse First $k$ (3):** `[5, 6, 7, 4, 3, 2, 1]`
    
3. **Reverse Rest (4):** `[5, 6, 7, 1, 2, 3, 4]` (Result!)
    

## 🖥️ Server Building Essentials — **Lesson 1: Initial Post-OS Setup and SSH Security**

Tags: #ServerSecurity #SSH #SystemAdmin

Goal: Configure the essential step for managing your new server remotely and securely. You will use the terminal for all future work, so securing SSH (Secure Shell) access is mandatory.

### 1. **SSH Fundamentals**

- **What it is:** The protocol used to securely connect to a remote server's command line.
    
- **Key Decisions:**
    
    - **Disable Root Login:** Why logging in directly as the `root` user is a major security risk.
        
    - **Use Key-Based Authentication:** Understand why SSH keys are vastly more secure than passwords.
        
    - **Change Default Port:** Why moving SSH from the standard port **22** to a high, non-standard port (e.g., 2222) is a simple, effective deterrent against automated scanning bots.
        

### 2. **Actionable Tasks (Conceptual/Practice)**

- **Task A: Create a New User:** Research the Linux command (`adduser` or `useradd`) and process for creating a new, non-root user (`yourname`).
    
- **Task B: SSH Key Generation:** Research how to generate an SSH key pair (`ssh-keygen`) and where the two files (public and private) are stored.
    
- **Task C: Secure the Config:** Using the `sed` command you mastered, sketch the `sed` line you would use to change the SSH port in the `/etc/ssh/sshd_config` file from `22` to `2222`.
    

## 🐧 Linux Learning — Command: **`systemctl`**

Tags: #Linux/Command/systemctl #ServiceManagement #Bootup

Why chosen: On modern Linux distributions (like Ubuntu and RHEL), systemctl is the command you will use constantly to manage all server services (web servers, databases, task runners, logging agents). Mastery of this is non-negotiable for a server admin.

### 🎯 **Core Uses and Practice Tasks**

| **Scenario**                         | **Command**                                           | **Reason**                                                                                                                      |
| ------------------------------------ | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Check service status (e.g., SSH)** | `sudo systemctl status sshd`                          | The **essential diagnostic command** to see if a service is running, failed, or disabled, and to read the last few log entries. |
| **Start/Stop/Restart a service**     | `sudo systemctl restart nginx`                        | Standard controls for applying changes or correcting errors.                                                                    |
| **Enable a service**                 | `sudo systemctl enable nginx`                         | **Ensures the service starts automatically after a reboot.** This is critical for server reliability.                           |
| **Disable a service**                | `sudo systemctl disable httpd`                        | Prevents a service from starting on boot.                                                                                       |
| **List all running services**        | `systemctl list-units --type=service --state=running` | Good for auditing what is consuming resources on your server.                                                                   |

### 💡 **Practice Task: Local Server Service Control**

1. Check the status of the SSH daemon: `systemctl status sshd`.
    
2. Practice enabling and disabling a harmless local service (like `cups` if you have it, or another non-critical service) to understand the `enable`/`disable` mechanism.
    
3. Use `systemctl list-units --type=service` to examine what services are currently configured to run on your machine.