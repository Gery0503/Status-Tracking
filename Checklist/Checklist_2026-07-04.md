# 📅 **Checklist_2026-07-04**

| **Category**               | **Task**                                                | **Status** |
| -------------------------- | ------------------------------------------------------- | ---------- |
| 🧠 LeetCode Practice       | **263. Ugly Number** (Math)                             | ✅          |
| ⚙️ DevOps Essentials       | **Ansible Basics: Ansible Vault**                       | ✅          |
| 🐧 Linux Learning          | Command: **`mount` / `umount`** (Filesystem Attachment) | ✅          |
| 🏭 **Dannie EMS Handbook** | **Top-of-Rack (ToR) Switches**                          | ✅          |

## 🧠 LeetCode — **263. Ugly Number** Tags: #Math

Difficulty: Easy

### 🎯 **Concept to learn today: Prime Factorization (Greedy Division)**

An **ugly number** is a positive integer whose prime factors are limited to `2`, `3`, and `5`. Given an integer `n`, return `True` if `n` is an ugly number.

- **The Strategy:** Instead of trying to find all prime factors of `n` (which is computationally expensive), you can use a greedy subtraction/division method. If a number is truly only made up of 2s, 3s, and 5s, then you should be able to continuously divide it by those numbers until you are left with exactly `1`.
    
- **The Flow:**
    
    1. Base case: If `n <= 0`, return `False` (ugly numbers are strictly positive).
        
    2. Loop through the allowed factors: `for factor in [2, 3, 5]:`
        
    3. Inside the loop, use a `while` loop to continuously divide `n` by the factor as long as there is no remainder (`n % factor == 0`).
        
        - `n = n // factor`
            
    4. After dividing out all possible 2s, 3s, and 5s, check what is left.
        
    5. If `n == 1`, return `True`. If anything else is left, it means there was another prime factor hiding inside it (like 7 or 11), so return `False`.
        
- **Efficiency:** You are aggressively dividing the number down, meaning the time complexity is $O(\log N)$. Space complexity is a perfectly flat $O(1)$. It is a very satisfying, low-energy mental loop.
    
- _Python Tip:_ If you were printing debug statements for this on Python 3.14+, you could use the new t-strings for clean template rendering (e.g., `print(t"Remaining value: {n}")`), avoiding the older f-string syntax.
    

## ⚙️ DevOps Essentials — **Ansible Basics: Ansible Vault**

Tags: #DevOps #Ansible #Security #SecretManagement

Goal: In previous sessions, we used Jenkins Credentials Binding to hide secrets. But when writing Ansible Playbooks (which are often stored in plain-text Git repositories), how do you store the root passwords needed to provision localized nodes? **Ansible Vault** encrypts these secrets directly inside your codebase.

### 🎯 **Quick Review Summary: Encrypted Playbooks**

Ansible Vault uses AES256 encryption to turn standard YAML variables into unreadable cryptographic hashes. You can encrypt entire files or just specific string variables.

|**Scenario**|**Command**|**Description**|
|---|---|---|
|**Create a Secret File**|**`ansible-vault create secrets.yml`**|**The Daily Driver.** Prompts you for a master password, then opens a text editor. Anything you save here is fully encrypted on disk.|
|**Edit Existing Secrets**|`ansible-vault edit secrets.yml`|**Maintenance.** Decrypts the file into a temporary editor, lets you change the database password, and re-encrypts it on save.|
|**Run the Playbook**|`ansible-playbook setup.yml --ask-vault-pass`|**Execution.** Tells Ansible to prompt you for the master password at runtime so it can unlock the `secrets.yml` file and inject the variables into the target servers.|

### 💻 **Real-World Code Execution**

Instead of writing `db_password: "admin123"` in plain text, you store it in your Vault. When the playbook runs, Ansible dynamically decrypts it in memory to authenticate against the target machine, ensuring the client credentials never leak into your Git commits.

## 🐧 Linux Learning — Command: **`mount` / `umount`** (Filesystem Attachment)

Tags: #Linux #Command #mount #Hardware #SysAdmin

Goal: When working with physical servers on a factory floor, plugging in a USB drive or attaching a network drive doesn't automatically make it pop up on your desktop like it does in Windows. In Linux, you have to manually "mount" the hardware to a specific folder to read its contents.

### 🎯 **Quick Review Summary: Bridging Hardware and Folders**

|**Scenario**|**Command**|**Description**|
|---|---|---|
|**View Attached Drives**|**`lsblk`**|Lists all block storage devices (hard drives, USBs) so you can find the device name (like `/dev/sdb1`).|
|**Attach the Drive**|`sudo mount /dev/sdb1 /mnt/usb`|**The Action.** Tells the kernel to map the physical USB partition (`/dev/sdb1`) to the empty folder `/mnt/usb`.|
|**Safely Eject**|`sudo umount /mnt/usb`|**Crucial.** Un-mounts the drive. If you pull a USB out before running this, data corruption is highly likely.|

### 💻 **Real-World Terminal Example**

1. You plug in a USB containing a Golden Image ISO to a bare-metal L10 server. You check the system logs (`dmesg`) and see the kernel assigned it the name `/dev/sdc1`.
    
2. You create a temporary folder and mount the drive to it.
    

Bash

```
$ sudo mkdir -p /media/golden_image
$ sudo mount /dev/sdc1 /media/golden_image
```

3. You can now use `cd /media/golden_image` to browse the files.
    

## 🏭 Dannie EMS Handbook — **Top-of-Rack (ToR) Switches**

Tags: #EMS #Manufacturing #Hardware #Networking

Goal: Understanding the physical network architecture that bridges individual, isolated L10 servers into a unified, communicative L11 cluster.

### 🎯 **Core Concept: The L11 Bridge**

If you have no prior experience with network topology, the concept of a Top-of-Rack (ToR) switch is visually exactly what it sounds like. It is a high-speed, enterprise-grade network switch physically bolted into the very top slot (usually "U41" or "U42") of a server rack.

- **L10 Isolation:** During L10 integration, each server in the rack is just an isolated box. It might have an OS, but it cannot talk to the server sitting directly beneath it.
    
- **The ToR Cable Matrix:** To transition to L11, technicians run short Ethernet or Fiber optic cables from the Network Interface Cards (NICs) of every single server in the rack directly up to the ToR switch.
    
- **The Gateway:** The ToR switch becomes the local "brain" of the rack. If Server 1 wants to talk to Server 15, the data goes up the cable to the ToR switch, and right back down.
    

### 🏢 **Factory Floor Application**

When you write software to support L11 deployments for clients, your code must often reach out to the ToR switch first to configure VLANs (Virtual Local Area Networks) or enable DHCP relays. The entire rack essentially becomes a single localized network, heavily relying on the ToR switch to route internal traffic smoothly before connecting the entire rack to the broader datacenter backbone.