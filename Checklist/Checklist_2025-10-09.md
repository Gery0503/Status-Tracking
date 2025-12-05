We’re now moving along your **LeetCode skill path** from stack/queue → **recursion & tree basics**, while keeping your **Work Enhancement** and **Linux Learning** short, actionable, and Obsidian-ready.

---

# 📌 2025-10-09 – Daily Learning Plan

| Task Category        | Task (short title + link)                                                     | Status |
| -------------------- | ----------------------------------------------------------------------------- | ------ |
| 🧠 LeetCode Practice | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | ✅      |
| 🧪 Work Enhancement  | Topic: Obsidian – Templates for Daily Notes                                   | ✅      |
| 🐧 Linux Learning    | Command: `lsof` — list open files and their owning processes                  | ✅      |

---

## 🧠 LeetCode Practice — [Subarray Sum Equals K]

**Tag:** #LeetCode #HashMap #PrefixSum #SlidingWindow

**Why chosen:**

- Introduces **prefix sum + hash map** combination — a common technique for subarray problems.
    
- Builds logic skills for “count patterns” and later **dynamic programming** problems.
    

**Key Concepts:**

- Use a running prefix sum to represent cumulative totals.
    
- For each index `i`, check if `prefix_sum[i] - k` has been seen before.
    
- Hash map tracks how many times each prefix sum occurred.
    

**Deep Dive Task:**

- Write out prefix sums for `[1,2,3]` manually to visualize the relationship.
    
- Try both brute-force (O(n²)) and optimized O(n) versions to feel the performance difference.

---

## 🧪 Work Enhancement — Deep Dive: Obsidian Templates for Daily Notes

**Tag:** #Obsidian #Workflow #Productivity

**Why it matters:** Templates speed up note-taking consistency—perfect for daily logs or meeting notes.

**Quick lesson:**

- Enable the **Templates plugin** (Settings → Core Plugins → Templates).
    
- Create a `/Templates/` folder with reusable files (e.g., Daily Plan, Meeting Notes).
    
- Use the **template hotkey** (`Ctrl/Cmd + T`) to insert predefined content instantly.
    

**Practice tasks:**

- Task A: Create `Daily Plan Template.md` with headers like “Goals”, “Highlights”, “Learnings”.
    
- Task B: Insert it into today’s note using the hotkey.
    
- Task C: Add a dynamic date snippet like `{{date:YYYY-MM-DD}}` inside.
    

---

## 🐧 Linux Learning — Deep Dive: `lsof`

**Tag:** #Linux/Command/lsof #Debugging

**What it is:** `lsof` (“list open files”) shows which processes are using which files, sockets, or ports.

**Scenario:** A port (e.g., 3000) is “already in use.” Use `lsof` to find and kill the culprit.

**Quick commands / cheatsheet:**

- Show open files: `lsof`
    
- Check what’s using port 3000: `lsof -i :3000`
    
- Find what’s locking a file: `lsof /path/to/file`
    
- Kill process holding a port: `kill -9 $(lsof -t -i :3000)`
    

**Why useful:** It’s the Swiss army knife for diagnosing “busy ports” or “file in use” errors.

**Practice tasks:**

- Task A: Run a simple Python server (`python -m http.server 8080`) → use `lsof -i :8080` to inspect it.
    
- Task B: Find all open network connections: `lsof -i`.
    
- Task C: Try `lsof +D /tmp` to see all open files in `/tmp`.
    

---

Would you like me to **add one “Weekly Integration Tip”** starting next week — something that combines your n8n / Cursor / Obsidian / Linux learnings into one small automation idea every Friday?