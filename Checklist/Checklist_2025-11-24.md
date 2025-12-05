
---

# 📌 **2025-11-24 — Daily Learning Plan**

| Category             | Task                                                                | Status |
| -------------------- | ------------------------------------------------------------------- | ------ |
| 🧠 LeetCode Practice | **728. Self Dividing Numbers**                                      | ✅      |
| 🧪 Work Enhancement  | n8n: **Webhook → Transform → Database Pattern**                     | ✅      |
| 🐧 Linux Learning    | Command: **`uniq`** (safe — not excluded & pairs well after `sort`) | ✅      |

---

# 🧠 LeetCode — **728. Self Dividing Numbers**

**Tags:** #Math #Simulation #DigitProcessing  
**Why chosen:**

- Not in exclusion list
    
- Light & refreshing after a long chain of tree/array/string practice
    
- Builds digit-iteration intuition used in many interview problems
    
- No heavy DS, perfect for a quick but meaningful daily exercise.
    

### Key Concepts

- A number is _self-dividing_ if every digit divides the number evenly.
    
- Zero digit immediately invalidates.
    
- Straightforward loop & digit parsing → good warmup.
    

Try to write a clean helper function `isSelfDividing(n)`.

---

# 🧪 Work Enhancement — n8n

## **Webhook → Transform → Database Pattern**

**Tags:** #n8n #ETL #Webhooks #DataPipelines

### Why today

You’ve been building more automations that pull external data. This is the **most fundamental ingestion pipeline** pattern in real-world n8n use.

### Standard Flow

1. **Webhook Node** — receives payload from outside (GitHub, Stripe, custom app).
    
2. **Function / Set Nodes** — clean + reshape the data.
    
3. **Database Write** (MySQL, Postgres, MongoDB, Supabase) — upsert or insert.
    
4. **Optional: AI Node** — auto-generate JSON summaries or categorize.
    

### Example field mapping pattern

```json
{
  "id": $json.id,
  "email": $json.user.email,
  "created_at": new Date().toISOString()
}
```

### Why this matters

- Teaches structure of scalable workflows
    
- Prepares for event-driven automation
    
- A reusable template for all your data integrations
    

---

# 🐧 Linux Command — **`uniq`**

**Tags:** #Linux/Command/uniq #TextProcessing  
**Why chosen:**

- Not in exclusion list
    
- Complements your recent `sort` learning
    
- Important in pipelines involving logs, metrics, or dedup
    

### Usage

Remove consecutive duplicates:

```bash
uniq names.txt
```

Count occurrences:

```bash
uniq -c names.txt
```

Get only duplicates:

```bash
uniq -d names.txt
```

Common real-world pipeline:

```bash
sort access.log | uniq -c | sort -nr
```

→ Gets most frequent IPs, errors, URLs, etc.

---

If you want, I can start generating **weekly streak summaries** or **auto-progress difficulty scaling** 😊