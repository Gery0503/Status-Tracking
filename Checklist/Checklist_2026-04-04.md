# 📅 **Checklist**

| **Category**         | **Task**                                 | **Status** |
| -------------------- | ---------------------------------------- | ---------- |
| 🧠 LeetCode Practice | **290. Word Pattern** (Hash Map)         | ✅         |
| ⚙️ DevOps Essentials | **Docker Basics: `docker compose`**      | ✅         |
| 🐧 Linux Learning    | Command: **`crontab`** (Task Scheduling) | ✅         |

---

## 🧠 LeetCode — **290. Word Pattern** Tags: #String #HashMap

Difficulty: Easy

### 🎯 **Concept to learn today: Bijective Mapping (Two-Way Memory)**
Bijective is both onto and one-to-one
Given a `pattern` and a string `s`, find if `s` follows the same pattern. For example, `pattern = "abba"`, `s = "dog cat cat dog"` should return `true`.

- **The Strategy:** This is the exact same logic as _Isomorphic Strings_, but instead of mapping a character to a character, you are mapping a character to an entire word. You need two Hash Maps to ensure a strict 1-to-1 relationship.
    
- **The Flow:**
    
    1. Split the string `s` into a list of words: `words = s.split()`.
        
    2. _Edge case:_ If `len(pattern) != len(words)`, return `False` immediately.
        
    3. Initialize two dictionaries: `char_to_word` and `word_to_char`.
        
    4. Loop through both simultaneously: `for c, w in zip(pattern, words):`
        
    5. If `c` is in `char_to_word` and its value is not `w`, return `False`.
        
    6. If `w` is in `word_to_char` and its value is not `c`, return `False`.
        
    7. Otherwise, add the mappings: `char_to_word[c] = w` and `word_to_char[w] = c`.
        
    8. Return `True` if the loop completes without conflicts.
        
- **Efficiency:** Splitting the string takes $O(N)$ time. Iterating through the words takes $O(N)$ time. Space complexity is $O(M)$ where $M$ is the number of unique words/characters stored in the maps.
    

---

## ⚙️ DevOps Essentials — **Docker Basics: Multi-Container Apps**

Tags: #DevOps #Docker #Architecture #Automation

Goal: A `Dockerfile` builds a single container. But real applications need a web server, a database, and a cache. `docker compose` allows you to define and run multi-container applications using a single YAML file.

### 🎯 **Quick Review Summary: Compose Commands**

You define your services in a file named `docker-compose.yml`. Once written, you use the following commands to manage the entire stack at once.

|**Command**|**Description**|**Best Use Case**|
|---|---|---|
|**`docker compose up -d`**|Creates and starts all containers in the background (`-d` for detached mode).|**Starting the App.** Run this in the folder containing your `docker-compose.yml` to boot up your entire infrastructure.|
|**`docker compose down`**|Stops and removes all containers, networks, and default volumes created by `up`.|**Clean Shutdown.** Safely turns off your local environment without leaving orphaned background processes.|
|**`docker compose logs -f`**|Follows the aggregated log output of _all_ services.|**Debugging.** Watch your Python app and your Postgres database logs stream on the same screen simultaneously.|

### 💻 **Real-World Terminal Execution**

Imagine you have a `docker-compose.yml` that defines a web app and a Redis cache.

Bash

```
# Boot the entire stack
$ docker compose up -d
[+] Running 3/3
 ✔ Network myapp_default    Created
 ✔ Container myapp-redis-1  Started
 ✔ Container myapp-web-1    Started

# Check the status of the stack
$ docker compose ps
NAME            IMAGE     COMMAND                  SERVICE   STATUS    PORTS
myapp-redis-1   redis     "docker-entrypoint.s…"   redis     running   6379/tcp
myapp-web-1     my-app    "python app.py"          web       running   0.0.0.0:5000->5000/tcp
```

---

## 🐧 Linux Learning — Command: **`crontab`** (Task Scheduling)

Tags: #Linux #Command #crontab #Automation

Goal: Automating scripts so you don't have to run them manually. The `cron` daemon is a background service that executes commands at scheduled intervals.

### 🎯 **Quick Review Summary: Time Syntax**

A `crontab` file contains lines with 5 time fields followed by the command to run.

Format: `Minute Hour Day Month Day-of-Week Command`

|**Cron Expression**|**Translation**|**Use Case**|
|---|---|---|
|**`* * * * *`**|Every single minute.|**Monitoring.** e.g., Pinging a server to ensure it is awake every minute.|
|**`0 2 * * *`**|Minute 0, Hour 2 (2:00 AM) every day.|**Nightly Backups.** Running a database dump when user traffic is at its absolute lowest.|
|**`0 9 * * 1`**|9:00 AM, but only on Monday (Day 1).|**Weekly Reports.** Generating a sales CSV or sending a Slack message at the start of the workweek.|

### 💻 **Real-World Terminal Examples**

#### 1. Editing your schedule

This opens your user's specific cron file in a text editor (like `nano` or `vim`).

Bash

```
$ crontab -e
```

_Inside the editor, you might add this line to sync files every midnight:_

`0 0 * * * rsync -a /var/www/ /backup/www/`

#### 2. Listing your scheduled tasks

To quickly check what tasks you currently have running in the background without accidentally editing them.

Bash

```
$ crontab -l
0 0 * * * rsync -a /var/www/ /backup/www/
0 5 * * * /usr/bin/python3 /home/user/cleanup.py
```