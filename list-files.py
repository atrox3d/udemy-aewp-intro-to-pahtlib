from pathlib import Path

# get relative and abolute Path objects for current directory
relative_cwd = Path()
absolute_cwd = Path.cwd()
print(f'{relative_cwd = }')
print(f'{absolute_cwd = }')

# get list of current directory items, adding trailing slash to subdirs
files_str = [f'{path}/' if path.is_dir() else str(path) for path in relative_cwd.iterdir()]
print(files_str)

# get list of subdirs items, adding trailing slash to subdirs
files_glob = [f'{path.as_posix()}/' if path.is_dir() else str(path.as_posix()) for path in relative_cwd.glob('*/*')]
print(list(files_glob))
