# 📅 Checklist

| **Category**         | **Task**                                                 | **Status** |
| -------------------- | -------------------------------------------------------- | ---------- |
| 🧠 LeetCode Practice | **205. Isomorphic Strings**                              | ✅          |
| ⚙️ DevOps Essentials | **Kubernetes Basics: Interacting with Pods (`kubectl`)** | ✅          |
| 🐧 Linux Learning    | Command: **`find`** (File Search & Execution)            | ✅          |

---

## 🧠 LeetCode — **205. Isomorphic Strings** Tags: #String #HashMap

Difficulty: Easy

### 🎯 **Concept to learn today: Bijective Mapping (Two-Way Memory)**

You are given two strings `s` and `t`. You need to determine if they are isomorphic. Two strings are isomorphic if the characters in `s` can be replaced to get `t`, but no two characters may map to the same character, and a character may map to itself.

- **The Strategy:** A single Hash Map is not enough because it only checks one direction. You must use _two_ Hash Maps to ensure a strict 1-to-1 relationship (a bijection) between the characters of `s` and `t`.
    
- **The Flow:**
    
    1. Initialize two empty dictionaries: `map_s_to_t` and `map_t_to_s`.
        
    2. Loop through both strings simultaneously by zipping them together: `for char_s, char_t in zip(s, t):`
        
    3. If `char_s` is already in `map_s_to_t`, check if its mapped value equals `char_t`. If not, return `False` (Conflict!).
        
    4. If `char_t` is already in `map_t_to_s`, check if its mapped value equals `char_s`. If not, return `False` (Conflict!).
        
    5. If neither exists, add the new mappings: `map_s_to_t[char_s] = char_t` and `map_t_to_s[char_t] = char_s`.
        
    6. If the loop finishes without any conflicts, return `True`.
        
- **Efficiency:** You iterate through the strings exactly once, giving a time complexity of $O(N)$. Since the number of possible unique characters is strictly bounded (e.g., 256 ASCII characters), the Hash Maps will never grow beyond a fixed size, making the space complexity $O(1)$.
    

---

## ⚙️ DevOps Essentials — **Kubernetes Basics: Interacting with Pods**

Tags: #DevOps #Kubernetes #Containers #CLI

Goal: Yesterday we learned that Pods are the smallest deployable units in K8s. Today, we learn how to inspect and troubleshoot them using the command-line tool, `kubectl`.

### 🎯 **Real-World Commands & Examples**

#### 1. Checking Pod Status

Before you can troubleshoot, you need to see if the Pod is actually running, crashing, or pending.

Bash

```
$ kubectl get pods
NAME                     READY   STATUS             RESTARTS   AGE
frontend-app-xyz         1/1     Running            0          2m
backend-api-abc          0/1     CrashLoopBackOff   3          5m
```

#### 2. Viewing Application Logs

If a Pod is crashing (like `backend-api-abc` above), your very first step is to pull the logs to see the error output from the container.

Bash

```
$ kubectl logs backend-api-abc
[ERROR] Database connection failed: Timeout at 10.0.5.12:5432
[FATAL] Shutting down application...
```

#### 3. Getting a Shell Inside the Pod

Sometimes logs aren't enough. You need to physically step inside the running container to check files, environment variables, or run network tests.

Bash

```
$ kubectl exec -it frontend-app-xyz -- sh
/usr/src/app # cat /etc/os-release
NAME="Alpine Linux"
/usr/src/app # exit
$ 
```

---

## 🐧 Linux Learning — Command: **`find`** (File Search & Execution)

Tags: #Linux #Command #find #Filesystem

### 🎯 **Core Uses & File Discovery**

`find` is a remarkably powerful tool for searching the Linux filesystem dynamically. It searches for files in a directory hierarchy based on names, sizes, dates, and permissions.

#### 1. Find by Name

Search the current directory (`.`) and all subdirectories for any file ending in `.log`.

Bash

```
$ find . -name "*.log"
./var/log/nginx/access.log
./var/log/nginx/error.log
./app/debug.log
```

#### 2. Find by Size

Search the entire root filesystem (`/`) for files larger than 500 Megabytes, which is incredibly useful for finding what is filling up a server's disk space.

Bash

```
$ find / -type f -size +500M
/var/lib/docker/containers/a1b2c3d4/a1b2c3d4-json.log
/home/user/backup_archive.tar.gz
```

#### 3. Find by Modification Time

Find files in the `/etc` directory that have been modified within the last `1` day (perfect for answering "What configuration file did I accidentally break yesterday?").

Bash

```
$ find /etc -mtime -1
/etc/resolv.conf
/etc/nginx/nginx.conf
```