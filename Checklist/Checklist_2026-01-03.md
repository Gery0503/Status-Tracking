It is **Saturday, January 3, 2026**.

To support your request for a deeper technical understanding, today’s **Server Building** module is expanded into a comprehensive architectural guide. We are moving away from "how to type commands" to "how the machine actually works."

Here is your sophisticated daily learning plan for **2026-01-03**.

---

# 📅 **2026-01-03 — Daily Learning Plan**

| **Category**                   | **Task**                                                 | **Status** |
| ------------------------------ | -------------------------------------------------------- | ---------- |
| 🧠 LeetCode Practice           | **461. Hamming Distance** (Bit Manipulation / XOR Logic) | ✅          |
| 🖥️ Server Building Essentials | **Deep Dive: The Anatomy of the Linux OS Layer**         | ✅          |
| 🐧 Linux Learning              | Command: **`strace`** (System Call Tracing)              | ✅          |

---

## 🧠 LeetCode — **461. Hamming Distance**

Tags: #BitManipulation #Math #XOR

Difficulty: Easy

Why chosen:

- It is a direct conceptual sequel to "Missing Number" and "Single Number" which you have practiced.
    
- It reinforces the **XOR** operator's primary property: measuring the "difference" between two binary states.
    

### 🎯 **Concept to learn today: "The Bitwise Difference"**

The "Hamming Distance" is the number of positions at which the corresponding bits of two integers are different.

- **The Intuition:** How many bits do I need to flip to turn integer `x` into integer `y`?
    
- **The Elegant Solution:**
    
    1. Perform `x ^ y` (XOR). This results in a new number where `1` represents a difference and `0` represents a match.
        
    2. Count the `1`s in that result (also known as the "Population Count" or "Hamming Weight").
        
    3. _Bonus:_ In Python, this is simply `bin(x ^ y).count('1')`. In C/Java, you might loop `n & (n-1)` to count bits efficiently.
        

---

## 🖥️ Server Building Essentials — **Deep Dive: The Anatomy of the Linux OS Layer**

Tags: #Kernel #SystemArchitecture #Filesystem #InitSystem

Goal: Understand the "Black Box." When you turn the server on, what physically happens to get from a powered-off chip to a listening web server?

### 1. The "Why" Behind Architecture & Partitioning

Unlike Windows, which often treats the `C:` drive as a singular bucket, Linux is modular. This influences how we partition storage.

- **The Kernel vs. Userland:**
    
    - **The Kernel** is the core program that manages CPU, RAM, and hardware. It has total privilege but provides no interface for the user.
        
    - **Userland** is everything else (your shell, Nginx, Python, `ls`, `cd`). They must ask the Kernel nicely (via **System Calls**) to touch hardware.
        
- **Partitioning Philosophy (The "Blast Radius" Defense):**
    
    - **`/var` Separation:** The `/var` directory holds variable data (logs, databases, cache). If an attacker spams your logs or a database query goes rogue, filling the disk, a single-partition system stops working entirely (root full = crash). If `/var` is a separate partition, only logging fails; the OS (on `/`) stays alive to let you fix it.
        
    - **`/home` Separation:** This allows you to reinstall or upgrade the OS (wipe `/`) without losing user data or configuration files.
        

### 2. The Mechanics of Initialization (From Power to PID 1)

How does the OS start?

1. **BIOS/UEFI:** Performs POST (Power-On Self-Test) and loads the Bootloader (GRUB) from the Master Boot Record (MBR) or EFI Partition.
    
2. **GRUB:** Loads the Linux Kernel (`vmlinuz`) and the Initial RAM Disk (`initrd`) into memory.
    
3. **The Kernel:** Detects hardware (CPU, Drives) and mounts the Root Filesystem (`/`) as Read-Only initially.
    
4. **Init (Systemd):** The Kernel starts **one** program: `/sbin/init` (which is a link to Systemd). This is **Process ID 1 (PID 1)**.
    
    - **The "Dependency Tree" Revolution:** Older systems (SysVinit) started services strictly sequentially ($A \to B \to C$). Systemd builds a dependency tree and starts services in parallel ($A+B+C$) wherever possible. This is why modern servers boot instantly.
        
    - **Targets:** Instead of "Runlevels," Systemd uses "Targets." Your server boots into `multi-user.target` (CLI mode), not `graphical.target` (GUI).
        

### 3. The Filesystem Hierarchy Standard (FHS)

Linux directories are not random; they are functional descriptions of the OS anatomy.

- **`/bin` vs `/usr/bin`:** Historically, `/bin` held commands needed _before_ other drives were mounted (like `ls`, `mount`). `/usr/bin` held user tools.
    
- **`/proc` and `/sys` (The Illusion):**
    
    - Go to `/proc`. You see files like `cpuinfo` or `meminfo`. These are **not real files** on the disk.
        
    - They are a **Virtual Filesystem**—a window into the Kernel's live memory. When you run `cat /proc/cpuinfo`, the Kernel generates that text on the fly. This is how the OS exposes hardware stats to software without specialized APIs.
        

### 4. The Network Stack & The "Socket"

When you "open a port" (like 80 for Web), what actually happens?

1. **Physical Layer:** Electrical signal hits the NIC (Network Card).
    
2. **Kernel Ring Buffer:** The NIC uses DMA (Direct Memory Access) to dump the packet into RAM and triggers a CPU interrupt.
    
3. **Protocol Stack:** The Kernel parses headers (Ethernet $\to$ IP $\to$ TCP) to identify the destination.
    
4. **The Socket:** This is the bridge. Your application (Nginx) asks the Kernel for a "File Descriptor" bound to Port 80.
    
    - _Critical Insight:_ In Linux, a network connection is treated just like a **file**. You read from it and write to it. This abstraction is why Linux tools (like `cat`, `grep`, and `sed`) can technically process network streams.
        

---

## 🐧 Linux Learning — Command: **`strace`**

Tags: #Linux/Command/strace #Debugging #Kernel #Syscall

Why chosen:

- You just learned about the Kernel/Userland divide. **`strace`** is the tool that lets you _see_ the conversation between them.
    
- It prints every **System Call** a program makes. It is the ultimate "why is this program hanging?" debugger.
    

### 🎯 **Core Uses & The "Under the Hood" View**

| **Scenario**                  | **Command**           | **What it reveals**                                                                                   |
| ----------------------------- | --------------------- | ----------------------------------------------------------------------------------------------------- |
| **Trace a command**           | `strace ls`           | You will see `openat()`, `getdents()`, `write()`—the actual kernel requests used to list files.       |
| **Attach to running process** | `sudo strace -p 1234` | Debug a frozen web server live. Is it stuck on a network read (`recvfrom`) or a disk write (`write`)? |
| **Summary of time**           | `strace -c ls`        | Shows a histogram: "This program spent 80% of its time waiting for the disk."                         |

### 💡 **Practice Task: See the "File" Concept**

1. Run `strace -e openat,read cat /etc/hostname`.
    
2. **Observation:**
    
    - You won't see "Cat reads file."
        
    - You will see: `openat(..., "/etc/hostname", ...)` $\to$ returns a number (File Descriptor, e.g., `3`).
        
    - Then `read(3, "server-name...\n", 128)`.
        
    - This proves that `cat` interacts with the disk entirely through Kernel handles.
        

For a deeper visual explanation of the Linux Boot Process, which is critical for understanding the "Init" step in server building, I recommend watching this video: Linux Boot Process

This video is relevant because it visualizes the exact sequence from BIOS to Systemd that we discussed in the "Mechanics of Initialization" section.