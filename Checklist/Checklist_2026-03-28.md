# 📅 Checklist

| **Category**         | **Task**                                        | **Status** |
| -------------------- | ----------------------------------------------- | ---------- |
| 🧠 LeetCode Practice | **27. Remove Element** (Two Pointers)           | ✅          |
| ⚙️ DevOps Essentials | **Kubernetes Basics: Understanding Pods**       | ✅          |
| 🐧 Linux Learning    | Command: **`jq`** (Command-line JSON Processor) | ✅          |

---

## 🧠 LeetCode — **27. Remove Element** Tags: #Array #TwoPointers

Difficulty: Easy

### 🎯 **Concept to learn today: The Reader/Writer Pointers**

You are given an integer array `nums` and an integer `val`. You must remove all occurrences of `val` in `nums` **in-place**. The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to `val`.

- **The Strategy:** Use two pointers starting at the same position (index 0). One pointer reads every item, and the other pointer only writes when it finds a "safe" (non-target) value.
    
- **The Flow:**
    
    1. Initialize a `writer` pointer at `0`.
        
    2. Loop through the array with a `reader` pointer from `0` to the end.
        
    3. If `nums[reader]` is NOT equal to `val`:
        
        - Copy the value: `nums[writer] = nums[reader]`.
            
        - Move the writer forward: `writer += 1`.
            
    4. If it IS equal to `val`, do nothing and just let the `reader` move on.
        
    5. Return `writer` (which now represents the length of the new array).
        
- **Efficiency:** The `reader` scans the array exactly once, giving a time complexity of $O(N)$. Since all modifications happen within the original array, space complexity is exactly $O(1)$.
    

---

## ⚙️ DevOps Essentials — **Kubernetes Basics: Understanding Pods**

Tags: #DevOps #Kubernetes #Containers #Architecture

Goal: Transitioning from single-server Docker environments to orchestrated, multi-node cluster concepts.

### 1. The Smallest Unit

In standard Docker, the smallest deployable unit is a Container. In Kubernetes (K8s), the smallest deployable computing unit is a **Pod**. You never run a container directly in K8s; you wrap it in a Pod.

### 2. The Pod Ecosystem

- **One-to-One:** Most of the time, one Pod holds exactly one Docker container (e.g., your Python web app).
    
- **One-to-Many (Sidecars):** A Pod can hold _multiple_ containers that need to work tightly together. For example, your web app container and a logging agent container.
    
- **Shared Resources:** All containers inside the same Pod automatically share the same IP address, the same port space (they can communicate via `localhost`), and the same attached storage volumes.
    

---

## 🐧 Linux Learning — Command: **`jq`** (Command-line JSON Processor)

Tags: #Linux #Command #jq #DevOps #JSON

### 🎯 **Core Uses & API Output Parsing**

`jq` is the absolute standard for slicing, filtering, and mapping JSON data directly in your terminal. When working with cloud APIs or Kubernetes outputs, `jq` turns massive, unreadable JSON blobs into exactly the data points you need.

#### 1. Pretty Print

Takes a minified or messy JSON output and formats it with proper indentation and color-coding for human readability.

Bash

```
$ echo '{"server":"web-01","status":"active"}' | jq '.'
{
  "server": "web-01",
  "status": "active"
}
```

#### 2. Extract Specific Field

Drills down into nested JSON objects using dot notation to return only the specific value.

Bash

```
$ echo '{"pod": {"name": "nginx", "phase": "Running"}}' | jq '.pod.phase'
"Running"
```

#### 3. Filter Arrays

The `[]` operator iterates through an array of objects, and the pipe `|` passes each object to extract just their specific keys.

Bash

```
$ echo '[{"id":1, "port":80}, {"id":2, "port":443}]' | jq '.[] | .port'
80
443
```

---

Would you like me to write a short 5-line Python script demonstrating the Reader/Writer pointer logic so you can test it directly?