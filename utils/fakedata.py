from pathlib import Path


def create_tree(root_dir='files/'):
    # create files/
    files = Path(root_dir)
    print(f'createtree | mkdir {root_dir}')
    files.mkdir(exist_ok=True)

    # prepare data for files creation
    file_list = [
        dict(folder='november', name='abc.txt', content='abc content'),
        dict(folder='november', name='def.txt', content='def content'),
        dict(folder='december', name='ghi.txt', content='ghi content'),
        dict(folder='december', name='jkl.txt', content='jkl content'),
    ]

    # create subdirs and text files and write content
    for file in file_list:
        subdir = Path(files, file['folder'])

        print(f'createtree | mkdir {subdir}')
        subdir.mkdir(exist_ok=True)
        path = Path(subdir, file['name'])
        print(f'createtree | create file  {path}')
        path.write_text(file['content'])
