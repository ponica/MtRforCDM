import sunau
import os
import shutil
import numpy as np
import csv

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig = plt.figure()

def getNearestValue(list, num):
    """
    概要: リストからある値に最も近い値を返却する関数
    @param list: データ配列
    @param num: 対象値
    @return 対象値に最も近い値
    """

    # リスト要素と対象値の差分を計算し最小値のインデックスを取得
    idx = np.abs(np.asarray(list) - num).argmin()
    return list[idx]

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
        print mfr
        print samplewidth
        """
        
        """convert csv"""
        red = 200
        fr = 0
        oa=[]
        wv = wave_file.readframes(mfr)
        data = np.frombuffer(wv, dtype = "int16")
        
        for fr in range(mfr/red):
            X = np.fft.fft(data[fr:fr+red])
            amp = [np.sqrt(c.real ** 2 + c.imag ** 2) for c in X]
            freqList = np.fft.fftfreq(red, d=1.0/framerate)
            fq = 0
            fqList = 0.0
            fqp = []
            print str(len(X))
            while (55*(2**(fqList/12))) < 1760:
        writer.writerow(oa)
                fqp.append(int( amp[ int(  ) ] )//200000)
                fqList = fqList+1
            oa.append(fqp)
            fr = fr+red
        
        print str(len(oa))
        
        opcsv = open(('./output/'+dataset+file).rstrip('.au')+'.txt', 'w')
        
        writer = csv.writer(opcsv, lineterminator='\n')
        
        writer.writerow(oa)
        opcsv.close()
        
        plt.clf()
        plt.plot(oa[0])
        plt.savefig(('./output/'+dataset+file).rstrip('.au')+'.png')

path = "./au/"
files = os.listdir(path)
files_dir = [f for f in files if os.path.isdir(os.path.join(path, f))]
print(files_dir)    # ['dir1', 'dir2']
for dirs in files_dir:
    shutil.rmtree("./output/"+dirs,1)
    os.mkdir("./output/"+dirs)
    print "done mkdir : "+dirs
    conv(dirs+"/")
