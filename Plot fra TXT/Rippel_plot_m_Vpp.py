# Denne koden tar inn 4 .txt filer, regner ut gjennomsnittlig spenning med np.mean og gir Vpp, printes i terminalen.
import numpy as np
import matplotlib.pyplot as plt

# Filter range in seconds
x_min = 0.00815
x_max = 0.00845

def load_and_filter(file_path, label):
    with open(file_path, "r") as f:
        f.readline()  # Skip header

    data = np.genfromtxt(file_path, delimiter='\t')
    x_vals = data[:, 0]
    y_vals = data[:, 1]

    # Filter range
    mask = (x_vals >= x_min) & (x_vals <= x_max)
    x_filtered = x_vals[mask]
    y_filtered = y_vals[mask]

    vpp = np.max(y_filtered) - np.min(y_filtered)
    print(f"{label}: Vpp = {vpp:.6f} V, Mean = {np.mean(y_filtered):.6f} V")

    return x_filtered, y_filtered

# File list
FILES = [
    ("Buck_converter_0_5_ohm.txt", "Last 0.5 Ohm, Vpp = 0.005444 V"),
    ("Buck_converter_1_ohm.txt", "Last 1 Ohm, Vpp = 0.005126 V"),
    ("Buck_converter_10_ohm (1).txt", "Last 10 Ohm, Vpp = 0.009528 V"),
    ("Buck_converter_100_ohm (1).txt", "Last 100 Ohm, Vpp = 0.007937 V"),
]

plt.figure()

for path, label in FILES:
    x, y = load_and_filter(path, label)
    plt.plot(x, y, label=label)

# Plot settings
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.title("Rippelspenning - LTSpice simulering")
plt.xlabel("Tid (s)")
plt.ylabel("Amplitude (V)")
plt.legend()
plt.show()
