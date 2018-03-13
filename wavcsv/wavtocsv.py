import wave
import os
import numpy as np
import csv

ddic = "./wav/"

infiles = os.listdir(ddic) #get file list

for file in infiles:
    print file
    
    wave_file = wave.open(ddic+file,"r") #open file
    
    nchannles = wave_file.getnchannels()
    framerate = wave_file.getframerate()
    mfr = wave_file.getnframes()
    samplewidth = wave_file.getsampwidth()
    print nchannles
    print framerate
    print mfr
    print samplewidth
    
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
        oa.append(data)
        wave_file.setpos(fr*10)
    
    print str(len(oa))
    
    opcsv = open(('./output/'+file).rstrip('.wav')+'.csv', 'w')
    
    writer = csv.writer(opcsv, lineterminator='\n')
    
    writer.writerow(oa)
    opcsv.close()