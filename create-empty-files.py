from pathlib import Path

from utils import rm

root = Path('files/')
rm.rmall(root)
root.mkdir()
for i in range(10, 21):
    filename = str(i) + '.txt'
    filepath = root / Path(filename)
    print(filepath)
    filepath.touch()
