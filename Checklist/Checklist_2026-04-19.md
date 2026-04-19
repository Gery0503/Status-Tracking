# 📅 **Checklist_2026-04-19**

| **Category**         | **Task**                                        | **Status** |
| -------------------- | ----------------------------------------------- | ---------- |
| 🧠 LeetCode Practice | **509. Fibonacci Number** (Dynamic Programming) | ✅          |
| ⚙️ DevOps Essentials | **Jenkins Basics: Docker as Build Agents**      | ✅          |
| 🐧 Linux Learning    | Command: **`ln`** (Symbolic Links)              | ✅          |

---

## 🧠 LeetCode — **509. Fibonacci Number** Tags: #Math #DynamicProgramming #Recursion

Difficulty: Easy

### 🎯 **Concept to learn today: Memoization and Bottom-Up State Tracking**

The Fibonacci numbers form a sequence where each number is the sum of the two preceding ones, starting from `0` and `1`. Given `n`, calculate `F(n)`.

- **The Strategy:** The standard mathematical formula `F(n) = F(n-1) + F(n-2)` naturally suggests recursion. However, pure recursion is terrible here because it recalculates the exact same branches repeatedly, taking exponential time. Instead, use a "Bottom-Up" iterative approach to dynamically carry the previous two states forward without a massive memory footprint.
    
- **The Flow:**
    
    1. Handle the base cases first: If `n == 0`, return `0`. If `n == 1`, return `1`.
        
    2. Initialize two variables to represent the starting window: `a = 0` (representing F(0)) and `b = 1` (representing F(1)).
        
    3. Loop from `2` up to `n` (inclusive):
        
        - Calculate the new number: `next_val = a + b`.
            
        - Slide the window forward: set `a = b`, and set `b = next_val`.
            
    4. After the loop finishes, return `b` (which now holds the final value of F(n)).
        
- **Efficiency:** You loop through the numbers exactly once, making the time complexity $O(N)$. Because you only rely on two variables to remember the past state instead of a massive array or recursive call stack, your space complexity is a perfectly optimized $O(1)$. This is the gateway concept to all advanced Dynamic Programming.
    

---

## ⚙️ DevOps Essentials — **Jenkins Basics: Docker as Build Agents**

Tags: #DevOps #Jenkins #Docker #CICD

Goal: In older setups, Jenkins servers became bloated because administrators had to manually install Java, Python, Node, and Go directly onto the machine. Modern pipelines solve this by running jobs _inside_ ephemeral Docker containers.

### 🎯 **Quick Review Summary: Agent Isolation**

By using Docker as an agent, Jenkins spins up a fresh, perfectly configured container just for your build, runs your code inside it, and then instantly deletes the container when finished.

|**Pipeline Syntax**|**Description**|**Best Use Case**|
|---|---|---|
|**`agent any`**|Runs directly on the Jenkins host machine.|**Simple/Legacy Jobs.** Relies heavily on whatever tools happen to be pre-installed on the server.|
|**`agent { docker 'python:3.10' }`**|Runs the entire pipeline inside a specified Docker image.|**Isolated Builds.** Ensures your Python tests run in a pristine 3.10 environment, completely avoiding dependency conflicts.|
|**Per-Stage Agents**|Different stages use different containers.|**Complex Workflows.** Stage 1 compiles React in a Node container; Stage 2 builds the backend in a Go container.|

### 💻 **Real-World Code Execution**

Here is a `Jenkinsfile` showing how to use an isolated Docker container for a build. Note how you don't have to install Python on the server—Jenkins pulls the image and handles it for you.

Groovy

```
pipeline {
    // Tell Jenkins to spin up a Python container to run this pipeline
    agent {
        docker { 
            image 'python:3.10-slim' 
            // Ensures the container shares the same workspace as Jenkins
            args '-v $WORKSPACE:/app -w /app' 
        }
    }
    
    stages {
        stage('Test') {
            steps {
                // This command executes inside the Python 3.10 container
                echo 'Running unit tests in isolated environment...'
                sh 'pip install -r requirements.txt'
                sh 'pytest tests/'
            }
        }
    }
}
```

---

## 🐧 Linux Learning — Command: **`ln`** (Symbolic Links)

Tags: #Linux #Command #ln #Filesystem #OS

Goal: A Symbolic Link (symlink) is the Linux equivalent of a "Shortcut" in Windows. It points to another file or folder. It is heavily used in DevOps to manage application versions and configuration files.

### 🎯 **Quick Review Summary: Linking Files**

|**Scenario**|**Command**|**Description**|
|---|---|---|
|**Create a Soft Link**|**`ln -s target_file link_name`**|**Daily Driver.** Creates a shortcut. If you delete the `target_file`, the `link_name` becomes a broken "dangling" link.|
|**Enable a Web Config**|`ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled/app`|**Standard Practice.** The official way to activate an Nginx website. You write the config in `available`, and symlink it to `enabled`.|
|**Force Overwrite**|`ln -sf new_version.jar app.jar`|**Deployment.** The `-f` (force) flag updates an existing link to point to a new target without throwing an "already exists" error.|

### 💻 **Real-World Terminal Example**

1. You are deploying a new version of your backend application (`backend-v2.0.log`), but your log monitoring tool expects a file strictly named `current.log`. You create a symlink to bridge the gap.
    

Bash

```
$ ln -s backend-v2.0.log current.log
```

2. You use `ls -l` to verify the link. The `l` at the start of the permissions string indicates it's a link, and the arrow `->` shows where it points.
    

Bash

```
$ ls -l current.log
lrwxrwxrwx 1 jenkins docker 16 Apr 19 12:00 current.log -> backend-v2.0.log
```

3. When `backend-v3.0.log` is released tomorrow, you simply force the link to point to the new file, allowing your monitoring tool to keep reading `current.log` without any configuration changes.
    

Bash

```
$ ln -sf backend-v3.0.log current.log
```