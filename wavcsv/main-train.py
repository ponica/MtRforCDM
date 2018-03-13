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
        print file
        
        wave_file = sunau.open("./au/"+dataset+file,"r") #open file
        
        nchannles = wave_file.getnchannels()
        framerate = wave_file.getframerate()
        mfr = wave_file.getnframes()
        samplewidth = wave_file.getsampwidth()
        
        """
        print nchannles
        print framerate
        print samplewidth
        """
        
        """convert csv"""
        fr = 0
        oa=[]
        
        for fr in range(mfr/10):
            b = wave_file.readframes(1)
            if samplewidth == 2:
                data = np.frombuffer(b, dtype='int16')
            elif samplewidth == 4:
                data = np.frombuffer(b, dtype='int32')
            if nchannles == 2:
                l_channel = data[::nchannles]
                r_channel = data[1::nchannles]
            oa.append(abs(data[0]))
            wave_file.setpos(fr*10)
        
        plt.clf()
        plt.plot(oa)
        plt.savefig(('./output/'+dataset+file).rstrip('.au')+'-10'+'.png')
        
        red = 100
        dsrate = 256
        fr = 0
        oa=[]
        
        """csv file output. if you need csv, you can get csv that coment out"""
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
            oa.append(abs(data[0]//256))
            wave_file.setpos(fr*red)
        
        print str(len(oa))
        
        opcsv = open(('./output/'+dataset+file).rstrip('.au')+'.txt', 'w')
        
        writer = csv.writer(opcsv, lineterminator='\n')
        
        writer.writerow(oa)
        opcsv.close()
        
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
            oa.append(data[0]//256)
            wave_file.setpos(fr*red)
        
        plt.clf()
        plt.plot(oa)
        plt.savefig(('./output/'+dataset+file).rstrip('.au')+'.png')

path = "./au/"
files = os.listdir(path)
files_dir = [f for f in files if os.path.isdir(os.path.join(path, f))]
print(files_dir)    # ['dir1', 'dir2']
for dirs in files_dir:
    shutil.rmtree("./output/"+dirs)
    os.mkdir("./output/"+dirs)
    print "done mkdir : "+dirs
    conv(dirs+"/")
