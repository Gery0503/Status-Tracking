# 📅 **Checklist_2026-07-14**

| **Category**               | **Task**                                   | **Status** |
| -------------------------- | ------------------------------------------ | ---------- |
| 🧠 LeetCode Practice       | **1108. Defanging an IP Address** (String) | ✅          |
| ⚙️ DevOps Essentials       | **Ansible Basics: Conditionals (`when`)**  | ✅          |
| 🐧 Linux Learning          | Command: **`history`** (Command Recall)    | ✅          |
| 🏭 **Dannie EMS Handbook** | **DHCP Option 82 (Relay Agent)**           | ✅          |

## 🧠 LeetCode — **1108. Defanging an IP Address** Tags: #String

Difficulty: Easy

### 💡 **My Intuition**

_Write down your thoughts, ideas, and insights here._

- **Observations:**
    
    1. The input is an IPv4 address formatted as a string.
        
    2. Strings in most programming languages (like Python) are immutable, meaning they cannot be changed in-place.
        
    3. Every instance of the `.` character needs to be replaced with `[.]`.
        
- **Edge cases:**
    
    - `Standard IPv4 format`: The problem guarantees a valid IPv4 address. Therefore, there are always exactly three periods, and we do not need to write complex regex to handle malformed inputs, missing numbers, or empty strings.
        
- **Expected approach and complexity:**
    
    1. Time: O(N) where N is the length of the string (we must look at every character once).
        
    2. Space: O(N) (a new string or character array must be allocated in memory to hold the longer modified result).
        

### 🎯 **Concept to learn today: Immutability and Replacement**

Given a valid (IPv4) IP address, return a defanged version of that IP address. A defanged IP address replaces every period `"."` with `"[.]"`.

- **The Strategy:** Since this is a low-energy session, do not overthink it with manual loops or character arrays. The goal is to leverage built-in language methods optimized in C. In Python, string replacement is handled natively and efficiently.
    
- **The Flow:**
    
    1. Take the input string `address`.
        
    2. Use the built-in string method to replace the target characters.
        
    3. Return `address.replace(".", "[.]")`.
        
- **Efficiency:** The built-in `.replace()` method traverses the string in a highly optimized C-level pass, yielding $O(N)$ time complexity and $O(N)$ space complexity.
    
- _Python Tip:_ When you want to print the final result to the terminal to verify it, remember to use Python 3.14's T-strings (e.g., `print(t"Defanged IP: {result}")`) instead of the older f-strings for secure, template-based rendering!
    

## ⚙️ DevOps Essentials — **Ansible Basics: Conditionals (`when`)**

Tags: #DevOps #Ansible #ConfigurationManagement #Automation

Goal: Your Ansible playbooks are getting smarter. But what if your playbook targets a mixed group of factory servers, half running Ubuntu and half running CentOS? You cannot run the `apt` installation command on a CentOS machine—it will crash. You need tasks to run conditionally.

### 🎯 **Quick Review Summary: Execution Gatekeepers**

Ansible uses the `when` keyword to evaluate system variables (Facts) or custom variables before executing a task. If the condition evaluates to `False`, Ansible gracefully skips the task and moves to the next one.

|**Syntax Component**|**Description**|
|---|---|
|**`when: condition`**|Added to the bottom of a task block. It acts as an IF statement.|
|**Fact Evaluation**|`when: ansible_distribution == "Ubuntu"` restricts the task to specific operating systems.|
|**Boolean Checks**|`when: is_database_node` will only run if you explicitly set that variable to `True` in your inventory file.|

### 💻 **Real-World Code Execution**

YAML

```
tasks:
  - name: Install Nginx via APT (Ubuntu/Debian)
    apt:
      name: nginx
      state: present
    # This task is completely skipped if the server is not Debian-based
    when: ansible_os_family == "Debian"

  - name: Install Nginx via YUM (CentOS/RedHat)
    yum:
      name: nginx
      state: present
    # This task takes over if the server is RedHat-based
    when: ansible_os_family == "RedHat"
```

## 🐧 Linux Learning — Command: **`history`** (Command Recall)

Tags: #Linux #Command #history #Productivity #SysAdmin

Goal: When managing factory infrastructure, you often type extremely long, complex commands (like an `ipmitool` hardware reboot string or a multi-flag `docker run`). Retyping them wastes energy and introduces typos. `history` is your terminal's built-in memory.

### 🎯 **Quick Review Summary: Terminal Time Travel**

Linux automatically records every command you type into a hidden file (usually `~/.bash_history`).

| **Scenario**             | **Command / Keystroke** | **Description**                                                                                                                                             |
| ------------------------ | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Search the Past**      | `history`               | `grep docker`                                                                                                                                               |
| **Execute by Number**    | `!105`                  | **The Shortcut.** Every command in `history` has a line number. Typing `!105` instantly re-runs exactly what is on line 105.                                |
| **Run the Last Command** | `sudo !!`               | **The Lifesaver.** If you run a command and get "Permission Denied", typing `sudo !!` immediately re-runs the exact last command, but with root privileges. |

## 🏭 Dannie EMS Handbook — **DHCP Option 82 (Relay Agent)**

Tags: #EMS #Manufacturing #Hardware #Networking #Provisioning

Goal: Understanding how the factory network automatically identifies exactly _where_ a server is physically located in a rack to assign it the correct IP address.

### 🎯 **Core Concept: Location-Based Intelligence**

We know that PXE booting uses DHCP to give a blank server an IP address. We also know that a Top-of-Rack (ToR) switch connects all these servers. But how does the central factory DHCP server know that the machine asking for an IP is physically plugged into "Port 12" on "Rack 4"?

It uses **DHCP Option 82** (The Relay Agent Information Option).

- **The Interception:** When a blank L10 server powers on, it shouts a DHCP request to the network. The ToR switch intercepts this shout.
    
- **The Injection:** Before passing the request along to the main factory router, the ToR switch literally opens the digital packet and injects an extra piece of data (Option 82). This data says: _"I am Switch #4, and this request came from Port #12."_
    
- **The Smart Assignment:** The central DHCP server reads Option 82. It checks its database: _"Ah, Port 12 on Switch 4 is designated for the Database Node. I will give it IP 10.10.5.212."_
    

### 🏢 **Factory Floor Application**

This is the holy grail of zero-touch provisioning. Because of Option 82, factory technicians do not need to manually configure IPs or scan MAC addresses for every single node. They simply bolt the server into Slot 12, plug the cable into Switch Port 12, and power it on. The network hardware handles the exact locational awareness, allowing your automated deployment scripts to target the correct machine every single time.