# 📅 **Checklist_2026-04-25**

| **Category**         | **Task**                                         | **Status** |
| -------------------- | ------------------------------------------------ | ---------- |
| 🧠 LeetCode Practice | **605. Can Place Flowers** (Array / Greedy)      | ✅          |
| ⚙️ DevOps Essentials | **Jenkins Basics: Archiving Artifacts**          | ✅          |
| 🐧 Linux Learning    | Command: **`chmod`** (Change Mode / Permissions) | ✅          |

---

## 🧠 LeetCode — **605. Can Place Flowers** Tags: #Array #Greedy

Difficulty: Easy

### 🎯 **Concept to learn today: Local Optimization (The Greedy Choice)**

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots. Given an integer array `flowerbed` containing `0`s (empty) and `1`s (planted), and an integer `n`, return `True` if `n` new flowers can be planted without violating the no-adjacent-flowers rule.

- **The Strategy:** A "Greedy" algorithm makes the optimal choice at every single step without worrying about the big picture. Here, the optimal choice is simple: as you scan left to right, the moment you see a valid empty spot, plant a flower immediately.
    
- **The Flow:**
    
    1. Handle the edge case: If `n == 0`, return `True` instantly.
        
    2. Loop through the `flowerbed` array using an index `i`:
        
        - Check if the current plot is empty (`flowerbed[i] == 0`).
            
        - Check if the left plot is safe: `i == 0` OR `flowerbed[i - 1] == 0`.
            
        - Check if the right plot is safe: `i == len(flowerbed) - 1` OR `flowerbed[i + 1] == 0`.
            
        - If _all three_ conditions are met:
            
            - Plant a flower: `flowerbed[i] = 1`. _(Crucial: you must mutate the array so future iterations know a flower is now here)._
                
            - Decrement your target: `n -= 1`.
                
            - If `n == 0`, return `True` early.
                
    3. If the loop finishes and `n` is still greater than 0, return `False`.
        
- **Efficiency:** You traverse the array a single time, checking local neighbors. Time complexity is $O(N)$. Because you modify the array in-place and only store the `n` counter, space complexity is exactly $O(1)$.
    

---

## ⚙️ DevOps Essentials — **Jenkins Basics: Archiving Artifacts**

Tags: #DevOps #Jenkins #CICD #Storage

Goal: In the last session, we learned that Docker build agents are ephemeral—they are destroyed the moment the pipeline finishes. But what if your pipeline compiles a finalized `app.jar` binary or generates an HTML test report? You must **archive** those files to save them back to the permanent Jenkins server before the container vaporizes.

### 🎯 **Quick Review Summary: The `post` Block**

In a declarative Jenkinsfile, the `post` section runs after your stages finish. It is the perfect place to safely extract and store your hard-earned build artifacts.

|**Post Condition**|**Description**|**Real-World Example**|
|---|---|---|
|**`always`**|Executes regardless of whether the build passed or failed.|**Test Reports.** You always want to save `pytest_report.xml` so developers can see exactly which tests failed.|
|**`success`**|Executes only if the entire pipeline passed.|**Compiled Binaries.** Saving the final `.zip`, `.jar`, or `.whl` file so it can be deployed to production.|
|**`failure`**|Executes only if the build crashed or tests failed.|**Error Notifications.** Sending a Slack or Email alert to the engineering team that the main branch is broken.|

### 💻 **Real-World Code Execution**

Here is how you extract files out of the temporary Docker agent and attach them permanently to the Jenkins Build history.

Groovy

```
pipeline {
    agent { docker 'node:18' }
    
    stages {
        stage('Build') {
            steps {
                sh 'npm run build' // Creates a 'dist/' folder
            }
        }
    }
    // Runs after all stages complete
    post {
        success {
            // Saves everything inside the 'dist' folder to the Jenkins UI
            archiveArtifacts artifacts: 'dist/**/*', fingerprint: true
            echo 'Build successful. Artifacts saved.'
        }
    }
}
```

---

## 🐧 Linux Learning — Command: **`chmod`** (Change Mode)

Tags: #Linux #Command #chmod #Security #OS

Goal: Previously, we used `chown` to change _who_ owns a file. Now, we use `chmod` to dictate _what_ those owners are allowed to do. This command modifies the Read (`r`), Write (`w`), and Execute (`x`) permissions.

### 🎯 **Quick Review Summary: Permission Syntax**

Permissions in Linux are divided into three tiers: **User** (the owner), **Group**, and **Others** (everyone else). `chmod` lets you assign permissions using either Symbols or Numbers.

|**Scenario**|**Command**|**Description**|
|---|---|---|
|**Make Executable (Symbolic)**|**`chmod +x deploy.sh`**|**Daily Driver.** The fastest way to make a newly written script runnable. It adds (`+`) the execute (`x`) flag.|
|**Revoke Access (Symbolic)**|`chmod go-rwx secret.key`|**Security Lockdown.** Removes (`-`) all read, write, and execute permissions from the Group (`g`) and Others (`o`).|
|**Standard Web File (Numeric)**|`chmod 644 index.html`|**Standard Practice.** The Owner can Read/Write (`6`). The Group and Others can only Read (`4`).|
|**Full Directory (Numeric)**|`chmod 755 /var/www/app`|**Standard Directory.** Owner has full access (`7`). Everyone else can Read and Execute (enter the folder) but not modify it (`5`).|

### 💻 **Real-World Terminal Example**

1. You pull a Python script from Git to run a database migration, but Linux denies execution because standard text files are not executable by default.
    

Bash

```
$ ./migrate.py
bash: ./migrate.py: Permission denied

$ ls -l migrate.py
-rw-r--r-- 1 jenkins developers 1024 Apr 25 10:00 migrate.py
```

2. You use `chmod` to add the execute capability.
    

Bash

```
$ chmod +x migrate.py
```

3. You verify the change. Notice the `x` has appeared in the permission string, and you can now run the script successfully.
    

Bash

```
$ ls -l migrate.py
-rwxr-xr-x 1 jenkins developers 1024 Apr 25 10:00 migrate.py

$ ./migrate.py
Migration successful!
```