


"""
Mahsa Sadeghi Code 
OPT Characterizations-Device
"""

import csv
import matplotlib.pyplot as plt
from math import sqrt
import pandas as pd 
import pandas as pd1
#polyfit
import numpy as np
from matplotlib.font_manager import FontProperties
#-------------------Format of the y-axis for scientific notation--------------------------------------
import matplotlib.ticker as mticker

#------------------------------------------------------------------------------
Vg = [] 
Id4 = [] #Idrain for Vg = -4V 
Id8 = [] #Idrain for Vg = -8V 
Id12 = [] #Idrain for Vg = -12V 
Id16 = [] #Idrain for Vg = -16V 
Id20 = [] #Idrain for Vg = 20 V 
currents = [Id4, Id8, Id12, Id16, Id20]
#------------------------------------------------------------------------------
fields = [] 
rows = []
#------------------------------------------------------------------------------
with open('OPT-IdVd-Device1-Plotting.csv') as csvDataFile:
    #csv reader object
    csvReader = csv.reader(csvDataFile)
 
    # extracting field names through first row 
    #fields = next(csvReader) 
    # extracting each data row one by one 
    for row in csvReader: 
        rows.append(row) 
        
  
    # get total number of rows 
    #print("Total no. of rows: %d"%(csvReader.line_num)) 
#------------------------------------------------------------------------------    
#making the Vg column 
i = 0 

for i in range(len(rows)): 
    #a = rows[0][i]
    #print(a)
    if rows[i][0] == '\ufeff0': 
   
        rows[i][0] = 6
    Vg.append(float(rows[i][0]))
    i = i + 1 
#------------------------------------------------------------------------------
#making the Id4 column 


k = 0
j = 1
print(len(rows[0]))

while(j < 10): 
    print(j)
    i = 0 
    #a = rows[0][i]
    #print(a)
    for i in range(len(rows)):
        #devided to 10E-7 for the y-axis presentation 
        currents[k].append(abs(float(rows[i][j]))/(10E-7))
        i = i + 1
    j = j + 2
    k = k + 1
   
  
    
#print(Id20[15])
#------------------------------------------------------------------------------
print(len(Vg))
print(len(Id4))

# gca stands for 'get current axis'
ax = plt.gca()
#df = pd.DataFrame({'Vg':Vg,'Id': Id4})#df for dataframe

#df.plot.line(x = Vg,y = Id4)
#plt.xlabel('Vg')
#plt.ylabel('Id')
#plt.semilogy()
#--------------Plotting the Id4, Id8, Id12, Id16, Id20-------------------------

           
#plt.plot(Vg,Id4,linewidth = '4',color = 'Maroon',marker='o',markersize = '2')
plt.plot(Vg,Id4,color = 'Maroon',linewidth = '3',label = r'$V_G (V)=-4V$')
plt.plot(Vg,Id8,'gold',linewidth = '3',label = r'$V_G (V)=-8V$')
plt.plot(Vg,Id12,'limegreen',linewidth = '3',label = r'$V_G (V)=-12V$')
plt.plot(Vg,Id16,'dodgerblue',linewidth = '3',label = r'$V_G (V)=-16V$')
plt.plot(Vg,Id20,'Navy',linewidth = '3',label = r'$V_G (V)=-20V$')

#--------------xaxis limit of the IdVg figure---------------------------------
plt.xlim(-20,0) 
plt.xticks(np.arange(-20, 0.5, step=5))
#--------------y-axis limit of the IdVg figure---------------------------------
val = max(Id20)
#plt.ylim(0,max(Id20)+0.0000002) 
plt.ylim(0,6) 
#plt.xticks(np.arange(-20, 0.5, step=5))

#--------------yaxis limit of the IdVd figure---------------------------------
#plt.ylim()
#--------------x-axis and y-axis label ---------------------------------------
plt.xlabel(r'$V_G (V)$',fontsize = 20, fontname = 'arial')
#r'$\mu(\frac{cm^2}{V.S})$'
plt.ylabel(r'$I_D ({\mu}A)$',fontsize = 20,fontname = 'arial', labelpad = 15)
#--------------
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
#---------------------Scientific notation and power of the numbers in the y-axis
"""
class MathTextSciFormatter(mticker.Formatter):
    def __init__(self, fmt="%1.2e"):
        self.fmt = fmt
    def __call__(self, x, pos=None):
        s = self.fmt % x
        decimal_point = '.'
        positive_sign = '+'
        tup = s.split('e')
        significand = tup[0].rstrip(decimal_point)
        sign = tup[1][0].replace(positive_sign, '')
        exponent = tup[1][1:].lstrip('0')
        if exponent:
            exponent = '10^{%s%s}' % (sign, exponent)
        if significand and exponent:
            s =  r'%s{\times}%s' % (significand, exponent)
        else:
            s =  r'%s%s' % (significand, exponent)
        return "${}$".format(s)

# Format with 2 decimal places
plt.gca().yaxis.set_major_formatter(MathTextSciFormatter("%1.2e"))
"""
#--------------

#-------------Change of ticks for the plot-------------------------------------
plt.tick_params(direction='in', length=5, width=1, colors='black')
plt.tick_params(axis = 'y', which = 'minor',direction='in', length=5, width=1, colors='black')
plt.tick_params(axis = 'x', which = 'major',direction='out', length=5, width=1, colors='black')


leg = plt.legend(frameon=False, fontsize = 12)


plt.savefig('IdVg-Device1.png', bbox_inches = 'tight')
plt.savefig('IdVg-Device1.eps', bbox_inches = 'tight')
#-----------------------------------
#plt.savefig('IdVg-Device1.png', transparent = True)
#plt.savefig('IdVg-Device1.eps', transparent = True)
#------------Removing the border around the label(label defined for each line in the plot) 
#leg = plt.legend()
#leg.get_frame().set_linewidth(0.0)
#-----------Another way of removing the legend boarder-------------------------



#-----------Changing the color around the legend boarder-----------------------
#leg = plt.legend()
#leg.get_frame().set_edgecolor('b')

