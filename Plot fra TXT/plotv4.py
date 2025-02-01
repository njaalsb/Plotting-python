# Kode for plot av amplituderespons og faserespons:
# Avhengig av at enkodingen til grader (°) symbolet er UTF-8
# Gir i utgangspunktet y-verdier i samme format som de puttes inn

import numpy as np
import matplotlib.pyplot as plt
import re

# Function to parse each line of the file
def parse_line(line):
    try:
        # Split the line into frequency and the polar value
        freq_part, value_part = line.split(maxsplit=1)
        freq = float(freq_part)  # Convert frequency to float
        
        # Extract magnitude in dB and phase in degrees
        match = re.search(r'\(([^,]+)dB,([^°]+)°\)', value_part)
        if match:
            magnitude_dB = float(match.group(1))  # Magnitude
            phase_deg = float(match.group(2))    # Phase
            return freq, magnitude_dB, phase_deg
        else:
            print(f"Regex did not match for line: {line}")
    except Exception as e:
        print(f"Error parsing line: {line} -> {e}")
    return None

# File path (update with your actual file path)
file_path = "TXT filer\steg3.txt"  # Replace with the correct file name

# Lists to store parsed data
freqs, magnitudes_dB, phases_deg = [], [], []

# Read and parse the file
with open(file_path, 'r') as file:
    for line in file:
        if not line.startswith("Freq."):  # Skip the header
            result = parse_line(line.strip())
            if result:
                freq, magnitude_dB, phase_deg = result
                freqs.append(freq)
                magnitudes_dB.append(magnitude_dB)
                phases_deg.append(phase_deg)

# Convert lists to numpy arrays
freqs = np.array(freqs)
magnitudes_dB = np.array(magnitudes_dB)
phases_deg = np.array(phases_deg)

# Check if data was successfully parsed
if freqs.size == 0 or magnitudes_dB.size == 0 or phases_deg.size == 0:
    print("No data was parsed. Please check the file format and path.")
else:
    # Plot the data
    # plt.figure(figsize=(12, 6))

    # Magnitude plot
    # plt.subplot(2, 1, 1)
    plt.plot(freqs, magnitudes_dB, label="Amplitude (dB)", color='b')
    plt.xscale('log')
    plt.xlabel("Frekvens (Hz)")
    plt.ylabel("Amplitude (dB)")
    plt.title("Frekvens Respons")
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    # plt.legend()
    
    # Vert lines:
    plt.axvline(x = 3*10**(-2), color = 'r', label = '30 mHz')
    plt.axvline(x = 1, color = 'g', label = '1Hz')
    plt.axvline(x = 50, color = 'y', label = '50 Hz')
    plt.legend()
    '''
    # Phase plot
    plt.subplot(2, 1, 2)
    plt.plot(freqs, phases_deg, label="Fase (°)", color='r')
    plt.xscale('log')
    plt.xlabel("Frekvens (Hz)")
    plt.ylabel("Fase (°)")
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend()

    plt.tight_layout()'''
    plt.show()
