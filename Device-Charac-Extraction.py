
"""
import csv

with open('Device1-IdVg.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    print(readCSV)
"""

"""
Mahsa Sadeghi Code 
OPT Characterizations-Device
"""

import csv
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
from math import sqrt
import pandas as pd 
import pandas as pd1
#polyfit
import numpy as np

 
V = []
I = []
#Cox capacitance 8nF/cm^2 
Cox = 8
with open('OPT-DClass1-IdVg-Device41.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)


    for row in csvReader:
        V.append(row[0]) #first column of the CSV file Vg voltage 
        I.append(row[1]) #second column of the CSV file Idrain 
        



Vg = []
Id = []
#SqrtVg is for mobility calculation 
SqrtId = []

for i in range(1307,1567): #voltage Vd=-20 starts at cell 1307 to 1567
    Vg.append(float(V[i]))
    
    absId = abs(float(I[i])) #normalized = abs(float(I[i])) /3.8
    #normalized = abs(float(I[i]))
    Id.append(absId)
    #print(absId)
    #print(sqrt(absId))

    
   
    #adding to SqrtId 
    SqrtId.append(sqrt(absId))
    
    i = i + 1
    
#------------------V_Threshold calculation-----------------------------------
#plotting square root of the IdVg at Vd = -20V 
"""
sqrtIdplot = pd.DataFrame({'Vg': Vg,'SqrtId': SqrtId})
plt.xlabel('Vg')
plt.ylabel('SqrtId')
#plt.semilogy()
plt.plot(Vg,SqrtId) 
"""


#----------------linear Polyfitting for finding intercetiopn for V_threshold 
SqrtIdLinear = [] #portion of SqrtId from Vg = -2 to Vg = -15 for linear fitting
VgLinear = []     #portion of Vg from Vg = -2 to Vg = -15 for linear fitting

for i in range(81,211): 
    VgLinear.append(float(V[i]))
    
    SqrtIdLinear.append(SqrtId[i])
    #print(absId)
    #print(sqrt(absId))
    i = i + 1

"""
IdPlot = pd1.DataFrame({'Vg': VgLinear,'SqrtIdLinear': SqrtIdLinear})
plt1.xlabel('Vg')
plt1.ylabel('SqrtIdLinear')
#plt1.semilogy()
plt1.plot(VgLinear,SqrtIdLinear) 
"""  



#----------------PolyFitting the portion of SqrtIdLinear---------------------

PolyLinearFit = np.polyfit(VgLinear, SqrtIdLinear, 1)
Vthreshold = PolyLinearFit[1]
#print(Vthreshold)

 
#----------------Plotting of the Id-Vg---------------------------------------
"""
IdPlot = pd1.DataFrame({'Vg': Vg,'Id': Id})
plt1.xlabel('Vg')
plt1.ylabel('Id')
plt1.semilogy()
plt1.plot(Vg,Id)   
print(len(Vg))
"""


#----------------------------------------------------------------------------
#------------------- Mobility Calculation------------------------------------
#Field Effect Mobility in Saturation 
#Idrain = 1/2*u*Ci*W/L*(Vg - Vth)^2
u = []
constant = (2*50*(10**9)/(150*Cox)) #10**9 is for nF 



#print(Vg[3] - Vthreshold)
#print((Id[200]/((Vg[200] - Vthreshold)**2))*constant)


j = 0 
avg = 0
for i in range(0,260):
  
    u.append((Id[i]/((Vg[i] - Vthreshold)**2))*constant)
    if i >= 100 and i<=150: 
        avg = avg + u[i]
        j = j + 1 
        
    #print(u[i])
    i = i + 1


#-----------------------------avgeraging mobility----------------------------
mobility = avg / j 
#print(mobility)
#plotting mobilities 
#IdPlot = pd1.DataFrame({'Vg': Vg,'Mobility': u})
#plt1.xlabel('Vg')
#plt1.ylabel('mobility')
#plt1.semilogy()
#plt1.plot(Vg,u)   
#print(len(Vg))
#----------------------------Subthreshold Swing------------------------------
  


SSId = [] #Subthreshold Swing List in the linear regime for finding the slope
SSId2 = [] #This is the list for plotting
SSVg = [] 
for i in range(45,55): #for previous measurements the range()
    SSId.append(np.log10(Id[i])) #np.log() is ln, np.log10() is log base 10 
    SSId2.append(Id[i])
    SSVg.append(Vg[i])
    i = i + 1 
  
         
#Fitting the SSVg and SSId line to get the slope 
PolySSFit = np.polyfit(SSVg, SSId, 1)
print(PolySSFit[0],'mahsa')
SS = -(1 / PolySSFit[0]) #This gives the first element of the list which is slope of the line, the second element is the interception 
#print(abs(SS))  

#"""
IdPlot = pd1.DataFrame({'Vg': SSVg,'Id':SSId2 })
plt1.xlabel('Vg')
plt1.ylabel('Id')
plt1.semilogy()
plt1.plot(SSVg,SSId2)  
#"""

#"""
IdPlot = pd1.DataFrame({'Vg': Vg,'Id': Id})
plt1.xlabel('Vg')
plt1.ylabel('Id')
plt1.semilogy()
plt1.plot(Vg,Id) 
#"""
#IdVg plotting log(Id) vs x 




    
#------------------------------------------------------------------------------

a = I[900]
#print(a)
#print(abs(float(a)))
 


#df.to_excel('1WL-IdVg.xlsx', sheet_name='sheet1', index=False)



#finding the slop
offcurrent=0
i = 0
#y = 0
offcurrentlist=[]
for i in range(len(Id)): 
    if Id[i] == min(Id): 
        break 
    else: 
        if Id[i] > min(Id): 
            offcurrent = offcurrent + Id[i]
            offcurrentlist.append(Id[i])
           
            i ++ 1 
leakavg=offcurrent/len(offcurrentlist)
#print(leakavg)
#plt.semilogy()
oncurrent=max(Id)
#print(Id)
minid = min(Id)

#print(len(offcurrentlist))

#print(offcurrentlist)
print(np.log10(oncurrent/minid)) 
OnOff = np.log10(oncurrent/leakavg)
print(np.log10(oncurrent/leakavg)) 



#slope 

#plt.plot(Vg,np.polyval(ss,Vg))
#------------------------characteristics printing-------------------------------
print()
print('Vthreshold:', Vthreshold)
print()
print('mobility:' , mobility)
print()
print('Subthreshold Swing (wrong):' , SS)
print()
print('ON-OFF:', OnOff)

    
 
print()
print(Vthreshold)
print(mobility)
print(SS)
print(OnOff) 
     
         




 

