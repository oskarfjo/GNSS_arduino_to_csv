import csv
import matplotlib.pyplot as plt
import os
import math
import numpy as np
#print("Current Working Directory:", os.getcwd()) # en pwd for pythonen. brukes til å finne path til csv

def extract_column_to_array(file_path, column_name):
    data_array = []
    row_count = 0
    n = -1 # grense for hvor mange målinger man vil ta fra csv.

    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            if n > 0 and row_count >= n + 10:
                break

            if not row_count < 10: # skipper de første 10 målingene for å bare hente stabil data
                data_array.append(float(row[column_name]))
            row_count += 1

    return data_array

def plot_coordinates(vec1, vec2): # nåværende er tilpasset til sammenligning av altitude data
    x1 = np.linspace(1, len(vec1) + 1, len(vec1))
    x2 = np.linspace(1, len(vec2) + 1, len(vec2))
    plt.scatter(x2, vec2, c='blue', marker='o', label='Coordinates - iPhone')
    plt.scatter(x1, vec1, c='red', marker='s', label='Coordinates - Arduino')
    plt.title("Altitude plot - mix")
    plt.xlabel("måling nr.")
    plt.ylabel("moh")
    plt.legend()
    plt.grid(True)
    plt.show()

def av(array): # gjennomsnitt
    n = len(array)
    sum = 0
    for i in range(n):
        sum += array[i]

    return sum/n

def var(array): # varians
    n = len(array)
    average = av(array)
    sum = 0
    for i in range(n):
        sum += (array[i] - average)**2

    return sum/(n-1)

def calculate_distance(array): # avstand mellom max og min verdi i meter

    #latitude = av(lat_array)
    #lat_to_m = 111320
    
    #lat_range = max(lat_array) - min(lat_array)
    #lon_range = max(lon_array) - min(lon_array)
    alt_range = max(array) - min(array)
    
    #lon_to_m = lat_to_m * math.cos(math.radians(latitude))

    #lat_distance = lat_range * lat_to_m
    #lon_distance = lon_range * lon_to_m
    
    return alt_range #lat_distance, lon_distance

### File path til csv'en ###
arduino_path = './skolen/skolen_god_antenne.csv'
iphone_path = './skolen/RawData.csv'


### Navn på kolonne som skal indexes ###
#lon_column = 'Longitude'
#lat_column = 'Latitude'
alt_column = 'Altitude'

### Henter ut dataene som skal brukes i oppgaven ###
#lon_array: list[float] = extract_column_to_array(file_path, lon_column)
#lat_array: list[float] = extract_column_to_array(file_path, lat_column)
alt_array_ard: list[float] = extract_column_to_array(arduino_path, alt_column)
alt_array_iph = extract_column_to_array(iphone_path, alt_column)
### Gjennomsnitt av dataene ###
#lon_av: float = av(lon_array)
#lat_av: float = av(lat_array)
alt_av_ard: float = av(alt_array_ard)
alt_av_iph: float = av(alt_array_iph)

### Varians av dataene ###
#lon_var: float = var(lon_array)
#lat_var: float = var(lat_array)
alt_var_ard: float = var(alt_array_ard)
alt_var_iph: float = var(alt_array_iph)

alt_range_ard = calculate_distance(alt_array_ard)
alt_range_iph = calculate_distance(alt_array_iph)

### Printer data i konsoll ###
print('**** Arduino ****')
print(f'n = {len(alt_array_ard)}')
print(f'gjennomsnitt = alt: {alt_av_ard: .2f}moh')
print(f'varians = alt: {alt_var_ard: .2f}m^2')
print(f'alt intervall = [{min(alt_array_ard): .2f}, {max(alt_array_ard): .2f}] ; {alt_range_ard: .2f}m')
print(f'S = {np.sqrt(alt_var_ard): .2f}m')
print(f'SE(x) :) = {(np.sqrt(alt_var_ard)) / (np.sqrt(len(alt_array_ard))): .2f}m')
print(' ')
print('**** iPhone ****')
print(f'n = {len(alt_array_iph)}')
print(f'gjennomsnitt = alt: {alt_av_iph: .2f}moh')
print(f'varians = alt: {alt_var_iph: .2f}m^2')
print(f'alt intervall = [{min(alt_array_iph): .2f}, {max(alt_array_iph): .2f}] ; {alt_range_iph: .2f}m')
print(f'S = {np.sqrt(alt_var_iph): .2f}m')
print(f'SE(x) :) = {(np.sqrt(alt_var_iph)) / (np.sqrt(len(alt_array_iph))): .2f}m')

### Plotter data ###
plot_coordinates(alt_array_ard, alt_array_iph)
