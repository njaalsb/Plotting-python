# Punkt med koordinater i 20.65 og i 2750 hZ

import pandas as pd
import matplotlib.pyplot as plt

lst = []
lst1 = []

columns = ['Time (s)', 'Channel 1 (V)', 'Channel 2 (V)']

df = pd.read_csv(r'CSV filer\Hele_programmet.csv', usecols= columns)

x_values = df['Time (s)']

y_values = df['Channel 1 (V)']

input_values = df['Channel 2 (V)']

for i in range (8193):
    lst.append(1)
    
for i in range (8193):
    lst1.append(1)

#plot
plt.title("Tidtaking-Programmet")
#plt.plot(x_values, y_values, x_values, lst, x_values, lst1)
# plt.plot(x_values, input_values, label="y [n]")
plt.plot(x_values, y_values, label="Utgangssignal")
# plt.plot(2062.5, -4.1519, 'bo', label='f_c (2062.5, -4.1519)')
# plt.plot(2750, -10.1092, 'ro', label='f_n (2750, -10.1092)')
#plt.plot(0.12, 1.54, 'ro', label = '(0.12, 1.54)')
#plt.plot(1.72, 1.546, 'bo', label = '(1.72, 1.546)')
#plt.plot(0.17, 2.039, 'yo', label = '(0.17, 2.039)')
plt.xlabel("T[s]")
plt.ylabel("Amplitude [V]")
plt.grid(True)
#plt.plot(x_values, y_values)
plt.axvline(x=-1.160590530611085, color = 'b', label = 'start, x = -1.160s')
plt.axvline(x=-0.8683114606110847, color = 'b', label = 'start, x = -0.868s')
plt.legend()
plt.show()



