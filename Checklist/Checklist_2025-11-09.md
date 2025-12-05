
---

# 📌 2025-11-09 – Daily Learning Plan

| Task Category        | Task (short title + link)                                                    | Status |
| -------------------- | ---------------------------------------------------------------------------- | ------ |
| 🧠 LeetCode Practice | Solve: [Number Complement](https://leetcode.com/problems/number-complement/) | ✅      |
| 🧪 Work Enhancement  | Topic: **LangChain Output Parsers** – structuring LLM responses              | ✅      |
| 🐧 Linux Learning    | Command: `df` — report file system disk space usage                          | ✅      |

---

## 🧠 LeetCode Practice — [Number Complement]

**Tag:** #LeetCode #BitManipulation  
**Skill path:** Binary operations and bitmasking logic.  
**Why chosen:** Builds intuition for **bitwise XOR and binary inversion**, foundational for optimizing algorithms that manipulate binary states (e.g., hashing, compression, or permissions).  
**Deep Dive Tag:** 🔍 _Algorithmic Optimization_

---

## 🧪 Work Enhancement — Deep Dive: **LangChain Output Parsers**

**Tag:** #LangChain #OutputParser #StructuredLLM  
**What it is:** Output Parsers in LangChain define **how model responses are structured and interpreted**, ensuring reliable downstream usage.  
**Quick lesson:**

1. **Core purpose:**  
    Transform raw text into structured formats like JSON, Pydantic models, or data objects.
    
2. **Common types:**
    
    - `StructuredOutputParser` — ensures output schema validation.
        
    - `CommaSeparatedListOutputParser` — for list extraction tasks.
        
    - `PydanticOutputParser` — converts to Python classes using `pydantic` models.
        
3. **Example:**
    
    ```python
    from langchain.output_parsers import PydanticOutputParser
    from pydantic import BaseModel
    
    class Task(BaseModel):
        name: str
        priority: int
    
    parser = PydanticOutputParser(pydantic_object=Task)
    output = parser.parse("{'name': 'Test Task', 'priority': 2}")
    print(output)
    ```
    

**Practical n8n Idea:**  
Embed a parser step to clean and structure model outputs before saving into databases or triggering follow-up automation.  
**Why useful:** Makes LLM workflows **robust and automatable**.  
**Deep Dive Tag:** 🧩 _AI Engineering / Workflow Reliability_

---

## 🐧 Linux Learning — Deep Dive: `df`

**Tag:** #Linux/Command/df #DiskUsage #SystemMonitoring  
**What it is:** The `df` command reports how much disk space is used and available on mounted filesystems.  
**Quick commands:**

- Human-readable format:
    
    ```bash
    df -h
    ```
    
- Show specific filesystem:
    
    ```bash
    df -h /home
    ```
    
- Include filesystem type:
    
    ```bash
    df -Th
    ```
    

**Why useful:**  
Essential for monitoring disk health, preventing space overflows, and managing partitions efficiently.  
**Practice tasks:**

- Task A: Check which filesystem your `/` root partition belongs to.
    
- Task B: Write a small bash alias `alias diskfree='df -h --total'` for quick reports.
    
- Task C: Compare `df` output with `du` for deeper directory-level analysis.
    

**Deep Dive Tag:** ⚙️ _System Insight / Admin Efficiency_

---

Would you like me to start auto-generating this plan **every morning (Taiwan time)** so you don’t have to ask manually?