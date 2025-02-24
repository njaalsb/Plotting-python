import numpy as np
import matplotlib.pyplot as plt
import datetime

# Filnavn (oppdater om nødvendig)
filename = r"C:\Users\bruhe\OneDrive - NTNU\Documents\ESI\ESI.sem4\IELS2003\GOD_TEST_EKGOSC.txt"

# Lister for å lagre data
time_ch0 = []
ch0_values = []
time_gen = []
gen_values = []

with open(filename, "r") as file:
    lines = file.readlines()

# Finn start på data (hopper over metadata)
data_start = None
for i, line in enumerate(lines):
    if "time[0]" in line:
        data_start = i + 1  # Neste linje er starten på dataene
        break

if data_start is None:
    raise ValueError("Fant ikke start på dataseksjonen i filen!")

# Les inn verdiene
for line in lines[data_start:]:
    values = line.split()
    if len(values) == 4:  # Sikre at vi har riktige kolonner
        try:
            t_ch0 = datetime.datetime.strptime(values[0], "%m/%d/%Y %H:%M:%S.%f")
            t_gen = datetime.datetime.strptime(values[2], "%m/%d/%Y %H:%M:%S.%f")
            ch0 = float(values[1])
            gen = float(values[3])

            time_ch0.append(t_ch0)
            ch0_values.append(ch0)
            time_gen.append(t_gen)
            gen_values.append(gen)
        except ValueError as e:
            print(f"Kunne ikke parse linje: {line.strip()} - Feil: {e}")

# Sjekk om data ble lest inn
if not time_ch0 or not time_gen:
    raise ValueError("Ingen gyldige data ble lest fra filen!")

# Konverter tid til relative verdier (sekunder fra start)
start_time = time_ch0[0]
time_ch0 = [(t - start_time).total_seconds() for t in time_ch0]
time_gen = [(t - start_time).total_seconds() for t in time_gen]

# Plot signalene
plt.figure(figsize=(8, 5))
plt.plot(time_ch0, ch0_values, "b-", label="Ch0")
plt.plot(time_gen, gen_values, "r-", label="Gen")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Waveform Data")
plt.legend()
plt.grid(True)
plt.show()
