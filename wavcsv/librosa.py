import sys
import librosa
import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig = plt.figure()

filename = "./mp3/blues/All_Men_Are_Dogs_-GIGOLETTE.mp3"

y,sr=librosa.load(filename)
print("loaded")
totaltime = len(y)/sr
time = np.arange(0, totaltime, 1/sr)
plt.clf()
plt.plot(time,y)
plt.savefig('./mp3/output/blues/All_Men_Are_Dogs_-GIGOLETTE.png')