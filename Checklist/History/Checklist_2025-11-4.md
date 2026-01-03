
---

# 📌 2025-11-04 – Daily Learning Plan

| Task Category        | Task (short title + link)                                                   | Status |
| -------------------- | --------------------------------------------------------------------------- | ------ |
| 🧠 LeetCode Practice | Solve: [Add Two Strings](https://leetcode.com/problems/add-strings/)        | ✅      |
| 🧪 Work Enhancement  | Topic: MCP (Model Context Protocol) – guiding AI agents with external tools | ☐      |
| 🐧 Linux Learning    | Command: `rsync` — efficient file sync and backups                          | ✅      |

---

## 🧠 LeetCode Practice — [Add Two Strings]

**Tag:** #LeetCode #String #Implementation

- **Skill path:** String manipulation + manual arithmetic simulation.
    
- **Why chosen:** Builds on string basics and introduces how to handle “digit-by-digit” logic without converting to integers — good prep for problems where built-in types overflow or are restricted.
    

---

## 🧪 Work Enhancement — Deep Dive: MCP (Model Context Protocol)

**Tag:** #MCP #AIWorkflow #Automation  
**Why it matters:** As you work with advanced automation tools, MCP allows AI to dynamically decide **which tool** to invoke and when, rather than you manually scripting every step. This makes workflow smarter, more flexible, and closer to an “assistant” rather than just “automation script”.  
**Quick lesson (what + how):**

1. Define tool interface(s) the AI can use (e.g., “read_file”, “run_script”, “fetch_api”).
    
2. Provide context to your model about your environment, permissions, and typical workflows.
    
3. Ask the model to choose a tool based on a goal (e.g., “I want to find all files larger than 100 MB and log them”).  
    **Practice tasks:**
    

- Task A: Write a simple JSON interface spec for one tool (e.g., “list_dir”).
    
- Task B: Prompt the model: “Using tools list_dir and filter_size, find files larger than 100 MB in ~/projects”.
    
- Task C: Log one action taken by the model into Notion or Google Sheets for audit.
    

---

## 🐧 Linux Learning — Deep Dive: `rsync`

**Tag:** #Linux/Command/rsync #Backup 
**What it is:** `rsync` synchronizes files/directories between locations, efficiently transferring only changed parts and preserving permissions, links, etc.  

**Scenario:** You want to back up your project folder to an external drive or remote server nightly, ensuring only changed files get copied to save time and bandwidth. 

**Quick commands / cheatsheet:**

- Basic sync: `rsync -av ~/projects/ /mnt/backup/projects/` (archive + verbose)
- Use deletion to mirror: `rsync -av --delete ~/projects/ /mnt/backup/projects/`
- Remote sync: `rsync -av ~/projects/ user@server:/backup/projects/`  
    **Why useful:** Faster than tar+scp for large incremental backups, preserves file metadata, good for mirroring or migration tasks.  
    
**Practice tasks:**
- Task A: `rsync -av ~/some_small_folder/ ~/some_backup_folder/` and verify contents.
- Task B: Modify one file, run `rsync` again, verify only delta copied.
- Task C: Add `--delete` option for mirror behavior, and check that deleted files in source are also removed in backup.

---

👍 Let me know how it goes today — and if you’d like me to **preview the next 3 days’ plans** so you can see upcoming skill path steps.