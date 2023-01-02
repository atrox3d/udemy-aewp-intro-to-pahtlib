from pathlib import Path
from datetime import datetime as dt

from utils import rm, fakedata

here = Path()

root_dir = Path('files/')

# remove files/
rm.rmall(root_dir)

# prepare data for files creation
file_list = fakedata.load_data('data/change-file-extensions.csv')
# create dirs and files
fakedata.create_tree(root_dir, file_list)

pattern = '**/*'
file_paths = root_dir.glob(pattern)
for path in file_paths:
    if path.is_file():
        print(path.stem, path.suffix)
        new_path = path.with_suffix('.csv')
        path.rename(new_path)
