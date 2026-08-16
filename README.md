# CS50P: Harvard CS50’s Introduction to Programming with Python

This repository documents my structured learning journey, solutions, and key takeaways through Harvard's CS50P course. The goal is to build independent Python proficiency and a deep understanding of the language.

---

## 🗺️ CS50P Learning Roadmap

```
                  ┌─────────────────────────────────────┐
                  │ 0. Functions, Variables             │
                  └──────────────────┬──────────────────┘
                                     │
                  ┌──────────────────▼──────────────────┐
                  │ 1. Conditionals                     │
                  └──────────────────┬──────────────────┘
                                     │
                  ┌──────────────────▼──────────────────┐
                  │ 2. Loops                            │
                  └──────────────────┬──────────────────┘
                                     │
                  ┌──────────────────▼──────────────────┐
                  │ 3. Exceptions                       │
                  └──────────────────┬──────────────────┘
                                     │
                  ┌──────────────────▼──────────────────┐
                  │ 4. Libraries                        │
                  └──────────────────┬──────────────────┘
                                     │
                  ┌──────────────────▼──────────────────┐
                  │ 5. Unit Tests                       │
                  └──────────────────┬──────────────────┘
                                     │
                  ┌──────────────────▼──────────────────┐
                  │ 6. File I/O                         │
                  └──────────────────┬──────────────────┘
                                     │
                  ┌──────────────────▼──────────────────┐
                  │ 7. Regular Expressions              │
                  └──────────────────┬──────────────────┘
                                     │
                  ┌──────────────────▼──────────────────┐
                  │ 8. Object-Oriented Programming     │
                  └──────────────────┬──────────────────┘
                                     │
                  ┌──────────────────▼──────────────────┐
                  │ 9. Et Cetera                        │
                  └─────────────────────────────────────┘
```

---

## 📁 Repository Structure & Organization Logic

To maintain a clean and structured learning repository, exercises are categorized into chapters (Weeks 0 to 9).

Inside each chapter directory, exercises follow a strict organizational rule depending on complexity and key learnings:

### 1. Standalone Python File (`exercise_name.py`)

- **When used:** Used when completing exercises without encountering errors.
- **Content:** Contains clean, functional Python code where top-of-file comments articulate the task requirements and implementation scope.

### 2. Dedicated Exercise Folder (`exercise_folder/`)

- **When used:** Used when encountering errors while building the code to document learnings and fixes.
- **Folder Contents:**
  - `solution.py` — The functional Python solution code.
  - `learnings.md` — A comprehensive markdown note documenting:
    - **Task Description:** Core problem requirements and constraints.
    - **Logic & Algorithm Flow:** Step-by-step breakdown of the approach.
    - **Code Implementation:** Clean, syntax-highlighted code block.
    - **Learnings & Gotchas:** Essential takeaways, mistake analysis, syntax notes, and optimization comparisons.

** Comparison with Javascript **
Having recently completed a JavaScript course, I also include JavaScript code comparisons in some of the learning reflections to reinforce syntax equivalencies and solidify my understanding across both languages.
---

## 🗂️ Course Modules Breakdown

### 0. Functions, Variables

- Basics of Python syntax and functions

### 1. Conditionals

- Decision-making constructs (`if`, `elif`, `else`), logical operators (`and`, `or`, `not`), and boolean expressions.

### 2. Loops

- Iteration techniques using `while` and `for` loops, and `break` / `continue` flow controls

### 3. Exceptions

- Runtime error management utilizing `try...except...else`, handling `ValueError` and `ZeroDivisionError`, re-prompting loops, and signal management via `EOFError`.

### 4. Libraries

- Utilizing built-in modules (`random`, `sys`, `statistics`) and third-party PyPI packages (`requests`, `cowsay`) alongside API integrations.

### 5. Unit Tests

- Software testing methodology using `pytest`, organizing test suites, asserting expectations, and validating code reliability.

### 6. File I/O

- Reading and writing persistent storage files (`.txt`, `.csv`), handling image binary buffers (`PIL`/`Pillow`), and structured data parsing.

### 7. Regular Expressions

- Pattern matching, data validation, and text extraction using the `re` module (quantifiers, capture groups, and validation bounds).

### 8. Object-Oriented Programming (OOP)

- Designing custom classes, encapsulating properties/methods, managing constructors (`__init__`), instance representation (`__str__`), and inheritance patterns.

### 9. Et Cetera

- Advanced Python concepts including generators, list/dict comprehensions, `map`, `filter`, `args` / `kwargs`, and type hinting.
