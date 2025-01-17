import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

columns = ['Freq', '.V(n008)']

#df = pd.read_csv('Plot fra CSV\Plot fra TXT\Steg2.txt', usecols= columns)

#df = pd.read_csv('Plot fra CSV\Plot fra TXT\Steg2.txt', sep=" ", header=None)

#x_values = df['Freq'][1]

#df = pd.read_table('Plot fra CSV\Plot fra TXT\Steg2.txt', delimiter=" ")

df = pd.read_table(r'Steg2.txt')

print(df)