# CLI File Renamer Tool - Technical Learnings & Takeaways

## Takeaway 1: Path Resolution & Recursive Searching (`os.path.abspath` vs `Path.home().rglob()`)

- **Originally used code**:
  ```python
  path = os.path.abspath(sys.argv[1])
  p = Path(path)
  ```

  - **The Problem**: `os.path.abspath()` only appends the relative input string to your current working directory (e.g., if you are running the script from a `CLI` folder, it only looks inside that specific folder). It does **not** scan your entire system.
- **The Solution for Global Search**: To search outward from your user home directory rather than a fixed local path, we use `Path.home()` combined with `.rglob()`.
  - **Precise Solution Code**:
    ```python
    search_root = Path.home()
    for path in search_root.rglob("Cat memes"):
        if path.is_dir():
            target_path = path
    ```
  - **`Path.home()`**: A class method on the `Path` class that returns a `Path` object representing the current user's home directory (e.g., `/Users/judypoon`).
  - **`.rglob(pattern)`**: An instance method called on a `Path` object that recursively glob-searches all directories and subdirectories matching the given pattern (e.g., searching for a target folder across the whole user tree).

---

## Takeaway 2: Leveraging the `pathlib` Library for File System Operations

- **Precise code example**:
  ```python
  if p.is_dir():
      for file in p.iterdir():
          time_since_last_access = datetime.now() - datetime.fromtimestamp(file.stat().st_atime)
  ```
- **Key methods & attributes**:
  - **`path.is_dir()`**: Instance method that returns a boolean (`True` or `False`) checking whether the given path points to an existing directory, safely preventing crashes if the path is invalid.
  - **`path.iterdir()`**: Instance method that yields `Path` objects for each item (files and subfolders) contained inside that directory.
  - **`file.stat().st_atime`**: Accesses the file status via `.stat()` (which retrieves system-level metadata like access and modification times) and extracts `st_atime` (last access time timestamp).

---

## Takeaway 3: Manipulating Paths and Moving Files (`os.path` vs `pathlib` operators)

- **Precise code example**:
  ```python
  underscore = name.replace(' ', '_')
  archived = f'archived_{underscore}'
  new_path = file.parent / archived
  os.rename(file, new_path)
  ```
- **How path assembly works**:
  - **`file.parent`**: A `Path` attribute that extracts the directory path containing the file (everything _before_ the filename, e.g., if the file is `/Users/judypoon/Cat memes/photo.png`, `file.parent` evaluates to `/Users/judypoon/Cat memes`, preserving the target folder structure so it doesn't strip away `Cat memes`).
  - **Path Division Operator (`/`)**: `pathlib` allows you to use the `/` operator to cleanly join a parent path and a new file or folder name together (e.g., `file.parent / archived`), automatically handling correct slash separators across different operating systems.
  - **Prefixing strings**: `archived = f'archived_{underscore}'` places the `'archived_'` string directly at the front of the filename string.
  - **`os.rename(src, dst)`**: A module-level function from the `os` library used to physically move or rename a file from the source path (`file`) to the new destination path (`new_path`).

---

## Takeaway 4: Studying Documentation — Class Methods vs Module-Level Functions

- **Classes & Class Methods (`Class.method()`)**:
  - **Precise code example**:

    ```python
    from pathlib import Path
    from datetime import datetime

    search_root = Path.home()
    current_time = datetime.now()
    ```

  - **Explanation**: `Path.home()` and `datetime.now()` are **class methods** called directly on their respective classes (`Path` and `datetime`). In both cases, calling these class methods instantiates and returns an **object** (`search_root` is a `Path` object, and `current_time` is a `datetime` object) ready for subsequent instance method calls.

- **Module-Level Functions (`module.submodule.function()`)**:
  - **Precise code example**:

    ```python
    import os

    path = os.path.abspath(dir)
    os.rename(file, new_path)
    ```

  - **Explanation**: Unlike classes where methods construct objects, `os.path.abspath()` is structured where `os` is the imported module, `path` is a submodule/nested namespace inside it, and `abspath` is the standalone function being called directly on that namespace, rather than being a factory method attached to a class blueprint.
