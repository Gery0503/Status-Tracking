# 📅 **Checklist_2026-07-21**

| **Category**               | **Task**                                               | **Status** |
| -------------------------- | ------------------------------------------------------ | ---------- |
| 🧠 LeetCode Practice       | **1773. Count Items Matching a Rule** (Array / String) | ✅          |
| ⚙️ DevOps Essentials       | **Docker Compose: Multi-Service (Samba & Relay)**      | ✅          |
| 🐧 Linux Learning          | Command: **`arp`** (Address Resolution Protocol)       | ✅          |
| 🏭 **Dannie EMS Handbook** | **The Interim Server Solution**                        | ✅          |

## 🧠 LeetCode — **1773. Count Items Matching a Rule** Tags: #Array #String

Difficulty: Easy

### 💡 **My Intuition**

_Write down your thoughts, ideas, and insights here._

- **Observations:**
    
    1. The input is an array of arrays. Each inner array always has exactly 3 elements: `[type, color, name]`.
        
    2. We are given a `ruleKey` (which will be "type", "color", or "name") and a `ruleValue` (the string we need to match).
        
    3. Instead of checking a bunch of `if/else` statements for every item, we can map the `ruleKey` to an exact index (0, 1, or 2) upfront.
        
- **Edge cases:**
    
    - `No matches`: The loop should naturally complete and return 0. String matching is strictly case-sensitive.
        
- **Expected approach and complexity:**
    
    1. Time: O(N) where N is the number of items. We only need to iterate through the list once.
        
    2. Space: O(1) as we only need a single integer to keep the count, plus a small dictionary for the key mapping.
        

### 🎯 **Concept to learn today: Index Mapping**

You are given an array `items`, where each `items[i] = [type, color, name]`, and two strings `ruleKey` and `ruleValue`. Return the number of items that match the given rule.

- **The Strategy:** Avoid writing a nested loop or a massive `if-elif-else` block inside your main loop. Determine which index (0, 1, or 2) the `ruleKey` refers to _before_ the loop starts. Then, you only have to check that single index for each item.
    
- **The Flow:**
    
    1. Create a hash map for the rules: `mapping = {"type": 0, "color": 1, "name": 2}`.
        
    2. Find the target index: `target_idx = mapping[ruleKey]`.
        
    3. Initialize a `count = 0`.
        
    4. Loop through each `item` in `items`:
        
        - If `item[target_idx] == ruleValue`, increment `count`.
            
    5. Return `count`.
        
- **Efficiency:** Traversing the array once guarantees $O(N)$ time complexity. Because the mapping dictionary is fixed at exactly 3 keys regardless of the input size, the space complexity is a highly optimized $O(1)$.
    

## ⚙️ DevOps Essentials — **Docker Compose: Multi-Service (Samba & Relay)**

Tags: #DevOps #Docker #Networking #Containers

Goal: Running a single container is easy. But when building out automated infrastructure, you often need multiple containers communicating with each other or the host network simultaneously. **Docker Compose** allows you to define and spin up entire environments using a single YAML file.

### 🎯 **Quick Review Summary: Infrastructure as Code**

Instead of typing long `docker run` commands with a dozen flags, you declare your services in a `docker-compose.yml` file.

When preparing local deployment scripts to hand over to colleague, packaging the required network tools in a Compose file ensures they can spin up the environment with zero dependency issues.

| **Service**       | **Factory Function**                                                                        | **Docker Implementation Focus**                                                                                                                                   |
| ----------------- | ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`samba` (SMB)** | Hosts the massive Golden Image OS files for the servers to download over the local network. | **Volume Mapping.** The container must mount a directory from the host laptop so it can actually serve the ISO files to the network.                              |
| **`dhcp-relay`**  | Forwards PXE boot broadcast requests across VLANs to the main DHCP server.                  | **Network Mode.** By default, Docker isolates containers. A relay _must_ use `network_mode: "host"` so it can hear physical hardware broadcasts on the local LAN. |

### 💻 **Real-World Code Execution**

Here is a conceptual `docker-compose.yml` to spin up a local provisioning environment.

YAML

```
version: '3.8'

services:
  # The File Share Service
  samba:
    image: dperson/samba
    ports:
      - "139:139"
      - "445:445"
    volumes:
      # Maps the laptop's local images folder into the container
      - /opt/factory_images:/mnt:ro
    command: '-s "images;/mnt;yes;no;yes;all"'

  # The Network Relay Service
  dhcp-relay:
    image: networkboot/dhcp-relay
    # CRITICAL: Bypasses Docker's virtual network to listen to physical cables
    network_mode: "host" 
    command: ["-i", "eth0", "10.10.5.200"] # Forwards requests to main DHCP server
```

_(Running `docker-compose up -d` brings both services online instantly in the background)._

## 🐧 Linux Learning — Command: **`arp`** (Address Resolution Protocol)

Tags: #Linux #Command #arp #Networking #Troubleshooting

Goal: You know that DHCP assigns an IP address to a MAC address. But how does your specific laptop know which MAC address belongs to the IP `10.10.5.50` when it tries to send a packet? The Linux kernel maintains an internal map called the ARP cache.

### 🎯 **Quick Review Summary: The IP-to-MAC Map**

|**Scenario**|**Command**|**Description**|
|---|---|---|
|**View the Cache**|**`arp -a`**|**The Daily Driver.** Prints the local ARP table, showing which IP addresses your machine has recently resolved to physical MAC addresses.|
|**Clear the Cache**|`sudo ip -s -s neigh flush all`|**Troubleshooting.** If a server's motherboard was replaced but it kept the same IP, your laptop will fail to connect because it has the _old_ MAC address cached. This clears it.|
|**Specific Lookup**|`arp -n 192.168.1.100`|Queries the cache for one specific IP without trying to resolve DNS hostnames.|

## 🏭 Dannie EMS Handbook — **The Interim Server Solution **

Tags: #EMS #Manufacturing #Architecture #Provisioning

Goal: Tying together Docker, Samba, and DHCP Relays into the physical reality of offline rack deployment.

### 🎯 **Core Concept: The Mobile Provisioning Brain**

Often, L10 bare-metal integration happens in a secure or isolated area of the factory floor where there is no direct, high-speed connection to the central enterprise servers. You cannot PXE boot 40 servers if the Golden Image is sitting on a server three buildings away over a slow link.

The solution is the Interim Server Solution.

- **The Hardware:** This is usually a heavy-duty, localized server that is physically rolled on a crash cart and plugged directly into the rack's Top-of-Rack (ToR) switch.
    
- **The Software:** The server runs Docker. Using Docker Compose (as seen above), it spins up localized, temporary versions of core factory services right next to the hardware.
    
- **The Execution:** It spins up a `samba` container holding a local copy of the OS images, a TFTP container for the bootloaders, and a `dhcp-relay` container to manage the initial PXE handshakes.
    

By containerizing these services, the deployment team ensures that the entire physical provisioning infrastructure can be instantly booted, torn down, and moved to the next rack on the factory floor without leaving residual configuration files behind.