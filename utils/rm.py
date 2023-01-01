from pathlib import Path


def rmtree(path_name):
    """deletes recursively the given path"""
    path = Path(path_name)
    print(f'rmtree | {path=}')

    if not path.is_dir():
        return

    for item in path.iterdir():
        if item.is_dir():
            print(f'rmtree | rmtree({item})')
            rmtree(item)
        else:
            print(f'rmtree | unlink {item}')
            item.unlink()

    print(f'rmtree | rmdir {path}')
    path.rmdir()


def rmall(pathname):
    path = Path(pathname)
    print(f'rmtree | {path=}')
    pattern = '**/*'
    print(f'rmtree | {pattern=}')

    file_paths = path.glob(pattern)
    files = [item for item in file_paths if item.is_file()]
    for f in files:
        print(f'rmtree | unlink {f}')
        f.unlink()

    file_paths = path.glob(pattern)
    dirs = [item for item in file_paths if item.is_dir()]
    dirs = sorted(dirs, key=lambda d: str(d.as_posix()).count('/'), reverse=True)
    for d in dirs:
        print(f'rmtree | rmdir {d}')
        d.rmdir()




if __name__ == '__main__':
    rmall('../files/')
