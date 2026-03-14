
---

It is **Saturday, March 14, 2026**.

With **30 minutes** and **Medium** energy, today’s plan is optimized for **smart efficiency and infrastructure control**. We will tackle an Easy LeetCode problem that acts as a perfect capstone by combining two pointer techniques, followed by foundational server configuration management and security tools.

Here is your focused daily learning plan for **2026-03-14**.

---

# 📅 **Checklist_2026-03-14**

| **Category**         | **Task**                                                 | **Status** |
| -------------------- | -------------------------------------------------------- | ---------- |
| 🧠 LeetCode Practice | **234. Palindrome Linked List** (Two Pointers)           | ✅          |
| ⚙️ DevOps Essentials | **Infrastructure as Code: Ansible Playbooks vs. Ad-Hoc** | ✅          |
| 🐧 Linux Learning    | Command: **`ufw`** (Uncomplicated Firewall)              | ✅          |

---

## 🧠 LeetCode — **234. Palindrome Linked List** Tags: #LinkedList #TwoPointers #Logic

Difficulty: Easy (Medium cognitive load for the combination)

Why chosen:

- **Avoids Duplication:** This is entirely absent from your provided completion history.
    
- **Skill Synergy:** This is the ultimate "combo" problem. It perfectly stitches together two algorithms: finding the middle of a linked list (using fast/slow pointers) and reversing a linked list. Since it builds on foundational concepts, it is an excellent stretch for a Medium energy state without needing to learn a net-new data structure.
    

### 🎯 **Concept to learn today: The Split-and-Reverse Technique**

You are given the `head` of a singly linked list. You need to return `true` if it is a palindrome (reads the same forwards and backwards) or `false` otherwise.

- **The Strategy:** A linked list cannot be traversed backward easily. To achieve $O(1)$ space complexity, you must manipulate the list in place by finding the middle, reversing the second half, and then comparing the two halves node by node.
    
- **The Flow:**
    
    1. **Find the Middle:** Use the `slow` and `fast` pointer technique. When `fast` reaches the end, `slow` will be at the middle.
        
    2. **Reverse the Second Half:** Take the node at `slow` and perform standard linked list reversal to flip the pointers of the back half.
        
    3. **Compare:** Set a `left` pointer to the `head` and a `right` pointer to the start of your newly reversed second half. Move them inward, checking if `left.val == right.val`.
        
    4. _(Optional but best practice)_ **Restore:** Reverse the second half back to its original state so you don't permanently mutate the input data.
        
- **Why efficient?** Time complexity is $O(N)$ because you iterate through the nodes sequentially, and space complexity is $O(1)$ because you only use a few pointer variables.
    

---

## ⚙️ DevOps Essentials — **Infrastructure as Code (IaC): Ansible**

Tags: #DevOps #Ansible #Automation #Architecture

Goal: Understanding how to deploy and manage server configurations automatically rather than SSHing into machines manually.

### 1. The Push Model

Unlike tools that require an "agent" to be installed on the target server, Ansible uses a pure "Push" model. It runs from your control node (like a laptop) and connects to target servers securely over standard SSH.

### 2. Ad-Hoc Commands vs. Playbooks

- **Ad-Hoc Commands:** Great for quick, one-off tasks. For example, checking the uptime of 50 servers at once. They are run directly from the terminal.
    
- **Playbooks:** The true power of Ansible. These are YAML files that declare the _desired state_ of a server. Instead of writing a script that says "install Nginx," a playbook says "ensure Nginx is installed and running." If Nginx is already running perfectly, Ansible safely does nothing (this is called _idempotency_).
    

---

## 🐧 Linux Learning — Command: **`ufw`** (Uncomplicated Firewall)

Tags: #Linux #Command #ufw #Security #Networking

Why chosen:

- Securing a server is the immediate next step after deploying it. `ufw` is the standard, user-friendly frontend for managing iptables on Linux distributions, ensuring only the ports you want are exposed.
    

### 🎯 **Core Uses & Server Protection**

|**Scenario**|**Command**|**Sophistication**|
|---|---|---|
|**Check the Status**|**`sudo ufw status verbose`**|**Daily Driver.** Shows if the firewall is active and lists all current rules (e.g., which ports are open and closed).|
|**Allow Critical Access**|`sudo ufw allow ssh`|**Mandatory Step.** Always allow SSH (port 22) _before_ enabling the firewall, otherwise you will permanently lock yourself out of your own server.|
|**Enable the Shield**|`sudo ufw enable`|**Activation.** Turns the firewall on. By default, it will block all incoming connections (except the ones you explicitly allowed) and allow all outgoing connections.|

---

Would you like me to draft a quick, 5-line Ansible YAML task showing how to automatically install and enable `ufw` on a target server?