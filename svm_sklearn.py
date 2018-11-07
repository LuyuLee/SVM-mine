"""
 the data from Machine Learning in Action. peter
 text.set
"""
from sklearn import svm
import numpy as np
import matplotlib.pyplot as plt
'''from sklearn.model_selection import train_text_split'''


def load(filename):  #输入文本数据
    x = []
    y = []
    fr = open(filename)
    for line in fr.readlines():          # readlines method is used to ergodic
        lineArr = line.strip().split('\t')        # strip method is used to wipe off blank space
        x.append([float(lineArr[0]), float(lineArr[1])])
        y.append(float(lineArr[2]))
    return x, y


def plot(x, y, support_vector_index, W, b):  #draw
    for i in range (np.shape(x)[0]):  # travel x(the data)
        if y[i] == 1:
            plt.scatter(x[i][0], x[i][1], c='b', s=20)
        else:
            plt.scatter(x[i][0], x[i][1], c='y', s=20)
    for j in support_vector_index:
        if y[j] == 1:
            plt.scatter(x[j][0], x[j][1], c='', s=100, alpha=0.5, linewidth=1.5, edgecolor='r')
        else:
            plt.scatter(x[j][0], x[j][1], c='', s=100, alpha=0.5, linewidth=1.5, edgecolor='g')
    x1 = np.arange(0, 10, 0.01)   # plot the line of super plant
    y1 = (W[0][0]*x1+b)/(-1*W[0][1])
    x_neg = x1[:901]
    x_pos = x1[99:]
    support_neg = (W[0][0]*x_neg+b+1)/(-1*W[0][1])
    support_pos = (W[0][0]*x_pos+b-1)/(-1*W[0][1])
    plt.scatter(x1, y1, s=5, marker='h')
    plt.plot(x_pos, support_pos, 'r--', x_neg, support_neg, 'g--', linewidth=2.0)
    font2 = {'family': 'Times New Roman',
             'weight': 'normal',
             'size': 22,
             }
    plt.xlabel("x1", font2)
    plt.ylabel("x2", font2)
    plt.show()


x, y = load("trainSet.txt")
t, l = load("textSet.txt")
'''X_train, X_test, y_train, y_test = svm.model_selection.train_test_split(x, y, test_size=.2, random_state=0)  # cross checking'''
# #开始训练
# clf=svm.SVC() ##默认参数：kernel='rbf'
clf = svm.SVC(kernel='linear')
clf.fit(x, y)
n_support_vector = clf.n_support_ # the numble of support vector
support_vector_index = clf.support_  # to find support vector
W = clf.coef_
b = clf.intercept_
plot(x, y, support_vector_index, W, b)
print(clf)  # target
 
print(clf.support_vectors_)  # support vectors
 
print(clf.support_)  # indeices of support vectors
 
print(clf.n_support_)
print("the super plant : the W is {} the intercept is {} ".format(W, b))
print("the score  is {}".format(clf.score(t, l)))

