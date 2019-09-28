# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 23:37:50 2019

@author: User
"""

import numpy as np
from matplotlib import pyplot as plt

alpha0 = -1.2396
beta = 0.08433
theta = -0.09382
gamma = 0.3285
ind = np.array([2, 195, 28, 247, 228, 273, 207, 280, 65, 286])
alpha = np.array([-0.4592, -0.1510, -0.5099, 3.2958, 3.3324, -0.1479,
                 -1.2065, 2.5265, -1.3220, -2.0291])

plt.figure(figsize=(5, 10))
for i, z in enumerate(range(2)):
  plt.subplot(2, 1, i + 1)

  x_range = np.arange(4.2, 13.9, 0.2)
  y_hat = (alpha0 + alpha).reshape(-1, 1) + (x_range * beta).reshape(1, -1)
  y_hat += z * gamma + (theta * z * x_range).reshape(1, -1)

  for i, a, y in zip(ind, alpha, y_hat):
    plt.plot(x_range, y, label='School %i: %.4f' % (i, a))

  plt.ylabel('TIMMS Maths Score', size=12)
  plt.xlabel('Home educational resources', size=12)
  plt.title('Model 3 (z = %i)' % z, size=12)
  plt.legend(bbox_to_anchor=(1, 1), fontsize=12)