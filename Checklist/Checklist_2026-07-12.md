# 📅 **Checklist_2026-07-12**

| **Category**               | **Task**                                    | **Status** |
| -------------------------- | ------------------------------------------- | ---------- |
| 🧠 LeetCode Practice       | **412. Fizz Buzz** (Math / Simulation)      | ✅          |
| ⚙️ DevOps Essentials       | **Ansible Basics: Handlers**                | ✅          |
| 🐧 Linux Learning          | Command: **`which`** (Locating Executables) | ✅          |
| 🏭 **Dannie EMS Handbook** | **Rack PDUs & A/B Power Redundancy**        | ✅          |

## 🧠 LeetCode — **412. Fizz Buzz** Tags: #Math #String #Simulation

Difficulty: Easy

### 🎯 **Concept to learn today: Order of Operations**

Given an integer `n`, return a string array `answer` (1-indexed) where:

- `answer[i] == "FizzBuzz"` if `i` is divisible by 3 and 5.
    
- `answer[i] == "Fizz"` if `i` is divisible by 3.
    
- `answer[i] == "Buzz"` if `i` is divisible by 5.
    
- `answer[i] == i` (as a string) if none of the above conditions are true.
    

- **The Strategy:** The most common mistake in this classic problem is checking for "3" first, then "5", and then "both". If a number is 15, the "divisible by 3" check catches it first, outputs "Fizz", and entirely misses the "FizzBuzz" requirement. You must always evaluate the most restrictive condition first.
    
- **The Flow:**
    
    1. Initialize an empty list `result = []`.
        
    2. Loop `i` from `1` to `n` (inclusive).
        
    3. _Condition 1 (Most Restrictive):_ `if i % 3 == 0 and i % 5 == 0:` append `"FizzBuzz"`.
        
    4. _Condition 2:_ `elif i % 3 == 0:` append `"Fizz"`.
        
    5. _Condition 3:_ `elif i % 5 == 0:` append `"Buzz"`.
        
    6. _Condition 4 (Fallback):_ `else:` append the string version of the number.
        
    7. Return `result`.
        
- **Efficiency:** You loop through the range exactly once, meaning the time complexity is $O(N)$. Aside from the output array, you use no extra memory, so the auxiliary space complexity is strictly $O(1)$.
    
- _Python Tip:_ If you are printing debug logs to the console during this exercise on Python 3.14+, remember to use the new t-strings (e.g., `print(t"Current value: {i}")`) for secure template evaluation instead of older string formatting methods!
    

## ⚙️ DevOps Essentials — **Ansible Basics: Handlers**

Tags: #DevOps #Ansible #ConfigurationManagement #Idempotency

Goal: Last session, you used a Jinja2 template to push a dynamic `nginx.conf` file to a server. However, Nginx doesn't automatically know its configuration changed. It needs to be restarted. But if you tell Ansible to run `systemctl restart nginx` every single time the playbook runs, you violate the core rule of automation: _Idempotency_ (only make changes if a change is actually needed).

### 🎯 **Quick Review Summary: Conditional Execution**

A **Handler** is a special type of task in Ansible that only runs if another task specifically "notifies" it that a change occurred.

|**Component**|**Description**|
|---|---|
|**`notify:`**|A keyword added to your main task. It acts like a tripwire. If the task changes a file, the tripwire is triggered.|
|**`handlers:`**|A separate block at the bottom of your playbook. These tasks sit completely dormant unless a tripwire wakes them up.|
|**End-of-Run Execution**|Handlers always wait until all other tasks in the playbook are finished before running. This ensures a service is only restarted _once_, even if 10 different files were modified.|

### 💻 **Real-World Code Execution**

YAML

```
tasks:
  - name: Deploy new Nginx configuration
    template:
      src: nginx.conf.j2
      dest: /etc/nginx/nginx.conf
    # If the file on the server is already identical, this task returns "OK" and does nothing.
    # If the file is updated, it returns "CHANGED" and triggers the notification.
    notify: Restart Nginx

# Handlers sit at the very bottom and only run if notified
handlers:
  - name: Restart Nginx
    service:
      name: nginx
      state: restarted
```

## 🐧 Linux Learning — Command: **`which`** (Locating Executables)

Tags: #Linux #Command #which #SysAdmin #Troubleshooting

Goal: Sometimes you run an Ansible playbook or a Python script, and it fails with a strange version error. This often happens because there are multiple versions of Python installed on the server, and Linux is executing the wrong one. `which` tells you exactly what the operating system is looking at.

### 🎯 **Quick Review Summary: Path Resolution**

When you type a command like `docker` or `python3`, Linux scans a hidden list of directories (known as the `$PATH` variable) from left to right. It runs the very first matching executable it finds.

|**Scenario**|**Command**|**Description**|
|---|---|---|
|**Find the Binary**|**`which python3`**|**The Daily Driver.** Returns the exact absolute path of the executable that will run if you type `python3`.|
|**Find All Binaries**|`which -a python3`|**Debugging.** Prints _every_ location where `python3` exists in your path. Crucial for discovering if a localized installation is overriding the global system installation.|
|**Deeper Inspection**|`whereis docker`|**The Audit.** Returns not just the executable binary, but also the location of the source code and the manual (`man`) pages.|

### 💻 **Real-World Terminal Example**

1. A deployment script crashes, claiming `ansible` is missing, but you know you installed it. You check where the shell thinks it is.
    

Bash

```
$ which ansible
/home/felton/.local/bin/ansible
```

_(You immediately see that Ansible was installed locally for your specific user account, rather than globally in `/usr/bin/ansible`. This means the automated deployment tool running as `root` legitimately cannot see it!)_

## 🏭 Dannie EMS Handbook — **Rack PDUs & A/B Power Redundancy**

Tags: #EMS #Manufacturing #Hardware #Infrastructure #Power

Goal: Understanding the physical electrical architecture of an enterprise server rack to prevent catastrophic outages during L11 integration and factory testing.

### 🎯 **Core Concept: Fault-Tolerant Power**

When deploying high-end infrastructure for enterprise clients, the physical power supply is just as critical as the software. Enterprise servers have dual (or sometimes quad) Power Supply Units (PSUs) plugged into the back of the chassis.

If both PSUs were plugged into the same wall outlet, a single blown circuit breaker would instantly crash the entire rack. To solve this, racks use **A/B Power Redundancy**.

- **The PDUs:** A rack contains two separate, vertical Power Distribution Units (essentially massive smart power strips running up the sides of the rack).
    
- **Strip A & Strip B:** PDU A is wired to one factory power grid (or Uninterruptible Power Supply / battery backup). PDU B is wired to a completely different physical grid.
    
- **The Interleaving:** Server PSU 1 is plugged into PDU A. Server PSU 2 is plugged into PDU B. If the primary factory breaker blows and PDU A loses all power, the server seamlessly draws 100% of its required load from PDU B without dropping a single packet.
    

### 🏢 **Factory Floor Application**

When you write deployment or diagnostic software for bare-metal racks, you must be hyper-aware of power states. If your automated Burn-In script commands all 40 servers in a rack to run their CPUs at 100% maximum capacity simultaneously, you must verify that a single PDU can safely handle the full electrical amperage load on its own. If you exceed the threshold and one PDU trips, the failover to the second PDU will immediately overload it as well, causing the entire cluster to go dark mid-deployment.