
---

# 📅 **Checklist_2026-04-26**

| **Category**               | **Task**                                             | **Status** |
| -------------------------- | ---------------------------------------------------- | ---------- |
| 🧠 LeetCode Practice       | **409. Longest Palindrome** (Hash Table / Greedy)    | ✅          |
| ⚙️ DevOps Essentials       | **Jenkins Basics: Secrets & Credentials Management** | ✅          |
| 🐧 Linux Learning          | Command: **`alias`** (Command Shortcuts)             | ✅          |
| 🏭 **Dannie EMS Handbook** | **L10 vs. L11 Server Integration**                   | ✅          |

---

## 🧠 LeetCode — **409. Longest Palindrome** Tags: #String #HashTable #Greedy

Difficulty: Easy

### 🎯 **Concept to learn today: Parity Counting (Odd vs. Even)**

Given a string `s` which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters. Letters are case sensitive, for example, `"Aa"` is not considered a palindrome here.

- **The Strategy:** A palindrome mirrors itself from the center. This means every character on the left must have a matching character on the right. Therefore, you can use _all_ characters that appear an even number of times. For characters that appear an odd number of times, you can use the even part of them (e.g., if you have 3 'A's, you can use 2). Finally, you can place exactly _one_ leftover odd character in the very center of the palindrome to maximize the length.
    
- **The Flow:**
    
    1. Create a Hash Map or array to count the frequency of every character in `s`.
        
    2. Initialize `length = 0` and a boolean `has_odd = False`.
        
    3. Loop through the counts in your Hash Map:
        
        - If the count is even: add the count to `length`.
            
        - If the count is odd: add `count - 1` to `length` (this makes it even and usable), and set `has_odd = True` (flagging that we have a center piece available).
            
    4. After the loop, if `has_odd` is `True`, add `1` to `length` for the exact center.
        
    5. Return `length`.
        
- **Efficiency:** You count the characters in $O(N)$ time. The Hash Map stores at most 52 unique characters (uppercase + lowercase), making space complexity a constant $O(1)$.
    

---

## ⚙️ DevOps Essentials — **Jenkins Basics: Credentials Management**

Tags: #DevOps #Jenkins #Security #Automation

Goal: In previous sessions, we automated builds and saved artifacts. But pipelines often require database passwords or AWS access keys. Hardcoding these in your Git repository is a massive security violation. Jenkins handles this via the **Credentials Binding Plugin**.

### 🎯 **Quick Review Summary: Secret Injection**

You manually save the sensitive data once in the Jenkins UI (Dashboard > Manage Jenkins > Credentials). Jenkins encrypts it and assigns it an ID (e.g., `prod-db-password`). You then reference that ID in your `Jenkinsfile`.

|**Method**|**How it works**|**Best Use Case**|
|---|---|---|
|**`environment` block**|Jenkins retrieves the secret and sets it as a Linux environment variable inside the agent.|**API Keys & Passwords.** Automatically passing `AWS_ACCESS_KEY_ID` to a deployment script.|
|**`withCredentials` step**|Creates temporary, scoped variables only for a specific step, and actively masks them in the console logs.|**Highly Sensitive Data.** Ensuring a database password is never accidentally printed in the Jenkins UI output logs.|

### 💻 **Real-World Code Execution**

Here is how you securely pull an AWS key into a deployment pipeline:

Groovy

```
pipeline {
    agent any
    
    // Global environment variables
    environment {
        // Jenkins fetches the secret ID 'aws-prod-key' and assigns it to MY_SECRET
        MY_SECRET = credentials('aws-prod-key')
    }

    stages {
        stage('Deploy') {
            steps {
                // The secret is safely injected at runtime
                sh 'echo "Deploying to AWS using secret..."'
                sh './deploy.sh --key $MY_SECRET'
            }
        }
    }
}
```

---

## 🐧 Linux Learning — Command: **`alias`** (Command Shortcuts)

Tags: #Linux #Command #alias #Productivity

Goal: When managing system administration tasks, typing long, repetitive commands (`kubectl get pods -n kube-system`) wastes time. `alias` allows you to create custom shorthand commands.

### 🎯 **Quick Review Summary: Customizing Your Shell**

|**Scenario**|**Command**|**Description**|
|---|---|---|
|**Create a Shortcut**|**`alias kgp="kubectl get pods"`**|**Temporary Creation.** Typing `kgp` will now execute the full string. (Note: no spaces around the `=` sign).|
|**View Aliases**|`alias`|**Audit.** Typing it without arguments lists all currently active shortcuts in your shell environment.|
|**Bypass Alias**|`\ls`|**Override.** If you aliased `ls` to `ls -la`, putting a backslash `\` in front runs the original, unmodified system command.|

### 💻 **Real-World Terminal Example**

1. You create an alias to quickly jump into your deployment folder.
    

Bash

```
$ alias gotodeploy="cd /var/www/html/app/deploy"
```

2. **The Catch:** Aliases created in the terminal disappear the second you close the SSH session. To make them permanent, you must append them to your user's shell profile file (`~/.bashrc`).
    

Bash

```
$ echo 'alias k="kubectl"' >> ~/.bashrc
$ source ~/.bashrc   # Reloads the file so it takes effect immediately
```

---

## 🏭 Dannie EMS Handbook — **L10 vs. L11 Server Integration**

Tags: #EMS #Manufacturing #Hardware #ServerBuilding

Goal: Standardizing the vocabulary used on the factory floor when bridging the gap between bare-metal hardware assembly and software/OS deployment for enterprise clients.

### 🎯 **Core Concept: Rack Integration Levels**

Manufacturing milestones in the server supply chain are defined by "Levels" (L-levels). Understanding the boundary between L10 and L11 is critical for diagnostic routing and software image flashing.

- **L10 (Rack Integration):** The phase where individual bare-metal servers are physically mounted into the server rack. This involves precision cabling, installing PDUs (Power Distribution Units), flashing the initial BIOS/BMC firmware, and pushing the OS. Crucially, this is where the rigorous hardware **Burn-In** (stress testing CPU/Memory) occurs.
    
- **L11 (Rack Rollout / Cluster Level):** The final factory phase before shipping. Multiple L10 racks are linked together. This involves configuring the Top-of-Rack (ToR) switches, setting up inter-rack networking, and verifying that the entire cluster acts as a cohesive unit.
    

### 🏢 **Factory Floor Application**

When working on automated provisioning systems, deploying software scripts to an L10 environment means targeting individual nodes directly for baseline diagnostics. At the L11 stage, the deployment scripts must be network-aware, handling switch configurations, DHCP Option 82 routing, and ensuring the entire rack can smoothly plug into the client's datacenter fabric without IP conflicts.