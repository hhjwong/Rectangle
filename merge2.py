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

grid=np.zeros((960,1230),dtype=int)
g_truth=np.zeros((960,1230),dtype=int)
for m in range (170,200):
    for n in range(330,960):
        g_truth[n,m]=200
for m in range (170,1230):
    for n in range(930,960):
        g_truth[n,m]=200
for m in range (1000,1230):
    for n in range(0,960):
        g_truth[n,m]=200
for m in range (170,1230):
    for n in range(0,30):
        g_truth[n,m]=200
for m in range (1130,1200):
    for n in range(30,330):
        g_truth[n,m]=200
for m in range (400,1200):
    for n in range(160,530):
        g_truth[n,m]=200
for m in range (200,270):
    for n in range(630,930):
        g_truth[n,m]=200
for m in range (400,500):
    for n in range(630,930):
        g_truth[n,m]=200
for m in range (700,800):
    for n in range(630,930):
        g_truth[n,m]=200
for m in range (1000,1100):
    for n in range(630,930):
        g_truth[n,m]=200

for m in range(0,1230):
    for n in range(0,960):
        if test1[n,m]=200 or test2[n,m]=200 or test3[n,m]=200 or test4[n,m]=200 or test5[n,m]=200:
            grid[n,m]=200

positive=0 #accessible
negative=0 # obstacles
true_positive=0
true_negative=0
for m in range(0,1230):
    for n in range(0,960):
        if m>170 or n<230:
            if g_truth[n,m]==200:
                negative+=1
                if grid[n,m]==0:
                    true_negative+=1
            if g_truth[n,m]==0:
                positive+=1
                if grid[n,m]==200:
                    true_positive+=1
                    
for m in range(0,170):
    for n in range(230,960):
        grid[n,m]=0

print("Accessible area accuracy: ",float(true_positive/positive))
print("Obstacle area accuracy: ",float(true_negative/negative))
print("Total accuracy: ",float((true_positive+true_negative)/(positive+negative)))
plt.imshow(grid,cmap='Blues',origin='lower')
np.save("result.npy",grid)
plt.show()
