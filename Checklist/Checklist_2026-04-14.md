# 📅 Checklist

| **Category**         | **Task**                                              | **Status** |
| -------------------- | ----------------------------------------------------- | ---------- |
| 🧠 LeetCode Practice | **11. Container With Most Water** (Two Pointers)      | ✅          |
| ⚙️ DevOps Essentials | **Jenkins Basics: Introduction to Pipelines**         | ✅          |
| 🐧 Linux Learning    | Command: **`kill` / `killall`** (Process Termination) | ✅          |
|                      |                                                       |            |

---

## 🧠 LeetCode — **11. Container With Most Water** Tags: #Array #TwoPointers #Greedy

Difficulty: Medium

### 🎯 **Concept to learn today: The Greedy Squeeze**

You are given an integer array `height` where each element represents a vertical line on a graph. Find two lines that together with the x-axis form a container, such that the container contains the most water.

- **The Strategy:** The width of the container is determined by the distance between two lines. The height is determined by the _shorter_ line. To maximize area, start with the maximum possible width (pointers at both ends). To find a potentially larger area, you must sacrifice width, so you should only ever move the pointer that points to the _shorter_ line in hopes of finding a taller one.
    
- **The Flow:**
    
    1. Initialize `left = 0` and `right = len(height) - 1`.
        
    2. Initialize `max_area = 0`.
        
    3. Loop while `left < right`:
        
        - Calculate the current area: `width = right - left`. The `current_height = min(height[left], height[right])`.
            
        - Update `max_area = max(max_area, width * current_height)`.
            
        - **The Greedy Choice:** If `height[left] < height[right]`, increment `left += 1`. Else, decrement `right -= 1`.
            
    4. Return `max_area`.
        
- **Efficiency:** You evaluate the container in a single pass inward, yielding an $O(N)$ time complexity and an $O(1)$ space complexity.
    

---

## ⚙️ DevOps Essentials — **Jenkins Basics: Introduction to Pipelines**

Tags: #DevOps #Jenkins #CICD #Automation

Goal: Transitioning from cloud-hosted automation (like GitHub Actions) to managing your own dedicated automation server. Jenkins is the industry-standard "butler" that builds, tests, and deploys your code.

### 🎯 **Quick Review Summary: The Declarative Pipeline**

Instead of manually clicking through a web interface to configure builds, modern Jenkins uses a file called a `Jenkinsfile` stored directly in your Git repository. This is known as "Pipeline as Code."

|**Pipeline Block**|**Description**|**Real-World Example**|
|---|---|---|
|**`agent`**|Defines _where_ the pipeline runs.|`agent { docker 'python:3.10' }` runs your entire pipeline inside a clean, isolated Python Docker container.|
|**`stages`**|The high-level phases of your workflow. Usually sequential.|`stage('Build')`, `stage('Test')`, `stage('Deploy')`. If the 'Test' stage fails, 'Deploy' is automatically skipped.|
|**`steps`**|The actual terminal commands Jenkins will execute inside a stage.|`sh 'pip install -r requirements.txt'` or `sh 'pytest tests/'`.|

### 💻 **Real-World Code Example**

Here is what a minimal, complete `Jenkinsfile` looks like:

Groovy

```
pipeline {
    agent any // Run on any available Jenkins server
    
    stages {
        stage('Test') {
            steps {
                echo 'Running unit tests...'
                sh 'python3 -m unittest discover'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying to Production...'
                sh './deploy_script.sh'
            }
        }
    }
}
```

---

## 🐧 Linux Learning — Command: **`kill` & `killall`** (Process Termination)

Tags: #Linux #Command #kill #OS #Debugging

Goal: When a background daemon freezes, a port is locked, or a script gets stuck in an infinite loop, you need to forcefully terminate the process using signals.

### 🎯 **Quick Review Summary: Termination Signals**

The `kill` command doesn't actually "kill" processes directly; it sends **Signals** to them. The default signal is `TERM` (15), which asks the program to shut down gracefully.

|**Command**|**Signal Type**|**Description & Best Use Case**|
|---|---|---|
|**`kill 1234`**|`SIGTERM` (15)|**Polite Request.** Asks Process ID 1234 to save its data and exit. Always try this first.|
|**`kill -9 1234`**|`SIGKILL` (9)|**The Nuclear Option.** The kernel instantly destroys the process without warning. Use only if a process is completely frozen.|
|**`killall nginx`**|`SIGTERM` (15)|**Mass Termination.** Kills processes by their _Name_ instead of their PID. Instantly shuts down all running Nginx worker processes at once.|

### 💻 **Real-World Terminal Example**

1. You try to start your Python web app, but get a `Port 8080 already in use` error.
    
2. You use `ps` or `lsof` (which you learned previously) to find the rogue PID.
    

Bash

```
$ lsof -i :8080
COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
python3  5678 user    3u  IPv4  12345      0t0  TCP *:8080 (LISTEN)
```

3. You terminate it gracefully.
    

Bash

```
$ kill 5678
```