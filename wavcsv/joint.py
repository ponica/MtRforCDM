import sunau
import os
import shutil
import numpy as np
import csv

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig = plt.figure()


def conv(dataset):
    
    infiles = os.listdir("./au/"+dataset) #get file list
    
    for file in infiles:
        
        wave_file = sunau.open("./au/"+dataset+file,"r") #open file
        
        nchannles = wave_file.getnchannels()
        framerate = wave_file.getframerate()
        mfr = wave_file.getnframes()
        samplewidth = wave_file.getsampwidth()
        
        red = 10
        fr = 0
        oa=[]
        
        """
        print nchannles
        print framerate
        print samplewidth
        """
        
        """convert csv"""
        """
        for fr in range(mfr/red):
            b = wave_file.readframes(1)
            if samplewidth == 2:
                data = np.frombuffer(b, dtype='int16')
            elif samplewidth == 4:
                data = np.frombuffer(b, dtype='int32')
            if nchannles == 2:
                l_channel = data[::nchannles]
                r_channel = data[1::nchannles]
            oa.append(data[0] + (2**((16*(samplewidth/2) - 1))) )
            wave_file.setpos(fr*red)
        
        opcsv = open(('./output/'+dataset+file).rstrip('.au')+'.csv', 'w')
        
        writer = csv.writer(opcsv, lineterminator='\n')
        
        writer.writerow(oa)
        opcsv.close()
        """
        
        """creat bytes"""
        fr = 0
        oa=[]
        for fr in range(mfr/red):
            b = wave_file.readframes(1)
            if samplewidth == 2:
                data = np.frombuffer(b, dtype='int16')
            elif samplewidth == 4:
                data = np.frombuffer(b, dtype='int32')
            if nchannles == 2:
                l_channel = data[::nchannles]
                r_channel = data[1::nchannles]
            dsam = bin(data[0] + (2**((16*(samplewidth/2) - 1))) )
            oa.append(dsam.replace('0b',''))
            wave_file.setpos(fr*red)
        
        
        opcsv = open(('./output/'+dataset+file).rstrip('.au')+'.txt', 'w')
        
        writer = csv.writer(opcsv, lineterminator='\n')
        
        output=[]
        output.append(''.join(oa))
        writer.writerow(output)
        opcsv.close()
        

path = "./au/"
files = os.listdir(path)
files_dir = [f for f in files if os.path.isdir(os.path.join(path, f))]
print(files_dir)    # ['dir1', 'dir2']
for dirs in files_dir:
    shutil.rmtree("./output/"+dirs)
    os.mkdir("./output/"+dirs)
    conv(dirs+"/")
    print "done covert : "+dirs
print("done.")