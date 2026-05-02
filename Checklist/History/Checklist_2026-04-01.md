# 📅 **Checklist**

| **Category**         | **Task**                                       | **Status** |
| -------------------- | ---------------------------------------------- | ---------- |
| 🧠 LeetCode Practice | **35. Search Insert Position** (Binary Search) | ✅          |
| ⚙️ DevOps Essentials | **Docker Basics: Writing a `Dockerfile`**      | ✅          |
| 🐧 Linux Learning    | Command: **`awk`** (Text & Data Extraction)    | ✅          |

---

## 🧠 LeetCode — **35. Search Insert Position** Tags: #Array #BinarySearch

Difficulty: Easy

### 🎯 **Concept to learn today: Divide and Conquer**

You are given a sorted array of distinct integers and a target value. Return the index if the target is found. If not, return the index where it would be if it were inserted in order. You must write an algorithm with $O(\log n)$ runtime complexity.

- **The Strategy:** A linear scan ($O(N)$) is too slow. Since the array is already sorted, you can use Binary Search to repeatedly halve the search space.
    
- **The Flow:**
    
    1. Initialize `left = 0` and `right = len(nums) - 1`.
        
    2. Loop while `left <= right`:
        
        - Calculate the middle index: `mid = (left + right) // 2`.
            
        - If `nums[mid] == target`: You found it! Return `mid`.
            
        - If `nums[mid] < target`: The target must be in the right half. Update `left = mid + 1`.
            
        - If `nums[mid] > target`: The target must be in the left half. Update `right = mid - 1`.
            
    3. If the loop finishes without finding the target, the `left` pointer will naturally sit at the exact index where the target _should_ be inserted. Return `left`.
        
- **Efficiency:** Halving the array every step guarantees an $O(\log N)$ time complexity. Since you only store a few integer pointers, space complexity is $O(1)$.
    

---

## ⚙️ DevOps Essentials — **Docker Basics: Writing a `Dockerfile`**

Tags: #DevOps #Docker #Architecture #Containers

Goal: Moving from running pre-made images (like Postgres or Nginx) to packaging your own applications into custom, deployable Docker images.

### 🎯 **Quick Review Summary: Core Dockerfile Instructions**

A `Dockerfile` is simply a text-based recipe that tells the Docker engine exactly how to build your application layer by layer.

|**Instruction**|**Real Example**|**Best Use Case & Description**|
|---|---|---|
|**`FROM`**|`FROM python:3.10-slim`|**The Foundation.** Every Dockerfile must start with this. It defines the base OS and pre-installed tools.|
|**`WORKDIR`**|`WORKDIR /app`|**The Directory.** Sets the starting directory inside the container for all subsequent commands.|
|**`COPY`**|`COPY requirements.txt .`|**File Transfer.** Copies files from your local laptop into the container's filesystem.|
|**`RUN`**|`RUN pip install -r requirements.txt`|**Execution (Build Time).** Runs terminal commands to install dependencies _during_ the image build process.|
|**`CMD`**|`CMD ["python", "main.py"]`|**The Entrypoint (Run Time).** The final default command that executes when the container actually spins up.|

### 💻 **Real-World Terminal Execution**

Once your `Dockerfile` is written, you use the `build` command to create the image, and then `run` it just like any public image.

Bash

```
# Build the image and tag (-t) it with a custom name
$ docker build -t my-python-app:v1 .

# Run the newly created image in detached mode (-d)
$ docker run -d -p 8000:8000 my-python-app:v1
```

---

## 🐧 Linux Learning — Command: **`awk`** (Text & Data Extraction)

Tags: #Linux #Command #awk #DataProcessing

Goal: While `grep` finds rows, and `cut` finds columns, `awk` is a fully-fledged programming language designed to slice, filter, and format structured text (like server logs or CSVs) on the fly.

### 🎯 **Quick Review Summary: Column Processing**

|**Scenario**|**Command**|**Description**|
|---|---|---|
|**Print Specific Column**|**`awk '{print $2}' file.txt`**|**Basic Extraction.** By default, `awk` splits lines by whitespace. `$1` is the first column, `$2` is the second. `$0` is the entire line.|
|**Custom Delimiter**|`awk -F',' '{print $1}' data.csv`|**CSV Parsing.** The `-F` flag changes the field separator. Here, it splits by commas instead of spaces.|
|**Filter and Print**|`awk '$3 > 500 {print $1}' log.txt`|**Conditional Logic.** Only prints the first column _if_ the numerical value in the third column is greater than 500.|

### 💻 **Real-World Terminal Examples**

#### 1. Extracting Process IDs from a system scan

Combine `ps` with `awk` to grab just the PIDs of a specific application so you can pass them to a kill script.

Bash

```
$ ps aux | grep nginx
root      4521  0.0  0.1  14234  1024 ?   Ss  10:00  0:00 nginx: master
$ ps aux | grep nginx | awk '{print $2}'
4521
```

#### 2. Parsing Disk Usage dynamically

Use `df` to check disk space, and use `awk` to print a clean, readable sentence alerting you to the capacity.

Bash

```
$ df -h | grep "/dev/sda1"
/dev/sda1       50G   40G   10G  80% /
$ df -h | grep "/dev/sda1" | awk '{print "Disk "$1" is at "$5" capacity."}'
Disk /dev/sda1 is at 80% capacity.
```