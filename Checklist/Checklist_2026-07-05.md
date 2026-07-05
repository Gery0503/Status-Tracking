# 📅 **Checklist_2026-07-05**

| **Category**               | **Task**                                    | **Status** |
| -------------------------- | ------------------------------------------- | ---------- |
| 🧠 LeetCode Practice       | **94. Binary Tree Inorder Traversal** (DFS) | ✅          |
| ⚙️ DevOps Essentials       | **Ansible Basics: Jinja2 Templates**        | ✅          |
| 🐧 Linux Learning          | Command: **`wget`** (Network Downloader)    | ✅          |
| 🏭 **Dannie EMS Handbook** | **Factory Network Isolation (VLANs)**       | ✅          |

## 🧠 LeetCode — **94. Binary Tree Inorder Traversal** Tags: #BinaryTree #DFS #Stack

Difficulty: Easy

### 🎯 **Concept to learn today: The Left-Root-Right Pattern**

Given the `root` of a binary tree, return the _inorder_ traversal of its nodes' values.

- **The Strategy:** Tree traversals dictate the order in which you visit nodes. "Inorder" means you must visit the left child, then the parent (root), and finally the right child. For a Binary Search Tree (BST), an inorder traversal will magically return all the numbers in perfectly sorted ascending order.
    
- **The Flow (Recursive):**
    
    1. Create an empty array `result = []`.
        
    2. Define a helper function `traverse(node)`:
        
        - Base case: If `node` is `None`, just `return`.
            
        - Recursive step 1 (Left): Call `traverse(node.left)`.
            
        - Recursive step 2 (Root): Append the current node's value to the array: `result.append(node.val)`.
            
        - Recursive step 3 (Right): Call `traverse(node.right)`.
            
    3. Call `traverse(root)` and then return `result`.
        
- **Efficiency:** You visit every single node exactly once, giving a time complexity of $O(N)$. The space complexity is an interesting analysis: if the tree is perfectly balanced, the maximum depth of the call stack is $O(\log N)$. However, if the tree is completely skewed (essentially a linked list), the call stack will grow to $N$, meaning the worst-case extra memory space complexity is strictly $O(N)$.
    
- _Python Tip:_ If you add print statements to trace your recursive stack during practice, use Python 3.14's template strings (e.g., `print(t"Visiting node: {node.val}")`) for native, secure string evaluation!
    

## ⚙️ DevOps Essentials — **Ansible Basics: Jinja2 Templates**

Tags: #DevOps #Ansible #ConfigurationManagement

Goal: You know how to define servers (Inventory) and run commands (Playbooks). But what if you need to copy an `nginx.conf` file to 50 laptops, and _each_ laptop needs its own specific IP address written inside the file? You can't use a static file. You need a **Template**.

### 🎯 **Quick Review Summary: Dynamic Configuration**

Ansible uses a templating language called **Jinja2** (files end in `.j2`). You write a standard configuration file, but you leave "blank spaces" using double curly braces `{{ }}`. When Ansible runs, it dynamically injects the correct variables into those blanks before saving the final file on the target server.

|**Component**|**Description**|
|---|---|
|**The Template (`.j2`)**|A text file containing variables. Example: `listen {{ ansible_default_ipv4.address }}:80;`|
|**The `template` Module**|The Ansible task used in your playbook to process the `.j2` file and push it to the server.|
|**Fact Injection**|Ansible automatically fills in the blanks using the system "Facts" it gathered during the setup phase (which we learned about on May 23).|

### 💻 **Real-World Code Execution**

**1. Create `app_config.j2` on your Ansible controller:**

Ini, TOML

```
# Auto-generated database configuration
db_host = {{ database_ip }}
node_name = {{ inventory_hostname }}
```

**2. Run the Playbook task:**

YAML

```
- name: Deploy dynamic configuration file
  template:
    src: app_config.j2
    dest: /opt/app/config.ini
```

_(Ansible will read the template, inject the target laptop's specific hostname, and save the finalized text file cleanly onto the remote machine)._

## 🐧 Linux Learning — Command: **`wget`** (Network Downloader)

Tags: #Linux #Command #wget #Networking #SysAdmin

Goal: When working purely in a terminal on a factory server, you don't have a web browser to click "Download". `wget` allows you to pull files, scripts, and OS images directly from the internet or local network servers straight to your command line.

### 🎯 **Quick Review Summary: Terminal Downloading**

| **Scenario**            | **Command**                              | **Description**                                                                                                                                                          |
| ----------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Basic Download**      | **`wget http://10.10.5.5/image.iso`**    | **The Daily Driver.** Downloads the file directly into your current directory, keeping its original name.                                                                |
| **Resume a Download**   | `wget -c http://.../huge_file.zip`       | **The Lifesaver.** If your SSH session drops or the network blips at 99%, the `-c` (continue) flag resumes the download exactly where it left off instead of restarting. |
| **Save as Custom Name** | `wget -O setup.sh http://.../raw/script` | **Formatting.** The uppercase `-O` (Output document) forces the downloaded file to be saved under a specific name you choose.                                            |

## 🏭 Dannie EMS Handbook — **Factory Network Isolation (VLANs)**

Tags: #EMS #Manufacturing #Networking #Infrastructure

Goal: Understanding how we prevent network traffic jams and secure the hardware provisioning process on a massive factory floor.

### 🎯 **Core Concept: Virtualizing the Network (VLAN)**

When thinking about networking from scratch, imagine a physical Top-of-Rack (ToR) switch as a simple multi-plug extension cord. If 40 servers are plugged into it, they can all "hear" each other shouting data. On a factory floor, having thousands of servers shouting at once creates a massive traffic jam (a broadcast storm).

A **VLAN (Virtual Local Area Network)** is a software trick that slices one physical switch into multiple invisible, isolated switches.

- **The Segregation:** You can configure the ToR switch to say: "Ports 1-20 are VLAN 10. Ports 21-40 are VLAN 20."
    
- **The Invisible Wall:** Even though all the cables plug into the exact same physical metal box, a server on VLAN 10 is mathematically forbidden from talking to a server on VLAN 20 without going through a dedicated router. It is as if they are in completely different buildings.
    

### 🏢 **Factory Floor Application**

Why do we do this during L10/L11 integration?

1. **OOB Management:** You put the tiny BMC/IPMI motherboards (which we learned about last week) on a dedicated "Management VLAN." This ensures that even if the main OS network is completely flooded with data, you can always reach the power controls.
    
2. **PXE Booting:** OS installation files are massive. You put blank servers on a "Provisioning VLAN" so they can aggressively download their Golden Images without slowing down the factory's main database servers.