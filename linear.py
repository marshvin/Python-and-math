import numpy as np
import matplotlib.pyplot as plt
def array():
    xvalue = np.array([1, 2, 3, 4, 5, 6])
    count = 0
    yvalue = []
    for i in range(len(xvalue)):
        count = count + 1
        yvalue.append(count)

    x = np.array(xvalue)
    y = np.array(yvalue)
    plt.plot(x, y, "r")
    plt.xlabel("input")
    plt.ylabel("iterations")
    plt.title("Linear time O(n)")
    plt.grid()
    plt.show()

array()