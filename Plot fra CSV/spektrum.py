# spektrumsanalysator med 6k hertz

import pandas as pd
import matplotlib.pyplot as plt


#columns = ['Frequency (Hz)', 'Trace 1 (dBV)', 'Phase (deg)' , 'Trace 2 (dBV)', 'Phase (deg)']

columns = ['Time (s)', 'Channel 1 (V)', 'Channel 2 (V)']

#columns = ['Frequency (Hz)','Channel 1 Magnitude (dB)','Channel 2 Magnitude (dB)']

df = pd.read_csv(r'CSV\UART.csv', usecols= columns)

x_values, y_values, input_values = df['Time (s)'], df['Channel 1 (V)'], df['Channel 2 (V)']


#x_values, y_values, input_values = df['Frequency (Hz)'], df['Channel 1 Magnitude (dB)'], df['Channel 2 Magnitude (dB)']

def f(x):
    return x

#plot
plt.title("Oscilloskop")
#plt.plot(x_values, y_values, x_values, lst, x_values, lst1)
plt.plot(x_values, y_values, label = "FSK-signal")
plt.plot(x_values, input_values, label = "UART-signal")
#plt.plot([10, f(10)])
#plt.plot(1.508, 1.035, 'ro', label='(x,y) = (1.508, 1.035)')
#plt.plot(2.634, 0.707, 'co', label='(x,y) = (2.634, 0.707)')
#plt.plot(2000,-80.3, 'r.', label = '(x,y) = (2000, -80.3)')
#plt.xlabel("Frekvens [Hz]")
plt.xlabel("Tid [s]")

#plt.ylabel("Amplitude [dB]")
plt.ylabel("Amplitude [V]")

#plt.plot(x_values, y_values)
plt.legend()
plt.show()

