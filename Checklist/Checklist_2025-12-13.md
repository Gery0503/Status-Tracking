To follow yesterday's "Fortress Mindset" lesson on Firewalls, today we move to **Active Defense**. A firewall is a wall; we need a sentry that watches that wall and reacts to attackers. This leads perfectly into mastering system logs.

Here is your sophisticated daily learning plan for **2025-12-13**.

---

# 📅 **2025-12-13 — Daily Learning Plan**

| **Category**                   | **Task**                                                 | **Status** |
| ------------------------------ | -------------------------------------------------------- | ---------- |
| 🧠 LeetCode Practice           | **119. Pascal's Triangle II** (Space Optimization)       | ✅          |
| 🖥️ Server Building Essentials | **Lesson 4: Active Defense & Log Heuristics (Fail2Ban)** | ✅          |
| 🐧 Linux Learning              | Command: **`journalctl`** (Systemd Log Management)       | ✅          |

---

## 🧠 LeetCode — **119. Pascal's Triangle II**

Tags: #DynamicProgramming #Array #SpaceOptimization

Difficulty: Easy

Why chosen:

- **Engineering Elegance:** Yesterday, you built the whole triangle ($O(n^2)$ space). Today, the requirement changes: "Give me _only_ the 33rd row."
    
- **The Constraint:** Allocating a massive matrix just to read the last row is wasteful. This problem teaches **Space Optimization**—reducing memory usage from $O(n^2)$ to $O(n)$. This is a critical skill for embedded systems or high-load servers.
    

### 🎯 **Concept to learn today: "The Rolling Array"**

You do not need the row from two steps ago to calculate the current row; you only need the _immediate previous row_.

- **Naive:** Keep all rows in memory.
    
- **Optimized:** Keep only one array. Update it **from right to left** to avoid overwriting values you still need to read.
    
    - _Logic:_ `row[j] = row[j] + row[j-1]`.
        
    - By iterating backwards, you use the "old" value of `row[j-1]` before it gets updated. This allows you to compute the next state **in-place**.
        

---

## 🖥️ Server Building Essentials — **Lesson 4: Active Defense (Fail2Ban)**

Tags: #Security #Fail2Ban #IntrusionPrevention #SysAdmin

Goal: Transform your server security from Passive (UFW blocking ports) to Active (Fail2Ban banning attackers who probe open ports).

### 1. **The Concept: Heuristic Blocking**

A firewall (UFW) effectively says, "The door is closed."

Fail2Ban says, "I see you rattled the handle 5 times in 10 seconds. Now I am boarding up the window and ignoring you for a week."

Fail2Ban scans log files (like `/var/log/auth.log` or the systemd journal) for patterns of failure—such as "Password failed for user root"—and dynamically updates the firewall rules to reject that specific IP address.

### 2. **Key Terminology: Jails**

Fail2Ban is organized into **Jails**. A "Jail" is a combination of:

- **Filter:** The regex pattern to look for in logs (e.g., `Failed password`).
    
- **Action:** What to do (e.g., `iptables-multiport`, `sendmail-whois`).
    
- **LogPath:** Which file to watch.
    

### 💡 **Actionable Task: The "Recidivism" Strategy**

When setting up Fail2Ban, sophisticated engineers configure two distinct SSH jails:

1. **Standard SSH Jail:**
    
    - `maxretry = 5`
        
    - `findtime = 10m` (Time window to count retries)
        
    - `bantime = 1h` (Short "cool off" period)
        
2. **Recidive Jail (The "Blackhole"):**
    
    - _Concept:_ If an IP gets banned by the Standard Jail 3 times in one week, they are not a confused user; they are a bot.
        
    - `logpath`: Monitors Fail2Ban's own log.
        
    - `bantime = 1w` (or permanent).
        
    - _Note:_ This drastically reduces log noise by permanently silencing persistent bots.
        

---

## 🐧 Linux Learning — Command: **`journalctl`**

Tags: #Linux/Command/journalctl #Logs #Systemd #Debugging

Why chosen:

- You are installing Fail2Ban today. Fail2Ban works by reading logs. To debug Fail2Ban (or any service), you must know how to read the logs yourself.
    
- `journalctl` is the interface for **systemd's binary logging system**. It is vastly superior to reading text files with `cat` because it is indexed, searchable, and time-aware.
    

### 🎯 **Core Uses & The "Time-Travel" Debug**

|**Scenario**|**Command**|**Sophistication**|
|---|---|---|
|**"Why is it broken _now_?"**|`journalctl -xe`|Jump to the end (`-e`) and show extra explanation (`-x`) for errors. The first command you run after a crash.|
|**Follow live logs**|`journalctl -f`|Equivalent to `tail -f`. Watch SSH attempts happen in real-time while you test from another terminal.|
|**Filter by Unit (Service)**|`journalctl -u ssh`|Ignore the noise. Show me _only_ what the SSH Daemon is saying.|
|**Time-Window Filtering**|`journalctl --since "1 hour ago"`|Excellent for incident response. "The server glitched at 10 AM; show me logs from 9:55 to 10:05."|

### 💡 **Practice Task: Watch the Sentry**

1. Open two terminals (or two SSH sessions).
    
2. **Terminal A:** Run `journalctl -u ssh -f` (Follow SSH logs).
    
3. **Terminal B:** Try to SSH into your server with a fake user: `ssh fakeuser@localhost`.
    
4. **Observe Terminal A:** You will see the connection attempt, the "Invalid user" error, and the "Connection closed" message appear instantly. This confirms your logging pipeline is working—the exact pipeline Fail2Ban will use to protect you.