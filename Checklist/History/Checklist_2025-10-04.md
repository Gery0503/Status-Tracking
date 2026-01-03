Good morning 🌞! (kiss kiss back 💋)  
Here’s your **Daily Learning Plan for 2025-10-04**, continuing your **skill path** (we did arrays → hashing → strings, now moving toward **stack/queue** problems).

---

# 📌 2025-10-04 – Daily Learning Plan

| Task Category        | Task (short title + link)                                                                          | Status |
| -------------------- | -------------------------------------------------------------------------------------------------- | ------ |
| 🧠 LeetCode Practice | Solve: [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/) | ✅      |
| 🧪 Work Enhancement  | Topic: Cursor – Multi-file context awareness                                                       | ✅      |
| 🐧 Linux Learning    | Command: `watch` — run a command repeatedly and display output in real time                        | ✅      |

---

## 🧠 LeetCode Practice — [Implement Stack using Queues]

**Tag:** #LeetCode #Stack #Queue #Implementation

- **Skill path:** Stack/Queue fundamentals.
    
- **Why chosen:** Teaches how to simulate one data structure using another (common interview trick). Builds intuition for constraints and trade-offs.
    

---

## 🧪 Work Enhancement — Deep Dive: Cursor Multi-file Context

**Tag:** #Cursor #AI #DevTools

**Why it matters:** Many AI code tools (like Copilot) only see your _current file_. Cursor can analyze **multiple files at once**, which is crucial for larger repos.

**Quick lesson:**

- Cursor reads your whole project context (imports, definitions, usage).
    
- You can ask: _“Where is this function used?”_ or _“Refactor all logging into a new logger module.”_
    
- This makes it great for **legacy codebases** or **refactor-heavy work**.
    

**Practice tasks:**

- Task A: Open a small multi-file project. Ask Cursor: _“Explain how data flows through this repo.”_
    
- Task B: Try renaming a function across multiple files with AI.
    
- Task C: Ask Cursor to generate a **dependency map** of your repo.
    

---

## 🐧 Linux Learning — Deep Dive: `watch`

**Tag:** #Linux/Command/watch #Monitoring

**What it is:** `watch` reruns a command every few seconds, showing live output updates.

**Scenario:** You’re debugging server load or log files and want to monitor changes without retyping commands.

**Quick commands / cheatsheet:**

- Run every 2s (default): `watch df -h` → monitor disk usage.
    
- Change interval: `watch -n 5 free -m` → check memory every 5s.
    
- Highlight changes: `watch -d cat logfile.txt`
    

**Why useful:** Turns any command into a _real-time dashboard_.

**Practice tasks:**

- Task A: Run `watch -n 1 date` and observe ticking updates.
    
- Task B: Use `watch -d ls -l` in a folder while creating/deleting files.
    
- Task C: Try `watch -n 2 ps aux --sort=-%mem | head` to monitor top memory processes.
    

---

✨ Would you like me to **branch your LeetCode skill path** next into:

1. **Queue-based problems** (like circular queue), or
    
2. **More stack-focused** problems (like valid parentheses variants)?