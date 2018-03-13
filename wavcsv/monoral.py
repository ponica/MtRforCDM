import wave
import os
import numpy as np
import csv

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig = plt.figure()

infiles = os.listdir("./wav/") #get file list

for file in infiles:
    print file
    
    wave_file = wave.open("./wav/"+file,"r") #open file
    
    nchannles = wave_file.getnchannels()
    framerate = wave_file.getframerate()
    mfr = wave_file.getnframes()
    samplewidth = wave_file.getsampwidth()
    print nchannles
    print framerate
    print mfr
    print samplewidth
    
    """original wave graph output"""
    
    fr = 0
    oa=[]
    
    for fr in range(mfr):
        b = wave_file.readframes(1)
        if samplewidth == 2:
            data = np.frombuffer(b, dtype='int16')
        elif samplewidth == 4:
            data = np.frombuffer(b, dtype='int32')
        if nchannles == 2:
            l_channel = data[::nchannles]
            r_channel = data[1::nchannles]
        bx = l_channel[0]
        oa.append(bx)
        wave_file.setpos(fr)
    
    plt.clf()
    plt.plot(oa)
    plt.savefig(('./output/'+file).rstrip('.wav')+'-original.png')
    
    
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
        bx = l_channel[0]
        oa.append(bx)
        wave_file.setpos(fr*red)
    
    print str(len(oa))
    
    opcsv = open(('./output/'+file).rstrip('.wav')+'.csv', 'w')
    
    writer = csv.writer(opcsv, lineterminator='\n')
    
    writer.writerow(oa)
    opcsv.close()
    
    """graph output"""
    
    plt.clf()
    plt.plot(oa)
    plt.savefig(('./output/'+file).rstrip('.wav')+'.png')