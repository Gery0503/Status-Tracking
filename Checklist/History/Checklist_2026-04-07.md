# 📅 **Checklist**

| **Category**         | **Task**                                          | **Status** |
| -------------------- | ------------------------------------------------- | ---------- |
| 🧠 LeetCode Practice | **485. Max Consecutive Ones** (Array Traversal)   | ✅          |
| ⚙️ DevOps Essentials | **Kubernetes Basics: Deployments & Scaling**      | ✅         |
| 🐧 Linux Learning    | Command: **`dig`** (DNS Lookup & Troubleshooting) | ✅         |

---

## 🧠 LeetCode — **485. Max Consecutive Ones** Tags: #Array

Difficulty: Easy

### 🎯 **Concept to learn today: The Resetting Counter**

You are given a binary array `nums` (containing only `0`s and `1`s). Return the maximum number of consecutive `1`s in the array.

- **The Strategy:** You need to keep track of two things: your _current_ streak of `1`s and the _maximum_ streak you've seen so far. When you hit a `0`, the current streak is broken and must be reset to zero.
    
- **The Flow:**
    
    1. Initialize `max_count = 0` and `current_count = 0`.
        
    2. Loop through each number in the array.
        
    3. If the number is `1`:
        
        - Increment `current_count` by 1.
            
        - Update `max_count` by taking the maximum of `max_count` and `current_count`.
            
    4. If the number is `0`:
        
        - Reset `current_count` back to 0.
            
    5. Return `max_count` after the loop ends.
        
- **Efficiency:** You only pass through the array a single time, so the time complexity is exactly $O(N)$. Because you are only storing two integer variables to track the counts, the space complexity is strictly $O(1)$.
    

---

## ⚙️ DevOps Essentials — **Kubernetes Basics: Deployments**

Tags: #DevOps #Kubernetes #Containers #Architecture

Goal: Previously, we looked at Pods. However, in production, you _never_ create a Pod directly. Pods are mortal—if they crash, they stay dead. To keep applications highly available, you use a **Deployment**.

### 🎯 **Quick Review Summary: Deployment Mechanics**

A Deployment acts as a supervisor. You tell it your _desired state_ (e.g., "I always want 3 copies of my web server running"), and it automatically creates, monitors, and replaces Pods to maintain that state.

| **Feature**         | **Description**                                                      | **Why it matters**                                                                                      |
| ------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Self-Healing**    | Automatically restarts or replaces Pods that fail or are deleted.    | If a worker node physically burns down, the Deployment instantly schedules new Pods on surviving nodes. |
| **Scaling**         | Easily increase or decrease the number of running Pods (`Replicas`). | Handles traffic spikes (Black Friday) by horizontally scaling out, then scaling back in to save money.  |
| **Rolling Updates** | Updates Pods to a new version one by one, rather than all at once.   | Achieves Zero-Downtime deployments. Users won't even notice the backend version was upgraded.           |

### 💻 **Real-World Terminal Execution**

#### 1. Creating and Scaling a Deployment

Bash

```
# Tell Kubernetes to run an Nginx deployment
$ kubectl create deployment my-web-app --image=nginx:latest
deployment.apps/my-web-app created

# Check the deployment status (currently 1 pod running)
$ kubectl get deployments
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
my-web-app   1/1     1            1           15s

# A traffic spike hits! Scale it out to 5 replicas instantly
$ kubectl scale deployment my-web-app --replicas=5
deployment.apps/my-web-app scaled

# Verify 5 Pods are now running
$ kubectl get pods
NAME                          READY   STATUS    RESTARTS   AGE
my-web-app-5c8f85f57-2q8x4    1/1     Running   0          5s
my-web-app-5c8f85f57-8p4jk    1/1     Running   0          5s
my-web-app-5c8f85f57-9tlmx    1/1     Running   0          5s
my-web-app-5c8f85f57-bg2w9    1/1     Running   0          5s
my-web-app-5c8f85f57-jkl12    1/1     Running   0          2m
```

---

## 🐧 Linux Learning — Command: **`dig`** (Domain Information Groper)

Tags: #Linux #Command #dig #Networking #DNS

Goal: When your app cannot connect to a database or a third-party API, DNS failure is the most common culprit. `dig` is the definitive tool to query DNS name servers and troubleshoot routing issues.

### 🎯 **Quick Review Summary: DNS Querying**

|**Scenario**|**Command**|**Description**|
|---|---|---|
|**Standard IP Lookup**|**`dig example.com`**|**Daily Driver.** Queries the A Record to find the exact IP address behind a domain name.|
|**Clean Output**|`dig example.com +short`|**Scripting.** Strips away all the verbose DNS metadata and returns _only_ the IP address.|
|**Specific Record Type**|`dig example.com MX`|**Mail Debugging.** Queries specific record types, such as `MX` (Mail Exchange) to verify email routing, or `CNAME` for aliases.|

### 💻 **Real-World Terminal Examples**

#### 1. Verifying an IP Address (The basic lookup)

If a user says your website is down, check if DNS is routing to the correct server IP.

Bash

```
$ dig google.com +short
142.250.190.46
```

#### 2. Querying a Specific DNS Server

Sometimes your local ISP caches bad DNS records. You can force `dig` to bypass your local network and ask a specific public DNS server directly (like Google's `8.8.8.8` or Cloudflare's `1.1.1.1`) by using the `@` symbol.

Bash

```
$ dig @8.8.8.8 mycompany.com

; <<>> DiG 9.18.18-0ubuntu0.22.04.2-Ubuntu <<>> @8.8.8.8 mycompany.com
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 48123
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; ANSWER SECTION:
mycompany.com.      300     IN      A       203.0.113.50

;; Query time: 14 msec
;; SERVER: 8.8.8.8#53(8.8.8.8) (UDP)
```