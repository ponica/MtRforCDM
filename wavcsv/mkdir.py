import os

path = "./au/"
files = os.listdir(path)
files_dir = [f for f in files if os.path.isdir(os.path.join(path, f))]
print(files_dir)    # ['dir1', 'dir2']
for dirs in files_dir:
    os.mkdir("./output/"+dirs)
    print "done mkdir : "+dirs