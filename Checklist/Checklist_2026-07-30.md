 
# 📅 **Checklist_2026-07-30**

| **Category**         | **Task**                                       | **Status** |
| -------------------- | ---------------------------------------------- | ---------- |
| 🧠 LeetCode Practice | **1920. Build Array from Permutation** (Array) | ✅          |
| ⚙️ DevOps Essentials | **Docker Basics: Networking Modes**            | ✅          |
| 🐧 Linux Learning    | Command: **`tree`** (Directory Visualization)  | ✅          |

## 🧠 LeetCode — **1920. Build Array from Permutation** Tags: #Array #Simulation

Difficulty: Easy

  

### 💡 **My Intuition**

_Write down your thoughts, ideas, and insights here._

  

- **Observations:**
    
      
    1. We are given a zero-based permutation array `nums`.
        
          
        
    2. The goal is to build a new array `ans` of the same length where `ans[i] = nums[nums[i]]`.
        
          
        
    3. This means the value at a given index in the original array acts as a pointer to _another_ index in that same array.
        
          
        
- **Edge cases:**
    
      
    - `Smallest constraints`: Even with an array length of 1, `nums[0]` will be `0`, and `nums[nums[0]]` safely evaluates to `0` without throwing out-of-bounds errors.
        
          
        
- **Expected approach and complexity:**
    
      
    1. Time: $O(N)$ where $N$ is the length of the array, since we simply need to look at each index exactly once.
        
          
        
    2. Space: $O(N)$ to allocate the memory for the new `ans` array that we will return.
        
          
        

### 🎯 **Concept to learn today: Index Mapping**

Given a zero-based permutation `nums` (an array where elements are distinct integers from `0` to `nums.length - 1`), build an array `ans` of the same length where `ans[i] = nums[nums[i]]` for each `0 <= i < nums.length` and return it.

  

- **The Strategy:** This is a pure simulation problem. Because energy is low today, we will not worry about complex bitwise operations to solve this in $O(1)$ space. We will take the straightforward, readable approach: create a new array and populate it exactly as the formula instructs.
    
      
    
- **The Flow:**
    
      
    1. Initialize an empty list called `ans`.
        
          
        
    2. Loop through each index `i` from `0` to the length of `nums`.
        
          
        
    3. Inside the loop, find the intermediate index: `target_index = nums[i]`.
        
          
        
    4. Fetch the final value: `final_value = nums[target_index]`.
        
          
        
    5. Append `final_value` to `ans`. (Or simply append `nums[nums[i]]` in one step).
        
          
        
    6. Return `ans`.
        
          
        
- **Efficiency:** The single pass through the array takes $O(N)$ time. Storing the new list takes $O(N)$ space.
    
      
    

## ⚙️ DevOps Essentials — **Docker Basics: Networking Modes**

Tags: #DevOps #Docker #Networking #Architecture

  

Goal: You know how to persist data using Volumes. But how do containers actually talk to the outside world, or to each other, without causing IP address conflicts on your host machine? Docker handles this via isolated Virtual Networks.

  

### 🎯 **Quick Review Summary: Container Communication**

When you spin up a Docker container, it does not automatically share your host computer's IP address. Docker assigns it to a virtual network.

  

|**Network Mode**|**Description**|**Best Use Case**|
|---|---|---|
|**`bridge`** (Default)|Docker creates an internal, private network (e.g., `172.17.0.x`). Containers can talk to each other, but the outside world cannot reach them unless you manually map/publish a port (like `-p 8080:80`).|**Standard Web Apps.** Running an API and a Database. They talk securely on the bridge, and you only expose the API's port to the public.|
|**`host`**|Completely removes network isolation. The container uses the host machine's exact network interface and IP address.|**DHCP/Network Services.** As we saw with the DHCP-Relay, if a container needs to hear raw hardware broadcast packets on the physical network, it must use this mode.|
|**`none`**|Disables all networking. The container has a loopback interface (`localhost`) but absolutely zero external access.|**High Security / Air-gapped.** Running a local script that generates highly sensitive cryptographic keys that should never touch the internet.|

### 💻 **Real-World Code Execution**

You can view all the virtual networks Docker is currently managing on your machine:

  

Bash

```
$ docker network ls
NETWORK ID     NAME      DRIVER    SCOPE
1a2b3c4d5e6f   bridge    bridge    local
9f8e7d6c5b4a   host      host      local
```

## 🐧 Linux Learning — Command: **`tree`** (Directory Visualization)

Tags: #Linux #Command #tree #Filesystem #SysAdmin

  

Goal: When exploring a new codebase or checking if an Ansible Role scaffolded its directory structure correctly, running `ls` over and over to dig into folders is tedious. `tree` visualizes the entire hierarchy at once.

  

### 🎯 **Quick Review Summary: The Filesystem Map**

| **Scenario**        | **Command** | **Description**                                                                                                                                                                    |
| ------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **The Full Map**    | **`tree`**  | **The Daily Driver.** Prints the current directory and every single file/folder nested inside it as a beautiful visual hierarchy.                                                  |
| **Limit the Depth** | `tree -L 2` | **Sanity Check.** If a folder has 10,000 files nested 8 layers deep, running a raw `tree` command will flood your terminal. `-L 2` limits the visual output to only 2 levels deep. |
| **Folders Only**    | `tree -d`   | **Architecture Review.** Hides all the files and only shows the directory structure. Perfect for verifying a playbook's layout before writing code.                                |

### 💻 **Real-World Terminal Example**

1. You create an Ansible Role and want to verify the folder layout.
    

Bash

```
$ tree -d my_role/
my_role/
├── defaults
├── handlers
├── meta
├── tasks
├── templates
└── vars

6 directories
```