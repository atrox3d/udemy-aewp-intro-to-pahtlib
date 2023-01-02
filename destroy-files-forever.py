from pathlib import Path

from utils import rm

rm.rmall('files/')
root = Path('files/')
root.mkdir()

for i in range(10, 21):
    file = root / Path(f'{i}.csv')
    file.write_text('csv file')

for file in root.glob('*.csv'):
    size = file.stat().st_size
    with open(file, 'wb') as f:
        f.write(b'\x00' * size)
    file.unlink()
