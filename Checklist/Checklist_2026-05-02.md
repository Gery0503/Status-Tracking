# 📅 **Checklist_2026-05-02**

| **Category**               | **Task**                                         | **Status** |
| -------------------------- | ------------------------------------------------ | ---------- |
| 🧠 LeetCode Practice       | **13. Roman to Integer** (String Parsing / Math) | ✅          |
| ⚙️ DevOps Essentials       | **Ansible Basics: The Inventory File**           | ✅          |
| 🐧 Linux Learning          | Command: **`dmesg`** (Kernel & Hardware Logs)    | ✅          |
| 🏭 **Dannie EMS Handbook** | **PXE Boot (Preboot eXecution Environment)**     | ✅          |

---

## 🧠 LeetCode — **13. Roman to Integer** Tags: #Math #String #HashTable

Difficulty: Easy

### 🎯 **Concept to learn today: Look-Ahead Subtraction**

Given a roman numeral string (e.g., `"MCMXCIV"`), convert it to an integer.

- **The Strategy:** Roman numerals are usually written largest to smallest from left to right (e.g., `XII` is `10 + 1 + 1`). The only exception is when a smaller numeral is placed _before_ a larger one to indicate subtraction (e.g., `IV` is `5 - 1 = 4`). Instead of writing complex nested `if` statements, you just need a simple look-ahead rule: if the current letter's value is strictly _less_ than the next letter's value, you subtract it. Otherwise, you add it.
    
- **The Flow:**
    
    1. Create a Hash Map of the roman values: `{'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}`.
        
    2. Initialize `total = 0`.
        
    3. Loop through the string using an index `i` from `0` to `len(s) - 1`.
        
    4. Inside the loop, check the rule: `if i + 1 < len(s)` AND `value[s[i]] < value[s[i+1]]`:
        
        - Subtract the current value: `total -= value[s[i]]`.
            
    5. Else:
        
        - Add the current value: `total += value[s[i]]`.
            
    6. Return `total`.
        
- **Efficiency:** You read the string exactly once from left to right, making the time complexity $O(N)$. The dictionary is fixed at 7 characters, meaning space complexity is $O(1)$. It's an elegant, low-energy mental exercise in rule simplification.
    

---

## ⚙️ DevOps Essentials — **Ansible Basics: The Inventory File**

Tags: #DevOps #Ansible #ConfigurationManagement #Automation

Goal: Jenkins is great for building and testing code, but what about managing the servers themselves? When utilizing laptops as localized servers to support factory services, or managing dozens of L11 rack nodes, you need a way to configure them simultaneously without SSH-ing into each one manually. Ansible solves this, and it begins with the **Inventory**.

### 🎯 **Quick Review Summary: Defining Your Fleet**

Ansible is "agentless." You don't need to install anything on the target servers; it just uses standard SSH. To tell Ansible _which_ servers to connect to, you write an Inventory file (usually named `hosts` or `inventory.ini`).

|**Syntax Component**|**Real-World Example**|**Description**|
|---|---|---|
|**Ungrouped Hosts**|`192.168.1.50`|A raw IP address sitting at the top of the file. Good for one-off tests.|
|**Groups**|`[factory_iss_nodes]`|Bracketed labels that let you group servers by function, allowing you to deploy configurations to specific clusters at once.|
|**Host Variables**|`node1 ansible_host=10.0.0.5`|Assigning a friendly alias (`node1`) to a raw IP so your output logs are human-readable.|

### 💻 **Real-World Code Execution**

Here is what a standard, simple Ansible `inventory.ini` file looks like for a factory floor setup:

Ini, TOML

```
# A group specifically for the servers/laptops
[cluster]
node-01 ansible_host=10.10.5.101 ansible_user=root
node-02 ansible_host=10.10.5.102 ansible_user=root

# A group for the factory database
[factory_db]
10.10.5.200 ansible_user=admin

# A parent group that encompasses both
[taiwan_site:children]
cluster
factory_db
```

