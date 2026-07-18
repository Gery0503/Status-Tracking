# 📅 **Checklist_2026-07-18**

| **Category**               | **Task**                                           | **Status** |
| -------------------------- | -------------------------------------------------- | ---------- |
| 🧠 LeetCode Practice       | **1672. Richest Customer Wealth** (Array / Matrix) | ✅          |
| ⚙️ DevOps Essentials       | **Ansible Basics: Loops (`loop`)**                 | ✅          |
| 🐧 Linux Learning          | Command: **`stat`** (Detailed File Metadata)       | ✅          |
| 🏭 **Dannie EMS Handbook** | **Network Bonding (LACP / Teaming)**               | ✅          |

## 🧠 LeetCode — **1672. Richest Customer Wealth** Tags: #Array #Matrix

Difficulty: Easy

### 💡 **My Intuition**

_Write down your thoughts, ideas, and insights here._

- **Observations:**
    
    1. The input is a 2D array (a matrix) where each row represents a single customer and the columns represent the money in their various bank accounts.
        
    2. The objective is simple: sum up the numbers in each row independently, and find the maximum resulting sum.
        
- **Edge cases:**
    
    - `1x1 Matrix`: The minimum possible constraint. The sum of the single row is just the single element, which becomes the maximum wealth automatically.
        
- **Expected approach and complexity:**
    
    1. Time: O(M * N) where M is the number of customers and N is the number of accounts. We must touch every single number once.
        
    2. Space: O(1) since we only need a single variable to track the highest sum found so far.
        

### 🎯 **Concept to learn today: 2D Array Iteration**

You are given an `m x n` integer grid `accounts` where `accounts[i][j]` is the amount of money the $i^{th}$ customer has in the $j^{th}$ bank. Return the wealth that the richest customer has.

- **The Strategy:** This is a pure iteration problem. You do not need to alter the data structure. You simply need an outer loop to walk through the customers (rows), and an inner loop to add up their money (columns). Keep a running tally of the highest sum you have seen.
    
- **The Flow:**
    
    1. Initialize `max_wealth = 0`.
        
    2. Loop through each `customer` (row) in `accounts`.
        
    3. Calculate the sum of the current `customer`'s accounts.
        
    4. If the current sum is greater than `max_wealth`, update `max_wealth`.
        
    5. Return `max_wealth`.
        
- **Efficiency:** You read every number in the grid exactly one time. Time complexity is $O(M \times N)$. Space complexity is optimized to $O(1)$.
    

## ⚙️ DevOps Essentials — **Ansible Basics: Loops (`loop`)**

Tags: #DevOps #Ansible #ConfigurationManagement #Automation

Goal: If your factory deployment playbook requires installing Docker, Nginx, Python, and Git, writing four separate Ansible tasks takes up unnecessary space and slows down the playbook execution. Ansible solves this with iterators.

### 🎯 **Quick Review Summary: DRY (Don't Repeat Yourself)**

The `loop` keyword allows you to run a single task multiple times with different values.

|**Syntax Component**|**Description**|
|---|---|
|**`loop:`**|Added to the bottom of a task. It accepts a standard list of items.|
|**`{{ item }}`**|The built-in variable Ansible uses to represent the current value in the loop during execution.|
|**List of Dictionaries**|You can loop over complex objects, not just strings (e.g., creating 5 different users with 5 different passwords).|

### 💻 **Real-World Code Execution**

YAML

```
tasks:
  - name: Install necessary deployment tools
    apt:
      name: "{{ item }}"
      state: present
    # Ansible will run the apt module 4 times in a row, swapping in these names
    loop:
      - docker.io
      - nginx
      - python3
      - git
```

## 🐧 Linux Learning — Command: **`stat`** (Detailed File Metadata)

Tags: #Linux #Command #stat #SysAdmin #Troubleshooting

Goal: Sometimes `ls -l` does not give you enough information. If an automated script is failing because it thinks a configuration file is outdated, you need to see exactly when that file was last modified or accessed down to the millisecond.

### 🎯 **Quick Review Summary: The Inode Inspector**

Every file in Linux has an "Inode"—a data structure that stores all the metadata about a file except its name and its actual content. `stat` reads this structure.

|**Scenario**|**Command**|**Description**|
|---|---|---|
|**The Deep Dive**|**`stat config.yaml`**|**The Daily Driver.** Displays the exact byte size, the Inode number, permissions in octal format (e.g., `0644`), and the exact timestamps.|
|**Access vs Modify**|_(Output Analysis)_|Shows **Access** (when it was last read), **Modify** (when the content was changed), and **Change** (when the permissions/ownership were changed).|
|**Format for Scripts**|`stat -c "%s" file.txt`|**Automation.** The `-c` flag formats the output. `%s` prints _only_ the file size in bytes, perfect for injecting into Bash scripts.|

## 🏭 Dannie EMS Handbook — **Network Bonding (LACP / Teaming)**

Tags: #EMS #Manufacturing #Hardware #Networking

Goal: Ensuring that a physical cable break or a port failure on a Top-of-Rack (ToR) switch does not take a localized factory cluster offline.

### 🎯 **Core Concept: Link Aggregation**

Enterprise servers never rely on a single physical network cable. When looking at the back of an L10 server, you will see multiple Ethernet or Fiber ports. **Network Bonding** (or Teaming) is the software configuration that binds these physical ports together into a single logical connection.

- **LACP (Link Aggregation Control Protocol):** The industry-standard protocol used to bundle these cables.
    
- **Redundancy (Active/Backup):** Port 1 handles 100% of the traffic. If a factory tech trips over Port 1's cable and rips it out, the OS instantly redirects all traffic to Port 2 without dropping the SSH session.
    
- **Load Balancing (Active/Active):** Port 1 and Port 2 both handle traffic simultaneously. If each port is 10Gbps, the server theoretically enjoys a 20Gbps data pipe.
    

### 🏢 **Factory Floor Application**

During L11 rack integration, automated provisioning scripts must configure the OS network interfaces (using tools like `netplan` or `NetworkManager`) to bond these physical interfaces together. If the automation successfully provisions the OS but fails to configure LACP, the rack violates high-availability standards and will fail its final outbound quality control check before shipping to the client's datacenter.