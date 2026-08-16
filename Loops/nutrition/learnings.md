# Exercise 2.5: Nutrition Facts (nutrition.py)

## 📌 Task Description

Implement a program that prompts users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the FDA's poster.

- **Input Example:** `Apple` or `strawberries`
- **Output Example:** `Calories: 130` or `Calories: 50`
- **Rule:** Ignore any input that is not an accepted fruit listed in the FDA poster (print nothing).

---

## 💡 Core Logic & Algorithm Mechanism

To map fruits to their respective calorie values efficiently:

1. **Case Normalization:** Convert user input to lowercase using `.lower()` to ensure case-insensitive matching.
2. **Dictionary Lookup Structure:** Store fruit-to-calorie key-value pairs inside a Python dictionary (`fruits = {...}`).
3. **Key Extraction & Membership Check:**
   - Extract the keys of the dictionary using `fruits.keys()` and convert them into a list (`list(fruits.keys())`).
   - Check if the user's input `f` exists within the list of valid keys using the `in` operator.
4. **Access Value:** If found, retrieve and print the corresponding calorie count using dictionary key indexing `fruits[f]`.

---

## 💻 Implementation (Python)

```python
def main():
    # Prompt the user for a fruit name and convert it to lowercase for matching
    fruit_name = input('What fruit do you want to enquire? ').lower()
    check(fruit_name)

def check(f):
    # Dictionary storing the 20 fruits and their corresponding calorie values
    fruits = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        ...
    }

    # Extract all fruit keys into a list for lookup
    a = list(fruits.keys())

    # Check if the entered fruit exists in the list
    if f in a:
        # If found, print the corresponding calorie count
        print(f'Calories: {fruits[f]}')
    else:
        # If not found, ignore and print nothing
        print()

if __name__ == '__main__':
    main()
```

---

## 🛠️ Python Learnings & Gotchas

### 1. Extracting Dictionary Keys into a List (`list(dict.keys())`)

- **Where:** `a = list(fruits.keys())`
- **Technique:** Calling `.keys()` on a dictionary returns a `dict_keys` view object. Wrapping it with `list()` converts all keys into an explicit, iterable list.

### 2. Checking Item Membership in a List (`if f in a:`)

- **Where:** `if f in a:`
- **Technique:** Use the `in` operator to check whether an item exists inside a list before attempting to access its corresponding value in the dictionary, preventing potential `KeyError` exceptions.
- **Pro Tip:** In Python, I can actually check key existence directly on the dictionary using `if f in fruits:` without converting keys to a list first! Both approaches achieve the exact same result.
