import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def read_waveform(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Finn delta t
    delta_t = None
    for line in lines:
        if "delta t" in line.lower():
            parts = line.strip().split()
            for part in parts:
                try:
                    delta_t = float(part)
                    break
                except ValueError:
                    continue
            break
    if delta_t is None:
        raise ValueError("Fant ikke gyldig 'delta t' i filen.")

    # Hopp over headeren (4 linjer) og les verdier
    voltages = []
    for line in lines[4:]:
        parts = line.strip().split()
        if len(parts) >= 3:
            try:
                voltages.append(float(parts[2]))
            except ValueError:
                continue

    if not voltages:
        raise ValueError(f"Ingen måleverdier funnet i {file_path}")

    voltages = np.array(voltages)
    time = np.arange(len(voltages)) * delta_t
    return time, voltages


filnavn = ["OSC EKG\OSC_maaling_1.txt", "OSC EKG\OSC_maaling_2.txt", "OSC EKG\OSC_maaling_3.txt"]
titler = ["Lead 1", "Lead 2", "Lead 3"]

fig, axs = plt.subplots(3, 1, figsize=(12, 8), sharex=True)
    
for i in range(3):
    t, v = read_waveform(filnavn[i])
    axs[i].plot(t, v)
    axs[i].set_title(titler[i])
    axs[i].set_ylabel("Spenning [V]")
    axs[i].grid(True)

axs[-1].set_xlabel("Tid [s]")
plt.tight_layout()
plt.show()
