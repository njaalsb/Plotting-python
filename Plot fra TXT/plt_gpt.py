import math
import numpy as np
import matplotlib.pyplot as plt

FILE_NAME = r"steg1.txt"

columns = ['Freq', '.V(n008)']

# Les data
with open(FILE_NAME, "r") as f:
    first_row = f.readline()
    

    my_data = np.genfromtxt(FILE_NAME, skip_header=True, usecols=(2), delimiter=',')
    #my_data = np.genfromtxt(FILE_NAME, skip_header=True, delimiter=', ')
    #print(len(my_data[2][0]))
#print((my_data[2][1].readlines().split(',')))
x = []
y = []  
'''
# Prosessering av data
for i in range(len(my_data)):
    x1 = float(my_data[i][0])
    y1 = float(my_data[i][1])
    y2 = my_data[i][1].split(",")
    y3 = y2[0]
    if not (math.isnan(x1) or math.isnan(y1)):
        x.append(x1)  # Beholder originale verdier
        y.append(y3)

# Sjekk dataene
print("x:", x[:5])
print("y:", y[:5])
print("mean = %f" % (np.mean(y)))

# Plot med logaritmisk x-akse
plt.semilogx(x, y, label="Steg #1")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

if math.isnan(my_data[0][0]) and math.isnan(my_data[0][1]):
    plt.xlabel("$" + first_row.split('\t')[0] + "\ (s)$")
    plt.ylabel("$" + first_row.split('\t')[1][:-1] + " $")

plt.legend()
plt.savefig(f"{FILE_NAME.split('/')[-1]}.svg", format="svg")
plt.show()
'''