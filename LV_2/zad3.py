import numpy as np
import matplotlib . pyplot as plt

originalImg = plt . imread ("road.jpg")
originalImg = originalImg [ :,:,0]. copy ()

img = originalImg - 20

plt . imshow ( img , cmap ="gray")
plt . show ()

croppedImg = img[0:,int(len(img[0])*0.25):int(len(img[0])*0.5)]
plt . imshow ( croppedImg , cmap ="gray")
plt . show ()

rotatedImg = originalImg
for i in range(3):
    rotatedImg = np.rot90(rotatedImg)

plt . imshow (rotatedImg , cmap ="gray")
plt . show ()

mirroredImage = originalImg[:,::-1]

plt . imshow (mirroredImage , cmap ="gray")
plt . show ()