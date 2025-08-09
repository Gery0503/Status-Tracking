Here’s a clearer summary of RESTful APIs from restfulapi.net, followed by a simple Python example:

---

## 🧠 What Is a RESTful API?

**REST** stands for **Representational State Transfer**, a design style introduced by Roy Fielding in 2000. It isn’t a protocol but a set of architectural principles for building distributed web systems using HTTP ([restfulapi.net][1]).

Key architectural constraints include ([restfulapi.net][2]):

1. **Client–Server**: Clear separation between front-end clients and back-end servers.
2. **Statelessness**: Each request contains all the info the server needs; no client context is stored.
3. **Cacheable**: Responses indicate whether they can be cached.
4. **Uniform Interface**: Uses consistent methods and URIs to work with resources.
5. **Layered System**: Architecture can include intermediaries without clients knowing.
6. **Code on Demand (optional)**: Servers may send executable code to clients when needed.

---

## 🔑 REST Principles Overview

1. **Resources Identified by URIs**
   Use nouns in paths—e.g., `/customers/{id}/orders`—not verbs ([restfulapi.net][2], [it.wikipedia.org][3], [restfulapi.net][4]).

2. **HTTP Verbs Map to CRUD**

   * `GET` = Retrieve (safe, idempotent)
   * `POST` = Create (non-idempotent)
   * `PUT` = Replace
   * `PATCH` = Partial update
   * `DELETE` = Remove ([restfulapi.net][5], [restfulapi.net][6]).

3. **Proper Use of HTTP Status Codes**

   * `200 OK`,
   * `201 Created`,
   * `204 No Content`,
   * `400 Bad Request`,
   * `404 Not Found`, etc. ([restfulapi.net][7], [restfulapi.net][8]).

4. **Consistent Resource Representations**
   Typically JSON or XML—response bodies should include metadata and hyperlinks (HATEOAS) when possible ([restfulapi.net][2], [en.wikipedia.org][9]).

5. **Versioning & Backward Compatibility**
   Support versioning via URI (`/api/v1/...`), headers, or content negotiation, and maintain compatibility across versions ([restfulapi.net][10]).

6. **Handle Long-Running & Async Tasks**
   Use `202 Accepted` and status endpoints, allow polling or webhooks for task results ([restfulapi.net][11]).

---

## ✅ Simple Python Example

A basic Python client using the popular `requests` library to interact with a RESTful API:

```python
import requests

BASE_URL = "https://api.example.com/tasks"

# 1️⃣ Create a new task
resp = requests.post(BASE_URL, json={"name": "Sample Task"})
resp.raise_for_status()  # ensure request succeeded
task = resp.json()
print("Created task:", task)
# e.g., {"id": 123, "name": "Sample Task", "status": "pending"}

# 2️⃣ Retrieve task details (safe & idempotent)
task_id = task["id"]
resp = requests.get(f"{BASE_URL}/{task_id}")
resp.raise_for_status()
print("Task details:", resp.json())

# 3️⃣ Update status (e.g., mark as completed)
resp = requests.patch(f"{BASE_URL}/{task_id}", json={"status": "completed"})
resp.raise_for_status()
print("Updated task:", resp.json())

# 4️⃣ Delete the task
resp = requests.delete(f"{BASE_URL}/{task_id}")
if resp.status_code == 204:
    print("Task deleted successfully")
```

This script follows REST conventions:

* **POST** to create,
* **GET** to read,
* **PATCH** to update,
* **DELETE** to remove.

---

## TL;DR

* RESTful APIs expose resources via clear URIs and use HTTP verbs for operations.
* They are **stateless**, **cacheable**, and follow a **uniform interface**.
* Use **JSON**, proper **HTTP status codes**, and include **versioning** and **hypermedia links** when applicable.
* The Python `requests` example shows typical CRUD interactions in just a few lines.

Let me know if you'd like to dive deeper into any specific part—like HATEOAS, pagination, error handling, or API versioning!

[1]: https://restfulapi.net/?utm_source=chatgpt.com "What is REST?: REST API Tutorial"
[2]: https://restfulapi.net/rest-architectural-constraints/?utm_source=chatgpt.com "REST Architectural Constraints - REST API Tutorial"
[3]: https://it.wikipedia.org/wiki/Representational_state_transfer?utm_source=chatgpt.com "Representational state transfer"
[4]: https://restfulapi.net/resource-naming/?utm_source=chatgpt.com "REST API URI Naming Conventions and Best Practices"
[5]: https://restfulapi.net/soap-vs-rest-apis/?utm_source=chatgpt.com "REST vs. SOAP: The Differences - REST API Tutorial"
[6]: https://restfulapi.net/http-methods/?utm_source=chatgpt.com "HTTP Methods - REST API Tutorial"
[7]: https://restfulapi.net/http-status-codes/?utm_source=chatgpt.com "HTTP Status Codes - REST API Tutorial"
[8]: https://restfulapi.net/versioning/?utm_source=chatgpt.com "REST API Versioning: How to Version a REST API? - REST API Tutorial"
[9]: https://en.wikipedia.org/wiki/HATEOAS?utm_source=chatgpt.com "HATEOAS"
[10]: https://restfulapi.net/rest-api-best-practices/?utm_source=chatgpt.com "REST API Best Practices"
[11]: https://restfulapi.net/rest-api-design-for-long-running-tasks/?utm_source=chatgpt.com "REST API Design for Long-Running Tasks - REST API Tutorial"

(Generated from ChatGPT)