Here is your **2025-11-28 Daily Learning Plan**, fully filtered to **avoid all previously completed LeetCode problems + Linux commands**, and with your new category:

📡 **Server Building Learning — a daily lesson to prepare you for going abroad to build a server.**

---

# 📌 **2025-11-28 — Daily Learning Plan**

| Category                   | Task                                                      | Status |
| -------------------------- | --------------------------------------------------------- | ------ |
| 🧠 LeetCode Practice       | **628. Maximum Product of Three Numbers**                 | ✅      |
| 🖥️ Server Building Basics | Topic: **Server Hardware 101 – CPU, RAM, RAID, PSU, NIC** | ✅      |
| 🐧 Linux Learning          | Command: **`tail`**                                       | ✅      |

---

# 🧠 LeetCode — **628. Maximum Product of Three Numbers**

**Tags:** #Array #Math #Sorting  
**Why chosen:**

- Good warm-up problem involving sorting + edge-case reasoning
    
- Helps practice data-handling patterns useful in coding interviews
    

### Key Points to Focus On

- Why negative numbers matter (two negatives = positive)
    
- Compare two strategies:
    
    1. Highest 3 numbers
        
    2. Highest number + two lowest (possibly negative) numbers
        
- Time complexity: sorting vs one-pass scanning
    

---

# 🖥️ Server Building Basics — **Lesson 1: Server Hardware 101**

This is the **first day** of your new daily track:  
📡 **“Teach me building a server from zero.”**

Today starts with the most fundamental knowledge you'll need before even touching the hardware.

---

## **1. CPU (Processor)**

- Brands: Intel Xeon, AMD EPYC
    
- What matters:
    
    - **Core count** → parallel processing
        
    - **Clock speed** → per-core performance
        
    - **Thermal design power (TDP)** → cooling requirements
        
- Server workloads often value **more cores** over high GHz.
    

---

## **2. RAM (Memory)**

- ECC vs non-ECC:
    
    - Servers use **ECC (Error-Correcting Code)** RAM
        
    - Can detect & correct bit errors → increases stability
        
- DIMM Types:
    
    - RDIMM (Registered), LRDIMM (Load-Reduced)
        
- Rule: Always install RAM in **matching pairs** for optimal channel performance.
    

---

## **3. Storage & RAID**

- SSD vs HDD:
    
    - SSD = speed
        
    - HDD = capacity
        
- Hardware RAID controller vs software RAID
    
- Common RAID setups:
    
    - **RAID 1** → mirror (safe)
        
    - **RAID 5** → parity (balance)
        
    - **RAID 10** → mirror + stripe (fast & safe)
        
- You will almost definitely encounter RAID when building an on-site server.
    

---

## **4. PSU (Power Supply Unit)**

- Servers use **redundant PSUs**: PSU A + PSU B  
    → If one fails, system stays alive.
    
- Wattage sizing: total hardware peak wattage × **1.5 buffer**.
    

---

## **5. NIC (Network Interface Card)**

- Usually 1G/10G/25G/40G
    
- Ports type: RJ-45 vs SFP+
    
- You might need to:
    
    - Configure bonding (LACP)
        
    - Set static IP
        
    - Assign VLANs
        

---

## 📌 Practical takeaway for today

When you arrive abroad, you should be able to **look at the bare server chassis and identify every component**, what it does, and why it matters.

Tomorrow’s lesson will be:  
🧰 **“How to physically build a server (step-by-step hardware installation)”**

---

# 🐧 Linux Command — **`tail`**

**Tags:** #Linux/Command/tail #Logs #Monitoring

### Why chosen

- Complements “head” nicely
    
- Critical for server log troubleshooting
    

### Usage

Show last 10 lines:

```bash
tail file.txt
```

Follow log updates in real time:

```bash
tail -f /var/log/syslog
```

Show last 50 lines:

```bash
tail -n 50 app.log
```

Great when you’re diagnosing server boot issues, service failures, or ongoing events.

---

If you want, I can also:  
📌 Add weekly server-building progress  
📌 Add a “hands-on practice task” each day  
📌 Add a Sunday review mode

Just tell me!