

---

# 📌 **2025-11-25 — Daily Learning Plan**

| Category             | Task                                                     | Status |
| -------------------- | -------------------------------------------------------- | ------ |
| 🧠 LeetCode Practice | **507. Perfect Number**                                  | ✅      |
| 🧪 Work Enhancement  | n8n Deep Dive: **Error Handling + Retry Logic Patterns** | ✅      |
| 🐧 Linux Learning    | Command: **`head`**                                      | ✅      |

---

# 🧠 LeetCode — **507. Perfect Number**

**Tags:** #Math #Factors #BruteforceOptimization  
**Why chosen:**
  
- Simple but great for practicing divisor loops and optimization
    
- Easy daily warmup without repetition
    
- Lets you explore edge cases + performance tricks
    

### Mini-Lesson

A number is **perfect** if it's equal to the sum of its **proper divisors** (excluding itself).

Example:  
`28 → 1 + 2 + 4 + 7 + 14 = 28`

### Key Thinking Points

- Why can you loop only to `sqrt(n)`?
    
- How to avoid double-adding divisors
    
- Why 1 is not perfect
    
- Limit constraints (the biggest perfect number in the problem)
    

---

# 🧪 Work Enhancement — n8n

## **Error Handling + Retry Logic Patterns**

**Tags:** #n8n #WorkflowResilience #ErrorHandling #Retries

### Why Today

Your automations are getting more complex — stability becomes more important.  
This is one of the **core professional n8n engineering skills**.

### What You’ll Learn

1. **The “Error Workflow” pattern**
    
    - A separate workflow triggers on failure
        
    - Useful for logging, Slack alerts, and fallback actions
        
2. **Built-in retry behavior**
    
    - Node → “Settings” → Execution → Retry
        
    - Configure backoff, delay, and max attempts
        
3. **Try/Catch pattern with Function nodes**
    
    ```js
    try {
      // risky API call
    } catch (e) {
      return [{ error: e.message }]
    }
    ```
    
4. **Graceful degradation**
    
    - If API fails → switch to cached data
        
    - Or skip step but keep execution alive
        

### Why This Matters

- Makes automations **robust**, not fragile
    
- Prevents broken workflows from silently stopping
    
- Helps when building production-grade internal tools
    

---

# 🐧 Linux Command — **`head`**

**Tags:** #Linux/Command/head #TextProcessing #Logs

**Why chosen:**
  
- Very useful for inspecting large data/log files
    
- Pairs well with other commands you’ve learned
    

### Common Uses

Show first 10 lines (default):

```bash
head file.txt
```

Show first N lines:

```bash
head -n 20 file.txt
```

Preview CSV structure:

```bash
head data.csv
```

Check log beginnings for metadata or header patterns.

### Practical Mini-Tasks

- View the first 15 lines of your largest file in ~/Downloads
    
- Combine with pipes:
    
    ```bash
    grep "error" app.log | head
    ```
    

---

If you want, I can also start:  
✅ weekly accumulated stats  
✅ rotating difficulty  
✅ a “review day” every Sunday

Just say “enable review mode” 😊