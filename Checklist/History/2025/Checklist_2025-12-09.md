
---

# 📅 **2025-12-09 — Daily Learning Plan**

| **Category**                   | **Task**                                                       | **Status** |
| ------------------------------ | -------------------------------------------------------------- | ---------- |
| 🧠 LeetCode Practice           | **977. Squares of a Sorted Array** (Easy)                      | ✅          |
| 🖥️ Server Building Essentials | **Lesson 2: Static IP Configuration** (Netplan/NetworkManager) | ✅          |
| 🐧 Linux Learning              | Command: **`ip`** (Modern Network Interface Management)        | ✅          |

---

## 🧠 LeetCode — **977. Squares of a Sorted Array**

Tags: #TwoPointers #Sorting #Array

Difficulty: Easy

Why chosen:
- It is a classic "Easy" problem that tricks beginners into a slower solution ($O(n \log n)$) while a faster, linear solution ($O(n)$) exists.
    
- It reinforces the **Two Pointer** technique (converging from the outside in), which is critical for many array problems.
    

### 🎯 **Concept to learn today: "Converging Pointers"**

The input array is sorted, but contains negatives (e.g., `[-4, -1, 0, 3, 10]`).

1. **The Naive Approach:** Square everything `[16, 1, 0, 9, 100]`, then sort. Cost: $O(n \log n)$.
    
2. **The Optimal Approach ($O(n)$):**
    
    - Notice that the largest squares are always at the **extremes** (far left or far right).
        
    - Place pointers at `left=0` and `right=n-1`.
        
    - Compare the absolute values.
        
    - Place the larger square at the end of your result array and move the pointer inward.
        

---

## 🖥️ Server Building Essentials — **Lesson 2: Static IP Configuration**

Tags: #Networking #Netplan #ServerSetup

Goal: Ensure your server stays at a fixed address so you can reliably SSH into it and map DNS to it.

### 1. **Why Static IP?**

By default, routers assign IPs via DHCP (Dynamic Host Configuration Protocol). This means your server's address might change from `192.168.1.10` to `192.168.1.50` after a reboot, breaking all your connections and automations. A **Static IP** prevents this.

### 2. **The Modern Tool: Netplan (Ubuntu Server Standard)**

Older Linux systems used `/etc/network/interfaces`. Modern Ubuntu Server uses **Netplan**, configured via YAML files.

**Key Concepts:**

- **YAML Syntax:** Indentation matters strictly (use spaces, not tabs).
    
- **Config Location:** Usually in `/etc/netplan/00-installer-config.yaml` or similar.
    
- **Commands:**
    
    - `sudo netplan try`: Safely test settings. If you lose connection, it reverts automatically after 120 seconds. **Always use this remotely.**
        
    - `sudo netplan apply`: Apply changes immediately (risky if remote).
        

### 💡 **Actionable Task: Analyze a Config**

Research a basic Netplan YAML structure. Identify where the following go:

- `addresses`: (e.g., `[192.168.1.50/24]`)
    
- `gateway4` or `routes`: (The router's IP)
    
- `nameservers`: (DNS, e.g., `8.8.8.8`)
    

---

## 🐧 Linux Learning — Command: **`ip`**

Tags: #Linux/Command/ip #Networking #DeprecatedIfconfig

Why chosen:

- You are learning Server Networking today.
    
- The old command `ifconfig` is deprecated and often not installed by default on minimal server OSs.
    
- The `ip` command (from the `iproute2` package) is the modern standard for checking addresses and routes.
    

### 🎯 **Core Uses and Practice Tasks**

|**Scenario**|**Old Command**|**Modern Command**|**Description**|
|---|---|---|---|
|**Show IP addresses**|`ifconfig`|**`ip a`** (or `ip addr`)|Shows IP, MAC address, and status (UP/DOWN) for all interfaces.|
|**Show routing table**|`route -n`|**`ip r`** (or `ip route`)|Shows the Gateway (default route) and local network segments.|
|**Bring interface Up/Down**|`ifconfig eth0 up`|**`ip link set eth0 up`**|Manually enables or disables a network card.|
|**Brief summary**|N/A|**`ip -c a`**|Shows output with color (easier to read).|

### 💡 **Practice Task: Local Network Audit**

1. Run `ip a`. Identify your main network interface (usually named `eth0`, `enp3s0`, or `wlan0`).
    
2. Find your current local IP address (look for `inet ...`).
    
3. Run `ip r` and identify your **default gateway** (the first line usually starting with `default via ...`). This is your router's IP.