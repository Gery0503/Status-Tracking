
---

# 📌 2025-10-27 – Daily Learning Plan

| Task Category        | Task (short title + link)                                                       | Status |
| -------------------- | ------------------------------------------------------------------------------- | ------ |
| 🧠 LeetCode Practice | [Find Common Characters](https://leetcode.com/problems/find-common-characters/) | ✅      |
| 🧪 Work Enhancement  | Topic: Git Productivity — Commit Message Templates                              | ✅      |
| 🐧 Linux Learning    | Command: `du` — summarize disk usage                                            | ✅      |

---

## 🧠 LeetCode Practice — [Find Common Characters]

**Tag:** #LeetCode #Easy #String #HashMap

**Why chosen:**

- Strengthens **frequency counting** and **intersection logic** between multiple strings.
    
- Reinforces use of Python’s `collections.Counter` or manual counting logic.
    

**Deep Dive Task:**

- Write a helper function that computes the intersection of character counts between two strings.
    
- Then extend it to handle a list of strings iteratively.
    
- Reflect: how could you generalize this to “find common elements in lists of lists”?
    

---

## 🧪 Work Enhancement — Deep Dive: Git Productivity (Commit Message Templates)

**Tag:** #Git #Workflow #Productivity

**Why it matters:**  
Consistent, structured commit messages make your repo readable and searchable.

**Quick Lesson:**

- Create `.gitmessage.txt` with your preferred structure:
    
    ```
    [Type]: Short summary
    
    Details (optional)
    Issue: #
    ```
    
- Then run:
    
    ```bash
    git config --global commit.template ~/.gitmessage.txt
    ```
    
- Try it with types like `feat`, `fix`, `docs`, `refactor`, etc.
    

---

## 🐧 Linux Learning — Deep Dive: `du`

**Tag:** #Linux/Command/du #SystemMonitoring

**Why it matters:**  
`du` helps you find which folders eat disk space — critical for Docker, logs, and large datasets.

**Quick Lesson:**

- Common usage:
    
    ```bash
    du -h --max-depth=1
    ```
    
- Combine with sort to find top offenders:
    
    ```bash
    du -sh * | sort -hr | head
    ```
    
- Try running inside your project folder and note the heaviest directories.
    

---
