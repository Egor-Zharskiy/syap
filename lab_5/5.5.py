import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def func(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot_surface(x, y, z)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()


# Построить графики функций

x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)

X, Y = np.meshgrid(x, y)
Z = np.power(X, 0.25) + np.power(Y, 0.25)

func(X, Y, Z)
Z = X ** 2 - Y ** 2

fig = plt.figure()
func(X, Y, Z)

Z = 2 * X + 3 * Y
func(X, Y, Z)

Z = X ** 2 + Y ** 2
func(X, Y, Z)

Z = 2 + 2 * X + 2 * Y - X ** 2 - Y ** 2
func(X, Y, Z)
