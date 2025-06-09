Here’s a clearer, easier-to-digest breakdown of the **Real Python – Primer on Python Decorators** article:

---

## 🔧 What Is a Decorator?

* **Definition:** A decorator is a callable (often a function) that takes another function and returns a modified version of it, without changing the original function’s source code ([realpython.com][1]).
* **Purpose:** It lets you *wrap* existing behavior to add new functionality like logging, timing, caching, or authentication.

---

## 🧠 Key Concepts Behind Decorators

1. **First-Class Functions**
   Functions in Python are objects: they can be passed around and returned just like variables ([medium.com][2]).

2. **Inner Functions & Closures**
   You can define functions inside functions, and inner functions can capture variables from their enclosing scope ([medium.com][2]).

3. **Higher-Order Functions**
   A decorator is essentially a higher-order function: it takes a function, defines a `wrapper` inside it (the inner function), and returns that wrapper ([realpython.com][3], [medium.com][2]).

---

## 🛠 How to Write a Simple Decorator

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before!")
        result = func(*args, **kwargs)
        print("After!")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
```

* When `say_hello()` is called, it runs `wrapper`, adding behavior before and after the original function ([realpython.com][4]).
* Using `@my_decorator` is syntactic sugar for `say_hello = my_decorator(say_hello)` ([realpython.com][5]).

---

## 🧩 Decorator Patterns & Use Cases

1. **Maintaining Metadata**
   Use `functools.wraps` to preserve the original function’s name and docstring inside wrappers .

2. **Decorators with Arguments**
   You can create decorator factories that take parameters, e.g.:

   ```python
   def repeat(n):
       def decorator(func):
           def wrapper(*args, **kwargs):
               for _ in range(n):
                   func(*args, **kwargs)
           return wrapper
       return decorator

   @repeat(3)
   def greet():
       print("Hi!")
   ```

   Here, `repeat(3)` returns the actual decorator ([codezup.com][6], [medium.com][2]).

3. **Stacking Decorators**
   You can apply multiple decorators to one function; they wrap in bottom-to-top order ([realpython.com][7]).

---

## 📚 Common Real-World Uses

* **Timing:** Measure how long a function takes.
* **Logging:** Record entry/exit of functions.
* **Access Control:** Enforce permissions before running.
* **Caching/Memoization:** Store results for repeat calls.
* **Plugins/System Hooks:** Registry functions dynamically.

---

## ✅ Best Practices

* Always use `@wraps` from `functools` to maintain metadata ([realpython.com][8], [realpython.com][1], [realpython.com][7]).
* Keep decorator logic simple and focused.
* Watch out for mutable defaults or hidden side-effects.
* Use closures responsibly when capturing variables ([realpython.com][9], [codezup.com][6]).

---

## 🧑‍💻 Quick Example

```python
import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f}s")
        return result
    return wrapper

@timer
def waste_time(n):
    sum(i*i for i in range(n))

waste_time(100_0000)
```

This adds timing behavior cleanly, without touching the original `waste_time` implementation.

---

### TL;DR

* Decorators **wrap** functions to *add behavior without modifying original code*.
* They rely on **first-class functions**, **inner functions**, and **closures**.
* Apply them via `@decorator`, and stack them if needed.
* Use `functools.wraps` to maintain proper function metadata.
* Commonly used for logging, timing, caching, and access control.

Let me know if you want help building your own decorators or unpacking specific sections!

[1]: https://realpython.com/primer-on-python-decorators/?utm_source=chatgpt.com "Primer on Python Decorators"
[2]: https://medium.com/%40sumeetsarkar/python-decorators-part-1-c1063a9b7d57?utm_source=chatgpt.com "Python Decorators [Part 1]. Primer | by Sumeet Sarkar - Medium"
[3]: https://realpython.com/lessons/python-return-decorators/?utm_source=chatgpt.com "Taking and Returning Functions With Decorators – Real Python"
[4]: https://realpython.com/ref/glossary/decorator/?utm_source=chatgpt.com "decorator | Python Glossary – Real Python"
[5]: https://realpython.com/videos/simple-decorators/?utm_source=chatgpt.com "Simple Decorators (Video) - Real Python"
[6]: https://codezup.com/practical-guide-to-python-decorators/?utm_source=chatgpt.com "Python Decorators: A Practical Guide to Enhancing Code Reusability"
[7]: https://realpython.com/lessons/more-flexible-decorators/?utm_source=chatgpt.com "More Flexible Decorators (Video) - Real Python"
[8]: https://realpython.com/lessons/decorators/?utm_source=chatgpt.com "Decorators (Video) - Real Python"
[9]: https://realpython.com/courses/python-decorators-101/?utm_source=chatgpt.com "Python Decorators 101"
