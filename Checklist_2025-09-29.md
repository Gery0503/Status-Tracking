# 📌 2025-09-29 – Daily Learning Plan

| Task Category        | Task (short title + link)                                                        | Status |
| -------------------- | -------------------------------------------------------------------------------- | ------ |
| 🧠 LeetCode Practice | Solve: [Relative Sort Array](https://leetcode.com/problems/relative-sort-array/) | ✅      |
| 🧪 Work Enhancement  | Topic: Cursor (AI-powered code editor)                                           | ✅      |
| 🐧 Linux Learning    | Command: `ncdu` — disk usage analyzer                                            | ✅      |

---

## 🧪 Work Enhancement — Deep Dive: Cursor (AI-powered code editor)

**Why it matters:** Cursor is a VS Code–like editor with integrated AI assistance for **editing, refactoring, and understanding code**. Unlike just chat-based AI, Cursor is tightly integrated into the coding workflow: inline code suggestions, context-aware edits, and multi-file reasoning.

**Quick lesson (what + how):**

1. *Core idea*: AI edits code directly in your editor, not just by suggestion.
2. *Key difference vs Copilot*: you can select code and **ask AI to refactor/explain** instead of only autocompleting.
3. *Use cases*: large-scale refactoring, documentation generation, or asking “what does this repo do?” across many files.

**Practice tasks (do these today):**

* Task A: Open a small script in Cursor → highlight a function → ask AI to explain it in plain English.
* Task B: Use Cursor to refactor a function name consistently across the file.
* Task C: Ask Cursor to add docstrings or inline comments for one file.

---

## 🐧 Linux Learning — Deep Dive: `ncdu`

**What it is:** `ncdu` (NCurses Disk Usage) is an interactive tool to analyze disk usage in a terminal, much faster and friendlier than `du`.

**Scenario:** Your server is running out of space (`df -h` shows 90% usage). Instead of manually checking with `du -sh *`, run `ncdu` to interactively explore and delete large files.

**Quick commands / cheatsheet:**

* Install: `sudo apt install ncdu` (Debian/Ubuntu) or `sudo yum install ncdu` (RHEL/CentOS).
* Run on root: `sudo ncdu /`
* Navigate: Arrow keys to browse directories.
* Delete: Press `d` on a file/folder to delete directly.
* Quit: `q`

**Why useful:** Saves huge amounts of time when debugging “disk full” issues, especially on servers with deep nested directories.

**Practice tasks (do these today):**

* Task A: Run `ncdu ~` and find your top 3 largest folders.
* Task B: Delete (or note) at least one unnecessary large file safely.
* Task C: Compare results of `du -sh *` vs `ncdu` in your home directory.

