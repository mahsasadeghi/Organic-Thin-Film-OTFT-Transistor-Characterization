#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#https://towardsdatascience.com/data-visualization-with-mathplotlib-using-python-a7bfb4628ee3
"""
Created on Mon Nov 11 19:28:35 2019

@author: mahsasadeghi
"""
# Import the libraries
#mobility=[1.710085,1.622626,1.477711,1.480233,1.477355,1.208531,1.229979,1.451601,1.399425,1.374794,1.503946,1.243352,1.556422,1.543425,1.494459,1.567597,1.744750,1.732009,1.585177,1.512137,1.355291,1.397667,1.542083,1.671267,1.369877,1.444903,1.206239,1.632699,1.610921,1.775391,1.544811,1.468579,1.690042,1.605823,1.509143,1.485769,1.398878,1.761086,1.41238,1.537265]

import csv
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 


vthreshold = pd.read_excel('Vthresholdcopy.xlsx')
print(vthreshold)

#-----------------------------------------------------
#edgecolor='black'--> board color of the bar  
# linewidth=1.2 --> size of the linewidth around the bar 
vthreshold.hist( bins='auto', color='lightskyblue',alpha = 1, rwidth=1,edgecolor='black', linewidth=1)
#-----------------------------------------------------
#Title Font 
plt.title(r'$V_{threshold}$', fontsize = 20)
#label of y-axis 
plt.ylabel('Counts',fontsize = 20)
#label of x-axis 

plt.xlabel(r'$\mu(\frac{cm^2}{V.S})$',fontsize = 20)



#plt.txt('\u03BC')

#-------------- x-axis 
plt.xticks(fontsize=18)
plt.xticks(np.arange(-0.0001,0.0003,0.00004)) 
#--------------The y-axis range from 0 to 15 with 2 spacing 
plt.yticks(np.arange(1, 12, 2))
plt.yticks(fontsize=18)
#plt.tick_params(axis="y",direction="in", pad=-22)
plt.tick_params(axis="y",direction="in")



plt.grid(b=None)
plt.savefig('mobility.png', transparent = True, bbox_inches = 'tight')
plt.savefig('mobility.eps', transparent = True, bbox_inches = 'tight')
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



