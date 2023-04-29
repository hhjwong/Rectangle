import numpy as np
from matplotlib import pyplot as plt
import math 
from math import sqrt
import random
import array as arr
from matplotlib.patches import Rectangle
import pylab as pl
from matplotlib import collections  as mc
from numpy import sin, cos, pi, linspace
from datetime import datetime

test1=np.load("track1.npy")
test2=np.load("track2.npy")
test3=np.load("track3.npy")
test4=np.load("track4.npy")
test5=np.load("track5.npy")

grid=np.zeros((890,1340),dtype=int)
g_truth=np.zeros((890,1340),dtype=int)
for m in range (0,30):
    for n in range(0,890):
        g_truth[n,m]=200
for m in range (0,1340):
    for n in range(0,30):
        g_truth[n,m]=200
for m in range (230,260):
    for n in range(230,890):
        g_truth[n,m]=200
for m in range (230,1030):
    for n in range(230,260):
        g_truth[n,m]=200
for m in range (230,1240):
    for n in range(860,890):
        g_truth[n,m]=200
for m in range (1240,1340):
    for n in range(760,890):
        g_truth[n,m]=200
for m in range (1310,1340):
    for n in range(230,760):
        g_truth[n,m]=200
for m in range (1110,1340):
    for n in range(230,260):
        g_truth[n,m]=200
for m in range (480,980):
    for n in range(430,480):
        g_truth[n,m]=200
for m in range (480,980):
    for n in range(580,630):
        g_truth[n,m]=200
for m in range (480,980):
    for n in range(730,780):
        g_truth[n,m]=200
for m in range (980,1030):
    for n in range(430,780):
        g_truth[n,m]=200

for m in range(0,1340):
    for n in range(0,890):
        if test1[n,m]=200 or test2[n,m]=200 or test3[n,m]=200 or test4[n,m]=200 or test5[n,m]=200:
            grid[n,m]=200

positive=0 #accessible
negative=0 # obstacles
true_positive=0
true_negative=0
for m in range(0,1340):
    for n in range(0,890):
        if g_truth[n,m]==200:
            negative+=1
            if grid[n,m]==0:
                true_negative+=1
        if g_truth[n,m]==0:
            positive+=1
            if grid[n,m]==200:
                true_positive+=1
print("Accessible area accuracy: ",float(true_positive/positive))
print("Obstacle area accuracy: ",float(true_negative/negative))
print("Total accuracy: ",float((true_positive+true_negative)/(positive+negative)))
plt.imshow(grid,cmap='Blues',origin='lower')
np.save("result.npy",grid)
plt.show()

