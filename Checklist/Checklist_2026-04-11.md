# 📅 Checklist

| **Category**         | **Task**                                                         | **Status** |
| -------------------- | ---------------------------------------------------------------- | ---------- |
| 🧠 LeetCode Practice | **278. First Bad Version** (Binary Search)                       | ✅          |
| ⚙️ DevOps Essentials | **Kubernetes Basics: Services (Internal & External Networking)** | ✅          |
| 🐧 Linux Learning    | Command: **`free`** (System Memory Monitoring)                   | ✅          |

---

## 🧠 LeetCode — **278. First Bad Version** Tags: #BinarySearch #Interactive

Difficulty: Easy

### 🎯 **Concept to learn today: API-Driven Binary Search**

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad. Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one. You are given an API `bool isBadVersion(version)` which returns whether `version` is bad.

- **The Strategy:** A linear scan `1` to `n` would take $O(N)$ API calls, which is too slow. Since the array of boolean results `[False, False, True, True, True]` is technically "sorted", you can use Binary Search to minimize the number of API calls.
    
- **The Flow:**
    
    1. Initialize `left = 1` and `right = n`.
        
    2. Loop while `left < right`:
        
        - Calculate the middle: `mid = left + (right - left) // 2`. _(Note: doing it this way instead of `(left+right)//2` prevents integer overflow bugs in some languages)._
            
        - Call the API: `if isBadVersion(mid) == True`:
            
            - The current version is bad, which means the _first_ bad version is either this one or one before it. Update `right = mid`.
                
        - `else`:
            
            - The current version is good, so the first bad version must be _after_ this one. Update `left = mid + 1`.
                
    3. When the loop terminates, `left` will equal `right`, pointing to the first bad version. Return `left`.
        
- **Efficiency:** You cut the search space in half every time, resulting in an $O(\log N)$ time complexity and $O(1)$ space complexity.
    

---

## ⚙️ DevOps Essentials — **Kubernetes Basics: Services**

Tags: #DevOps #Kubernetes #Networking #Architecture

Goal: You have a Deployment keeping 5 Pods running. But Pod IP addresses change every time they crash and restart. How does your frontend app know where to send traffic if the backend IPs keep changing? Enter the **Service**.

### 🎯 **Quick Review Summary: Service Types**

A Kubernetes Service gives you a single, static IP address and DNS name that acts as a stable load balancer sitting in front of your mortal, ever-changing Pods.

| **Service Type** | **Description**                                                                     | **Best Use Case**                                                                                                       |
| ---------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **ClusterIP**    | (Default). Exposes the Service on a cluster-internal IP.                            | **Backend APIs / Databases.** Makes the service reachable _only_ from within the Kubernetes cluster. Secure and hidden. |
| **NodePort**     | Exposes the Service on each Node's IP at a static port (e.g., 30007).               | **Local Testing / Direct Access.** Opens a specific port directly on the physical server to route traffic inside.       |
| **LoadBalancer** | Provisions an external load balancer (via AWS, GCP, Azure) and assigns a public IP. | **Public Web Servers.** Exposes your app to the public internet so real users can access it.                            |

### 💻 **Real-World Terminal Execution**

#### 1. Exposing a Deployment

Let's expose the Nginx deployment we made previously so the public can see it.

Bash

```
# Create a LoadBalancer service for our web app targeting port 80
$ kubectl expose deployment my-web-app --type=LoadBalancer --port=80
service/my-web-app exposed
```

#### 2. Checking the Service Routing

Bash

```
$ kubectl get services
NAME         TYPE           CLUSTER-IP       EXTERNAL-IP     PORT(S)        AGE
my-web-app   LoadBalancer   10.110.15.220    203.0.113.50    80:31450/TCP   2m
kubernetes   ClusterIP      10.96.0.1        <none>          443/TCP        10d
```

_(Notice the `EXTERNAL-IP`. If you put `203.0.113.50` into your browser, the Cloud LoadBalancer forwards the request to the Kubernetes Service, which then balances the traffic across your 5 Nginx Pods)._

---

## 🐧 Linux Learning — Command: **`free`** (System Memory Monitoring)

Tags: #Linux #Command #free #Debugging #OS

Goal: When a server becomes unresponsive, or a Docker container suddenly crashes with an "OOMKilled" (Out Of Memory) error, `free` is the 5-second diagnostic tool to check if your server has exhausted its RAM.

### 🎯 **Quick Review Summary: Memory Flags**

|**Flag**|**Description**|**Best Use Case**|
|---|---|---|
|**`free -h`**|Human-readable output.|**Daily Driver.** Prints numbers in Gigabytes (G) or Megabytes (M) instead of raw bytes.|
|**`free -m`**|Output in strict Megabytes.|**Scripting.** Useful if you are passing the output into `awk` and need a consistent unit of measurement.|
|**`free -s 2`**|Continuous polling.|**Live Monitoring.** Runs the command automatically every 2 seconds (`-s 2`) so you can watch memory drain in real-time.|

### 💻 **Real-World Terminal Examples**

#### 1. Reading the Memory Table

Bash

```
$ free -h
               total        used        free      shared  buff/cache   available
Mem:           7.8Gi       3.2Gi       1.1Gi        45Mi       3.4Gi       4.2Gi
Swap:          2.0Gi          0B       2.0Gi
```

**How to interpret this like a DevOps Engineer:**

- **used:** The RAM actively consumed by your applications (3.2G).
    
- **free:** RAM that is completely empty and doing absolutely nothing (1.1G).
    
- **buff/cache:** RAM the Linux kernel is temporarily using to make reading/writing files faster (3.4G). _This is a good thing!_
    
- **available:** **This is the most important number.** This is how much RAM is _actually_ ready for new applications to use (4.2G) because Linux will instantly drop the `buff/cache` if a real application needs the space.
    
- _Rule of thumb: If `available` gets close to 0, or `Swap` starts being heavily used, your server is in critical danger of crashing._