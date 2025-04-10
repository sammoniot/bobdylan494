import os
import re

root_dir = '../lyrics-txt'
regex = r'\[.+?\]'
ignore_case = False
compiled_pattern = re.compile( r'\[.+?\]')
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.lower().endswith('.txt'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
                if not compiled_pattern.search(text):
                    print(f"Pattern not found: {file_path}")
                