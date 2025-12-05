2025-06-11  
**Watch**: FastAPI crash course [FastAPI Crash Course Ep 1: Build a To‑Do List API in 10 Minutes][1]
---

## ✅ FastAPI Beginner Setup Notes

### 📁 1. Create and Activate a Virtual Environment

Use these commands in your terminal to isolate dependencies:

```bash
py -m venv env                   # Create virtual environment
env\Scripts\activate.ps1         # Activate it (PowerShell)
```

Once activated, your prompt should change to show `(env)`.

---

### 📦 2. Install Required Packages

Install **FastAPI** and **Uvicorn** (a lightweight ASGI server):

```bash
pip install fastapi uvicorn
```

---

### 🐍 3. Basic FastAPI App Code

Create a Python file (e.g., `main.py`) with this starter code:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

✅ This sets up a basic FastAPI web server with a single root route.

---

### 🚀 4. Run the Server

In the terminal, use this command to run your app with auto-reload:

```bash
uvicorn main:app --reload
```

* `main` = the Python file name (without `.py`)
* `app` = the FastAPI app instance
* `--reload` = enables auto-reload when code changes

---

### 🌐 5. Visit the App

Once running, open this in your browser:

```
http://127.0.0.1:8000/
```

You should see:

```json
{"Hello": "World"}
```

Bonus: Go to `/docs` for auto-generated Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

(Generated from chatGPT)

[1]: https://www.youtube.com/watch?v=lmHltbt9ct8 "FastAPI Crash Course Ep 1: Build a To-Do List API in 10 Minutes ..."