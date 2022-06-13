# Python Code for Implementation and running time Algorithm
# Plots its time Complexity on list of different sizes
import numpy as np
import matplotlib.pyplot as plt
try:
    plt.style.use("bmh")
    n = np.linspace(1, 10, 1000)
    labels = ['constant','Logarithmic','Linear','Log Linear','Qaudratic','Exponential']
    big_o = [np.ones(n.shape), np.log(n), n, n*np.log(n), n**2, n**3, 2**n]

    plt.figure(figsize=(12, 10))
    plt.ylim(0, 40)
    for i in range(len(big_o)):
        plt.plot(n, big_o[i-1], label=labels[i])

    plt.legend(loc=0)
    plt.title("Big-o notations")
    plt.ylabel("Relative Runtime")
    plt.xlabel('Input Size')
    plt.grid()
    plt.show()
except:
    pass