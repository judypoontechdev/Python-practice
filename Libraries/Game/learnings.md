## 1. Mastering `while True`, `try-except-else` Control Flow

### Takeaway 1.1: Strategic Use of `break` vs. `continue`

When running an infinite loop (`while True`) to sanitize inputs, **we only have one `break` keyword per loop** before it exits completely.

- **First Loop (Getting `level`):** The sole purpose of this loop is to prompt until a valid positive integer is supplied. Once `level > 0` passes, we can immediately call `break` to exit and move on to generating the secret number.
- **Second Loop (Processing `guess`):** Here, the loop's final exit condition must be reserved for when the player actually wins (`generate(answer, guess)` returns `True`). Therefore, to validate `guess` as a positive integer within the loop without prematurely exiting, we **flip the validation logic** using `if guess <= 0: continue`. This rejects invalid inputs by forcing a re-prompt while saving the single `break` trigger for the win state.

```python
# Reserve `break` for the win condition in the second loop:
while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            continue  # Flip logic to reprompt on invalid values
    except ValueError:
        continue
    else:
        if generate(answer, guess):
            break  # Reserved break for when the game is won
```

### Takeaway 1.2: Implicit Reprompting (Omitting Redundant `else: continue`)

In block configurations like `if level > 0: break`, writing `else: continue` is unnecessary.

- When `level > 0` evaluates to `False`, Python skips the `break` statement and continues execution downward.
- Since there is no further code remaining in that iteration, control naturally loops back to the top of `while True:`, re-prompting the user automatically.

---

## 2. Writing Modular & Clean Code with Boolean Return Values

Separating game logic from input/output loops creates clean, testable, and maintainable code.

### Takeaway 2.1: Function Decoupling via `True` / `False` Signals

Instead of jamming input prompts, comparison logic, and loop management into a single giant block, delegate evaluation to a helper function (`generate` / `guess`).

- **Helper Function (`generate`):** Handles string printing (`Too small!`, `Too large!`, `Just right!`) and evaluates the state. It returns `True` if the game is over (correct guess) and `False` otherwise.
- **Main Caller (`main`):** Evaluates the returned boolean using an `if calling_function(): break` pattern to cleanly decide whether to reprompt or break out of the loop.

```python
def generate(answer, guess):
    if guess < answer:
        print("Too small!")
        return False
    elif guess == answer:
        print("Just right!")
        return True
    else:
        print("Too large!")
        return False
```

---

## Summary Checklist for Input-Driven Loops

1. Identify the **exact single condition** that should end the loop.
2. Use `continue` for error handling, string parsing failures (`ValueError`), and invalid ranges (`x <= 0`).
3. Leverage **Boolean helper functions** to pass state back to the caller instead of mixing control flow with function logic.
