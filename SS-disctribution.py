# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 



SS = pd.read_excel('SS.xlsx')

#-----------------------------------------------------
#edgecolor='black'--> board color of the bar  
# linewidth=1.2 --> size of the linewidth around the bar 
SS.hist( bins='auto', color='steelblue',alpha = 1, rwidth=1,edgecolor='black', linewidth=1)

#-----------------------------------------------------
#Title Font 
plt.title('Subthreshold Slope', fontsize = 20)
#label of y-axis 
plt.ylabel('Counts',fontsize = 20)
#label of x-axis 

plt.xlabel(r'$SS(\frac{V}{dec})$',fontsize = 20)



#plt.txt('\u03BC')

#-------------- x-axis 
plt.xticks(fontsize=18)
plt.xticks(np.arange(0,6, 1)) 
#--------------The y-axis range from 0 to 15 with 2 spacing 
plt.yticks(np.arange(1, 14, 2))
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


