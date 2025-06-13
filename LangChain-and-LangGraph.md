Study notes based on YouTube video **“LangChain vs LangGraph: A Tale of Two Frameworks”**:

---

## 🧠 LangChain vs LangGraph – Summary Notes

---

### 🔹 What Are They?

| Framework     | Description                                                                                            |
| ------------- | ------------------------------------------------------------------------------------------------------ |
| **LangChain** | Framework for building LLM-powered applications using sequential **chains** of components.             |
| **LangGraph** | LangChain extension for creating **stateful**, **multi-agent** systems with **graph**-based workflows. |

---

### 🧱 LangChain – Key Concepts

**Workflow Example**:
`Retrieve ➝ Summarize ➝ Answer`

#### 📦 Components:

* **Doc Loader**: Load documents from various sources.
* **Text Splitter**: Break large texts into smaller chunks.
* **Prompt**: Instructions for the LLM.
* **LLM**: The large language model doing the task.
* **Memory**: Stores chat history/context between turns.
* **Agent**: Orchestrates tool usage and decision making.

#### 🛠 Used For:

* Linear workflows (e.g., fetch → summarize → respond).
* Tasks where each step follows the next.

---

### 🌐 LangGraph – Key Concepts

**Architecture**:

```
[Process Input]
   ↓      ↓      ↓
Add   Complete  Summarize
Tasks   Tasks    Tasks
```

All transitions return to **Process Input**.

#### 📦 Components:

* **Nodes**: Individual actions or steps (e.g., Add Task).
* **Edges**: Connections or transitions between nodes.
* **State**: Shared, persistent data across the entire graph.

#### 🧩 Features:

* Can loop, revisit nodes, or branch based on conditions.
* Built for **multi-agent**, interactive, and adaptive systems.

---

### 🔁 Comparison Table

| Feature           | **LangChain**                                      | **LangGraph**                                            |
| ----------------- | -------------------------------------------------- | -------------------------------------------------------- |
| **Primary Focus** | LLM apps via chained operations                    | Stateful, multi-agent systems                            |
| **Structure**     | Chain (DAG: Directed Acyclic Graph)                | Graph (with loops and branching)                         |
| **Components**    | Memory, Prompt, LLM, Agent                         | Nodes, Edges, State                                      |
| **State Mgmt**    | Limited (can pass info forward)                    | Robust, central state accessed by all nodes              |
| **Use Cases**     | Sequential processes (e.g., data → summarize → QA) | Complex workflows (e.g., interactive agents, assistants) |

---

### 🏁 Takeaways

* **Use LangChain** when you:

  * Know the task order.
  * Need simple pipelines like Retrieval-Augmented Generation (RAG).
  * Want to use modular components quickly.

* **Use LangGraph** when you:

  * Need adaptive workflows.
  * Are building agents that interact, remember, and decide dynamically.
  * Require robust state and non-linear transitions.

---

(Generated from chatGPT)
(based on video https://www.youtube.com/watch?v=qAF1NjEVHhY&t=19s)