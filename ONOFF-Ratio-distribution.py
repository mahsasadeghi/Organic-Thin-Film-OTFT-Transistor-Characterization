#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:09:20 2019

@author: mahsasadeghi
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 



SS = pd.read_excel('ONOFF-Ratio.xlsx')

#-----------------------------------------------------
#edgecolor='black'--> board color of the bar  
# linewidth=1.2 --> size of the linewidth around the bar 
SS.hist( bins='auto', color='gold',alpha = 1, rwidth=1,edgecolor='black', linewidth=1)

#-----------------------------------------------------
#Title Font 
plt.title('ON‐OFF ratio', fontsize = 20)
#label of y-axis 
plt.ylabel('Counts',fontsize = 20)
#label of x-axis 

plt.xlabel(r'$Log(\frac{I_{ON}}{I_{OFF}})$',fontsize = 20)



#plt.txt('\u03BC')

#-------------- x-axis 
plt.xticks(fontsize=18)
plt.xticks(np.arange(0,9, 1)) 
#--------------The y-axis range from 0 to 15 with 2 spacing 
plt.yticks(np.arange(1, 18, 2))
plt.yticks(fontsize=18)
#plt.tick_params(axis="y",direction="in", pad=-22)
plt.tick_params(axis="y",direction="in")



plt.grid(b=None)
plt.savefig('ONOFF-Ratio.png', transparent = True, bbox_inches = 'tight')
plt.savefig('ONOFF-Ratio.eps', transparent = True, bbox_inches = 'tight')
plt.show()

#plt.savefig('destination_path.eps', format='eps')




"""
y-axis limit 
#plt.ylim(0, 11)
#x-axis limit
plt.xlim(0, 3)
"""















"""
import matplotlib.pyplot as plt
import pandas
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)
data.hist()
plt.show()


"""


