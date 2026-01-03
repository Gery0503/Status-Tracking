

---

# 📅 **2025-11-30 — Daily Learning Plan**

| Category                   | Task                                                              | Status |
| -------------------------- | ----------------------------------------------------------------- | ------ |
| 🧠 LeetCode Practice       | **942. DI String Match**                                          | ✅      |
| 🖥️ Server Building Basics | Topic: **Server BIOS / UEFI Configuration — What to check & why** | ✅      |
| 🐧 Linux Learning          | Command: **`sed`**                                                | ✅      |

---

# 🧠 LeetCode — **942. DI String Match**

**Tags:** #Greedy #TwoPointers  
**Difficulty:** Easy  
**Why this problem today:**

- A very clean greedy technique, great for warming up
    
- Helps build confidence in pointer-based solutions you’ll need in many interview questions
    

### 🎯 **Concept to learn today: “Greedy with dynamic bounds”**

Given a string of `"I"` and `"D"`, you want to output a permutation of `0..n` such that:

- `"I"` → next number must be larger
    
- `"D"` → next number must be smaller
    

Key greedy idea:

- Maintain two pointers:
    
    - `low = 0`
        
    - `high = n`
        
- For each character:
    
    - If `"I"`, assign the current value as `low` then `low++`
        
    - If `"D"`, assign the current value as `high` then `high--`
        
- Last number will naturally be the remaining `low == high`.
    

### 📝 What to focus on

- Understanding _why_ greedy guarantees correctness
    
- Visualizing the shrinking number range
    
- Comparing this to backtracking (which would be overkill)
    

This problem teaches a technique that appears in many future medium-level problems.

---

# 🖥️ Server Building Basics — **Lesson 3: BIOS / UEFI Configuration**

Today’s lesson moves from pure hardware knowledge into **actual pre-OS server configuration**, something you’ll definitely touch when building servers on-site.

This is one of the most important chapters because incorrect BIOS settings can kill performance, break RAID, cause OS install failures, or make the server unable to boot.

---

## 🧩 1. **What is BIOS / UEFI in the context of servers?**

BIOS/UEFI is the “control room” of the server’s hardware.  
Before Linux or Windows Server ever loads, BIOS controls:

- CPU features
    
- RAM timing
    
- Storage controllers
    
- Boot devices
    
- Virtualization flags
    
- Security settings
    
- Fan and power behavior
    

Servers (Dell iDRAC, HPE iLO, Supermicro, Lenovo) usually have more options than consumer PCs.

Knowing what to change — and what NOT to touch — is key.

---

## ⚙️ 2. **Configurations you must check when building a server**

### **(A) CPU Settings**

- **Intel VT-x / AMD-V** → Must enable if running VMs or containers with nested virtualization
    
- **Hyper-Threading** (Enable unless explicitly required to disable)
    
- **Turbo Boost / Precision Boost** → Helps performance unless you need strict thermal control
    
- **Power governor (Performance vs Balanced vs Energy-Saving)**
    
    - For most servers:
        
        - Choose **Performance** for workloads
            
        - Choose **Balanced** only if power constraints exist
            

---

### **(B) Memory Settings**

- Ensure the system detects all RAM channels
    
- ECC status must show **enabled**
    
- NUMA:
    
    - Leave enabled; only disable for very specific applications
        
- Memory interleaving:
    
    - Usually leave default; “Auto” gives best stability
        

---

### **(C) Storage / RAID**

This is critical for preventing OS install or boot failures.

- Select **RAID Mode** or **AHCI Mode** depending on setup
    
    - If using RAID controller → RAID Mode
        
    - If installing OS on NVMe SSDs → Usually AHCI or Vendor-specific NVMe mode
        
- Enable / disable SATA ports based on actual physical use
    
- Confirm presence of the RAID virtual disk (VD)
    
- Boot order:
    
    - RAID controller → correct VD → USB for OS installation
        
- If NVMe devices exist:
    
    - Check “PCIe bifurcation” settings if multiple NVMe drives share a riser
        

---

### **(D) Virtualization**

Enable if using Docker, Kubernetes, VMware, Proxmox, Hyper-V.

Must enable:

- **Intel VT-x / AMD-V**
    
