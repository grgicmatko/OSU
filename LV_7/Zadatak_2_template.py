import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as Image
from sklearn.cluster import KMeans
from mpl_toolkits import mplot3d

# ucitaj sliku
img = Image.imread("imgs\\test_1.jpg")

# prikazi originalnu sliku
plt.figure()
plt.title("Originalna slika")
plt.imshow(img)
plt.tight_layout()
plt.show()


clusters = 4
# pretvori vrijednosti elemenata slike u raspon 0 do 1
img = img.astype(np.float64) / 255

# transfromiraj sliku u 2D numpy polje (jedan red su RGB komponente elementa slike)
(h,w,c) = img.shape
img_array = np.reshape(img, (h*w, c))

# rezultatna slika
img_array_aprox = img_array.copy()

# broj razlicitih boja u slici
print(len(np.unique(img_array_aprox,axis=0)))

# primjena K-means algoritma
km = KMeans ( n_clusters =clusters ) 
labels = km.fit_predict(img_array_aprox)

# promjena vrijednosti u K-means centre
rgb_cols = km.cluster_centers_.astype(np.float64)
print(rgb_cols)
img_quant = np.reshape(rgb_cols[labels],(h,w,c))

plt.imshow(img_quant)
plt.show()


for i in range(clusters):
    bit_values = labels==[i]
    binary_img = np.reshape(bit_values, (img.shape[0:2]))
    binary_img = binary_img*1
    x=int(i/2)
    y=i%2
    plt.imshow(binary_img)
    plt.show()





