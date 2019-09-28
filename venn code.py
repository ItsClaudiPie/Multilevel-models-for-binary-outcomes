# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 18:00:12 2019

@author: User
"""

import pandas as pd
from matplotlib import pyplot as plt
from venn import venn
import numpy as np

data = pd.read_csv('/users/carel17/Downloads/timss.csv')
data = data[['IDSCHOOL', 'C_LAB', 'C_AREA', 'C_DISADV', 'eq', 'dq']]

data = data.groupby('IDSCHOOL').max()

data_dict = {'Labs': set(np.where(data.C_LAB > 0)[0].tolist()),
             'City': set(np.where(data.C_AREA > 0)[0].tolist()),
             'Privileged': set(np.where(data.C_DISADV == 0)[0].tolist()),
             'Emphasis on\nacademics': set(np.where(data['eq'] > 0)[0].tolist()),
             'Disciplined': set(np.where(data.dq > 0)[0].tolist())}

venn(data_dict)
plt.title('Second level school variables.')
plt.savefig('/users/carel17/Downloads/venn.png')