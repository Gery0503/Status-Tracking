# 📅 **Checklist_2026-10-24**

| **Category**         | **Task**                                           | **Status** |
| -------------------- | -------------------------------------------------- | ---------- |
| 🧠 LeetCode Practice | **1051. Height Checker** (Array / Sorting)         | ✅          |
| ⚙️ DevOps Essentials | **Docker Compose: Environment Variables & `.env`** | ✅          |
| 🐧 Linux Learning    | Command: **`lsblk`** (List Block Devices)          | ✅          |

## 🧠 LeetCode — **1051. Height Checker** Tags: #Array #Sorting #Counting_Sort

Difficulty: Easy

  

### 💡 **My Intuition**

- **Observations:**
    
      
    1. We are given an array `heights` representing the current standing order of students.
        
          
        
    2. We need to find how many students are standing in the wrong positions compared to what a non-decreasing sorted order would look like.
        
          
        
    3. If we create a sorted copy of the original array, we can compare it element-by-element against the original array to count every mismatch.
        
          
        
- **Edge cases:**
    
      
    - `Already sorted array`: If the input array is already in correct non-decreasing order, the mismatch count will naturally be `0`.
        
          
        
- **Expected approach and complexity:**
    
      
    1. Time: $O(N \log N)$ due to the sorting step, where $N$ is the number of elements in the array. (Can be optimized to $O(N)$ using counting sort since student heights have a bounded range, but sorting is clean and standard for an easy session).
        
          
        
    2. Space: $O(N)$ to store the duplicated, sorted copy of the array for comparison.
        
          
        

### 🎯 **Concept to learn today: Index-by-Index Comparison**

A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line. Let the non-decreasing order of the heights be represented by the integer array `expected` where `expected[i]` is the expected height of the $i^{th}$ student in line. Return the number of indices where `heights[i] != expected[i]`.

  

- **The Strategy:** Create an exact clone of the input array, sort that clone, and iterate through both arrays simultaneously to count discrepancies.
    
      
    
- **The Flow:**
    
      
    1. Create a sorted copy of the heights: `expected = sorted(heights)`.
        
          
        
    2. Initialize a counter: `mismatches = 0`.
        
          
        
    3. Loop through each index `i` from `0` to the length of the array:
        
          
        - If `heights[i] != expected[i]`, increment `mismatches`.
            
              
            
    4. Return `mismatches`.
        
          
        
- **Efficiency:** The primary cost is sorting the array, giving a time complexity of $O(N \log N)$ and an auxiliary space complexity of $O(N)$ for the new array.
    
      
    

## ⚙️ DevOps Essentials — **Docker Compose: Environment Variables & `.env`**

Tags: #DevOps #Docker #ConfigurationManagement #Security

  

Goal: Hardcoding database passwords, API keys, or custom port numbers directly inside a `docker-compose.yml` file is a major security risk and makes moving configurations between development and production environments difficult. You need a clean way to inject configuration values dynamically.

  

### 🎯 **Quick Review Summary: Decoupling Configuration**

Docker Compose natively supports reading environment variables from a hidden file named `.env` located in the exact same directory as your `docker-compose.yml`.

  

|**Component**|**Description**|
|---|---|
|**The `.env` File**|A simple flat text file containing key-value pairs (e.g., `POSTGRES_PASSWORD=secret123`). Never commit this file to public Git repositories.|
|**Variable Interpolation**|Inside your Compose file, you can inject these variables using syntax like `${POSTGRES_PASSWORD}` or provide defaults like `${PORT:-8080}`.|
|**The Environment Block**|Passing variables directly into containers so the internal application code can read them via standard OS environment calls.|

### 💻 **Real-World Code Execution**

**1. Create a `.env` file:**

  

Ini, TOML

```
DB_USER=admin
DB_PASS=secure_password_99
APP_PORT=5000
```

**2. Reference variables in your `docker-compose.yml`:**

  

YAML

```
version: '3.8'

services:
  web_app:
    image: my_custom_app:latest
    ports:
      - "${APP_PORT}:80"
    environment:
      - USER=${DB_USER}
      - PASSWORD=${DB_PASS}
```

_(When you run `docker-compose up`, Docker automatically evaluates the `.env` file and substitutes the variables before launching the containers)._

  

## 🐧 Linux Learning — Command: **`lsblk`** (List Block Devices)

Tags: #Linux #Command #lsblk #Storage #SysAdmin

  

Goal: When managing servers, you frequently need to check what hard drives, SSDs, or USB partitions are physically attached to the machine, what their total storage capacity is, and where they are mounted. `lsblk` prints this out in a clean, readable tree structure.

  

### 🎯 **Quick Review Summary: The Block Device Tree**

Unlike older commands that only list raw mount points, `lsblk` visualizes the hierarchical relationship between physical drives and their logical partitions.

  

|**Scenario**|**Command**|**Description**|
|---|---|---|
|**View the Tree**|**`lsblk`**|**The Daily Driver.** Lists all available block devices, their sizes, and their current mount points in an easy-to-read tree format.|
|**Show File System Types**|`lsblk -f`|**Auditing.** The `-f` flag displays the filesystem type (e.g., `ext4`, `xfs`, `swap`) and unique UUIDs for each partition.|
|**Exclude RAM/Loops**|`lsblk -e 7,11`|**Filtering.** The `-e` (exclude) flag hides loop devices and RAM disks, keeping your terminal output clean and focused purely on physical hardware storage.|

### 💻 **Real-World Terminal Example**

You plug a new storage drive into a server and want to verify that the kernel recognized it and find its device name:

  

Bash

```
$ lsblk
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda      8:0    0 465.8G  0 disk 
├─sda1   8:1    0   512M  0 part /boot/efi
└─sda2   8:2    0 465.3G  0 part /
sdb      8:16   1  29.9G  0 disk 
└─sdb1   8:17   1  29.9G  0 part 
```

_(The output instantly shows your primary OS drive (`sda`) and a newly attached 30GB USB drive (`sdb` with partition `sdb1`) that is currently unmounted)._