
"""
Python Automation Template
--------------------------
Use this structure for any script:
1. Setup / Imports
2. Input (file paths, user settings)
3. Processing Logic
4. Output (print, save, rename)
"""

# 1. Setup / Imports
import csv
import os
import itertools
from datetime import datetime

# 2. Input
file_path = 'your_file.csv'  # Example input file
folder_path = 'your_folder'  # Example folder for renaming

# 3. Processing Logic
# Example: Read CSV header and count rows
with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    num_cols = len(header)
    row_count = 0
    for row in reader:
        row_count += 1

# Example: Rename files in folder
date_prefix = datetime.now().strftime('%Y-%m-%d')
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        old_path = os.path.join(folder_path, filename)
        new_filename = f"{date_prefix}_{filename}"
        new_path = os.path.join(folder_path, new_filename)
        os.rename(old_path, new_path)

# 4. Output
print("✅ CSV Summary")
print(f"Rows: {row_count}, Columns: {num_cols}")
print("✅ Files renamed successfully!")
