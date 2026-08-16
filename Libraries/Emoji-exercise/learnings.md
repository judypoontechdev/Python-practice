# Emoji Exercise - Learnings

## Overview

The goal of this exercise is to use the external library `emoji` to convert text strings into actual emojis. During this exercise, I have mainly strengthened my usage of the terminal for setting up a virtual environment. Key commands and explanations include:

1. **`python3 -m venv venv`**
   - _Purpose:_ Creates a local virtual environment folder (`venv`) to sandbox project dependencies and avoid global package conflicts.

2. **`source venv/bin/activate`**
   - _Purpose:_ Activates the virtual environment on macOS. Directs all terminal commands and package installations exclusively to the local sandbox, indicated by the `(venv)` prompt.

3. **`pip install emoji`**
   - _Purpose:_ Installs the external Python library directly into the active virtual environment.

4. **`pip list`**
   - _Purpose:_ Outputs installed packages in the current environment to verify successful installation and confirm isolation from the global system.

5. **`python3 -m pip install --upgrade pip`**
   - _Purpose:_ Updates the internal package installer within the virtual environment to its latest stable release.
