

---

# 📅 **2025-12-12 — Daily Learning Plan**

| **Category**                   | **Task**                                                              | **Status** |
| ------------------------------ | --------------------------------------------------------------------- | ---------- |
| 🧠 LeetCode Practice           | **118. Pascal's Triangle** (Dynamic Programming Foundation)           | ✅          |
| 🖥️ Server Building Essentials | **Lesson 3: The Fortress Mindset — 'Deny by Default' & UFW Strategy** | ✅          |
| 🐧 Linux Learning              | Command: **`nc`** (Netcat — The "Swiss Army Knife" of Networking)     | ✅          |

---

## 🧠 LeetCode — **118. Pascal's Triangle**

Tags: #Array #DynamicProgramming #Math

Difficulty: Easy

Why chosen:

- It is a visually intuitive introduction to **Dynamic Programming (DP)** logic: "The state of the current element depends on the state of previous elements."
    
- It requires precise **2D-Array indexing**, a skill often needed when handling matrix data or image processing buffers.
    

### 🎯 **Concept to learn today: "Memoization in Geometry"**

In Pascal's Triangle, each number is the sum of the two numbers directly above it.

- **The Logic:** `triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]`
    
- **The Edge Case:** The first and last element of every row are always `1`.
    
- **The Elegance:** Instead of calculating factorials (which is computationally expensive), you essentially "cache" the previous row's results to build the new row. This is the heart of efficient computing.
    

---

## 🖥️ Server Building Essentials — **Lesson 3: The Fortress Mindset (UFW)**

Tags: #Security #Firewall #UFW #SystemHardening

Goal: Move beyond "opening ports" to understanding Packet Filtering Strategy. We will configure the Uncomplicated Firewall (UFW) not just to work, but to distinguish legitimate traffic from noise.

### 1. **The Philosophy: "Deny by Default"**

A sophisticated server admin does not ask "What should I block?"

They ask: "What is the absolute minimum I must allow?"

- **Ingress (Incoming):** **DENY**. If a packet arrives that we didn't ask for, drop it silently.
    
- **Egress (Outgoing):** **ALLOW**. The server usually needs to fetch updates (apt/yum) or reach APIs.
    

### 2. **The Mechanism: Stateful Inspection**

UFW (an interface for `iptables`/`nftables`) is **stateful**.

- If you allow an _outgoing_ connection (e.g., `curl google.com`), the firewall automatically permits the _returning_ answer. You do not need to manually open ports for return traffic. This is a critical distinction from simple router ACLs.
    

### 3. **The Elegant Configuration (Rate Limiting)**

Instead of a binary "Open/Closed" for SSH, we use **Rate Limiting**.

- **The Problem:** Bots will hammer your SSH port 1000 times a minute.
    
- **The Elegant Fix:** `ufw limit ssh`.
    
    - This allows the connection _initially_, but if an IP addresses attempts to connect 6 times within 30 seconds, it is blocked. This filters out brute-force scripts while allowing your legitimate human login.
        

### 💡 **Actionable Task: The Hardening Sequence**

Run these commands in this **exact order** (to avoid locking yourself out):

1. Set Defaults:
    
    sudo ufw default deny incoming
    
    sudo ufw default allow outgoing
    
2. The Lifeline (Limit SSH):
    
	    sudo ufw limit 2222/tcp (Assuming you changed your port to 2222 in Lesson 1).
    
    - _Note: Using `limit` is more sophisticated than `allow`._
        
3. Enable:
    
    sudo ufw enable
    
4. Verify:
    
    sudo ufw status verbose (Look for "Logging: on (low)" and your rules).
    

---

## 🐧 Linux Learning — Command: **`nc` (Netcat)**

Tags: #Linux/Command/nc #Networking #Troubleshooting

Why chosen:

- You just built a Firewall (Lesson 3). Now you need a tool to **probe** that firewall from the outside to prove it works.
    
- `nc` is legendary. It allows you to read and write to network connections using TCP or UDP directly. It is the "debugger" for the network layer.
    

### 🎯 **Core Uses & The "Zero-I/O" Scan**

| **Scenario**                         | **Command**                                                    | **Sophistication**                                                                                                                                                                 |
| ------------------------------------ | -------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Port Scanning (The Gentle Probe)** | `nc -zv 192.168.1.50 22-80`                                    | **`-z` (Zero-I/O mode)**: Tells `nc` to scan for listening daemons without sending any data. **`-v`**: Verbose. This safely tells you if a port is "Open" or "Connection Refused." |
| **Test UDP Connectivity**            | `nc -zvu 192.168.1.50 123`                                     | Adds **`-u`**. Crucial for debugging things like DNS (53) or NTP (123) which don't use TCP.                                                                                        |
| **Chat Server (The Magic Trick)**    | `nc -l 1234` (Server)<br><br>  <br><br>`nc <IP> 1234` (Client) | Creates an instant raw text pipe between two computers. Great for testing if a firewall is dropping packets between two specific machines.                                         |

### 💡 **Practice Task: "Red Team" Your Server**

1. On your local laptop (or a second terminal), use `nc -zv <your_server_ip> 2222`.
    
    - _Expected:_ `Connection to ... port 2222 [tcp/*] succeeded!`
        
2. Now try a port you **didn't** open, like 8080: `nc -zv <your_server_ip> 8080`.
    
    - _Expected:_ The command should hang (if dropped) or say "Connection refused".
        
3. This confirms your "Deny by Default" policy is active.