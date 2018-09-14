# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 08:41:07 2018

@author: StrongPria
https://plot.ly/matplotlib/bar-charts/
"""

import random
import numpy as np
import matplotlib.pyplot as plt

def plotData(plt, data):
  x = [p[0] for p in data]
  y = [p[1] for p in data]
  plt.plot(x, y, '-o')

maxNum = 100
  
ans = np.zeros((maxNum))
x = range(maxNum)

for i in range(10000):
    num_r = random.randint(0,maxNum-1)
    ans[num_r] += 1

#plt.hist(ans)
plt.bar(x, ans)#, 0.8, 0)
plt.show()