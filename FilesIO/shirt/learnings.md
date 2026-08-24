# Learnings: CS50p Shirt Exercise & PIL/Pillow Concepts

Here are the key takeaways and technical learnings from working through the `shirt.py` exercise, structured in Markdown for your revision notes:

### 1. Class Methods (`Image.open`)

- **Why we use a class method for opening files:** For standard objects like a custom class, you might instantiate them directly (e.g., `Dog(name='cookie')`). However, for an image, simply passing a file path string as an attribute to a basic constructor is meaningless because the file hasn't been read or loaded into memory yet.
- **How `Image.open` works:** It acts as a class/factory method. Because we cannot instantiate an image object without first reading the file data, `Image.open()` bridges the gap by running the necessary file-loading logic inside the method and returning a fully instantiated `Image` object simultaneously.

### 2. Class Methods (`Image.open`) vs. Instance Methods (`paste`, `save`)

- **`Image.open` (Class/Factory Method):** Called directly on the class (`Image.open()`) without needing a pre-existing object. Its primary job is to create and return a new `Image` object and hence we need to assign the outcome to a variable.
- **`Image.paste` & `Image.save` (Instance Methods):** These require an existing `Image` object to call them (e.g., `cropped_image.paste(...)` or `cropped_image.save(...)`), as they **return `None`** rather than a new object, the pixel data of the object calling the method is being directly modified.
