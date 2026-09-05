# This CLI tool is a file renamer.  There are several functions:
# 1. For files that haven't been opened for 30 days, add 'archived_' in the start of the file name
# 2. Clean files: substitute white spaces with _

import os
import sys
from pathlib import Path
from datetime import datetime

# Let user input folder name
search_root = Path.home()
target_dir = sys.argv[1]

# Check whether dry-run mode is being activated
is_dry = '--dry' in sys.argv

# Get absolute path from relative path
# path = os.path.abspath(dir)
# p = Path(path)

# Check whether it is really a folder
try:
    for path in search_root.rglob(target_dir):
        if path.is_dir():
            for file in path.iterdir():

                # Replace all empty spaces with underscore regardless of latest access time
                name = file.name
                underscore = name.replace(' ', '_')

                # Calculate days since file last access
                time_since_last_access = datetime.now() - datetime.fromtimestamp(file.stat().st_atime)
                days_since_last_access = time_since_last_access.days

                # Determine if last access has exceeded 30 days and if yes, add archived_ to the beginning of the filename
                if days_since_last_access > 30:
                    archived = f'archived_{underscore}'

                    new_path = file.parent / archived
                    os.rename(file, new_path)
                    
                else:
                    new_path = file.parent / underscore
                    os.rename(file, new_path)

                # Dry-run
                if is_dry:
                    print(f"[DRY RUN] Would rename: '{file.name}' -> '{new_path.name}' (Days inactive: {days_since_last_access})")
                else:
                    os.rename(file, new_path)
                    print(f"[SUCCESS] Renamed: '{file.name}' -> '{new_path.name}'")

except FileNotFoundError:
    raise FileNotFoundError('File not exists, please retype!')
