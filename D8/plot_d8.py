import matplotlib.pyplot as plt
import numpy as np

# Baud-rater og tilsvarende BER i prosent
baud_rates = [9600, 19200, 38400, 57600, 76800, 115200]
ber_percent = [0, 0, 0, 4.65, 33.75, 42.55]

# Beregn standardavvik (kun på de faktiske BER-verdiene)
std_dev = np.std(ber_percent)
print(f"Standardavvik i BER: {std_dev:.2f} %")

# Plotting
plt.figure(figsize=(10, 6))
plt.bar([str(b) for b in baud_rates], ber_percent, color='skyblue', edgecolor='black')
plt.xlabel('Baud-rate')
plt.ylabel('Bitfeilrate (%)')
plt.title('Bitfeilrate ved SNR=0')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
