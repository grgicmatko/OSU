import pandas as pd
import numpy as np
data = pd . read_csv('data_C02_emission.csv')

#a
print(len(data))
print(data.info())
print(data.dropna())
print(data.drop_duplicates())
data[data.select_dtypes(['object']).columns] = data.select_dtypes(['object']).apply(lambda x: x.astype('category')) #pretvaranje u category tip
print(data.info())

#b
subdata = data[['Fuel Consumption City (L/100km)', 'Make', 'Model']]

print(subdata.nsmallest(3, 'Fuel Consumption City (L/100km)'))
print(subdata.nlargest(3, 'Fuel Consumption City (L/100km)'))

#c
csub = data[(data['Engine Size (L)'] > 2.5) & (data['Engine Size (L)'] < 3.5)]
print(len(csub))
print(csub['CO2 Emissions (g/km)'].mean())

#d
print(len(data[(data['Make'] == 'Audi')]))
dsub = data[(data['Make'] == 'Audi') & (data['Cylinders'] == 4)]
print(dsub['CO2 Emissions (g/km)'].mean())

#e
print(len(data[(data['Cylinders'] % 2 == 0)]))
print(data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean())

#f
fsubD = data[(data['Fuel Type'] == 'D')]
print(fsubD['Fuel Consumption City (L/100km)'].mean())
fsubX = data[(data['Fuel Type'] == 'X')]
print(fsubX['Fuel Consumption City (L/100km)'].mean())
#medijalne vrijednosti
print(fsubD['Fuel Consumption City (L/100km)'].median(),fsubX['Fuel Consumption City (L/100km)'].median())

#g
print(data[(data['Cylinders'] == 4) & (data['Fuel Type'] == 'D')]
      ['Fuel Consumption City (L/100km)'].max())

#h
print(len(data[(data['Transmission'].str.startswith('M'))]))

#i
print(data.corr(numeric_only=True))
# na dijagonali su 1 jer su jednake vrijednosti - maksimalna korelacija
