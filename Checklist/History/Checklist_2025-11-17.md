

---

# 📌 2025-11-17 – Daily Learning Plan

| Category             | Task                                                                            | Status |
| -------------------- | ------------------------------------------------------------------------------- | ------ |
| 🧠 LeetCode Practice | **[Valid Mountain Array](https://leetcode.com/problems/valid-mountain-array/)** | ✅      |
| 🧪 Work Enhancement  | n8n: **Webhook → AI preprocessing pattern**                                     | ✅      |
| 🐧 Linux Learning    | Command: **`cut`** — extract columns cleanly                                    | ✅      |

---

## 🧠 LeetCode — **Valid Mountain Array**

**Tag:** #LeetCode #Array #TwoPointers  
**Why chosen:**  
This builds reasoning for array structure validation using pointer scanning without falling into common traps (plateaus, partial climbs).

**Core Ideas (short & actionable):**

- Strictly increasing → peak → strictly decreasing
    
- No equal adjacent values
    
- Peak cannot be first or last
    

**Deep Dive Tag:** 🔍 _Array Structure Reasoning_

---

## 🧪 Work Enhancement — n8n: **Webhook → AI Preprocessing Pattern**

**Tag:** #n8n #Automation #LLM #WorkflowDesign  
**Why chosen:**  
You often design workflows involving AI + input transformation. Today’s focus is a minimal but scalable pattern.

### 🧩 Pattern: Webhook → Code Node → AI → Output

**Flow Logic:**

1. **Webhook Node** receives raw input (form, API, frontend).
    
2. **Code Node** converts messy input → structured JSON.
    
    ```js
    const body = $json.body || {};
    return [{ json: { prompt: body.text?.trim() || "" } }];
    ```
    
3. **LLM Node** processes the structured prompt.
    
4. **Respond via Webhook Response** for synchronous execution.
    

**Why this matters:**  
This structure becomes reusable for:

- AI agents
    
- text rewriting
    
- log explanations
    
- technical summaries
    
- Slack/GitHub/Gmail automations
    

**Deep Dive Tag:** 🧩 _Workflow Engineering / Input Normalization_

---

## 🐧 Linux Learning — `cut`

**Tag:** #Linux/Command/cut #TextProcessing  
**Why chosen:**  
`cut` is the next essential stream-processing tool that pairs well with pipes and logs.

### Essentials

- Extract 3rd column (tab-delimited):
    
    ```bash
    cut -f3 file.txt
    ```
    
- Extract characters 1–5:
    
    ```bash
    cut -c1-5 file.txt
    ```
    
- Extract multiple fields:
    
    ```bash
    cut -d',' -f1,4,5 data.csv
    ```
    

### Practice

- Pull only the PID column from `ps aux`.
    
- Print all usernames from `/etc/passwd`.
    

**Deep Dive Tag:** ⚙️ _Developer Efficiency / Text Stream Mastery_

---

If you want, I can also start preparing **weekly meta-themes** (e.g., “array mastery week”, “workflow architecture week”, “Linux text-processing week”).