It is **Saturday, March 7, 2026**.

With exactly **30 minutes** and **Medium** energy, today’s plan is optimized for **steady progress and conceptual linking**. We will dedicate the first half of the session to a powerful algorithmic pattern that requires careful state tracking but minimal code. The second half will connect a core Docker concept directly to a modern Linux networking tool.

Here is your focused daily learning plan for **2026-03-07**.

---

# 📅 **2026-03-07 — Daily Learning Plan**

| **Category**         | **Task**                                      | **Status** |
| -------------------- | --------------------------------------------- | ---------- |
| 🧠 LeetCode Practice | **739. Daily Temperatures** (Monotonic Stack) | ✅          |
| ⚙️ DevOps Essentials | **Docker Networking: Bridge vs. Host Modes**  | ✅          |
| 🐧 Linux Learning    | Command: **`ss`** (Socket Statistics)         | ✅          |

---

## 🧠 LeetCode — **739. Daily Temperatures** Tags: #Stack #Array #MonotonicStack

Difficulty: Medium (Moderate cognitive load)

Why chosen:

- **Avoids Duplication:** This problem introduces a distinct data structure pattern not present in your completed list.
    
- **Fits the Energy Level:** A 30-minute session is the perfect amount of time to wrap your head around a "Monotonic Stack." The code is short, but the mental visualization requires a solid Medium energy focus.
    

### 🎯 **Concept to learn today: The Monotonic Decreasing Stack**

You are given an array of daily temperatures. For each day, you need to find out how many days you have to wait until a warmer temperature. If there is no future day for which this is possible, keep it `0`.

- **The Strategy:** Instead of using a nested loop to look forward (which is slow), use a stack to remember the _indices_ of the days you are still waiting to resolve. The temperatures corresponding to the indices in the stack will strictly decrease from bottom to top (hence, monotonic).
    
- **The Flow:**
    
    1. Initialize an array `result` of the same length as the input, filled with `0`. Initialize an empty `stack`.
        
    2. Iterate through the array using the current index `i` and `temp`.
        
    3. While the `stack` is not empty AND the current `temp` is greater than the temperature at the index stored at the top of the `stack`:
        
        - Pop the index from the top of the `stack`. Let's call it `prev_day`.
            
        - Calculate the difference in days: `result[prev_day] = i - prev_day`.
            
    4. Push the current index `i` onto the `stack`.
        
- **Why efficient?** Every index is pushed onto the stack exactly once and popped exactly once. This guarantees a time complexity of $O(N)$ and a space complexity of $O(N)$, completely avoiding the dreaded $O(N^2)$ nested loop timeout.
    

---

## ⚙️ DevOps Essentials — **Docker Networking: Bridge vs. Host**

Tags: #DevOps #Docker #Networking #Architecture

Goal: Understanding how containers talk to the outside world. When deploying server solutions, misconfigured networks are the number one cause of "service unreachable" errors.

### 1. The Default: Bridge Network

When you run a Docker container normally, it connects to a virtual private network inside your server called a "bridge."

- The container gets its own isolated internal IP address (e.g., `172.17.0.2`).
    
- To let the outside world in, you must explicitly **publish ports** (e.g., `-p 8080:80`). The Docker daemon acts as a router, forwarding traffic from your server's port 8080 into the container's port 80.
    

### 2. The Bypass: Host Network

If you run a container with `--network host`, the container entirely bypasses Docker's virtual network layer.

- It does **not** get its own IP address.
    
- It binds directly to your server's physical network interface. If the container runs a web server on port 80, it will directly consume port 80 on the host machine.
    
- _Pros:_ Maximum network performance (no routing overhead).
    
- _Cons:_ Zero isolation, and high risk of port conflicts with other services running on the server.
    

---

## 🐧 Linux Learning — Command: **`ss`** (Socket Statistics)

Tags: #Linux #Command #ss #Networking #Debugging

Why chosen:

- `ss` is the modern, faster replacement for the deprecated `netstat` command. It is the absolute best tool to verify if your Docker container is actually listening on the ports you expect.
    

### 🎯 **Core Uses & Network Debugging**

| **Scenario**                 | **Command**    | **Sophistication**                                                                                                                                                                                                                         |
| ---------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **List All Listening Ports** | **`ss -tuln`** | **Daily Driver.** Shows all TCP (`-t`) and UDP (`-u`) sockets that are currently Listening (`-l`), resolving them as Numeric (`-n`) IP addresses/ports instead of slow DNS names.                                                          |
| **Find the Process ID**      | `ss -tulnp`    | Generates a list of all listening TCP/UDP sockets with numeric addresses and process IDs. <br>**`-p`**: Shows the **p**rocess information (PID and program name). _Note: You often need to run this with `sudo` to see all process names._ |
| **Check Active Connections** | `ss -ta`       | **Traffic Monitoring.** Lists all established connections (not just listening ports) to see who is currently connected to your server's services.                                                                                          |

---

Would you like me to write out a quick Python snippet demonstrating the Monotonic Stack logic for the temperatures problem, or would you prefer a mock terminal output showing how `ss -tulnp` reveals a Docker port conflict?