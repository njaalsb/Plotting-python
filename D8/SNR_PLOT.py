import matplotlib.pyplot as plt
import numpy as np

# Gitt data
V_hat = 1.8974  # Konstant signalverdi
V_omega = np.array([0.2, 0.4, 0.8, 1.0, 1.2, 1.4, 1.6, 1.7, 1.8])
ber = np.array([0, 0, 0.31, 7.81, 30.19, 45.50, 49.94, 50, 50])

# Beregn SNR i dB
snr_db = 20 * np.log10(V_hat / V_omega)

# Plot med loggskala på x-aksen
plt.figure(figsize=(10, 6))
plt.semilogx(10**(snr_db/10), ber, marker='o', linestyle='-', color='b')
plt.xlabel("SNR logaritmisk")
plt.ylabel("Bitfeilrate (%)")
plt.title("Bitfeilrate med økende SNR og fast baudrate på 9600")
plt.grid(True, which="both", ls="--", lw=0.5)
plt.tight_layout()
plt.show()