_(With this file saved, typing `ansible cluster -m ping` in your terminal will instantly ping all your localized servers at once)._

---

## 🐧 Linux Learning — Command: **`dmesg`** (Kernel Ring Buffer)

Tags: #Linux #Command #dmesg #Hardware #SysAdmin

Goal: When working with physical servers on a factory floor, you aren't just debugging software—you are debugging bare-metal hardware. `dmesg` (Diagnostic Message) allows you to read the literal "mind" of the Linux kernel to see exactly what hardware it is detecting, failing to detect, or complaining about.

### 🎯 **Quick Review Summary: Reading Hardware Logs**

When a server boots up or new hardware is plugged in, the kernel writes highly technical messages to a temporary memory space called the "Ring Buffer".

|**Scenario**|**Command**|**Description**|
|---|---|---|
|**Human Readable Time**|**`dmesg -T`**|**Daily Driver.** By default, `dmesg` prints timestamps in "seconds since boot". The `-T` flag translates those into standard calendar dates and times.|
|**Filter by Severity**|`dmesg --level=err,crit`|**Burn-in Diagnostics.** Filters out the boot noise and _only_ shows critical hardware errors (like Machine Check Exceptions, RAM faults, or thermal throttling).|
|**Live Hot-Swapping**|`dmesg -w`|**Hardware Integration.** The `-w` (watch) flag keeps the stream open. Perfect for watching the kernel react in real-time when a factory tech plugs in a new drive or network cable.|

### 💻 **Real-World Terminal Example**

1. A factory tech plugs a USB drive into a server, but it isn't showing up in the filesystem. You use `dmesg` to see if the kernel even registered the physical electrical connection.
    
2. You run the command and check the last few lines.
    

Bash

```
$ dmesg -T | tail -n 5
[Sat May  2 10:14:22 2026] usb 2-1: new high-speed USB device number 4 using xhci_hcd
[Sat May  2 10:14:23 2026] usb-storage 2-1:1.0: USB Mass Storage device detected
[Sat May  2 10:14:23 2026] scsi host4: usb-storage 2-1:1.0
[Sat May  2 10:14:24 2026] sd 4:0:0:0: [sdb] 30253056 512-byte logical blocks: (15.5 GB/14.4 GiB)
[Sat May  2 10:14:24 2026]  sdb: sdb1
```

_(The output proves the hardware works perfectly and the drive is mounted at `sdb1`. If it's not showing up in the OS, it's a software mounting issue, not a broken USB port)._

---

## 🏭 Dannie EMS Handbook — **PXE Boot (Preboot eXecution Environment)**

Tags: #EMS #Manufacturing #Hardware #Provisioning

Goal: Understanding how to mass-deploy operating systems to hundreds of bare-metal factory servers simultaneously without using a single physical USB drive.

### 🎯 **Core Concept: Network Booting**

When a fresh server rolls off the assembly line at the L10 stage, its hard drives are completely blank. It has no OS. **PXE Boot** (pronounced "Pixie Boot") is an industry-standard protocol built directly into the server's network card (NIC) that allows it to download and install its operating system directly over the factory network.

- **The DHCP Handshake:** When the blank server is powered on, the NIC broadcasts a request for an IP address. The factory's DHCP server replies with an IP, _and_ provides the location of the PXE Server.
    
- **The TFTP Transfer:** The server then connects to the PXE Server using TFTP (Trivial File Transfer Protocol) to download a tiny, lightweight bootloader image (like `pxelinux`).
    
- **The Kickstart:** This bootloader pulls down the full OS installation files (like Ubuntu or Oracle Linux) and an automated configuration script (often called a Kickstart or Preseed file) that formats the drives and installs the OS completely unattended.
    

### 🏢 **Factory Floor Application**

If you are managing the networking services via Docker containers for your localized server deployments, ensuring the TFTP and DHCP services are correctly configured and containerized is the exact mechanism that enables a seamless, zero-touch L10 integration line. If PXE fails, the entire factory line stops because the hardware cannot be brought to life.