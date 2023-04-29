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

grid=np.zeros((2240,1150),dtype=int)
g_truth=np.zeros((2240,1150),dtype=int)
for m in range (440,480):
    for n in range(570,600):
        g_truth[n,m]=200
for m in range (350,440):
    for n in range(570,1200):
        g_truth[n,m]=200
for m in range (300,350):
    for n in range(570,600):
        g_truth[n,m]=200
for m in range (0,300):
    for n in range(570,600):
        g_truth[n,m]=200
for m in range (0,30):
    for n in range(600,2240):#5
        g_truth[n,m]=200
for m in range (30,230):
    for n in range(750,850):
        g_truth[n,m]=200
for m in range (230,270):
    for n in range(750,780):
        g_truth[n,m]=200
for m in range (30,90):
    for n in range(1110,1170):
        g_truth[n,m]=200
for m in range (30,270):
    for n in range(1170,1200):
        g_truth[n,m]=200
for m in range (30,180):#10
    for n in range(1300,1390):
        g_truth[n,m]=200
for m in range (180,270):
    for n in range(1300,1330):
        g_truth[n,m]=200
for m in range (30,100):
    for n in range(1500,2040):
        g_truth[n,m]=200
for m in range (100,380):
    for n in range(1650,1680):
        g_truth[n,m]=200
for m in range (350,380):
    for n in range(1300,1650):
        g_truth[n,m]=200
for m in range (100,380):#15
    for n in range(1960,1990):
        g_truth[n,m]=200
for m in range (350,380):
    for n in range(1760,1960):
        g_truth[n,m]=200        
for m in range (380,550):
    for n in range(1910,1940):
        g_truth[n,m]=200
for m in range (30,350):
    for n in range(2210,2240):
        g_truth[n,m]=200
for m in range (350,380):
    for n in range(2070,2240):
        g_truth[n,m]=200
for m in range (380,1150):#20
    for n in range(2140,2240):
        g_truth[n,m]=200
for m in range (1050,1150):
    for n in range(1510,2240):
        g_truth[n,m]=200
for m in range (630,1050):
    for n in range(1910,1940):
        g_truth[n,m]=200
for m in range (830,930):
    for n in range(1610,1810):
        g_truth[n,m]=200
for m in range (780,1150):
    for n in range(1480,1510):
        g_truth[n,m]=200
for m in range (1120,1150):
    for n in range(1530,1480):#25
        g_truth[n,m]=200
for m in range (780,810):
    for n in range(1380,1400):
        g_truth[n,m]=200
for m in range (780,860):
    for n in range(1330,1380):
        g_truth[n,m]=200
for m in range (780,1150):
    for n in range(1230,1330):
        g_truth[n,m]=200
for m in range (810,1120):
    for n in range(930,960):
        g_truth[n,m]=200
for m in range (1120,1150):#30
    for n in range(930,1480):
        g_truth[n,m]=200
for m in range (780,810):
    for n in range(600,1000):
        g_truth[n,m]=200
for m in range (680,810):
    for n in range(570,600):
        g_truth[n,m]=200
for m in range (980,1040):
    for n in range(960,1110):
        g_truth[n,m]=200
for m in range (580,650):
    for n in range(800,950):
        g_truth[n,m]=200


positive=0 #accessible
negative=0 # obstacles
true_positive=0
true_negative=0
for m in range(0,1150):
    for n in range(0,2240):
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
np.save("grid.npy",grid)
#plt.scatter(all_loc[:,0]*100+380,all_loc[:,1]*100+600,color = 'green',s=1)
plt.show()
