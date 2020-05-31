import os

desktop_path = '/users/moinm/Desktop/'

os.chdir(desktop_path)

path = os.path.split('/Github/mytext.txt')
path_exists = os.path.exists('/Github/mytext.txt')
directory_exists = os.path.isdir('/Github/mytext.txt')     # check if directory exists
file_exists = os.path.isfile('/Github/mytext.txt')         # check if file exists
file_extension = os.path.splitext('/Github/mytext.txt')    # split file and its extension

print(path)
print("Path Exists  :  ", path_exists)