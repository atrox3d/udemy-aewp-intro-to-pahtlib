from pathlib import Path
from utils import rm, fakedata

here = Path()

# cleanup files/ for this execution
rm.rmtree('files/')

# create files/ subdir
# files = Path('files')
# files.mkdir(exist_ok=True)

# prepare data for files creation
file_list = fakedata.load_data('rename-files.csv')
fakedata.create_tree('files/', file_list)

files = Path('files')

# create text files and write content
for file in file_list:
    path = Path(files, file['name'])
    path.write_text(file['content'])

# rename files
for file in files.iterdir():
    print(file)
    newname = f'renamed-{file.name}'
    newfile = file.with_name(newname)       # keep file's path while renaming
    print(f'renaming {file} to {newname}')
    file.rename(newfile)
