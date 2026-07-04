# 📅 **Checklist_2026-05-23**

| **Category**               | **Task**                                                | **Status** |
| -------------------------- | ------------------------------------------------------- | ---------- |
| 🧠 LeetCode Practice       | **1480. Running Sum of 1d Array** (Prefix Sum)          | ✅          |
| ⚙️ DevOps Essentials       | **Ansible Basics: Gathering Facts**                     | ✅          |
| 🐧 Linux Learning          | Command: **`env` / `printenv`** (Environment Variables) | ✅          |
| 🏭 **Dannie EMS Handbook** | **The Golden Image (Master Image)**                     | ✅          |

## 🧠 LeetCode — **1480. Running Sum of 1d Array** Tags: #Array #PrefixSum

Difficulty: Easy

### 🎯 **Concept to learn today: In-Place Accumulation**

Given an array `nums`. We define a running sum of an array as `runningSum[i] = sum(nums[0]...nums[i])`. Return the running sum of `nums`. (For example, `[1, 2, 3, 4]` becomes `[1, 3, 6, 10]`).

- **The Strategy:** The brute-force way is to recalculate the sum from the beginning for every single index. But that wastes energy. Since you already know the sum of everything that came before the current step, you simply add the current number to the previous sum.
    
- **The Flow:**
    
    1. Start a loop from index `1` (the second element) to the end of the array.
        
    2. Update the current element by adding the previous element to it: `nums[i] = nums[i] + nums[i-1]`.
        
    3. Return `nums`.
        
- **Efficiency:** You loop through the array exactly one time, giving a time complexity of $O(N)$. Because you update the array _in-place_ instead of creating a brand new array to hold the answers, your space complexity is perfectly optimized at $O(1)$.
    

## ⚙️ DevOps Essentials — **Ansible Basics: Gathering Facts**

Tags: #DevOps #Ansible #Automation #SystemAdmin

Goal: When managing a cluster of laptops or a rack of L11 servers, you often need to run tasks conditionally based on the hardware (e.g., "Only install this driver if the OS is Ubuntu and the CPU is Intel"). Ansible figures this out automatically using **Facts**.

### 🎯 **Quick Review Summary: System Discovery**

When an Ansible Playbook runs, the very first thing it does in the background is run a module called `setup`. This module interrogates the target machine and pulls down hundreds of data points (Facts) about the hardware, network, and OS, making them available as variables in your Playbook.

|**Fact Variable**|**What it discovers**|**Best Use Case**|
|---|---|---|
|`ansible_distribution`|The OS type (Ubuntu, CentOS, RedHat).|Writing a Playbook that automatically uses `apt` for Ubuntu targets, but switches to `yum` for CentOS targets.|
|`ansible_default_ipv4.address`|The primary IP address of the machine.|Dynamically injecting the correct IP address into a database configuration file template.|
|`ansible_processor_vcpus`|The number of CPU cores.|Tuning Docker or Nginx worker processes to exactly match the hardware capabilities of the specific node.|

## 🐧 Linux Learning — Command: **`env` / `printenv`** (Environment Variables)

Tags: #Linux #Command #env #SysAdmin #Configuration

Goal: Applications, deployment scripts, and CI/CD pipelines rely on hidden system variables to know where to find files, what passwords to use, or what environment they are running in. You need a fast way to view these hidden values.

### 🎯 **Quick Review Summary: Inspecting the Environment**

|**Scenario**|**Command**|**Description**|
|---|---|---|
|**View Everything**|**`printenv`**|**Daily Driver.** Prints every single environment variable currently active in your shell session.|
|**Check Specific Target**|`printenv USER`|**Targeted Query.** Quickly checks the value of a specific variable (e.g., verifying that the current session recognizes you as `root`).|
|**Injecting on the Fly**|`env DEBUG=True ./script.py`|**Testing.** Temporarily passes the `DEBUG` variable to a script for a single execution without permanently changing the system environment.|

### 💻 **Real-World Terminal Example**

1. A Docker container script is failing because it cannot find the Java installation path. You want to see if the `$JAVA_HOME` variable is actually set on the server.
    
2. You use `printenv` combined with `grep` to quickly filter the massive list of variables.
    

Bash

```
$ printenv | grep JAVA
JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

_(If nothing returns, you know exactly why the deployment is failing: the environment variable is missing)._

## 🏭 Dannie EMS Handbook — **The Golden Image (Master Image)**

Tags: #EMS #Manufacturing #Provisioning #QualityControl

Goal: Standardizing the software state of a machine to eliminate "configuration drift" and dramatically speed up mass provisioning on the factory floor.

### 🎯 **Core Concept: Cloning Perfection**

While PXE booting and Ansible Playbooks are fantastic for configuring a server from scratch, running dozens of installation scripts on 500 servers simultaneously takes hours and heavily strains the factory network. The solution is the **Golden Image**.

- **The Process:** A senior engineer takes a single physical server and perfectly configures it. They install the OS, run the Ansible playbooks, harden the security, configure the network settings, and pass all local testing.
    
- **The Snapshot:** Once this single server is certified as perfect, the entire hard drive is converted into a compressed snapshot file (the Golden Image).
    
- **Mass Duplication:** Instead of running complex installation scripts on the remaining 499 servers, the factory simply performs a block-level byte-for-byte copy (often via tools like Clonezilla or specific PXE imaging protocols) of the Golden Image onto the blank hard drives.
    

### 🏢 **Factory Floor Application**

When supporting client-facing missions for Dell, speed and consistency are everything. If every node in a cluster is built by running individual scripts, an intermittent network drop could cause Node 12 to miss a package installation, leading to catastrophic cluster failure at L11. By deploying a Golden Image, you guarantee that every single server in the rack is mathematically identical at the bit level before it even powers on.