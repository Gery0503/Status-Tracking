****
---

# 📌 2025-11-22 — Daily Learning Plan

| Category             | Task                                                                                                            | Status |
| -------------------- | --------------------------------------------------------------------------------------------------------------- | ------ |
| 🧠 LeetCode Practice | **[Binary Search — Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/)** | ✅      |
| 🧪 Work Enhancement  | n8n: **Error Handling Pattern (Try/Catch Flow)**                                                                | ✅      |
| 🐧 Linux Learning    | Command: **`sort`** (safe, useful, not in exclusion list)                                                       | ✅      |

---

## 🧠 LeetCode — **Guess Number Higher or Lower**

**Tag:** #BinarySearch #LogicDeduction  
**Why chosen:**

- You’ve done many classic binary-search–related problems.
    
- This one reinforces _binary search reasoning_ but is clean, light, and builds confidence.
    
- Good prep for harder monotonic-function search problems.
    

**Core Ideas:**

- Maintain `low`, `high` bounds.
    
- Use mid → adjust based on `guess(mid)`.
    
- Converge until low == high.
    

**Deep Dive Tag:** 🔍 _Binary Search Mental Model_

---

## 🧪 Work Enhancement — n8n **Error Handling Pattern (Try/Catch Flow)**

**Tag:** #n8n #WorkflowResilience #ErrorHandling

### 🎯 Why this today

You’re building more workflows that depend on external APIs and LLMs. Proper error handling prevents silent failures and makes debugging dramatically easier.

### 🧩 Pattern:

Use **"Error Trigger"** + **"Error Branch"** to protect the main workflow.

**Structure:**

1. **Main Workflow**
    
    - Critical nodes wrapped using the **“Execute Workflow”** node or **Try/Catch pattern**
        
2. **Error Trigger Workflow**
    
    - Receives exceptions
        
    - Logs to Slack/Gmail/Filemaker/etc.
        
3. **Optional: AI Node** to auto-explain error logs in plain English
    

**Example Catch Block Schema:**

```json
{
  "error": $json.message,
  "node": $node.name,
  "stack": $json.stack,
  "input": $json.data
}
```

**Why this matters:**

- Production-grade reliability
    
- Easy debugging
    
- Reusable in multiple automations
    

**Deep Dive Tag:** 🧩 _Workflow Reliability Engineering_

---

## 🐧 Linux — `sort`

**Tag:** #Linux/Command/sort #LogAnalysis

### Why today

You’ve covered many essential text-processing commands.  
`sort` is the next powerful building block for real-use cases (logs, reports, CSV, pipelines).

### Essentials

- Sort file alphabetically:
    
    ```bash
    sort file.txt
    ```
    
- Sort numerically:
    
    ```bash
    sort -n scores.txt
    ```
    
- Sort by a field (3rd column):
    
    ```bash
    sort -k3 file.txt
    ```
    
- Reverse order:
    
    ```bash
    sort -r file.txt
    ```
    

### Practice

- Sort `/etc/passwd` by UID
    
- Sort server logs by timestamp
    

**Deep Dive Tag:** ⚙️ _Developer Efficiency / Text Stream Manipulation_

---

If you want, I can also start generating **weekly difficulty progression** or **themed practice weeks**.