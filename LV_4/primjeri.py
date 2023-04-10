#primjer 1
from sklearn import datasets
from sklearn . model_selection import train_test_split
# ucitaj ugradeni podatkovni skup
X , y = datasets . load_diabetes ( return_X_y = True )
# podijeli skup na podatkovni skup za ucenje i poda tkovni skup za testiranje
X_train , X_test , y_train , y_test = train_test_split (X , y , test_size = 0.2 , random_state =1 )

#primjer 2
from sklearn . preprocessing import MinMaxScaler
# min - max skaliranje
sc = MinMaxScaler ()
X_train_n = sc . fit_transform ( X_train )
X_test_n = sc . transform ( X_test )

