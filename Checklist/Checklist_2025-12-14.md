It is Sunday, December 14, 2025.

Since it is Sunday, we will focus on **Automation**. The mark of a sophisticated engineer is not how much work they do, but how much work they _automate_. Today, we will make your server self-maintaining and teach you the time-based job scheduler of Linux.

Here is your daily learning plan for **2025-12-14**.

---

# 📅 **2025-12-14 — Daily Learning Plan**

| **Category**                   | **Task**                                                       | **Status** |
| ------------------------------ | -------------------------------------------------------------- | ---------- |
| 🧠 LeetCode Practice           | **832. Flipping an Image** (Matrix Manipulation + Bitwise XOR) | ✅          |
| 🖥️ Server Building Essentials | **Lesson 5: The Self-Healing Fortress (Unattended Upgrades)**  | ✅          |
| 🐧 Linux Learning              | Command: **`crontab`** (Automated Task Scheduling)             | ✅          |

---

## 🧠 LeetCode — **832. Flipping an Image**

Tags: #Array #Matrix #BitManipulation #Simulation

Difficulty: Easy

Why chosen:

- It combines two skills you have practiced recently: **Reversing Arrays** (from _Rotate Array_) and **Bitwise Inversion** (XOR).
    
- It requires you to manipulate a 2D Matrix row-by-row, reinforcing nested loop logic.

### 🎯 **Concept to learn today: "Composite Manipulation"**

The problem asks you to take a binary matrix, **flip** it horizontally (reverse each row), and then **invert** it ($0 \to 1$, $1 \to 0$).

- **The Elegant Approach:** You can do both steps in a single pass.
    
- **The Bitwise Trick:** To invert a binary value (`0` or `1`), you don't need an `if/else` statement. You can use **XOR**:
    
    - `1 ^ 1 = 0`
        
    - `0 ^ 1 = 1`
        
    - So, `value = value ^ 1` toggles the bit instantly.
        

---

## 🖥️ Server Building Essentials — **Lesson 5: The Self-Healing Fortress**

Tags: #Automation #Security #Maintenance #UnattendedUpgrades

Goal: A "Fortress" that requires manual patching is vulnerable the moment you go to sleep. We will configure the server to patch itself automatically and reboot gracefully only when necessary. This is "Zero-Touch" maintenance.

### 1. **The Tool: `unattended-upgrades`**

Most beginners run sudo apt update && sudo apt upgrade manually.

Sophisticated admins install unattended-upgrades. This service runs in the background, checks for Security Updates (ignoring feature updates to maintain stability), installs them, and can even remove unused kernels to save space.

### 2. **The Configuration: `/etc/apt/apt.conf.d/50unattended-upgrades`**

You don't just "turn it on"; you tune it.

- **The Origins:** Ensure only `"${distro_id}:${distro_codename}-security";` is enabled. We want security patches, not experimental features.
    
- **The Reboot Strategy:** The most critical setting.
    
    - `Unattended-Upgrade::Automatic-Reboot "true";`
        
    - `Unattended-Upgrade::Automatic-Reboot-Time "03:00";`
        
- **The Result:** If a critical Kernel vulnerability is found on Tuesday, your server patches itself and reboots at 3:00 AM Wednesday while you are sleeping. You wake up to a secure system.
    

### 💡 **Actionable Task: Verify the Pulse**

1. Install the package: `sudo apt install unattended-upgrades`.
    
2. Enable the background configuration: `sudo dpkg-reconfigure -plow unattended-upgrades`.
    
3. **The Pro Check:** The logs for this are _not_ in `journalctl`. They are in a specific text file.
    
    - Run: `cat /var/log/unattended-upgrades/unattended-upgrades.log`
        
    - If the file is empty, you can force a dry-run to prove it works:
        
        sudo unattended-upgrade --dry-run --debug
        

---

## 🐧 Linux Learning — Command: **`crontab`**

Tags: #Linux/Command/cron #Automation #Scheduling

Why chosen:

- You just learned about automatic upgrades. Now you need a generic tool to automate _anything_ else (backups, log cleanup, custom scripts).
    
- `cron` is the heartbeat of a Linux server.
    

### 🎯 **Core Uses & The "Five Star" Syntax**

|**Syntax**|**Meaning**|**Example**|
|---|---|---|
|`* * * * *`|Minute, Hour, Day-of-Month, Month, Day-of-Week|The sequence of 5 stars defining "when".|
|`0 3 * * *`|"At Minute 0 of Hour 3 (3:00 AM), every day."|Standard time for heavy tasks (backups).|
|`*/5 * * * *`|"Every 5 minutes."|Useful for monitoring scripts.|
|`@reboot`|"Run once when the server starts."|Useful for starting custom scripts that aren't systemd services.|

### 💡 **Practice Task: The "Alive" Signal**

1. Open your user's schedule: `crontab -e` (select `nano` if asked).
    
2. Add a line that writes the date to a file every minute:
    
    \* * * * * date >> /home/youruser/heartbeat.log
    
3. Save and exit.
    
4. Wait 2 minutes. Check the file: `cat ~/heartbeat.log`.
    
5. **Important Cleanup:** Run `crontab -e` again and **delete the line**. If you forget, your file will grow forever and fill the disk. This teaches you the danger of unchecked logs!