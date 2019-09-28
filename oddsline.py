# -*- coding: utf-8 -*-
"""
Created on Wed May  8 22:05:03 2019

@author: User
"""

import pandas as pd
import matplotlib.pyplot as plt
from math import e

intercept = -0.6621
est = 0.2416
odds = list()


for i in range(3): 
    odds.append( e **(intercept + est*(i-2)))
    
actual_odds = [ 0.2 , 0.3  , 0.85]
 



x = [-1,0,1]

fig = plt.figure()
ax1 = fig.add_subplot(111)
plt.title('Estimating Odds Using a Slope in Multilevel Logistic Regression')

ax1.scatter(x, odds, s=10, c='b', marker="s", label='estimated odds')
ax1.scatter(x,actual_odds, s=10, c='r', marker="o", label='actual odds')
ax1.plot(x, odds)
ax1.plot(x,actual_odds)
plt.legend(loc='upper left');

plt.ylim(0, 2.5)
plt.xlabel("S_DEVICES")
plt.ylabel("Odds")
plt.savefig(r'C:\Users\User\Desktop\oddsline.png')


plt.show()



