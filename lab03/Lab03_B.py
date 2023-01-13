import numpy as np
from random import randrange


# A = np.arange(5, -5.2, -0.2)
A = np.matrix([10, 20])

B = np.logspace(0, 1, num=101)

C = np.arange(1, 101).reshape((10, 10), order='F')

D = np.mgrid[1:13, 1:13][0] * np.mgrid[1:13, 1:13][1]

def E(X): 
    return X[::2, ::2]

def F(X):
    return X[1:-1, 1:-1]

def G(X):
    # The shape of return value will be (M, 2)
    # a = np.diag(np.diag(X, k=1), k=1)
    # b = np.diag(np.diag(X, k=-1), k=-1)
    c = np.diag(X, k=1)
    d = np.diag(X, k=-1)
    e = np.array([c, d])
    return e.T


# Do NOT modifiy the main function
def main():
    print('A: \n', A, '\n')
    print('B: \n', B, '\n')
    print('C: \n', C, '\n')
    print('D: \n', D, '\n')

    M = randrange(3, 8)
    X = np.random.randint(10, size=(M, M))

    print('X: \n', X, '\n')
    print('E: \n', E(X), '\n')
    print('F: \n', F(X), '\n')
    print('G: \n', G(X), '\n')


if __name__ == "__main__":
    main()