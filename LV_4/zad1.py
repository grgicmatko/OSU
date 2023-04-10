import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn . model_selection import train_test_split
from sklearn . preprocessing import MinMaxScaler
from sklearn . preprocessing import OneHotEncoder
import sklearn . linear_model as lm
from sklearn import metrics

#a
data = pd . read_csv('data_C02_emission.csv')

input_variables = ['Fuel Consumption City (L/100km)','Fuel Consumption Hwy (L/100km)',
                   'Fuel Consumption Comb (L/100km)','Fuel Consumption Comb (mpg)',
                   'Engine Size (L)','Cylinders']

output_variables = ['CO2 Emissions (g/km)']
X = data[input_variables].to_numpy()
y = data[output_variables].to_numpy()

X_train , X_test , y_train , y_test = train_test_split (X , y , test_size = 0.2 , random_state =1 )

#b
plt.scatter(X_train[:,0],y_train,c='blue',s=2)
plt.scatter(X_test[:,0],y_test,c='red',s=2)
plt.show()

#c
plt.figure()

plt.hist(X_train[:,0])
plt.show()
# min - max skaliranje
sc = MinMaxScaler ()
X_train_n = sc . fit_transform ( X_train )
X_test_n = sc . transform ( X_test )

plt.hist(X_train_n[:,0])
plt.show()

# d
linearModel = lm . LinearRegression ()
linearModel . fit ( X_train_n , y_train )

print(linearModel.coef_)

# e
y_test_p = linearModel . predict ( X_test_n )
plt.scatter(y_test, y_test_p, s=2)
plt.show()

# f
MSE = metrics.r2_score(y_test, y_test_p)
print(MSE)

# e
# Povecavanjem broja ulaznih podataka imamo bolje učenje, tj. r2_score je blize 1