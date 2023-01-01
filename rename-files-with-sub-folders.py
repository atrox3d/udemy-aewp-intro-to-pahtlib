from pathlib import Path

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
        print(path)
        parent_folder = path.parts[-3] + '-' + path.parts[-2]
        print(parent_folder)
        new_filename = parent_folder + '-' + path.name
        new_path = path.with_name(new_filename)
        print(new_path)
        path.rename(new_path)
