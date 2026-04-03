# 📅 **Checklist**

| **Category**         | **Task**                                          | **Status** |
| -------------------- | ------------------------------------------------- | ---------- |
| 🧠 LeetCode Practice | **203. Remove Linked List Elements** (Dummy Node) | ✅          |
| ⚙️ DevOps Essentials | **Docker Basics: Data Persistence & Volumes**     | ✅          |
| 🐧 Linux Learning    | Command: **`ps`** (Process Status)                | ✅          |

---

## 🧠 LeetCode — **203. Remove Linked List Elements** Tags: #LinkedList #Pointers

Difficulty: Easy

### 🎯 **Concept to learn today: The Dummy Node Pattern**

You are given the `head` of a linked list and an integer `val`. Remove all the nodes of the linked list that have `Node.val == val`, and return the new head.

- **The Strategy:** Deleting a node in the _middle_ of a list is easy (`prev.next = curr.next`). But what if the node you need to delete is the very first one (the `head`)? To avoid writing messy edge-case `if` statements just for the head, you temporarily attach a "Dummy Node" to the very front of the list.
    
- **The Flow:**
    
    1. Create a `dummy` node: `dummy = ListNode(next=head)`.
        
    2. Set a `curr` pointer starting at `dummy`.
        
    3. Loop while `curr.next` is not null:
        
        - If `curr.next.val == val`: skip the target node by pointing `curr.next = curr.next.next`. (Do _not_ move `curr` forward yet, as the new next node might also equal `val`).
            
        - Else: move `curr` forward (`curr = curr.next`).
            
    4. Return `dummy.next` (which is the true head of your cleaned list).
        
- **Efficiency:** You iterate through the linked list exactly once, yielding an $O(N)$ time complexity. You only use a single pointer variable, keeping space complexity at $O(1)$.
    

---

## ⚙️ DevOps Essentials — **Docker Basics: Data Persistence**

Tags: #DevOps #Docker #Architecture #Storage

Here is the refined and translated version of your Docker notes:

# 🐳 Docker Data Persistence Notes

**Core Goal:** Understanding how to save data permanently. By default, Docker containers are **ephemeral**. If a container crashes or is deleted, all the data inside it vanishes. To save data, you must mount external storage into the container.

---

### 🎯 Storage Strategies Overview

|**Storage Type**|**Command Example (-v syntax)**|**Best Use Case & Technical Traits**|
|---|---|---|
|**Named Volume**|`docker run -v pgdata:/var/lib/postgresql/data postgres`|**Database Persistence (Best for Production).** Completely managed by Docker and hidden safely on the host machine (e.g., `/var/lib/docker/volumes/...` on Linux). Offers the best performance, security, and isolation.|
|**Bind Mount**|`docker run -v $(pwd)/src:/app/src node`|**Live Code Reloading (Best for Local Dev).** Directly links a specific folder on your laptop to a folder inside the container. Using `$(pwd)` ensures consistent relative paths regardless of which developer runs the command.|
|**Anonymous Volume**|`docker run -v /app/logs nginx`|**Temporary Host Storage (Performance Optimization).** Docker creates a randomly named folder. Useful for bypassing the slow writable layer for high-frequency writes (like logs) when you don't care about keeping the data.|

---

### 💡 Expert Tips & Under the Hood

#### 1. The Writable Layer & Performance

- **Definition:** Every container has a thin, top writable layer powered by a Union File System (UnionFS).
    
- **The Catch:** Frequent I/O operations (reading/writing) in this layer place a heavy burden on the storage driver, resulting in extremely poor performance compared to native disk speeds.
    
- **Best Practice:** Even for temporary files you don't intend to keep, it is better to mount an Anonymous Volume. This bypasses the container's writable layer, routing writes directly to the host's disk for optimal speed and preventing the container size from ballooning.
    

#### 2. Command Selection: `-v` vs. `--mount` (Highly Recommended)

While the `-v` syntax is shorter, official Docker guidelines strongly recommend using `--mount` for professional development and production. Here is why:

- **The `-v` Auto-Creation Trap:** If you specify a host path that doesn't exist using `-v`, Docker won't throw an error. Instead, it will automatically create an empty directory owned by `root`. This often leads to frustrating permission errors or unexpected bugs (e.g., expecting a configuration file but getting an empty folder).
    
- **The `--mount` Fail-Fast Principle:** If the source path doesn't exist, `--mount` will **immediately throw an error and refuse to start the container**. This strict behavior is crucial for automation and debugging.
    

**Syntax Comparison:**

Bash

```
# Traditional (Prone to silent folder creation)
docker run -v $(pwd)/src:/app/src node

# Professional (Explicit, fails fast if path is missing)
docker run --mount type=bind,source=$(pwd)/src,target=/app/src node
```

#### 3. Permission Warnings

When the Docker daemon (which runs as `root`) auto-creates a directory via the `-v` flag, standard users are often locked out of modifying those files on the host machine. To avoid "Permission Denied" headaches, either manually create the directories before running the container, or use `--mount` to ensure you catch missing paths immediately.

---

## 🐧 Linux Learning — Command: **`ps`** (Process Status)

Tags: #Linux #Command #ps #Debugging #OS

Goal: `ps` provides a snapshot of the current processes running on your machine. It is the absolute first step when a server is running slow or a port is locked up, letting you identify the rogue application.

### 🎯 **Quick Review Summary: Process Discovery**

|**Command Flag**|**Description**|**Best Use Case**|
|---|---|---|
|**`ps aux`**|Shows all processes from all users in BSD format.|General system monitoring. Shows CPU and Memory % usage for each process.|
|**`ps -ef`**|Shows all processes in standard UNIX format.|Finding Parent Process IDs (PPID) to see which application launched another application.|
|**`ps -o`**|Custom output format.|Scripting. e.g., `ps -o pid,comm` only prints the exact columns you request.|

### 💻 **Real-World Terminal Examples**

#### 1. Finding a specific running service

Using `ps aux` mixed with `grep` is the daily-driver method for checking if a service (like a web server or database) is actually running.

Bash

```
$ ps aux | grep nginx
root        1234  0.0  0.1  14234  1024 ?        Ss   10:00   0:00 nginx: master process
www-data    1235  0.0  0.2  14536  2048 ?        S    10:00   0:00 nginx: worker process
user        1289  0.0  0.0   6432   720 pts/0    S+   10:05   0:00 grep --color=auto nginx
```

_(Notice how it shows the user running the process, the Process ID (PID) `1234`, and the exact command executed)_

#### 2. Viewing the Process Tree

If a background daemon is spawning dozens of sub-processes (like a Python worker pool), you can view them hierarchically.

Bash

```
$ ps -ejH
  PID  PGID   SID TTY          TIME CMD
    1     1     1 ?        00:00:02 systemd
  500   500   500 ?        00:00:00   sshd
  510   510   500 ?        00:00:00     bash
  520   520   500 ?        00:00:01       python3 worker.py
  521   520   500 ?        00:00:00         python3 sub_worker.py
```