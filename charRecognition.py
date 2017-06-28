#Importing necessary Modules.
#pyplot is used to plot chart.
#SVM is the sklearn Support Vector Machine
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

#define loaded digit dataset.
digits = datasets.load_digits()
#specify classifier
clf = svm.SVC(gamma=0.00001, C=100)

print(len(digits.data))
#loads in all but last 10 data points for testing.
#X is all of cooridinates and y is target.
#x is pixel data in this case, y is the actual number
X,y = digits.data[:-10], digits.target[:-10]
#train the machine
clf.fit(X,y)
#predict 5th from the last element.
print(clf.predict(digits.data[-5]))
#visualize this with an image of the number in question.
plt.imshow(digits.images[-5], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()
