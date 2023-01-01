from pathlib import Path


def create_tree(root_dir='files/', file_list=[]):
    # create files/
    files = Path(root_dir)
    print(f'createtree | mkdir {root_dir}')
    files.mkdir(exist_ok=True)

    # create subdirs and text files and write content
    for file in file_list:
        if 'folder' in file.keys():
            subdir = Path(files, file['folder'])
            print(f'createtree | mkdir {subdir}')
            subdir.mkdir(exist_ok=True)
        else:
            subdir = Path(files)

        path = Path(subdir, file['name'])
        print(f'createtree | create file  {path}')
        path.write_text(file['content'])
