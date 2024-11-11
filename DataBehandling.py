import csv
import matplotlib.pyplot as plt
import os
import math
import numpy as np
print("Current Working Directory:", os.getcwd()) # en pwd for pythonen. brukes til å finne path til csv

def extract_column_to_array(file_path, column_name):
    data_array = []
    row_count = 0

    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            if row_count >= 210: # skal ta 210 - 10 målinger i et array
                break

            if not row_count < 10: # skipper de første 10 målingene for å bare hente stabil data
                data_array.append(float(row[column_name]))

            row_count += 1

    return data_array

def calculate_distance(): # avstand mellom max og min verdi i meter

    latitude = 62.4746318618
    lat_to_m = 111320
    
    lat_range = max(lat_array) - min(lat_array)
    lon_range = max(lon_array) - min(lon_array)
    
    lon_to_m = lat_to_m * math.cos(math.radians(latitude))

    lat_distance = lat_range * lat_to_m
    lon_distance = lon_range * lon_to_m
    
    return lat_distance, lon_distance

x = np.linspace(1, 201, 200)

def plot_coordinates():
    y_range, x_range = calculate_distance()
    plt.figure(figsize=(x_range, y_range))
    plt.scatter(lat_array, lon_array, c='blue', marker='o', label='Coordinates')
    plt.plot(lat_av, lon_av, c='red', marker='x', label='Average')
    plt.title("GPS Coordinates")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.legend()
    plt.grid(True)
    plt.show()

def average(array): # gjennomsnitt
    n = len(array)
    sum = 0
    for i in range(n):
        sum += array[i]

    return sum/n

def e_varians(array): # empirisk varians
    n = len(array)
    av = average(array)
    sum = 0
    for i in range(n):
        sum += (array[i] - av)**2

    return sum/(n-1)


### File path til csv'en ; må endres for ny fil eller pc ###
#file_path = './skolen/skolen_god_antenne.csv'
#file_path = './skolen/RawData.csv'
#file_path = './fotballbane/fotballbane_god_antenne.csv'
file_path = './fotballbane/RawData.csv'

### Navn på kolonne som skal indexes ###
lon_column = 'Longitude'
lat_column = 'Latitude'
alt_column = 'Altitude'

### Henter ut dataene som skal brukes i oppgaven ###
lon_array: list[float] = extract_column_to_array(file_path, lon_column)
lat_array: list[float] = extract_column_to_array(file_path, lat_column)
alt_array: list[float] = extract_column_to_array(file_path, alt_column)

### Gjennomsnitt av dataene ###
lon_av: float = average(lon_array)
lat_av: float = average(lat_array)
alt_av: float = average(alt_array)

### Varians av dataene ###
lon_var: float = e_varians(lon_array)
lat_var: float = e_varians(lat_array)
alt_var: float = e_varians(alt_array)

lat_range, lon_range = calculate_distance()

### Printer data i konsoll ###
print(f'n = {len(alt_array)}')
print(f'gjennomsnitt = lat: {lat_av}, lon: {lon_av}, alt: {alt_av}')
print(f'varians = lat: {lat_var}, lon: {lon_var}, alt: {alt_var}')
print(f'lat_max: {max(lat_array)}, lat_min: {(min(lat_array))}')
print(f'lon_max: {max(lon_array)}, l')
print(f'lat intervall = [{min(lat_array)}, {max(lat_array)}] ; {lat_range: .6f}m, lon intervall = [{min(lon_array)}, {max(lon_array)}] ; {lon_range: .6f}m')

#plot_coordinates()