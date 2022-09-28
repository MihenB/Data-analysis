import numpy as np
import matplotlib.pyplot as plt


def y(x, a1, a2, b):
    if a2 != 0:
        return (b - a1 * x) / a2
    else:
        print("Impossible to build a graph")
        return 0


try:
    a11, a12, b1 = map(float, input().split(' '))
    a21, a22, b2 = map(float, input().split(' '))

    matrix_a = np.array([[a11, a12],
                         [a21, a22]])
    matrix_b = np.array([b1, b2])
    matrix = np.array([[a11, a12],
                       [a21, a22],
                       [b1, b2]])
    det = np.linalg.det(matrix_a)
    if det != 0:
        x = np.linspace(-100, 100, 100)
        reversed_matrix_a = np.linalg.inv(matrix_a)
        answer = np.matmul(reversed_matrix_a, matrix_b)
        plt.scatter(answer[0], answer[1])
        print(answer)
        plt.plot(x, y(x, a11, a12, b1), label='first equation')
        plt.plot(x, y(x, a21, a22, b2), label='second equation')
    else:
        x = np.linspace(-100, 100, 100)
        if np.linalg.matrix_rank(matrix) == np.linalg.matrix_rank(matrix_a) \
                and np.linalg.matrix_rank(matrix_a) < 2:
            print("Infinity solves")
            plt.plot(x, y(x, a11, a12, b1), label='first equation')
            plt.plot(x, y(x, a21, a22, b2), label='second equation')

        else:
            print("Solve not existence")
            plt.plot(x, y(x, a11, a12, b1), label='first equation')
            plt.plot(x, y(x, a21, a22, b2), label='second equation')
    plt.xlabel(r'$x$', fontsize=16)
    plt.ylabel(r'$y(x)$', fontsize=16)
    plt.grid()
    plt.legend()
    plt.show()
except ValueError:
    print("Invalid input format")


