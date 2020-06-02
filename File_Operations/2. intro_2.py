import os

path = '/Users/moinm/Desktop/GitHub/Core_Python_PyCharm/File_Operations/videos'

os.chdir(path)

for file in os.listdir():
    f_name, f_ext = os.path.splitext(file)
    print(file.split())
    #print()
    #print(os.path.splitext(file))
