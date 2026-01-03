
---

# 📌 2025-10-02 – Daily Learning Plan

| Task Category        | Task (short title + link)                                              | Status |
| -------------------- | ---------------------------------------------------------------------- | ------ |
| 🧠 LeetCode Practice | Solve: [Detect Capital](https://leetcode.com/problems/detect-capital/) | ✅      |
| 🧪 Work Enhancement  | Topic: n8n – Error Handling & Retries                                  | ☐      |
| 🐧 Linux Learning    | Command: `tee` — write output to file **and** stdout simultaneously    | ✅      |

---

## 🧠 LeetCode Practice — [Detect Capital]

**Tag:** #LeetCode #String #Implementation

- **Skill path:** String manipulation (capitalization rules).
    
- **Why chosen:** Reinforces string traversal + condition checks. Prepares for trickier parsing/string matching problems.
    

---

## 🧪 Work Enhancement — Deep Dive: n8n Error Handling & Retries

**Tag:** #n8n #Automation #Resilience

**Why it matters:** Automations often fail (API timeout, invalid input). n8n lets you handle errors gracefully with retry logic.

**Quick lesson:**

- Each node has **Error Workflow** triggers you can define.
    
- Built-in **retry on failure**: configure max attempts + delay.
    
- Use **“Error Trigger” workflow** to log failures (e.g., send Slack/Email when a job fails).
    

**Practice tasks:**

- Task A: Create a simple workflow (HTTP GET → Slack). Simulate failure (wrong URL).
    
- Task B: Enable retry (3x, 2s delay) and observe.
    
- Task C: Add an Error Trigger workflow that logs the error to Google Sheets.
    

---

## 🐧 Linux Learning — Deep Dive: `tee`

**Tag:** #Linux/Command/tee #Productivity

**What it is:** `tee` duplicates command output: writes it to a file _and_ displays it on screen.

**Scenario:** You run a long script and want to both **see output live** and **save it to a log**:

```bash
./myscript.sh | tee logfile.txt
```

**Quick commands / cheatsheet:**

- Append instead of overwrite: `command | tee -a logfile.txt`
    
- Combine with `sudo`: `echo "config" | sudo tee /etc/myconfig.conf`
    
- Debug pipelines: `ls | tee files.txt | grep ".py"`
    

**Why useful:** Saves you from choosing between **visibility** and **logging**.

**Practice tasks:**

- Task A: Run `ls -l | tee files.txt` → check both console and file.
    
- Task B: Try appending with `-a`.
    
- Task C: Use `echo "alias ll='ls -l'" | tee -a ~/.bashrc` to add alias.
    

---
