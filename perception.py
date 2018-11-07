# lly practice perception

import numpy as np
import matplotlib.pyplot as plt

def draw(inp, label):
    for i in range(len(inp)):
        if label[i] == 1:
            plt.plot(inp[i][0], inp[i][1], 'ro')
        else:
            plt.plot(inp[i][0], inp[i][1], 'bo')


def gradient_descent(W, inter, x, label):
    for k in range(1000):
        choice = -1      # 判断是否到达最小值
        for j in range(len(x)):
            print("the predict is: {}".format(np.sign(np.dot(W, x[j]) + inter)))
            print("the item is :{}  the number is:{}".format(k, j))
            if label[j] != np.sign(np.dot(W, x[j]) + inter): # ？？？
                choice = j
                break
        if choice == -1:
            print("out in item{}".format(k))
            break
        W = W + delta * label[choice]*x[choice]
        inter = inter + delta * label[choice]
        print("the w is: {}".format(W))
        print("the intercept is: {}".format(inter))
    return W, inter
'''
shuju 
3.542485, 1.977398	-1
3.018896, 2.556416	-1
7.551510, -1.580030	1
2.114999, -0.004466	-1
8.127113, 1.274372	1
7.108772, -0.986906	1
8.610639, 2.046708	1
'''
p_x = np.array([[2.5, 2.0], [2.04, 2.6], [3.6, 2.6], [1.1, -0.1],
                [4.1, 1.3], [3.14, -1.0], [4.6, 2.0]])
y = np.array([-1, -1, 1, -1, 1, 1, 1])
plt.figure()   # 打开画布 好像不打开也能用。。。
w = np.array([1, 0])
b = 0
delta = 0.1
draw(p_x, y)
w, b = gradient_descent(w, b, p_x, y)
print("the W is: {}".format(w))
print("the intercept is: {}".format(b))
# 绘制超平面
line_x = np.array([0, 6])
line_y = [0, 0]
for i in range(len(line_x)):
    line_y[i] = (-w[0] * line_x[i] - b)/w[1]
    print("x is {} and y is {}".format(line_x[i], line_y[i]))
plt.plot(line_x, line_y)
plt.show()
plt.savefig("picture.pdf")
