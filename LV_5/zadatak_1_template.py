import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

from sklearn . linear_model import LogisticRegression
from sklearn . metrics import accuracy_score,precision_score,recall_score
from sklearn . metrics import confusion_matrix , ConfusionMatrixDisplay


X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                            random_state=213, n_clusters_per_class=1, class_sep=1)

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

# a
plt.figure()
plt.scatter(X_train[:,0],X_train[:,1],c=y_train,cmap='coolwarm')
plt.scatter(X_test[:,0],X_test[:,1],c=y_test,cmap='coolwarm',marker='x')


# b
LogRegression_model = LogisticRegression ()
LogRegression_model . fit ( X_train , y_train )

# c
print(LogRegression_model.coef_)
th = LogRegression_model.coef_[0]
a = -th[0] / th[1]
x1 = np.linspace(-5, 5)
x2 = a * x1 - (LogRegression_model.intercept_[0]) / th[1]

plt.plot(x1, x2, 'k-')
plt.show()

#d
y_pred = LogRegression_model . predict ( X_test )

cm = confusion_matrix ( y_test , y_pred )
print (" Matrica zabune:\n" , cm )
disp = ConfusionMatrixDisplay ( confusion_matrix ( y_test , y_pred ) )
disp . plot ()
plt . show ()

print("Accuracy: " , accuracy_score(y_test , y_pred ))
print("Precision: ", precision_score(y_test , y_pred ))
print("Recall: ", recall_score(y_test , y_pred))


# e

customCmap = matplotlib.colors.ListedColormap(["red", "blue"])
customCmap2 = matplotlib.colors.ListedColormap(["orange", "green"]) #Black and Green are too similar
y_isTrue = np.arange(len(y_test))

for i in range(len(y_test)):
    if(y_test[i] == y_pred[i]):
        y_isTrue[i] = 1
    else:
        y_isTrue[i] = 0

plt.figure()
plt.scatter(X_test[:,0],X_test[:,1],c=y_isTrue,cmap=customCmap)
plt.show()

print(y_test,'\n',y_pred,'\n',y_isTrue)

