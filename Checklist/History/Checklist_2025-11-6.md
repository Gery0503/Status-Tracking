

---

# 📌 2025-11-06 – Daily Learning Plan

| Task Category        | Task (short title + link)                                                            | Status |
| -------------------- | ------------------------------------------------------------------------------------ | ------ |
| 🧠 LeetCode Practice | Solve: [Relative Sort Array II](https://leetcode.com/problems/sort-array-by-parity/) | ✅      |
| 🧪 Work Enhancement  | Topic: **Obsidian Templates** – Automate repetitive notes with Templater plugin      | ✅      |
| 🐧 Linux Learning    | Command: `ncdu` — visualize and manage disk usage interactively                      | ✅      |

---

## 🧠 LeetCode Practice — [Sort Array by Parity]

**Tag:** #LeetCode #Array #TwoPointers  
**Skill path:** Strengthen mastery of array manipulation and partition logic.  
**Why chosen:** Builds your fluency with in-place operations and efficient data movement — key for later sorting and partitioning challenges.

---

## 🧪 Work Enhancement — Deep Dive: **Obsidian Templates (Templater Plugin)**

**Tag:** #Obsidian #WorkflowAutomation #Productivity  
**What it is:** The **Templater** plugin lets you create dynamic note templates that can auto-fill metadata, dates, or custom scripts.  
**Quick lesson:**

1. Install **Templater** via _Community Plugins → Browse → “Templater”_.
    
2. Create a `Templates/` folder (set it in Templater settings).
    
3. Use variables like `<% tp.date.now("YYYY-MM-DD") %>` for auto dates.
    
4. Trigger templates via **Ctrl+P → “Templater: Insert Template.”**  
    **Practice idea:**
    

- Build a “Daily Log” template that auto-generates your action table.
    
- Add custom Templater commands for tags or mood tracking.  
    **Why useful:** Saves time, ensures consistent note structure, and enables automation without leaving Obsidian.
    

---

## 🐧 Linux Learning — Deep Dive: `ncdu`

**Tag:** #Linux/Command/ncdu  #DiskUsage #Productivity  
**What it is:** A **visual, interactive alternative to `du`**, great for finding large files and cleaning up space.  
**Scenario:** Your server is full, and you need to quickly locate space hogs.  
**Quick commands:**

- Install: `sudo apt install ncdu`
    
- Run: `ncdu /` → navigate with arrow keys, delete with `d`.  
    **Why useful:** Faster and more readable than `du`; perfect for diagnosing disk bloat in projects or containers.  
    **Practice tasks:**
    
- Task A: Run `ncdu ~` to analyze your home directory.
    
- Task B: Identify the top 3 largest folders and clean unnecessary logs or cache.
    
- Task C: Try `ncdu /var` on a server environment to audit system usage.
    

---

Would you like tomorrow’s Work Enhancement to **shift toward MCP or LangChain** next (to balance AI-automation with your current note/workflow tools)?