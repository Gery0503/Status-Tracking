

---

# 📌 2025-11-07 – Daily Learning Plan

| Task Category        | Task (short title + link)                                                                | Status |
| -------------------- | ---------------------------------------------------------------------------------------- | ------ |
| 🧠 LeetCode Practice | Solve: [Unique Morse Code Words](https://leetcode.com/problems/unique-morse-code-words/) | ✅      |
| 🧪 Work Enhancement  | Topic: **MCP (Model Context Protocol)** – How AI tools securely share memory & context   | ✅      |
| 🐧 Linux Learning    | Command: `htop` — real-time system performance monitor                                   | ✅      |

---

## 🧠 LeetCode Practice — [Unique Morse Code Words]

**Tag:** #LeetCode #String #HashSet  
**Skill path:** Hashing fundamentals and data transformation.  
**Why chosen:** Reinforces hashing, set usage, and string transformation — essential for building memory and deduplication logic.

---

## 🧪 Work Enhancement — Deep Dive: **MCP (Model Context Protocol)**

**Tag:** #MCP #AIInfrastructure #OpenAI  
**What it is:** MCP is a **protocol that lets local or external tools share “context”** (like files, data, or commands) with an AI model securely and consistently.  
**Quick lesson:**

1. **Purpose:** It creates a standardized way for AI systems to access tools or APIs (like LangChain, Cursor, or n8n workflows) without leaking sensitive info.
    
2. **Structure:**
    
    - _Client:_ the AI model (e.g., ChatGPT).
        
    - _Server:_ a connector to local or remote data sources.
        
    - _Protocol:_ defines what data and functions can be exchanged.
        
3. **Example idea:** Use MCP to expose your local `notes/` folder to your AI assistant, so it can summarize or cross-reference data directly.  
    **Why useful:** Bridges local productivity tools (Obsidian, VS Code, n8n) with cloud AI — safely enabling true “context-aware” automation.  
    **Try:**
    

- Read MCP spec: [modelcontextprotocol.io](https://modelcontextprotocol.io/)
    
- Sketch how your Obsidian vault could register as an MCP data source.
    

---

## 🐧 Linux Learning — Deep Dive: `htop`

**Tag:** #Linux #Monitoring #Performance  
**What it is:** A colorized, interactive process viewer — an upgrade over `top`.  
**Scenario:** You want to identify CPU or memory bottlenecks on your dev server.  
**Quick commands:**

- Install: `sudo apt install htop`
    
- Run: `htop` → sort by CPU (F6) or memory (M).
    
- Kill a process: select → press `F9`.  
    **Why useful:** Perfect for monitoring workloads in real time during builds, Docker runs, or training jobs.  
    **Practice tasks:**
    
- Task A: Run `htop` and observe your top CPU-intensive tasks.
    
- Task B: Filter by user (`u` key) to isolate your own processes.
    
- Task C: Save a system snapshot with `htop --no-color > htop.log`.
    

---

Would you like tomorrow’s **Work Enhancement** to move toward **LangChain integration concepts** or focus again on **Obsidian automation** next?