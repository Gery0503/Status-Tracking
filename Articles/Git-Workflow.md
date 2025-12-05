
---
Here are the **Git command lines** commonly demonstrated in that section for a small team collaborating via feature branches:

1. **Clone the repository**

   ```bash
   git clone <repo-url>
   ```

2. **Create and switch to a new feature branch**

   ```bash
   git checkout -b feature-branch
   ```

3. **Make commits locally**

   ```bash
   git add .
   git commit -m "Your message"
   ```

4. **Fetch the latest from main (optional sync)**

   ```bash
   git fetch origin
   git rebase origin/main
   ```

5. **Push the feature branch to the remote**

   ```bash
   git push origin feature-branch
   ```

6. **Open a pull request (via the platform’s UI like Bitbucket or GitHub)**

7. **After approval and merge, sync local main**

   ```bash
   git checkout main
   git pull origin main
   ```

These commands illustrate a typical Git feature-branch flow for collaborative development. For the full example and explanation, you can view the article directly here:


### ✅ **Other Core Concepts**

* **Git workflow** = a set of rules and branching strategies for team collaboration in Git.
* Choosing the right workflow depends on **team size**, **release frequency**, and **comfort with Git**.

---

### 🔄 **Common Git Workflows**

1. **Centralized Workflow**

   * Single `main` branch.
   * Simple, familiar (like SVN).
   * Best for small teams or Git beginners.

2. **Feature Branch Workflow**

   * Each feature gets its own branch.
   * Encourages clean, testable `main`.
   * Supports pull requests and code reviews.

3. **Gitflow Workflow**

   * Structured branching: `main`, `develop`, `release`, `hotfix`, `feature`.
   * Suits larger teams and defined release cycles.
   * Can be complex to manage.

4. **Forking Workflow**

   * Every contributor forks the main repo.
   * Great for open-source and distributed teams.
   * Promotes safe experimentation and external contributions.

---

### 📌 **Best Practices**

* Keep branches **short-lived** to avoid merge headaches.
* Use **pull requests** to enable reviews and feedback.
* Choose a workflow that matches your **team’s habits** and **release rhythm**.
* Avoid unnecessary complexity—**simpler is better** unless your project demands more structure.

---
**Read**: Git workflows best practices [Atlassian Git Tutorial – Git Workflows](https://www.atlassian.com/git/tutorials/comparing-workflows)

(Generated from chatGPT)

