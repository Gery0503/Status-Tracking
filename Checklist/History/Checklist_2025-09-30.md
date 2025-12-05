# 📌 2025-09-30 – Daily Learning Plan

| Task Category        | Task (short title + link)                                          | Status |
| -------------------- | ------------------------------------------------------------------ | ------ |
| 🧠 LeetCode Practice | Solve: [Happy Number](https://leetcode.com/problems/happy-number/) | ✅      |
| 🧪 Work Enhancement  | Topic: Obsidian – Backlinks & Graph View                           | ✅      |
| 🐧 Linux Learning    | Command: `xargs` — build & execute commands from input             | ✅      |
|                      |                                                                    |        |

---

## 🧪 Work Enhancement — Deep Dive: Obsidian Backlinks & Graph View

**Tag:** #Obsidian #KnowledgeManagement

**Why it matters:** Obsidian transforms plain Markdown into a *knowledge network* with backlinks and a graph view. Instead of isolated notes, you build a **web of connected thoughts**.

**Quick lesson (what + how):**

* **Backlinks:** Every time you link `[[Note A]]` inside `Note B`, Obsidian shows the reverse link too. This creates *two-way connections*.
* **Graph View:** Lets you *visualize connections* across your vault, like a mind map generated from your notes.

**Practice tasks (do today):**

* Task A: Create 2 new notes and link them to an older one using `[[ ]]`.
* Task B: Open the **Backlinks panel** and see which notes now reference each other.
* Task C: Open the **Graph View** and explore clusters of related notes.

---

## 🐧 Linux Learning — Deep Dive: `xargs`

**Tag:** #Linux/Command/xargs #Automation

**What it is:** `xargs` takes input (from a file, pipe, or output of another command) and turns it into arguments for another command.

**Scenario:** You delete multiple `.tmp` files scattered across directories. Instead of doing it manually:

```bash
find . -name "*.tmp" | xargs rm
```

This finds all `.tmp` files and deletes them in one go.

**Quick commands / cheatsheet:**

* Count lines in multiple files: `cat filelist.txt | xargs wc -l`
* Move images: `ls *.png | xargs -I{} mv {} images/`
* Parallel execution: `cat hosts.txt | xargs -n1 -P4 ping -c1`

**Why useful:** It bridges commands together, especially when outputs are too long for a single line or need flexible processing.

**Practice tasks (do today):**

* Task A: Create 5 dummy `.tmp` files → delete them with `find . -name "*.tmp" | xargs rm`.
* Task B: Try `echo "file1 file2 file3" | xargs touch` to create multiple files quickly.
* Task C: Use `ls | xargs -n 1 echo "Processing:"` to understand its behavior.
