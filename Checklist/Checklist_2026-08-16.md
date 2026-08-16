# 📅 **Checklist_2026-08-16**

| **Category**         | **Task**                                                   | **Status** |
| -------------------- | ---------------------------------------------------------- | ---------- |
| 🧠 LeetCode Practice | **238. Product of Array Except Self** (Array / Prefix Sum) | ✅          |
| ⚙️ DevOps Essentials | **Docker Basics: The Dockerfile**                          | ✅          |
| 🐧 Linux Learning    | Command: **`traceroute`** (Network Path Diagnosis)         | ✅          |

## 🧠 LeetCode — **238. Product of Array Except Self** Tags: #Array #PrefixSum

Difficulty: Medium

  

### 💡 **My Intuition**

_Write down your thoughts, ideas, and insights here._

  

- **Observations:**
    
      
    1. The problem asks for an array where `answer[i]` is the product of all elements _except_ `nums[i]`.
        
          
        
    2. The easiest way to do this mathematically is to multiply every single number together to get a `total_product`, and then just divide `total_product` by `nums[i]` for each index.
        
          
        
    3. _However_, the problem explicitly forbids using the division operator. This means we have to calculate the products of the numbers strictly to the "left" of the index, and strictly to the "right" of the index, and multiply those two bounds together.
        
          
        
- **Edge cases:**
    
      
    - `Zeroes in the array`: If there is exactly one `0`, the entire result array will be `0` except for the index where the zero was. If there are multiple `0`s, every single index will be `0`. Avoiding division inherently protects us from `ZeroDivisionError` crashes.
        
          
        
- **Expected approach and complexity:**
    
      
    1. Time: $O(N)$ because we can pre-calculate the left and right products by sweeping through the array in two linear passes.
        
          
        
    2. Space: $O(1)$ auxiliary space if we use the output array itself to store the intermediate "left" and "right" passes (the problem states the output array does not count toward space complexity).
        
          
        

### 🎯 **Concept to learn today: Bidirectional Prefix Products**

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`. You must write an algorithm that runs in $O(N)$ time and without using the division operation.

  

- **The Strategy:** Use the output array to gather the "Left" products in one pass. Then, use a single integer variable to keep a running total of the "Right" products as you sweep backward, multiplying it into the output array on the fly.
    
      
    
- **The Flow:**
    
      
    1. Initialize `ans` as an array of `1`s with the same length as `nums`.
        
          
        
    2. **Pass 1 (Left to Right):**
        
          
        - Initialize `left_product = 1`.
            
              
            
        - Loop `i` from `0` to the end of the array.
            
              
            
        - Set `ans[i] = left_product`.
            
              
            
        - Update `left_product = left_product * nums[i]`.
            
              
            
    3. **Pass 2 (Right to Left):**
        
          
        - Initialize `right_product = 1`.
            
              
            
        - Loop `i` backward from the end of the array down to `0`.
            
              
            
        - Multiply the current answer: `ans[i] = ans[i] * right_product`.
            
              
            
        - Update `right_product = right_product * nums[i]`.
            
              
            
    4. Return `ans`.
        
          
        
- **Efficiency:** You loop over the array exactly twice, cleanly locking in the $O(N)$ time complexity constraint without nesting any operations.
    
      
    

## ⚙️ DevOps Essentials — **Docker Basics: The Dockerfile**

Tags: #DevOps #Docker #Architecture #CI_CD

  

Goal: Previously, we downloaded pre-built images (like Samba, Nginx, or Postgres) from Docker Hub. But when you write a custom Python deployment script or a Go application, you must package it into a container yourself. You do this by writing a **Dockerfile**.

  

### 🎯 **Quick Review Summary: The Build Instructions**

A Dockerfile is simply a text document containing all the commands a user could call on the command line to assemble an image. Docker reads these instructions from top to bottom.

  

|**Instruction**|**Description**|
|---|---|
|**`FROM`**|Always the first line. Defines your base OS. (e.g., `FROM python:3.10-slim` gives you a tiny Linux distro with Python pre-installed).|
|**`WORKDIR`**|Creates a folder inside the container and navigates into it. Acts as the `cd` command.|
|**`COPY`**|Copies files from your local laptop into the container's filesystem.|
|**`RUN`**|Executes terminal commands _during the build process_ (e.g., `RUN pip install -r requirements.txt`).|
|**`CMD`**|The default command that executes _when the container actually starts up_.|

### 💻 **Real-World Code Execution**

Here is a standard Dockerfile for a Python application. You save this in the same directory as your Python code.

  

Dockerfile

```
# 1. Start with a lightweight Python environment
FROM python:3.10-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy your local code into the /app directory
COPY . /app

# 4. Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Tell Docker how to run the application
CMD ["python", "main.py"]
```

_(To turn this text file into an actual runnable image, you run `docker build -t my_custom_app .` in your terminal)._

  

## 🐧 Linux Learning — Command: **`traceroute`** (Network Path Diagnosis)

Tags: #Linux #Command #traceroute #Networking #Troubleshooting

  

Goal: If `ping` tells you _if_ a server is reachable, `traceroute` tells you exactly _how_ your data gets there. When deploying automation across heavily segmented VLANs, `traceroute` reveals exactly which router or switch is dropping your connection.

  

### 🎯 **Quick Review Summary: Tracking the Hops**

When you send data to an IP address, it doesn't go there directly. It bounces (hops) from router to router. `traceroute` maps every single router along the path.

  

|**Scenario**|**Command**|**Description**|
|---|---|---|
|**The Full Map**|**`traceroute 10.10.5.50`**|**The Daily Driver.** Lists every gateway IP address the packet hits on its way to the destination.|
|**Skip DNS Lookups**|`traceroute -n 10.10.5.50`|**Speed.** The `-n` flag forces it to only show raw IP addresses, preventing it from wasting time trying to resolve human-readable domain names.|
|**The Modern Alternative**|`mtr 10.10.5.50`|**Continuous Tracing.** `mtr` (My Traceroute) combines `ping` and `traceroute` into a live, continuously updating terminal dashboard. (Requires installation on some systems).|

### 💻 **Real-World Terminal Example**

You are trying to deploy a Docker container to `10.50.2.100`, but it keeps timing out. You run `traceroute`.

  

Bash

```
$ traceroute -n 10.50.2.100
 1  192.168.1.1  1.123 ms  1.054 ms  1.002 ms
 2  10.10.0.1    2.450 ms  2.501 ms  2.412 ms
 3  * * *
 4  * * *
```

_(The output shows the data successfully hit your local router (`192.168.1.1`), passed to the main building switch (`10.10.0.1`), but then completely died (the asterisks `*`). This proves the destination server isn't broken; the router at hop 3 is explicitly blocking your traffic)._