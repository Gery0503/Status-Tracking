# 📅 **Checklist_2026-05-01**

| **Category**               | **Task**                                                | **Status** |
| -------------------------- | ------------------------------------------------------- | ---------- |
| 🧠 LeetCode Practice       | **746. Min Cost Climbing Stairs** (Dynamic Programming) | ✅          |
| ⚙️ DevOps Essentials       | **Jenkins Basics: Slack/Email Notifications**           | ✅          |
| 🐧 Linux Learning          | Command: **`find`** (Advanced File Searching)           | ✅          |
| 🏭 **Dannie EMS Handbook** | **Hardware Burn-In Testing**                            | ✅          |

---

## 🧠 LeetCode — **746. Min Cost Climbing Stairs** Tags: #Array #DynamicProgramming

Difficulty: Easy

### 🎯 **Concept to learn today: Cost Optimization (DP Array)**

You are given an integer array `cost` where `cost[i]` is the cost of the $i^{th}$ step on a staircase. Once you pay the cost, you can either climb one or two steps. You can either start from the step with index 0, or the step with index 1. Return the minimum cost to reach the top of the floor (which is one step past the last element in the array).

- **The Strategy:** This perfectly builds upon the _Fibonacci_ logic you learned previously. To find the cheapest way to reach step $i$, you only need to look at the cheapest way to reach the _two steps right below it_. The minimum cost to reach step $i$ is the cost of step $i$ itself, plus the minimum of the total costs to reach step $i-1$ and step $i-2$.
    
- **The Flow:**
    
    1. You can modify the `cost` array in-place to save memory.
        
    2. Loop through the array starting from index `2` up to the end.
        
    3. For each step `i`, update its value: `cost[i] += min(cost[i-1], cost[i-2])`.
        
    4. Once the loop finishes, the "top" of the staircase is reached by taking a step from either the last element or the second-to-last element.
        
    5. Return `min(cost[-1], cost[-2])`.
        
- **Efficiency:** You iterate through the array exactly once, yielding an $O(N)$ time complexity. Because you overwrite the existing array values instead of creating a new one, the space complexity is optimized to $O(1)$.
    

---

## ⚙️ DevOps Essentials — **Jenkins Basics: Post-Build Notifications**

Tags: #DevOps #Jenkins #Automation #Monitoring

Goal: A CI/CD pipeline is only useful if the engineering team knows its status. If a deployment fails or a test suite breaks, developers shouldn't have to constantly refresh the Jenkins dashboard to find out.

### 🎯 **Quick Review Summary: The Notification Flow**

You combine the `post` block (which you learned when archiving artifacts) with notification plugins (like the Slack Notification Plugin or Email Extension) to push alerts directly to your team's communication channels.

|**Block**|**When it triggers**|**Best Use Case**|
|---|---|---|
|**`success`**|The pipeline ran flawlessly.|Sending a quiet, green checkmark to a `#deployments` Slack channel to log that v2.1 went live.|
|**`failure`**|A stage crashed or a test failed.|Tagging the `@on-call` team in an `#alerts` channel with a direct link to the broken Jenkins log.|
|**`fixed`**|The previous build failed, but _this_ build succeeded.|Letting the team know the pipeline has returned to a healthy state after an outage.|

### 💻 **Real-World Code Execution**

Here is how you configure a pipeline to alert a Slack channel if someone breaks the main branch.

Groovy

```
pipeline {
    agent any
    stages {
        stage('Test') {
            steps { sh 'pytest tests/' }
        }
    }
    post {
        failure {
            // Requires the Slack Integration plugin to be configured
            slackSend (
                color: '#FF0000', // Red for failure
                message: "🚨 BUILD FAILED: Job '${env.JOB_NAME}' (${env.BUILD_NUMBER}). Check logs here: ${env.BUILD_URL}"
            )
        }
        success {
            slackSend (
                color: '#00FF00', // Green for success
                message: "✅ BUILD SUCCESS: Job '${env.JOB_NAME}' is green."
            )
        }
    }
}
```

---

## 🐧 Linux Learning — Command: **`find`** (Advanced File Searching)

Tags: #Linux #Command #find #Filesystem #Debugging

Goal: When managing servers, you will constantly lose track of where specific configurations are stored, or you will need to hunt down massive log files that are eating up your disk space. `find` is the ultimate search tool for the Linux filesystem.

### 🎯 **Quick Review Summary: Search Parameters**

Unlike `grep` (which searches _inside_ files), `find` searches for the files themselves based on names, sizes, or creation dates.

|**Scenario**|**Command**|**Description**|
|---|---|---|
|**Find by Name**|**`find /etc -name "nginx.conf"`**|**The Daily Driver.** Searches the `/etc` directory (and all sub-folders) for a file exactly named `nginx.conf`.|
|**Find by Size**|`find /var/log -type f -size +1G`|**Disk Cleanup.** Searches `/var/log` for files (`-type f`) that are strictly larger than 1 Gigabyte (`+1G`).|
|**Find by Time**|`find . -mtime -7`|**Audit Trail.** Searches the current directory (`.`) for files that have been modified (`mtime`) within the last 7 days (`-7`).|

### 💻 **Real-World Terminal Example**

1. A Docker container is failing to start because it cannot find its database configuration file. You know the file ends in `.yaml`, but you don't know where the junior developer placed it.
    
2. You search the entire `/opt/app/` directory using a wildcard (`*`).
    

Bash

```
$ find /opt/app/ -name "*.yaml"
/opt/app/src/legacy_config.yaml
/opt/app/secrets/database.yaml
```

---

## 🏭 Dannie EMS Handbook — **Hardware Burn-In Testing**

Tags: #EMS #Manufacturing #Hardware #QualityControl

Goal: Understanding why we aggressively stress-test hardware components on the factory floor before software is finalized, and how it reduces costly RMAs (Return Merchandise Authorizations) for enterprise clients.

### 🎯 **Core Concept: The Bathtub Curve & Early Mortality**

In electronics manufacturing, hardware failure rates follow a "Bathtub Curve." Components are highly likely to fail in the first 48 hours of use (infant mortality). If they survive that initial period, they will likely run perfectly for years, before the failure rate spikes again at the end of their physical lifespan (wear-out).

- **Burn-In Testing:** A mandatory L10 process where fully assembled servers are powered on and run at maximum capacity (100% CPU utilization, heavy RAM read/writes) in a temperature-controlled environment for 12 to 72 hours.
    
- **MCE (Machine Check Exception):** Hardware-level errors generated by the CPU during Burn-In. If a RAM stick is slightly defective, normal booting might not catch it, but a 24-hour Burn-In will trigger an MCE, allowing the factory floor to replace the RAM _before_ the server ships.
    

### 🏢 **Factory Floor Application**

When you write or maintain deployment automation scripts, those scripts must often interface with the Burn-In testing suite (like Stress-ng or PTU). The automation must trigger the Burn-In at the L10 stage, monitor the output logs for thermal throttling or MCEs, and automatically flag the physical server's serial number with a "FAIL" status in the shop-floor database if the hardware degrades under pressure.