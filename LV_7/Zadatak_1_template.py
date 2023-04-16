import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import dendrogram
from sklearn.datasets import make_blobs, make_circles, make_moons
from sklearn.cluster import KMeans, AgglomerativeClustering


def generate_data(n_samples, flagc):
    # 3 grupe
    if flagc == 1:
        random_state = 365
        X,y = make_blobs(n_samples=n_samples, random_state=random_state)
    
    # 3 grupe
    elif flagc == 2:
        random_state = 148
        X,y = make_blobs(n_samples=n_samples, random_state=random_state)
        transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
        X = np.dot(X, transformation)

    # 4 grupe 
    elif flagc == 3:
        random_state = 148
        X, y = make_blobs(n_samples=n_samples,
                        centers = 4,
                        cluster_std=np.array([1.0, 2.5, 0.5, 3.0]),
                        random_state=random_state)
    # 2 grupe
    elif flagc == 4:
        X, y = make_circles(n_samples=n_samples, factor=.5, noise=.05)
    
    # 2 grupe  
    elif flagc == 5:
        X, y = make_moons(n_samples=n_samples, noise=.05)
    
    else:
        X = []
        
    return X

# generiranje podatkovnih primjera
X = generate_data(10000, 4)

# prikazi primjere u obliku dijagrama rasprsenja
plt.figure()
plt.scatter(X[:,0],X[:,1],s=3)
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title('podatkovni primjeri')
plt.show()


# inicijalizacija algoritma K srednjih vrijednosti
km = KMeans ( n_clusters =8 , init ='random',n_init =10 , random_state =0 )

# pokretanje grupiranja primjera
km . fit ( X )

# dodijeljivanje grupe svakom primjeru
labels = km.predict ( X )

plt.figure()
plt.scatter(X[:,0],X[:,1],s=3,c=labels)
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title('podatkovni primjeri')
plt.show()

distortions = []
K = range(1,10)
for k in K:
    kmeanModel = KMeans ( n_clusters =k , init ='random',n_init =10 , random_state =0 )
    kmeanModel.fit(X)
    distortions.append(kmeanModel.inertia_) #inertia mjeri koliko je dobro dataset grupiran K-means metodom

plt.plot(K, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k')
plt.show()

km = KMeans ( n_clusters =4 , init ='random',n_init =10 , random_state =0 ) #4 is an elbow value
km . fit ( X )
labels = km.predict ( X )

plt.figure()
plt.scatter(X[:,0],X[:,1],s=3,c=labels)
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title('podatkovni primjeri')
plt.show()

#After value k=4, J stops rapid decline. (J from LV7.pdf)

