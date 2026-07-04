# 📅 **Checklist_2026-06-27**

| **Category**               | **Task**                                            | **Status** |
| -------------------------- | --------------------------------------------------- | ---------- |
| 🧠 LeetCode Practice       | **1046. Last Stone Weight** (Heap / Priority Queue) | ✅          |
| ⚙️ DevOps Essentials       | **Ansible Basics: Roles & Ansible Galaxy**          | ✅          |
| 🐧 Linux Learning          | Command: **`tmux`** (Terminal Multiplexer)          | ✅          |
| 🏭 **Dannie EMS Handbook** | **OOB Management (IPMI / BMC)**                     | ✅          |

## 🧠 LeetCode — **1046. Last Stone Weight** Tags: #Array #Heap #PriorityQueue

Difficulty: Easy

### 🎯 **Concept to learn today: The Max-Heap Advantage**

You are given an array of integers `stones` where `stones[i]` is the weight of the $i^{th}$ stone. Every turn, you smash the two heaviest stones together. If they have the same weight, both are destroyed. If they have different weights, the smaller one is destroyed, and the larger one's weight becomes the difference. Return the weight of the last remaining stone (or 0 if there are no stones left).

- **The Strategy:** The brute-force approach is to sort the array, pick the last two elements, calculate the difference, append it, and _re-sort_ the array every single turn. This is horribly slow. Instead, use a **Heap** (Priority Queue), a special tree-based data structure that automatically keeps the largest (or smallest) element at the top, allowing you to fetch and insert numbers extremely fast without full sorting.
    
- **The Flow:**
    
    1. Python's built-in `heapq` library is a _Min-Heap_ by default (keeps the smallest numbers at the top). To simulate a _Max-Heap_, simply multiply all your stones by `-1` (e.g., `10` becomes `-10`).
        
    2. Convert the array into a heap: `heapq.heapify(stones)`.
        
    3. Loop while the length of `stones` is greater than 1:
        
        - Pop the two "heaviest" (most negative) stones: `y = heapq.heappop(stones)` and `x = heapq.heappop(stones)`.
            
        - If they are not equal, push the difference back into the heap: `heapq.heappush(stones, y - x)`. _(Note: `y` is more negative, so `y - x` keeps the math correct)._
            
    4. If the heap is empty, return `0`. Otherwise, return `-stones[0]` to convert the last stone back to a positive integer.
        
- **Efficiency:** Popping and pushing to a heap takes $O(\log N)$ time. Doing this for $N$ stones gives a highly optimized time complexity of $O(N \log N)$. Space complexity is $O(1)$ or $O(N)$ depending on whether you mutate the input array in place.
    

## ⚙️ DevOps Essentials — **Ansible Basics: Roles & Galaxy**

Tags: #DevOps #Ansible #Architecture #Scale

Goal: Writing a 300-line `playbook.yml` file is fine for a quick test, but it becomes unmaintainable for enterprise deployments. Ansible **Roles** solve this by breaking playbooks into modular, reusable, and sharable directory structures.

### 🎯 **Quick Review Summary: Modular Automation**

A Role automatically loads variables, tasks, and handlers based on a strict directory structure. Instead of writing one massive file, you create a folder called `docker_setup/`, containing subfolders like `tasks/main.yml` and `vars/main.yml`.

**Ansible Galaxy:** Because Roles are standardized, you don't even have to write them yourself. Ansible Galaxy is the official hub (like `npm` for Node or `pip` for Python) where you can download pre-written, highly tested roles.

|**Concept**|**Command / Syntax**|**Description**|
|---|---|---|
|**Download a Role**|**`ansible-galaxy install geerlingguy.docker`**|**The Daily Driver.** Downloads a highly trusted, community-maintained role to install Docker perfectly on any OS.|
|**Use a Role**|`roles: - geerlingguy.docker`|**Playbook Integration.** Instead of writing `tasks:`, you simply list the downloaded role in your playbook, reducing a 100-line installation script to a single line.|
|**Create a Role**|`ansible-galaxy init my_custom_role`|**Scaffolding.** Automatically generates the standard folder structure (`tasks`, `handlers`, `templates`) for you to build your own reusable module.|

## 🐧 Linux Learning — Command: **`tmux`** (Terminal Multiplexer)

Tags: #Linux #Command #tmux #SysAdmin #Productivity

Goal: If you SSH into an L10 server to run a 4-hour Python compilation or hardware burn-in script, and your laptop's Wi-Fi drops for one second, the SSH connection breaks and the script instantly dies. `tmux` creates virtual sessions that run completely independently of your SSH connection.

### 🎯 **Quick Review Summary: Session Persistence**

|**Scenario**|**Command / Keystroke**|**Description**|
|---|---|---|
|**Start a Session**|**`tmux new -s build_job`**|Creates a new named virtual terminal session. You can now start your long-running scripts here.|
|**Detach (The Magic)**|`Ctrl + b`, then press `d`|Disconnects you from the `tmux` session, leaving it running safely in the background. You can now close your laptop or drop Wi-Fi safely.|
|**List Sessions**|`tmux ls`|Shows all background sessions currently running on the server.|
|**Reattach**|`tmux attach -t build_job`|Jumps right back into the running session, exactly where you left off, even days later.|

## 🏭 Dannie EMS Handbook — **OOB Management (IPMI / BMC)**

Tags: #EMS #Manufacturing #Hardware #Infrastructure

Goal: Understanding how to forcefully manage, monitor, and reboot a physical server when the Operating System has completely crashed or the power is physically turned off.

### 🎯 **Core Concept: The Motherboard's Mini-Computer**

When a server OS freezes (e.g., a kernel panic during Burn-In testing), standard networking and SSH are dead. **OOB (Out-of-Band) Management** solves this. Every enterprise server has a tiny, independent computer built directly onto the motherboard, known as the **BMC** (Baseboard Management Controller).

- _Note: Dell heavily brands their BMC as **iDRAC** (Integrated Dell Remote Access Controller)._
    
- **Always On:** As long as the server is plugged into a wall outlet, the BMC is running, even if the main server CPU and RAM are completely powered off.
    
- **IPMI Protocol:** The BMC uses its own dedicated physical network port and IP address, communicating via the Intelligent Platform Management Interface (IPMI).
    

### 🏢 **Factory Floor Application**

If you are managing the Interim Server Solution (ISS) or deploying L10 hardware, automation scripts cannot rely on SSH to reboot a frozen machine. Instead, your deployment orchestrator sends an IPMI signal (using tools like `ipmitool`) directly to the BMC's IP address.

- Example: `ipmitool -I lanplus -H 10.10.5.50 -U root -P password power cycle`
    
    This bypasses the dead OS entirely, sending an electrical signal to the motherboard to forcefully cut and restore power, allowing the automated factory line to recover without a human technician walking over to physically press the power button.