import numpy as np
import matplotlib . pyplot as plt



my_data = np.loadtxt('data.csv', delimiter=',',skiprows=1)
print(len(my_data)) #number of rows/people

plt.scatter(my_data[:, 1], my_data[:, 2], s=1)
plt.scatter(my_data[::50, 1], my_data[::50, 2], s=1)
plt.show()

print(min(my_data[:,1]))
print(max(my_data[:,1]))
print(np.mean(my_data[:,1]))

male = (my_data[:,0] == 1)
female = (my_data[:,0] == 0)

print("Men")
print(min(my_data[male,1]))
print(max(my_data[male,1]))
print(np.mean(my_data[male,1]))

print("Women")
print(min(my_data[female,1]))
print(max(my_data[female,1]))
print(np.mean(my_data[female,1]))


