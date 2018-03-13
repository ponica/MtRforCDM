#coding=utf-8
import pretty_midi
import csv
import numpy as np
import os

#ファンクション準備

#tonal-centroid-representation
def tonalc(a):
    b = np.array([0,0,0,0,0,0])
    al = np.linalg.norm(a,1)
    for p in range(len(a)):
        c = np.array([np.sin(p*7*np.pi/6),np.cos(p*7*np.pi/6),np.sin(p*3*np.pi/2),np.cos(p*3*np.pi/2),np.sin(p*2*np.pi/3)/2,np.cos(p*2*np.pi/3)/2])
        d = a[p] * c
        b = b + d
    b = b/al
    return b

#1オクターブに重ねたあと6bit列に変換（Tonal Centroid Representation）

def tconeoround(data):
    output = [0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(128):
        output[i % 12] += (data[i]) #全てオクターブにおける音階成分を一つのオクターブに重ねている
    output = np.array(output) #numpyで扱える行列に変換
    tcoutput = []
    output = output.T
    for t in range(len(output)):
        suzi = tonalc(output[t])
        bina = []
        for o in range(6):
            if(suzi[o]<0):
                bina.append(0)
            else:
                bina.append(1)
        tcoutput.append(bina)
    tcoutput = np.array(tcoutput)
    tcoutput = tcoutput.astype(int) #int型にしておく
    return tcoutput

#TCR用getpianoroll
def tcgetpianoroll(midi):
    data = midi_data.get_piano_roll(50)
    ooct = tconeoround(data)
    op = []
    
    for i in range(len(ooct)):
        o = 0
        for j in range(len(ooct[3])):
            o += ooct[i][j] * (2 ** j)
        op.append(o)
    return op

#1オクターブに重ねる
def oneoround(data):
    output = [0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(128):
        output[i % 12] += (data[i]/1000000000000) #全てオクターブにおける音階成分の合計が1以上にならないように重ねている
    output = np.array(output) #numpyで扱える行列に変換
    output = np.ceil( output ) #ここで繰り上げをして0ではない1未満の要素成分を持つ音階をすべて1にしている
    output = output.astype(int) #int型にしておく
    return output

#単位時間ごとにピアノロールを取得し、音階成分の有無を1オクターブに重ねたあとそれを2進数の数字として扱わせる
def getpianoroll(midi):
    data = midi_data.get_piano_roll(50)
    ooct = oneoround(data)
    ooct = ooct.T
    op = []
    
    for i in range(len(ooct)):
        o = 0
        for j in range(len(ooct[3])):
            o += ooct[i][j] * (2 ** j)
        op.append(o)
    return op

#引数のパス以下のファイルリスト生成
def getfilelist(path):
    root_dir = path
    target_files = []
    for root, dirs, files in os.walk(root_dir):
        targets = [os.path.join(root, f) for f in files]
        target_files.extend(targets)
    return target_files

#txtファイルとして出力
def writetxt(path,data):
    path = path.lstrip('./')
    tgtdir = "./output/1oct/"+os.path.split(path)[0]
    if not(os.path.isdir(tgtdir)):
        os.makedirs(tgtdir.lstrip('./'))
    with open('./output/1oct/'+path.rstrip('.mid')+'.txt', 'wt') as f:
        writer = csv.writer(f,lineterminator='\n')
        writer.writerows([data])
        

def tcwritetxt(path,data):
    path = path.lstrip('./')
    tgtdir = "./output/tcr/"+os.path.split(path)[0]
    if not(os.path.isdir(tgtdir)):
        os.makedirs(tgtdir.lstrip('./'))
    with open('./output/tcr/'+path.rstrip('.mid')+'.txt', 'wt') as f:
        writer = csv.writer(f,lineterminator='\n')
        writer.writerows([data])

"""main"""

tgtpath = "./midi/"
filelist = getfilelist(tgtpath)
i=0
for datapath in filelist:
    print "[File]"+datapath
    midi_data = pretty_midi.PrettyMIDI(datapath)
    pianoroll = getpianoroll(midi_data)
    writetxt(datapath,pianoroll)
    pianoroll = tcgetpianoroll(midi_data)
    tcwritetxt(datapath,pianoroll)
    i=i+1
    print "done convert\n"+"[Progress]"+str(i)+"/"+str(len(filelist))+"\n"



"""
#oneoround関数のテスト用
midi_data=pretty_midi.PrettyMIDI(filelist[1])
data = midi_data.get_piano_roll(50)
ooct = oneoround(data)
ooct = ooct.T
writetxt("./hoge.mid",ooct)
"""