# 📅 **Checklist_2026-05-03**

| **Category**               | **Task**                                     | **Status** |
| -------------------------- | -------------------------------------------- | ---------- |
| 🧠 LeetCode Practice       | **258. Add Digits** (Math / Number Theory)   | ✅          |
| ⚙️ DevOps Essentials       | **Ansible Basics: The Playbook**             | ✅          |
| 🐧 Linux Learning          | Command: **`uptime`** (System Load Averages) | ✅          |
| 🏭 **Dannie EMS Handbook** | **MAC Address Harvesting**                   | ✅          |

---

## 🧠 LeetCode — **258. Add Digits** Tags: #Math #NumberTheory

Difficulty: Easy

### 🎯 **Concept to learn today: The Digital Root (O(1) Math Trick)**

Given an integer `num`, repeatedly add all its digits until the result has only one digit, and return it. For example, if `num = 38`, the process is $3 + 8 = 11$, and then $1 + 1 = 2$. Return `2`.

- **The Strategy:** The brute-force way is to use a `while` loop to convert the number to a string, split it, add the digits, and repeat until the length is 1. However, since energy is low today, we will learn the mathematical "cheat code." This specific process calculates what mathematicians call the **Digital Root**. The digital root of a base-10 integer is simply the remainder when that number is divided by 9.
    
- **The Flow:**
    
    Instead of looping, you can solve this instantly using Modulo arithmetic (`%`).
    
    1. Base case: If `num == 0`, return `0`.
        
    2. Check the exact multiple case: If `num % 9 == 0`, the digital root is always `9`. (e.g., 18: $1+8=9$. 27: $2+7=9$).
        
    3. For everything else: Return `num % 9`.
        
        _You can compress this into a single line of logic:_ `return 0 if num == 0 else (9 if num % 9 == 0 else num % 9)`
        
- **Efficiency:** Because you skip the loops entirely and just perform a single mathematical division operation, the time complexity is a perfectly flat $O(1)$. Space complexity is also $O(1)$.
    

---

## ⚙️ DevOps Essentials — **Ansible Basics: The Playbook**

Tags: #DevOps #Ansible #ConfigurationManagement #Automation

Goal: Yesterday, you learned how to define your fleet of servers using the Inventory file. Today, we move from defining _where_ to run commands to defining _what_ commands to run. You do this by writing a **Playbook**.

### 🎯 **Quick Review Summary: Declarative Automation**

Unlike a Bash script which tells Linux _how_ to do something step-by-step, an Ansible Playbook is written in YAML and tells Ansible the _desired state_. Ansible figures out how to make it happen safely (making it "idempotent"—safe to run multiple times).

| **Playbook Component** | **Description**                                                                                                                           |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **`hosts:`**           | Tells the playbook which group from your Inventory file to target (e.g., `hosts: cluster`).                                               |
| **`become: yes`**      | The Ansible equivalent of running `sudo`. Elevates privileges to root to install software.                                                |
| **`tasks:`**           | The list of actions to perform.                                                                                                           |
| **Modules**            | Built-in Ansible tools used inside tasks. E.g., the `apt` module installs packages; the `service` module starts/stops background daemons. |

### 💻 **Real-World Code Execution**

Here is a conceptual look at a `setup.yml` playbook that installs and starts Docker across your entire cluster.

YAML

```
---
- name: Configure Factory Nodes
  hosts: cluster
  become: yes

  tasks:
    - name: Ensure Docker is installed
      apt:
        name: docker.io
        state: present

    - name: Ensure Docker daemon is running
      service:
        name: docker
        state: started
        enabled: yes
```

_(By running `ansible-playbook setup.yml`, Ansible logs into all your laptops simultaneously, checks if Docker is there, installs it if it isn't, and ensures the service is running)._

---

## 🐧 Linux Learning — Command: **`uptime`** (System Load Averages)

Tags: #Linux #Command #uptime #SysAdmin #Performance

Goal: When a factory server is running sluggishly or a deployment is timing out, you need a 1-second way to check if the CPU is drowning in tasks. `uptime` provides this instantly.

### 🎯 **Quick Review Summary: Reading the Load**

When you type `uptime` in the terminal, you get a single line of output that ends with three very specific numbers: **The Load Average**.

|**Metric**|**Description**|**Best Use Case**|
|---|---|---|
|**1-Minute Load**|The first number.|**Immediate Spikes.** Did deploying that container just now lock up the system?|
|**5-Minute Load**|The second number.|**Trend checking.** Has the system been struggling for a little while?|
|**15-Minute Load**|The third number.|**Long-term health.** Is the server fundamentally under-powered for its current workload?|

### 💻 **Real-World Terminal Example**

1. You SSH into an L10 diagnostic server that feels unresponsive. You type `uptime`.
    

Bash

```
$ uptime
 10:45:12 up 14 days,  3:12,  2 users,  load average: 4.50, 1.15, 0.30
```

**How to interpret this like a SysAdmin:**

- Load averages represent the number of processes waiting for CPU time.
    
- **The Rule of 1.0:** A load of `1.0` means one single CPU core is exactly 100% utilized.
    
- If this server has a **4-core CPU**, a 1-minute load of `4.50` means the server is currently overwhelmed (4.5 > 4.0), and 0.5 processes are "waiting in line."
    
- Looking at the 15-minute load (`0.30`), the server was totally fine 15 minutes ago. This tells you a sudden, massive task just hit the CPU in the last minute.
    

---

## 🏭 Dannie EMS Handbook — **MAC Address Harvesting**

Tags: #EMS #Manufacturing #Hardware #Networking

Goal: Understanding how we bridge the physical hardware to the logical factory network so PXE Booting can be targeted and automated.

### 🎯 **Core Concept: The Hardware-to-IP Map**

Yesterday, we learned that PXE Booting uses DHCP to give a blank server an IP address and an OS image. But on a factory floor with hundreds of servers powering on simultaneously, how does the DHCP server know _which_ server gets the Database image and _which_ server gets the Web Server image? It relies on the **MAC Address**.

- **The Unique Identifier:** Every Network Interface Card (NIC) in the world has a hardcoded, unique physical MAC address (e.g., `00:1A:2B:3C:4D:5E`).
    
- **Harvesting:** During early physical assembly, factory technicians use barcode scanners to scan the sticker on the motherboard/NIC. This MAC address is instantly uploaded to the factory's Shop Floor Control (SFC) database.
    
- **DHCP Reservations:** The deployment automation scripts pull those scanned MAC addresses and pre-configure the DHCP server.
    

### 🏢 **Factory Floor Application**

When you power on a freshly racked L10 server, it shouts its MAC address to the network. Because you already _harvested_ that MAC and updated the DHCP configuration, the network says: _"Ah, MAC 00:1A:2B... you are designated to be Node 5 in the cluster. Here is IP 10.10.5.105, and here is your specific Ubuntu Kickstart file."_ Without MAC harvesting, automated, targeted bare-metal deployment is impossible.