- **Intel VT-d / AMD IOMMU** → Required for PCIe passthrough
    
- SR-IOV for advanced NIC virtualization
    

---

### **(E) Power & Cooling**

- Redundant PSU features → ensure “Auto” or “Balanced”
    
- Fan mode:
    
    - “Optimal” for general use
        
    - “Full” only for high-heat environments or GPU servers
        
- PCIe ASPM (power-saving for PCIe) → turn off if using high-performance NVMe
    

---

### **(F) Security**

- Secure Boot:
    
    - Enable for modern OS (Ubuntu 22+, Windows Server)
        
    - Disable only if using specialized or unsigned drivers
        
- TPM:
    
    - Leave enabled for most installations
        
- Password protection:
    
    - Ensure BIOS admin password set after setup is done
        

---

## 🗂️ 3. Checklist you will use onsite

When you arrive to build the server abroad, go through these items:

### ✓ CPU virtualization enabled

### ✓ ECC RAM confirmed

### ✓ RAID controller in correct mode

### ✓ Boot sequence validated

### ✓ Fan mode appropriate for environment

### ✓ Secure Boot settings match OS

### ✓ All unused ports disabled (for security)

### ✓ Time/Date correct — important for logs and certificates

### ✓ IPMI/iDRAC/iLO network config confirmed

This checklist alone solves >50% of early boot problems.

---

# 🐧 **Linux Learning 

## 🔧 Command of the Day: **`sed`**

**Tags:** #Linux #StreamEditor #TextProcessing  
**Category:** Ultra-useful for server admins, scripting, and log manipulation

`sed` (stream editor) is one of the most powerful tools in Linux for **editing text non-interactively**.  
It's essential in automation, n8n workflows, server provisioning scripts, and CI pipelines.

---

# ⭐ Why `sed` is worth learning

Because it allows you to:

- Clean logs
    
- Replace text automatically
    
- Delete specific lines from config files
    
- Modify configuration files during deployment
    
- Extract key-value pairs
    
- Automate system maintenance scripts
    
- Pre-process data before feeding it into Python, Bash, or n8n
    

If you manage servers, `sed` is basically mandatory.

---

# 📌 **Quick and Actionable Cheatsheet (copy-ready for Obsidian)**

###  **1. Replace text**

```bash
sed 's/old/new/' file.txt
```

Replaces only the **first occurrence** per line.

Replace **all occurrences**:

```bash
sed 's/old/new/g' file.txt
```

Replace and save **in-place** (important for automation):

```bash
sed -i 's/old/new/g' config.ini
```

---

### **2. Delete lines**

Delete line 3:

```bash
sed '3d' file.txt
```

Delete lines containing a keyword:

```bash
sed '/ERROR/d' app.log
```

---

### **3. Print only matching lines (like grep but with extraction)**

```bash
sed -n '/nginx/p' server.conf
```

---

### **4. Extract fields using capture groups**

Example: extract values after `key=`

```bash
sed -n 's/.*key=\(.*\)/\1/p' config.env
```

---

### **5. Edit config files during server setup**

Example: change SSH port

```bash
sed -i 's/^#Port 22/Port 2222/' /etc/ssh/sshd_config
```

---

### **6. Insert lines**

Insert text **before** line 1:

```bash
sed '1i # Added by automation' file.txt
```

Insert after line 10:

```bash
sed '10a new-line-here' file.txt
```

---

### **7. Replace only on lines containing a pattern**

```bash
sed '/database/ s/localhost/127.0.0.1/' settings.conf
```

This is extremely useful with large config files.

---

# 💡 Real-World Application Scenarios

### **🟦 Server Deployment (your new study area)**

Modify config files during setup:

- Nginx
    
- SSH
    
- Docker daemon
    
- Systemd service files
    

Instead of opening the file manually.

### **🟦 Log Cleanup**

Remove noisy debug logs:

```bash
sed '/DEBUG/d' api.log
```

### **🟦 Mass Replace during Refactoring (Cursor / bash scripts)**

```bash
grep -rl "v1/api" src | xargs sed -i 's/v1\/api/v2\/api/g'
```

### **🟦 n8n Node Preprocessing**

Before sending text into an automation pipeline:

```bash
sed 's/[()]//g' input.txt
```

---
