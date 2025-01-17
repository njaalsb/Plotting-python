# Kode for dekadisk plot
# Fungerer bare med to kolonner separert med mellomrom

import sys
import math
import numpy as np
import matplotlib.pyplot as plt

FILE_NAME = r"TXT filer\LTC3807.txt"

with open(FILE_NAME, "r") as f:
	first_row = f.readline()
# print (first_row)


my_data = np.genfromtxt(FILE_NAME, delimiter='\t')

x = []
y = []


    

for i in range(len(my_data)):
    x1 = float(my_data[i][0])
    y1 = float(my_data[i][1])	
    if not (math.isnan(x1) or math.isnan(y1)):
        x.append(x1)
        #x.append(abs(200*np.log(x1)))
        y.append(y1)
        


print ("mean = %f" %(np.mean(y)))


# plotting
plt.semilogx(x, y, label="Steg #1")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

#plt.plot(x,y)

# plt.title("$"+first_row.split('\t')[1][:-1] + " $")
if math.isnan(my_data[0][0]) and math.isnan(my_data[0][1]):
	plt.xlabel("$"+first_row.split('\t')[0] + "\ (s)$")
	plt.ylabel("$"+first_row.split('\t')[1][:-1] + " $")
plt.grid(True)
#plt.xticks(np.arange(min(x), max(x)+1, 10.0))
plt.savefig(f"{FILE_NAME.split('/')[-1]}.svg", format='svg')
plt.show()