import torch
import math
import numpy as np
import matplotlib.pyplot as plt


def get_grad_y(start_position, end_position, accuracy):
    data = []
    for i in range(start_position * accuracy, (end_position + 1)*accuracy):
        x = torch.tensor(float(i/accuracy), requires_grad=True)
        y = torch.sin(x) * x
        y.backward()
        data.append(x.grad.item())
    return data


def get_y(start_position, end_position, accuracy):
    data = []
    for i in range(start_position * accuracy, (end_position + 1)*accuracy):
        data.append(math.sin(i/accuracy) * i/accuracy)
    return data


def get_x(start_position, end_position, accuracy):
    return [float(i/accuracy) for i in range(start_position * accuracy,
                                             (end_position + 1)*accuracy)]


def draw(start, end, accuracy):
    points_grad_y = get_grad_y(start, end, accuracy)
    points_x = get_x(start, end, accuracy)
    points_y = get_y(start, end, accuracy)
    plt.plot(points_x, points_grad_y, label='grad of sin(x) * x')
    plt.plot(points_x, points_y, label='sin(x) * x')
    plt.xlabel(r'$x$', fontsize=16)
    plt.ylabel(r'$f(x), f\'(x)$', fontsize=16)
    plt.grid()
    plt.legend()
    plt.show()


def main():
    draw(-20, 20, 10)


if __name__ == '__main__':
    main()







