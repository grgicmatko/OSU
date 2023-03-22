import numpy as np
import matplotlib . pyplot as plt

black = np.zeros((50,50))
white = np.ones((50,50))*255

col1 = np.vstack((black,white))
col2 = np.vstack((white,black))

img = np.hstack((col1,col2))

plt . imshow ( img , cmap ="gray")
plt . show ()
