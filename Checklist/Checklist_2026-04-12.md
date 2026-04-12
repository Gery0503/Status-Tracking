# 📅 Checklist

| **Category**         | **Task**                                    | **Status** |
| -------------------- | ------------------------------------------- | ---------- |
| 🧠 LeetCode Practice | **228. Summary Ranges** (Array & Intervals) | ✅          |
| ⚙️ DevOps Essentials | **Kubernetes Basics: ConfigMaps & Secrets** | ✅          |
| 🐧 Linux Learning    | Command: **`scp`** (Secure Copy Protocol)   | ✅          |

---

## 🧠 LeetCode — **228. Summary Ranges** Tags: #Array #TwoPointers

Difficulty: Easy

### 🎯 **Concept to learn today: Streak Detection and Formatting**

You are given a sorted unique integer array `nums`. A range `[a,b]` is the set of all integers from `a` to `b` (inclusive). Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That means if you have consecutive numbers like `0, 1, 2`, they get bundled into `"0->2"`.

- **The Strategy:** Iterate through the array using a pointer. You need to anchor a `start` value and then peek ahead to see if the next number is exactly `current + 1`. When the streak breaks, you format the string and reset the `start` anchor.
    
- **The Flow:**
    
    1. Initialize an empty list `ranges = []` and index `i = 0`.
        
    2. Loop while `i < len(nums)`:
        
        - Set `start = nums[i]`.
            
        - Enter an inner loop: while `i + 1 < len(nums)` AND `nums[i + 1] == nums[i] + 1`, increment `i += 1`. _(This safely advances the pointer to the end of the consecutive streak)._
            
        - After the inner loop breaks, check if `start == nums[i]`.
            
            - If yes, append `"{start}"` (it was a standalone number).
                
            - If no, append `"{start}->{nums[i]}"` (it was a range).
                
        - Increment `i += 1` to move to the next fresh number.
            
    3. Return `ranges`.
        
- **Efficiency:** Despite having an inner `while` loop, every element is visited exactly once, making the time complexity strictly $O(N)$. Space complexity is $O(1)$ excluding the output array.
    

---

## ⚙️ DevOps Essentials — **Kubernetes Basics: ConfigMaps & Secrets**

Tags: #DevOps #Kubernetes #Architecture #Security

Goal: A core principle of modern application development (like the 12-Factor App) is **separating configuration from code**. You should never hardcode database URLs or API keys inside your Docker image. Kubernetes solves this using ConfigMaps (for plain text) and Secrets (for sensitive data).

### 🎯 **Quick Review Summary: Configuration Objects**

These objects store data as key-value pairs, which your Pods can then inject as Environment Variables or mount as physical files.

|**Object Type**|**Description**|**Best Use Case**|
|---|---|---|
|**ConfigMap**|Plain text key-value storage.|**Environment Variables.** Setting the `NODE_ENV=production` or `DATABASE_PORT=5432` for your backend service.|
|**Secret**|Base64 encoded key-value storage.|**Sensitive Data.** Storing passwords, SSH keys, or OAuth Tokens securely so they aren't exposed in your Git repository.|

### 💻 **Real-World Terminal Execution**

#### 1. Creating a ConfigMap dynamically

Instead of writing a complex YAML file, you can create a ConfigMap directly from the terminal for quick configuration.

Bash

```
$ kubectl create configmap backend-config --from-literal=LOG_LEVEL=debug --from-literal=API_ENDPOINT=/v1/data
configmap/backend-config created

# Inspect what you just made
$ kubectl describe configmap backend-config
Name:         backend-config
Namespace:    default
Data
====
API_ENDPOINT:
----
/v1/data
LOG_LEVEL:
----
debug
```

#### 2. Creating a Secret from a file

If you have a sensitive SSL certificate or an AWS credentials file, you can upload it straight into Kubernetes memory.

Bash

```
$ kubectl create secret generic aws-creds --from-file=credentials.json
secret/aws-creds created
```

_(Once created, you update your Deployment YAML to mount `aws-creds` directly into your Pod, ensuring your application has secure access to it)._

---

## 🐧 Linux Learning — Command: **`scp`** (Secure Copy Protocol)

Tags: #Linux #Command #scp #Networking #Filesystem

Goal: When working with remote servers, you frequently need to move files between your local laptop and the cloud infrastructure. `scp` allows you to copy files securely using the same encrypted tunnel as SSH.

### 🎯 **Quick Review Summary: Remote File Transfer**

The syntax works exactly like the standard `cp` (copy) command: `scp [source] [destination]`. The only difference is that you add `user@ip_address:` for remote locations.

|**Scenario**|**Command**|**Description**|
|---|---|---|
|**Upload to Server**|**`scp data.csv user@10.0.5.12:/var/www/`**|**Local to Remote.** Copies the local `data.csv` file directly into the `/var/www/` directory on the remote server.|
|**Download to Laptop**|`scp user@10.0.5.12:/var/log/nginx/error.log .`|**Remote to Local.** Downloads the `error.log` file from the server and saves it in your current local directory (denoted by the `.`).|
|**Upload a Folder**|`scp -r ./app user@10.0.5.12:/opt/`|**Recursive Copy.** The `-r` flag allows you to upload an entire directory and all its contents at once.|

### 💻 **Real-World Terminal Examples**

#### 1. Passing an SSH Key

If your server rejects password logins (which it always should for security), you must pass your private SSH key using the `-i` (identity file) flag, just like you would with normal SSH.

Bash

```
# Uploading an updated Nginx configuration file securely
$ scp -i ~/.ssh/my-aws-key.pem nginx.conf ubuntu@203.0.113.50:/etc/nginx/
nginx.conf                                    100% 1245    1.2KB/s   00:00
```