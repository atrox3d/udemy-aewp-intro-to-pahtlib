from pathlib import Path

here = Path()

# create files/ subdir
files = Path('files')
files.mkdir(exist_ok=True)

# cleanup files/ for this execution
for file in files.iterdir():
    file.unlink(missing_ok=True)

# prepare data for files creation
file_list = [
    dict(name='abc.txt', content='abc content'),
    dict(name='def.txt', content='def content'),
    dict(name='ghi.txt', content='ghi content'),
]

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
