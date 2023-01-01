from pathlib import Path

from utils import rm, fakedata

here = Path()

root_dir = Path('files/')

# remove files/
rm.rmall(root_dir)

# prepare data for files creation
file_list = [
    dict(folder='november', name='abc.txt', content='abc content'),
    dict(folder='november', name='def.txt', content='def content'),
    dict(folder='december', name='ghi.txt', content='ghi content'),
    dict(folder='december', name='jkl.txt', content='jkl content'),
]

# create dirs and files
fakedata.create_tree(root_dir, file_list)


pattern = '**/*'
file_paths = root_dir.glob(pattern)
for path in file_paths:
    if path.is_file():
        parent_folder = path.parts[-2]
        new_filename = parent_folder + '-' + path.name
        new_path = path.with_name(new_filename)
        print(new_path)
        path.rename(new_path)
