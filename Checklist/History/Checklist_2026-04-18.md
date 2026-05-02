# 📅 **Checklist_2026-04-18**

| **Category**         | **Task**                                              | **Status** |
| -------------------- | ----------------------------------------------------- | ---------- |
| 🧠 LeetCode Practice | **83. Remove Duplicates from Sorted List** (Pointers) | ✅          |
| ⚙️ DevOps Essentials | **Jenkins Basics: Triggers & Webhooks**               | ✅          |
| 🐧 Linux Learning    | Command: **`chown`** (Change File Owner and Group)    | ✅          |

---

## 🧠 LeetCode — **83. Remove Duplicates from Sorted List** Tags: #LinkedList #Pointers

Difficulty: Easy

### 🎯 **Concept to learn today: The Look-Ahead Pointer**

You are given the `head` of a sorted linked list. You must delete all duplicates such that each element appears only once. Return the linked list sorted as well.

- **The Strategy:** Since the linked list is _already sorted_, any duplicate values will be directly next to each other. You only need a single pointer (`curr`) to look at the current node and "peek" at the next node. If they match, you simply bypass the next node.
    
- **The Flow:**
    
    1. Check for the edge case: If `head` is `None`, return `None`.
        
    2. Initialize a pointer `curr = head`.
        
    3. Loop while `curr` is not null AND `curr.next` is not null:
        
        - If `curr.val == curr.next.val`: You found a duplicate! Bypass it by setting `curr.next = curr.next.next`. _(Do NOT move `curr` forward yet, because the new `next` node might also be a duplicate)._
            
        - If `curr.val != curr.next.val`: It's a unique number. Move forward by setting `curr = curr.next`.
            
    4. Return `head`.
        
- **Efficiency:** You traverse the linked list exactly one time, giving a time complexity of $O(N)$. You do not create any new nodes, keeping space complexity strictly at $O(1)$. This is an excellent low-energy algorithmic exercise because the logic is purely mechanical.
    

---

## ⚙️ DevOps Essentials — **Jenkins Basics: Triggers & Webhooks**

Tags: #DevOps #Jenkins #CICD #Automation

Goal: In the last session, we wrote a Pipeline script (`Jenkinsfile`). But a pipeline is useless if you have to click "Build" manually every time. Today, we learn how Jenkins knows _when_ to execute your pipeline automatically.

### 🎯 **Quick Review Summary: Pipeline Triggers**

|**Trigger Type**|**Description**|**Best Use Case**|
|---|---|---|
|**Webhooks**|GitHub/GitLab sends an HTTP POST request to Jenkins the exact second code is pushed.|**Continuous Integration.** The absolute industry standard. Code is tested immediately upon push.|
|**Poll SCM**|Jenkins asks Git every X minutes: "Are there any new commits?"|**Legacy Systems.** Used when your Jenkins server is hidden behind a strict corporate firewall and cannot receive inbound webhooks from GitHub.|
|**Cron (Schedule)**|Runs at a specific time (e.g., midnight).|**Nightly Builds.** Running heavy security scans, database backups, or generating daily reports.|
|**Upstream**|Triggered only when _another_ Jenkins job finishes successfully.|**Deployment Chains.** Run the "Deploy to Staging" job, and if it passes, automatically trigger the "Deploy to Production" job.|

### 💻 **Real-World Code Execution**

You define these triggers directly inside your `Jenkinsfile` using the `triggers` block.

Groovy

```
pipeline {
    agent any
    
    // Tell Jenkins exactly when to run this pipeline automatically
    triggers {
        // Run every night at midnight (Cron syntax)
        cron('0 0 * * *')
        
        // OR run whenever GitHub sends a webhook (Configured in GitHub settings)
        githubPush() 
    }
    
    stages {
        stage('Build') {
            steps {
                echo 'Building the application...'
            }
        }
    }
}
```

---

## 🐧 Linux Learning — Command: **`chown`** (Change File Owner and Group)

Tags: #Linux #Command #chown #Security #OS

Goal: When working with DevOps tools like Docker or Jenkins, you will constantly encounter `Permission Denied` errors. This usually happens because a file was created by the `root` user, but Jenkins needs broader access than what the default group or "others" permissions allow. `chown` fixes this by reassigning ownership.

### 🎯 **Quick Review Summary: Ownership Transfer**

|**Scenario**|**Command**|**Description**|
|---|---|---|
|**Change User Only**|**`sudo chown jenkins app.log`**|**Targeted Fix.** Transfers ownership of `app.log` from its current owner to the `jenkins` user.|
|**Change User and Group**|`sudo chown jenkins:developers app.log`|**Standard Practice.** Changes the owner to `jenkins`, and changes the group access to the `developers` group simultaneously (separated by a colon).|
|**Change a Directory**|`sudo chown -R www-data:www-data /var/www/`|**The Recursive Fix.** The `-R` flag applies the ownership change to the folder and _every single file_ inside it. Crucial for web servers.|

### 💻 **Real-World Terminal Example**

1. You create a deployment script using `sudo`, which makes `root` the owner. The default permissions allow "Others" to read and execute the file, but _not_ write to it.
    

Bash

```
$ ls -l deploy.sh
-rwxr-xr-x 1 root root 1024 Apr 18 10:00 deploy.sh
```

2. During the CI/CD pipeline, Jenkins attempts to dynamically append the current Build Number or inject environment variables into the script before running it (e.g., `echo "BUILD=55" >> deploy.sh`). Because Jenkins falls under "Others", it lacks the `w` (write) permission and the pipeline crashes with a `Permission denied` error.
    

To fix this, you use `chown` to give ownership to the `jenkins` user and the `docker` group, granting Jenkins the full `rwx` privileges reserved for the file owner.

Bash

```
$ sudo chown jenkins:docker deploy.sh
```

3. You verify the ownership has successfully transferred. Now Jenkins can modify the file before executing it.
    

Bash

```
$ ls -l deploy.sh
-rwxr-xr-x 1 jenkins docker 1024 Apr 18 10:00 deploy.sh
```