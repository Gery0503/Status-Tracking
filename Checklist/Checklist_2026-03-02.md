With only **10 minutes** and **Medium** energy, today’s plan is optimized for **rapid comprehension and high cognitive return**. We will focus on pure logic and OS-level debugging tools that require zero environment setup.

Here is your focused daily learning plan for **2026-03-02**.

---

# 📅 **2026-03-02 — Daily Learning Plan**

| **Category**                   | **Task**                                                  | **Status** |
| ------------------------------ | --------------------------------------------------------- | ---------- |
| 🧠 LeetCode Practice           | **876. Middle of the Linked List** (Fast & Slow Pointers) | ✅          |
| 🖥️ Server Building Essentials | **The OS Layer: Everything is a File (File Descriptors)** | ✅          |
| 🐧 Linux Learning              | Command: **`strace`** (System Call Tracer)                | ✅          |

---

## 🧠 LeetCode — **876. Middle of the Linked List** Tags: #LinkedList #TwoPointers #Logic

Difficulty: Easy (High logic density)

Why chosen:

- **Fits the Time Matrix:** Requires minimal code and strictly relies on pointer visualization, making it perfect for a rapid 10-minute session.
    

### 🎯 **Concept to learn today: Half-Speed Traversal**

You need to find the middle node of a linked list. If there are two middle nodes, you must return the second middle node.

- **The Strategy:** Deploy two pointers moving at different speeds. When the fast pointer reaches the end of the list, the slow pointer will naturally sit exactly in the middle.
    
- **The Flow:**
    
    1. Initialize `slow` and `fast` pointers, both starting at the `head` node.
        
    2. Loop while `fast` is not null and `fast.next` is not null.
        
    3. Move `slow` forward by one single node.
        
    4. Move `fast` forward by two nodes.
        
    5. Return the `slow` pointer once the loop terminates.
        
- **Why efficient?** You iterate through the list only one time, resulting in a time complexity of $O(N)$ and a space complexity of $O(1)$.
    

---

## 🖥️ Server Building Essentials — **The OS Layer: File Descriptors**

Tags: #DevOps #OS #Architecture #Filesystem

Goal: Understanding how the Linux kernel tracks resources. This is a foundational software-layer concept for troubleshooting server bottlenecks and application crashes.

### 1. The "Everything is a File" Philosophy

In Linux, almost all system resources are treated as files by the kernel. This includes actual text files, directories, keyboards, printers, and active network connections (sockets).

### 2. File Descriptors (FDs)

When a process opens a resource, the kernel grants it a File Descriptor. An FD is simply a non-negative integer that acts as a handle for the operating system to track it.

- `0` is strictly reserved for Standard Input (stdin).
    
- `1` is strictly reserved for Standard Output (stdout).
    
- `2` is strictly reserved for Standard Error (stderr).
    
- `3` and above are dynamically assigned to newly opened files or network sockets by your applications.
    

### 3. The Limits

Servers have a hard maximum limit on the number of files they can keep open simultaneously. If a web server or Docker container reaches this FD limit, it will crash or silently drop new connections, leading to critical and hard-to-diagnose service failures.

---

## 🐧 Linux Learning — Command: **`strace`**

Tags: #Linux #Command #strace #Debugging #OS

Why chosen:

- Directly complements the OS-layer theory of File Descriptors. If FDs are how the kernel tracks resources, `strace` is how you watch an application request those resources from the kernel in real-time.
    

### 🎯 **Core Uses & Troubleshooting**

| **Scenario**                | **Command**                         | **Sophistication**                                                                                                                                                                      |
| --------------------------- | ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Watch a Failing Command** | **`strace ls /root`**               | **Direct Execution.** Runs the command and prints every single system call it makes. You will immediately see the exact `EACCES (Permission denied)` error requested from the kernel.   |
| **Debug a Frozen Server**   | `strace -p 1234`                    | **Live Attachment.** Attaches to an already-running process ID (PID). If your Python app or Nginx server is hung, this tells you exactly which kernel operation it is stuck waiting on. |
| **Trace File Usage**        | `strace -e trace=open,read -p 1234` | **Targeted Filtering.** Filters the noise to show only specific system calls. Perfect for verifying if a background daemon is actually reading the configuration file you just edited.  |

---

Would you like me to map out a quick debugging scenario showing how `strace` can reveal exactly why a Dockerized app is failing to start?