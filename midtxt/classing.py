import os
import shutil
import random

def getfile(directory,count):
    outd = "./classing/"+directory.lstrip("./output/")
    if not(os.path.exists(outd)):
        os.makedirs(outd)
        os.makedirs("./classing/tcr/"+outd.lstrip("./classing/1oct/"))
        os.makedirs("./classing/combine/1oct/"+outd.lstrip("./classing/1oct/"))
        os.makedirs("./classing/combine/tcr/"+outd.lstrip("./classing/1oct/"))
    else:
        shutil.rmtree(outd)
        shutil.rmtree("./classing/tcr/"+outd.lstrip("./classing/1oct/"))
        shutil.rmtree("./classing/combine/1oct/"+outd.lstrip("./classing/1oct/"))
        shutil.rmtree("./classing/combine/tcr/"+outd.lstrip("./classing/1oct/"))
        os.makedirs(outd)
        os.makedirs("./classing/tcr/"+outd.lstrip("./classing/1oct/"))
        os.makedirs("./classing/combine/1oct/"+outd.lstrip("./classing/1oct/"))
        os.makedirs("./classing/combine/tcr/"+outd.lstrip("./classing/1oct/"))
    files = os.listdir(directory)
    random.shuffle(files)
    print files
    for c in files[0:count]:
        shutil.copy(directory+"/"+c,outd+"/"+c)
        shutil.copy("./output/tcr/"+directory.lstrip("./output/1oct/")+"/"+c,"./classing/tcr/"+outd.lstrip("./classing/1oct/")+"/"+c)
        shutil.copy("./output.combine/1oct/"+directory.lstrip("./output/1oct/")+"/"+c,"./classing/combine/1oct/"+outd.lstrip("./classing/1oct/")+"/"+c)
        shutil.copy("./output.combine/tcr/"+directory.lstrip("./output/1oct/")+"/"+c,"./classing/combine/tcr/"+outd.lstrip("./classing/1oct/")+"/"+c)
    print "done classing:"+directory
    
path = "./output/1oct/midi/"
dirs = os.listdir(path)
all_dir = [f for f in dirs if os.path.isdir(os.path.join(path, f))]
print(all_dir)
for d in all_dir:
    getfile(path+d,100)