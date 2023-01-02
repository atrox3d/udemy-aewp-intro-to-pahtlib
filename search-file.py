from pathlib import Path


search_term = 'files'
pattern = f'**/*{search_term}*'
root = Path()

files = root.glob(pattern)
for file in files:
    # if not str(file).startswith(('.idea', 'venv')):
    if file.parts[0] not in ['venv', '.idea']:
        print(file.absolute())

