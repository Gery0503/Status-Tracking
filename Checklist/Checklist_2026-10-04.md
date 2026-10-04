 
# 📅 **Checklist_2026-10-04**

| **Category**         | **Task**                                                  | **Status** |
| -------------------- | --------------------------------------------------------- | ---------- |
| 🧠 LeetCode Practice | **496. Next Greater Element I** (Array / Monotonic Stack) | ✅          |
| ⚙️ DevOps Essentials | **Ansible Basics: Roles & Directory Structure**           | ✅          |
| 🐧 Linux Learning    | Command: **`tcpdump`** (Network Packet Analyzer)          | ✅          |

## 🧠 LeetCode — **496. Next Greater Element I** Tags: #Array #Hash_Table #Monotonic_Stack

Difficulty: Easy

  

### 💡 **My Intuition**

_Write down your thoughts, ideas, and insights here._

  

- **Observations:**
    
      
    1. We have two arrays, `nums1` and `nums2`, where `nums1` is a subset of `nums2`.
        
          
        
    2. For each element in `nums1`, we need to find it in `nums2`, then look to the _right_ to find the first number that is larger than it. If none exists, return `-1`.
        
          
        
    3. A brute-force approach would be nested loops: find the number, then scan everything to its right. But that is slow $O(N \times M)$.
        
          
        
    4. Since we are looking for the "next greater" item, a stack is the perfect data structure. We can pre-calculate the next greater element for _every_ item in `nums2` in a single pass, store the results in a hash map, and then instantly look up the answers for `nums1`.
        
          
        
- **Edge cases:**
    
      
    - `No greater element exists`: The largest number in the array, or any number sorted in descending order at the end of the array, will never have a greater element to its right. The hash map must safely return `-1` for these.
        
          
        
- **Expected approach and complexity:**
    
      
    1. Time: $O(N + M)$ because we iterate through `nums2` once to build our map, and `nums1` once to build our result array.
        
          
        
    2. Space: $O(N)$ to store the stack and the hash map containing the mappings for `nums2`.
        
          
        

### 🎯 **Concept to learn today: The Monotonic Stack**

The "Next Greater Element" problem is the classic introduction to the **Monotonic Stack** pattern—a stack whose elements are strictly increasing or decreasing.

  

- **The Strategy:** Iterate through `nums2`. Keep a stack of numbers that are "waiting" to find their next greater element. When you encounter a new number that is _larger_ than the number at the top of your stack, you have found the answer for that stacked number. Pop it off, record the answer in a hash map, and repeat.
    
      
    
- **The Flow:**
    
      
    1. Initialize an empty stack and an empty hash map (dictionary).
        
          
        
    2. Loop through each `num` in `nums2`:
        
          
        - While the stack is not empty AND the current `num` is greater than the top of the stack:
            
              
            - `popped_val = pop from stack`
                
                  
                
            - `hash_map[popped_val] = num` (We found the next greater element!)
                
                  
                
        - Push the current `num` onto the stack so it can wait for its own greater element.
            
              
            
    3. After the loop, any numbers still left in the stack never found a greater element. You can optionally map them to `-1` (or just handle the default `-1` during lookup).
        
          
        
    4. Loop through `nums1`, look up each number in your hash map (defaulting to `-1` if not found), and append to your result array.
        
          
        
    5. Return the result array.
        
          
        

## ⚙️ DevOps Essentials — **Ansible Basics: Roles & Directory Structure**

Tags: #DevOps #Ansible #Architecture #ConfigurationManagement

  

Goal: Writing a 500-line `playbook.yml` file with dozens of tasks, handlers, and variables becomes unmaintainable quickly. To deploy complex infrastructure, you need to break your automation down into modular, reusable components called **Roles**.

  

### 🎯 **Quick Review Summary: Modular Automation**

An Ansible Role automatically loads variables, tasks, and handlers based on a strict, predictable folder structure. Instead of writing out the installation steps for Docker in every single playbook, you write a `docker` role once and call it whenever needed.

  

|**Directory**|**Purpose inside a Role**|
|---|---|
|**`tasks/main.yml`**|The core logic. This replaces the `tasks:` section of a flat playbook.|
|**`handlers/main.yml`**|Contains your service restarts (e.g., system restarts). Tasks can notify these handlers automatically.|
|**`vars/main.yml`**|Variables specifically heavily tied to this role that rarely change.|
|**`defaults/main.yml`**|Default variables. These have the lowest priority and are designed to be easily overridden by the main playbook.|

### 💻 **Real-World Code Execution**

Instead of a massive playbook, your main deployment file becomes incredibly clean. It simply acts as a master list pointing to the roles.

  

**`site.yml` (The Master Playbook):**

  

YAML

```
- name: Configure Server Infrastructure
  hosts: web_nodes
  become: true
  roles:
    - common_security  # Runs the firewall setup role
    - docker           # Installs the Docker daemon role
    - nginx            # Configures the Nginx reverse proxy role
```

_(When you execute this playbook, Ansible automatically dives into the `roles/docker/tasks/main.yml` file and executes it seamlessly)._

  

## 🐧 Linux Learning — Command: **`tcpdump`** (Network Packet Analyzer)

Tags: #Linux #Command #tcpdump #Networking #Diagnostics

  

Goal: When deploying containerized network services across VLANs, sometimes ping or tracing tools aren't enough. You need to see the actual raw data packets hitting your server's network interface. `tcpdump` is the ultimate command-line packet sniffer.

  

### 🎯 **Quick Review Summary: The Wire Sniffer**

|**Scenario**|**Command**|**Description**|
|---|---|---|
|**Listen to an Interface**|**`sudo tcpdump -i eth0`**|**The Firehose.** Captures and prints every single packet crossing the `eth0` network interface. Usually too noisy without filters.|
|**Filter by Port**|`sudo tcpdump -i eth0 port 80`|**Targeted.** Only captures HTTP traffic. Crucial when checking if a reverse proxy is actually receiving web requests from the outside world.|
|**Filter by Source IP**|`sudo tcpdump src 10.10.5.200`|**Isolation.** Ignores all other factory traffic and only shows you packets originating from one specific IP address (e.g., a specific switch or node).|

### 💻 **Real-World Terminal Example**

You deploy a DHCP-relay container, but it doesn't seem to be catching broadcasts. You run a quick capture to see if UDP port 67 (DHCP) is even hitting your physical server:

  

Bash

```
$ sudo tcpdump -i eth0 udp port 67
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), snapshot length 262144 bytes
09:05:12.123456 IP 0.0.0.0.bootpc > 255.255.255.255.bootps: BOOTP/DHCP, Request from 00:1a:2b:3c:4d:5e
```

_(Seeing this output confirms the hardware broadcast is successfully reaching your server's network card, meaning the issue is likely within your Docker networking configuration, not the physical switch)._