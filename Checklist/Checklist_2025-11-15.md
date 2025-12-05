
---

# 📌 2025-11-15 – Daily Learning Plan

| Task Category        | Task (short title + link)                                                                          | Status |
| -------------------- | -------------------------------------------------------------------------------------------------- | ------ |
| 🧠 LeetCode Practice | Solve: **[Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/)** | ✅      |
| 🧪 Work Enhancement  | Topic: **n8n – Using Code Node vs Function Node**                                                  | ✅      |
| 🐧 Linux Learning    | Command: `grep` — search text patterns efficiently                                                 | ✅      |

---

## 🧠 LeetCode Practice — **Repeated Substring Pattern**

**Tag:** #LeetCode #String #KMP  
**Skill path:** Pattern searching, string manipulation, intro to **Knuth-Morris-Pratt** thinking.  
**Why chosen:**  
Understanding repeated patterns builds foundational skills for handling substring search, string hashing, and more advanced string algorithms.  
**Deep Dive Tag:** 🔍 _String Pattern Recognition_

---

## 🧪 Work Enhancement — Deep Dive: **n8n Code Node vs Function Node**

**Tag:** #n8n #Automation #JavaScript  
**Why this topic:**  
You often integrate AI + automation + workflows; knowing when to use each node is crucial for maintainable flows.

### 🧩 Code Node (recommended for most logic)

- Uses `items[]` array pattern
    
- Most flexible
    
- Great for mapping, transforming, filtering
    
- Example:
    
    ```js
    return items.map(item => {
      item.json.count = item.json.text.length;
      return item;
    });
    ```
    

### 🛠 Function Node

- Processes a _single item_ at a time
    
- Preferred when logic is simple and isolated
    
- Deprecated in many advanced tutorials—Code Node supersedes it.
    

### When to use which?

|Scenario|Node|
|---|---|
|Transform a batch of items|Code Node|
|Run step-by-step math logic|Function Node|
|Prepare structured JSON for LLM|Code Node|
|Migrate from old workflows|Function Node (legacy only)|

**Why useful:**  
Building clean, predictable n8n flows is key to scaling automation across teams and AI agents.  
**Deep Dive Tag:** 🧩 _Workflow Engineering_

---

## 🐧 Linux Learning — Deep Dive: `grep`

**Tag:** #Linux/Command/grep #Search #Regex  
**What it is:**  
`grep` searches for text patterns inside files using strings or regex.

**Essentials:**

- Case-insensitive search:
    
    ```bash
    grep -i "error" log.txt
    ```
    
- Show line numbers:
    
    ```bash
    grep -n "main" *.py
    ```
    
- Recursive search in directories:
    
    ```bash
    grep -R "TODO" ~/projects
    ```
    
- Use regex:
    
    ```bash
    grep -E "cat|dog" file.txt
    ```
    

**Practice tasks:**

- Task A: Search for all `.sh` scripts that contain the word `sudo`.
    
- Task B: Filter lines ending with a number using regex.
    
- Task C: Compare `grep` vs `rg` (ripgrep, if installed).
    

**Deep Dive Tag:** ⚙️ _Developer Efficiency / System Insight_

---

If you want, I can:  
✅ auto-generate your plan every morning  
or  
📅 create a weekly roadmap for Nov 15–21.

Just tell me!