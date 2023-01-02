import zipfile
from pathlib import Path

from utils import rm


def create_files(root):
    rm.rmall(root)
    root.mkdir()
    for i in range(10, 21):
        filename = str(i) + '.txt'
        filepath = root / Path(filename)    # calls __truediv__
        print(filepath)
        filepath.touch()


root = Path('files/')
create_files(root)
archive_path = root / Path('archive.zip')
print(archive_path)

with zipfile.ZipFile(archive_path, 'w') as zf:
    for path in root.rglob('*.txt'):
        zf.write(path)
        # path.unlink()
