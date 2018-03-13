import sunau
import os
import numpy as np
import csv


import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig = plt.figure()

path = "reggae/"

infiles = os.listdir("./au/"+path) #get file list

for file in infiles:
    print file
    
    wave_file = sunau.open("./au/"+path+file,"r") #open file
    
    nchannles = wave_file.getnchannels()
    framerate = wave_file.getframerate()
    mfr = wave_file.getnframes()
    samplewidth = wave_file.getsampwidth()
    print nchannles
    print framerate
    print mfr
    print samplewidth
    
    """convert csv"""
    red = 100
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
        oa.append(data[0])
        wave_file.setpos(fr*red)
    
    print str(len(oa))
    
    opcsv = open(('./output/'+path+file).rstrip('.au')+'.txt', 'w')
    
    writer = csv.writer(opcsv, lineterminator='\n')
    
    writer.writerow(oa)
    opcsv.close()
    
    plt.clf()
    plt.plot(oa)
    plt.savefig(('./output/'+path+file).rstrip('.au')+'.png')