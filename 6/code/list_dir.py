import os
root = '.'
# dirs are the directory list under dirpath
# files are the file list under dirpath
for dirpath, dirs, files in os.walk(root):
    for filename in files:
        fullpath = os.path.join(dirpath, filename)
        print fullpath
