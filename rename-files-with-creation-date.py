from pathlib import Path
from datetime import datetime as dt

from utils import rm, fakedata

here = Path()

root_dir = Path('files/')

# remove files/
rm.rmall(root_dir)

# prepare data for files creation
file_list = fakedata.load_data('data/rename-files-with-sub-folders.csv')
print(file_list)
# create dirs and files
fakedata.create_tree(root_dir, file_list)

pattern = '**/*'
file_paths = root_dir.glob(pattern)
for path in file_paths:
    if path.is_file():
        stats = path.stat()
        # for key in dir(stats):
        #     if key.startswith('st_'):
        #         val = getattr(stats, key)
        #         print(key, val, type(val))
        ctime = stats.st_ctime
        timestamp = dt.fromtimestamp(ctime)
        date_creation = timestamp.strftime('%Y-%m-%d_%H-%M-%S')
        new_name = date_creation + '-' + path.name
        date_path = path.with_name(new_name)
        path.rename(date_path)
