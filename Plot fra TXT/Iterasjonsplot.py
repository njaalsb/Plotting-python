# Kode for fire plot, plotter alle i samme figur
# Plottes i utgangspunktet lineært, men kan også plottes dekadisk

import sys
import math
import numpy as np
import matplotlib.pyplot as plt

start, stop = 10,900000

# Plot 1:
FILE_NAME = r"Buck_converter_0_5_ohm.txt"

with open(FILE_NAME, "r") as f:
	first_row = f.readline()
# print (first_row)

my_data_PLOT1 = np.genfromtxt(FILE_NAME, delimiter='\t')

x_1 = []
y_1 = []    

for i in range(start, stop):
    x1 = float(my_data_PLOT1[i][0])
    y1 = float(my_data_PLOT1[i][1])	
    if not (math.isnan(x1) or math.isnan(y1)):
        x_1.append(x1)
        y_1.append(y1)
        #x.append(abs(200*np.log(x1)))
        

print ("mean = %f" %(np.mean(y_1)))

# Plot 2:

FILE_NAME_PLOT2 = r"Buck_converter_1_ohm.txt"

with open(FILE_NAME_PLOT2, "r") as f:
	first_row = f.readline()
# print (first_row)

my_data_PLOT2 = np.genfromtxt(FILE_NAME_PLOT2, delimiter='\t')

x_2 = []
y_2 = []    

for i in range(start, stop):
    x2 = float(my_data_PLOT2[i][0])
    y2 = float(my_data_PLOT2[i][1])	
    if not (math.isnan(x1) or math.isnan(y1)):
        x_2.append(x2)
        y_2.append(y2)
        #x.append(abs(200*np.log(x1)))
        
print ("mean = %f" %(np.mean(y_2)))

# Plot 3:

FILE_NAME_PLOT3 = r"Buck_converter_10_ohm (1).txt"

with open(FILE_NAME_PLOT3, "r") as f:
	first_row = f.readline()
# print (first_row)

my_data_PLOT3 = np.genfromtxt(FILE_NAME_PLOT3, delimiter='\t')

x_3 = []
y_3 = []    

for i in range(start, stop):
    x3 = float(my_data_PLOT3[i][0])
    y3 = float(my_data_PLOT3[i][1])	
    if not (math.isnan(x3) or math.isnan(y3)):
        x_3.append(x3)
        y_3.append(y3)
        #x.append(abs(200*np.log(x1)))
        
print ("mean = %f" %(np.mean(y_3)))

# Plot 3:

FILE_NAME_PLOT4 = r"Buck_converter_100_ohm (1).txt"

with open(FILE_NAME_PLOT4, "r") as f:
	first_row = f.readline()
# print (first_row)

my_data_PLOT4 = np.genfromtxt(FILE_NAME_PLOT4, delimiter='\t')

x_4 = []
y_4 = []    

for i in range(start, stop):
    x4 = float(my_data_PLOT4[i][0])
    y4 = float(my_data_PLOT4[i][1])	
    if not (math.isnan(x4) or math.isnan(y4)):
        x_4.append(x4)
        y_4.append(y4)
        #x.append(abs(200*np.log(x1)))
        
print ("mean = %f" %(np.mean(y_4)))

# plotting
#plt.semilogx(x, y, label="Steg #1")
plt.plot(x_1,y_1, label="Plot 0.5 Ohm")
plt.plot(x_2,y_2, label="Plot 1 Ohm")
plt.plot(x_3,y_3, label="plot 10 Ohm")
plt.plot(x_4,y_4, label ="plot 100 Ohm")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

plt.title("Rippel")

# plt.title("$"+first_row.split('\t')[1][:-1] + " $")
"""if math.isnan(my_data_PLOT4[0][0]) and math.isnan(my_data_PLOT4[0][1]):
	plt.xlabel("$"+first_row.split('\t')[0] + "\ (s)$")
	plt.ylabel("$"+first_row.split('\t')[1][:-1] + " $")"""
 
plt.xlabel("Amplitude (v)")
plt.ylabel("Tid (s)")
plt.grid(True)
plt.legend()
#plt.xticks(np.arange(min(x), max(x)+1, 10.0))
#plt.savefig(f"{FILE_NAME.split('/')[-1]}.svg", format='svg')
plt.show()