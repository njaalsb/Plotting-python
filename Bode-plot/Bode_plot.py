import numpy as np
import matplotlib.pyplot as plt

# Filnavn (oppdater med riktig sti hvis nødvendig)
filename = r"\Users\bruhe\OneDrive - NTNU\Documents\ESI\ESI.sem4\IELS2003\Bodeplot_steg3.txt"

# Les inn data
freqs = []
gains = []
phases = []

with open(filename, "r") as file:
    lines = file.readlines()

# Finn start på data (hopper over metadata)
for i, line in enumerate(lines):
    if "Freq" in line:  
        data_start = i + 1  # Neste linje er starten på dataene
        break

# Les inn verdiene
for line in lines[data_start:]:
    values = line.split()
    if len(values) == 3:  # Sikre at vi har riktige kolonner
        freq, gain, phase = map(float, values)
        freqs.append(freq)
        gains.append(gain)
        phases.append(phase)

# Plot Gain (Amplitude)
plt.figure(figsize=(8, 5))
plt.xscale("log")
plt.plot(freqs, gains, "b-o", label="Gain (dB)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Gain (dB)")
plt.title("Gain vs Frequency")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.legend()

# Plot Phase
plt.figure(figsize=(8, 5))
plt.xscale("log")
plt.plot(freqs, phases, "r-s", label="Phase (deg)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (degrees)")
plt.title("Phase vs Frequency")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.legend()

plt.show()


