import numpy as np
import matplotlib.pyplot as plt
import math

# Files to plot
FILES = [
    (r"C:\Users\bruhe\OneDrive - NTNU\Documents\ESI\ESI.sem4\IELS2031\Lab\100ohm\WFM04.CSV", "Last 100 Ohm, Vpp = 29.89mV"),
    (r"C:\Users\bruhe\OneDrive - NTNU\Documents\ESI\ESI.sem4\IELS2031\Lab\10ohm\WFM03.CSV", "Last 10 Ohm, Vpp = 74.97mV"),
    (r"C:\Users\bruhe\OneDrive - NTNU\Documents\ESI\ESI.sem4\IELS2031\Lab\1ohm\WFM02.CSV", "Last 1 Ohm, Vpp = 212.17mV"),
    (r"C:\Users\bruhe\OneDrive - NTNU\Documents\ESI\ESI.sem4\IELS2031\Lab\0.5ohm\WFM01.CSV", "Last 0.5 Ohm, Vpp = 298mV"),
]

start, stop = 10, 900000

plt.figure()

for file_path, label in FILES:
    # Read data, skip the first row (header), use comma delimiter
    data = np.genfromtxt(file_path, delimiter=',', skip_header=1)

    # Make sure we don't go out of bounds
    stop_idx = min(stop, len(data))

    x = []
    y = []
    sum_y = 0
    count = 0

    for i in range(start, stop_idx):
        x_val, y_val = data[i]
        if not (math.isnan(x_val) or math.isnan(y_val)):
            x.append(x_val)
            y.append(y_val)
            sum_y += y_val
            count += 1

    mean_y = np.mean(y)
    average_y = sum_y / count if count != 0 else float('nan')

    print(f"{label}:")
    print(f"  Mean (numpy) = {mean_y:.6f} V")
    print(f"  Average (manual) = {average_y:.6f} V\n")

    plt.plot(x, y, label=label)

# Plot settings
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.title("Rippelspenning - Oscilloskop")
plt.xlabel("Tid (s)")
plt.ylabel("Amplitude (V)")
plt.legend()
plt.show()
