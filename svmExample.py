#array conversion
import numpy as np
#data visualisation
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn import svm

#sample set of two features
x = [1, 5, 1.5, 8, 1, 9, 0.2, 6.8]
y = [2, 8, 1.8, 8, 0.6, 11, 0.8, 7]

#graph data in scatter plot
plt.scatter(x,y)
#plt.show()

#x and y coordinates into an array, x is a feature and y is a feature
X = np.array([[1,2],
             [5,8],
             [1.5,1.8],
             [8,8],
             [1,0.6],
             [9,11],
             [0.2,0.8], 
             [6.8,7]])

#label our array, using 0 or 1 depending on where it lands in the graph.
y = [0,1,0,1,0,1,0,1]
#define classifier with clf
#(support vector classifier, support vector machine)
#C is "how badly" you want to properly classify or fit everything
#it is complicated and relatively new, 1.0 is default.
clf = svm.SVC(kernel='linear', C = 1.0)

clf.fit(X,y)

example = np.array([7.58,9.76])
example = example.reshape(1, -1)
prediction = clf.predict(example)
print(prediction)

w = clf.coef_[0]
print(w)

a = -w[0] / w[1]

xx = np.linspace(0,12)
yy = a * xx - clf.intercept_[0] / w[1]

h0 = plt.plot(xx, yy, 'k-', label="non weighted div")

plt.scatter(X[:, 0], X[:, 1], c = y)
plt.legend()
plt.show()



