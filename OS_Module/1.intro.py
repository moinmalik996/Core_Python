import os
from datetime import datetime

github_path = '/users/moinm/Desktop/GitHub/'

print("\n", os.getcwd())  # cwd = current working directory
os.chdir(github_path)
print("\n", os.getcwd())

for dirpath, dirname, filenames in os.walk(github_path):
    print('Directory Path     :  ', dirpath)
    print('Directory Name     :  ', dirname)
    print('Files in Directory :  ', filenames)
    print()

# os.mkdir('New Folder/')                   # make the directory
# os.makedirs('New Folder 2/Subfolder')

# os.rmdir('New Folder')                   # remove the directory
# os.removedirs('New Folder 2/Subfolder')

# modtime = os.stat('demo.txt').st_mtime

# print(modtime)
# print(datetime.fromtimestamp(modtime))


# print("\n", os.getcwd())
# print(os.listdir())
