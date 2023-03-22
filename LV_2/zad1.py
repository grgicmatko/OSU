import numpy as np
import matplotlib . pyplot as plt

x = np.array([1,2,3,3,1], float)
y = np.array([1,2,2,1,1], float)
plt.plot(x,y,'g',linewidth =3 , marker ="*", markersize =12)
plt . axis ([0.0 ,4.0 ,0.0 ,4.0])
plt . xlabel ('x')
plt . ylabel ('vrijednosti funkcije')
plt . title ('Primjer')
plt . show ()