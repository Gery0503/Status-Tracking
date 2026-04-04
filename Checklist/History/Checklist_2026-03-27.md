# 📅  Checklist

| **Category**         | **Task**                                       | **Status** |
| -------------------- | ---------------------------------------------- | ---------- |
| 🧠 LeetCode Practice | **344. Reverse String** (Two Pointers)         | ✅          |
| ⚙️ DevOps Essentials | **CI/CD Basics: GitHub Actions Workflows**     | ✅          |
| 🐧 Linux Learning    | Command: **`curl`** (Client URL & API Testing) | ✅          |

---

## 🧠 LeetCode — **344. Reverse String** Tags: #TwoPointers #String #Array

Difficulty: Easy (Extremely low cognitive load)   

### 🎯 **Concept to learn today: The In-Place Swap**

You must write a function that reverses a string. The input string is given as an array of characters `s`. You must do this by modifying the input array **in-place** with $O(1)$ extra memory.

- **The Strategy:** Set up two pointers at opposite ends of the array and swap their values, moving them inward until they meet in the middle.
    
- **The Flow:**
    
    1. Initialize a `left` pointer at index `0`.
        
    2. Initialize a `right` pointer at index `len(s) - 1`.
        
    3. Enter a loop that continues while `left < right`.
        
    4. Swap the characters: `s[left], s[right] = s[right], s[left]`.
        
    5. Move `left` forward (`left += 1`) and `right` backward (`right -= 1`).
        
- **Why efficient?** You only traverse half the array to swap all elements, meaning time complexity is $O(N)$. Because you only use two integer pointers for the indices, space complexity is strictly $O(1)$.
    

---

## ⚙️ DevOps Essentials — **CI/CD Basics: GitHub Actions**

Tags: #DevOps #Automation #CICD #GitHub

Goal: Understanding how to automate scripts, tests, and deployments so they run automatically in the cloud every time you push code.

### 1. The Core Philosophy of CI/CD

Continuous Integration / Continuous Deployment (CI/CD) means you never manually test or deploy your code. Instead, you write a configuration file that tells a remote server how to do it for you.

### 2. The Components of GitHub Actions

GitHub Actions uses YAML files (stored in `.github/workflows/`) to define automation.

- **Events:** The trigger. (e.g., "Whenever code is pushed to the `main` branch").
    
- **Runners:** The remote virtual machine (often Ubuntu Linux) that GitHub spins up to execute your tasks.
    
- **Jobs:** A set of sequential steps executed on the runner. (e.g., "Install Python", then "Run tests", then "Deploy to server").
    

---

## 🐧 Linux Learning — Command: **`curl`** (Client URL)

Tags: #Linux #Command #curl #Networking #APIs

Why chosen:

- It requires absolutely zero environment setup. You can run it instantly from your terminal to interact with the internet, test APIs, or download files. It is the absolute standard for debugging web services in DevOps.
    

### 🎯 **Core Uses & API Testing**

|**Scenario**|**Command**|**Sophistication**|
|---|---|---|
|**Fetch a Webpage**|**`curl https://example.com`**|**Daily Driver.** Downloads the raw HTML response of the URL and prints it directly to your terminal screen.|
|**View Headers Only**|`curl -I https://api.github.com`|**Network Debugging.** The `-I` (capital i) flag fetches only the HTTP headers. Perfect for quickly checking if a server returns a `200 OK` or a `404 Not Found` without downloading massive payloads.|
|**Download a File**|`curl -O https://example.com/file.zip`|**File Retrieval.** The `-O` (capital o) flag saves the output to a local file with the same name as the remote file, rather than dumping the binary text into your terminal.|

---

Would you like me to draft a minimal, 10-line GitHub Actions YAML file that automatically runs a Python script every time you push to a repository, so you can see exactly how the syntax looks?