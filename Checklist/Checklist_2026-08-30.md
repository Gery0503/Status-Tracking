# 📅 **Checklist_2026-08-30**

| **Category**         | **Task**                                        | **Status** |
| -------------------- | ----------------------------------------------- | ---------- |
| 🧠 LeetCode Practice | **15. 3Sum** (Array / Two Pointers)             | ✅          |
| ⚙️ DevOps Essentials | **Docker Basics: Multi-Stage Builds**           | 🔲         |
| 🐧 Linux Learning    | Command: **`journalctl`** (Systemd Log Manager) | 🔲         |

## 🧠 LeetCode — **15. 3Sum** Tags: #Array #TwoPointers #Sorting

Difficulty: Medium

  

### 💡 **My Intuition**

_Write down your thoughts, ideas, and insights here._

  

- **Observations:**
    
      
    1. We need to find three numbers that add up to `0`.
        
          
        
    2. If we pick one number (let's call it `a`), the problem instantly simplifies into finding two other numbers (`b` and `c`) that add up to `-a`. This is exactly the "Two Sum" problem.
        
          
        
    3. Because we need to return the actual values (not the indexes) and we cannot have duplicate triplets, sorting the array first will allow us to easily skip duplicate numbers and use a sliding window (two pointers) to find the remaining sum.
        
          
        
- **Edge cases:**
    
      
    - `Duplicate combinations`: An array like `[-1, -1, 0, 1, 2]` has two `-1`s. If we don't explicitly write logic to skip the second `-1` after processing the first, our final output will contain identical duplicate triplets.
        
          
        
    - `All positive numbers`: If the array is sorted and our first picked number is $> 0$, we can immediately stop searching. Three positive numbers can never sum to zero.
        
          
        
- **Expected approach and complexity:**
    
      
    1. Time: $O(N^2)$ because we must loop through the array once to pick our first number, and for each number, run a nested linear two-pointer search. The initial $O(N \log N)$ sorting time is absorbed by the larger $O(N^2)$ operation.
        
          
        
    2. Space: $O(1)$ or $O(N)$ depending on the sorting algorithm used by the programming language under the hood (ignoring the space used to store the output array).
        
          
        

### 🎯 **Concept to learn today: Target Reduction & Two Pointers**

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`. Notice that the solution set must not contain duplicate triplets.

  

- **The Strategy:** Sort the array first. Iterate through the array, treating the current number as the "fixed" target. Then, use a `left` pointer (just past your fixed number) and a `right` pointer (at the end of the array) to squeeze inward, hunting for the two values that balance the fixed number to zero.
    
      
    
- **The Flow:**
    
      
    1. Sort `nums` in ascending order.
        
          
        
    2. Loop through `nums` with index `i`.
        
          
        
    3. _Duplicate check:_ If `i > 0` and `nums[i] == nums[i-1]`, `continue` to the next loop iteration to avoid duplicate results.
        
          
        
    4. Set `left = i + 1` and `right = length of nums - 1`.
        
          
        
    5. While `left < right`:
        
          
        - Calculate `current_sum = nums[i] + nums[left] + nums[right]`.
            
              
            
        - If `current_sum > 0`, the total is too high. Decrease it by moving `right` pointer left.
            
              
            
        - If `current_sum < 0`, the total is too low. Increase it by moving `left` pointer right.
            
              
            
        - If `current_sum == 0`, append the triplet to your results. Move both pointers inward and _skip any adjacent duplicates_ for both the left and right pointers to prevent identical triplet outputs.
            
              
            
    6. Return the results list.
        
          
        

## ⚙️ DevOps Essentials — **Docker Basics: Multi-Stage Builds**

Tags: #DevOps #Docker #Architecture #Optimization

  

Goal: When writing a Dockerfile for a compiled application (or installing heavy deployment frameworks), your container ends up massive because it includes all the compilers and build tools. Multi-stage builds allow you to use one container to compile the code, and a second, much smaller container to actually run it.

  

### 🎯 **Quick Review Summary: Leaving the Baggage Behind**

Instead of a single `FROM` statement in your Dockerfile, you use multiple. Each `FROM` begins a new "stage". You can selectively copy artifacts from one stage to another, leaving all the heavy, temporary build dependencies behind.

  

|**The Problem**|**The Multi-Stage Solution**|
|---|---|
|**Bloated Images**|An image with Python/C++ build headers and compilers might be 1.2GB. Moving this across a factory network is slow.|
|**Security Risks**|Leaving build tools (like `pip` or `gcc`) in a production container gives attackers extra utilities if they compromise the application.|
|**The Execution**|Stage 1 (The Builder) installs everything and compiles the application. Stage 2 (The Runner) is a tiny, bare-bones OS that simply copies the finished binary from Stage 1. The final image size drops from 1.2GB to 50MB.|

### 💻 **Real-World Code Execution**

Here is a conceptual Multi-Stage Dockerfile.

  

Dockerfile

```
# ---- STAGE 1: The Builder ----
# Uses a heavy image to compile/install dependencies
FROM ubuntu:22.04 AS builder
WORKDIR /build
RUN apt-get update && apt-get install -y build-essential
COPY . .
# (Imagine a command here that compiles the app into a binary called 'server_app')
RUN make server_app 

# ---- STAGE 2: The Production Runner ----
# Uses a tiny, ultra-lightweight base image
FROM alpine:latest
WORKDIR /app
# ONLY copy the finished binary from the 'builder' stage. The build tools are discarded.
COPY --from=builder /build/server_app .
CMD ["./server_app"]
```

## 🐧 Linux Learning — Command: **`journalctl`** (Systemd Log Manager)

Tags: #Linux #Command #journalctl #SysAdmin #Troubleshooting

  

Goal: If a critical background service (like Docker or an Ansible-deployed network daemon) crashes on an Ubuntu server, simply using `cat` on a text file won't cut it anymore. Modern Linux distributions use `systemd` to manage services, and `systemd` stores all its logs in a centralized, binary format.

  

### 🎯 **Quick Review Summary: The Service Interrogator**

`journalctl` is the tool you use to read these centralized logs. Because the logs are indexed, you can filter them precisely by time, service, or priority.

  

|**Scenario**|**Command**|**Description**|
|---|---|---|
|**Check a Specific Service**|**`sudo journalctl -u docker.service`**|**The Daily Driver.** Filters the massive system log to _only_ show logs generated by the Docker daemon.|
|**Tail the Logs Live**|`sudo journalctl -u ssh -f`|**Real-time Monitoring.** The `-f` (follow) flag acts exactly like `tail -f`, streaming new SSH login attempts to your terminal as they happen.|
|**Filter by Time**|`sudo journalctl --since "1 hour ago"`|**Incident Response.** When you know a server configuration failed at a specific time, this isolates the logs to the exact window of the failure.|
