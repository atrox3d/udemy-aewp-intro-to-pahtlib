from pathlib import Path
import zipfile

root = Path('files/')
dest = root / 'destination/'
print(dest)
dest.mkdir(exist_ok=True)

for zip in root.rglob('*.zip'):
    with zipfile.ZipFile(zip, 'r') as zf:
        final_path = dest / zip.stem
        zf.extractall(path=final_path)

