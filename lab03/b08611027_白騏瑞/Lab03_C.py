import numpy as np

def swap_rows(x, r1, r2):
    x[[r1, r2]] = x[[r2, r1]]

def most_value(x):    
    return np.bincount(x).argmax()

def top_n(x, n):
    sorted_index_array = np.argsort(x)
    sorted_array = x[sorted_index_array]
    tops = sorted_array[-n:]

    return tops
    
def pythagorean(x):
    x_hypotenuse = np.hypot(x[:,0], x[:, 1])
    a = np.array([x_hypotenuse])
    return np.concatenate((x, a.T), axis=1)

def replace_me(v, a, b=None, c=None):
    if b is None:
        b = c = 0
    elif c is None:
        c = b

    x = v.copy()
    where = np.argwhere(v == a).flatten()
    x[where] = b
    x = np.insert(x, where[0]+1, c)
   
    return x


# You may test your function here
def main():

    # Lab04_C1 Swap rows
    print('Lab04_C1 Swap rows:')
    x1 = np.arange(9).reshape(3, 3)
    swap_rows(x1, 0, 1)
    print(x1, '\n')

    # Lab04_C2 Find most frequent value
    print('Lab04_C2 Find most frequent value:')
    x2 = np.array([1, 2, 2, 1, 3, 2, 4, 1, 2])
    print('The most frequent value is: ', most_value(x2), '\n')

    # Lab04_C3 top n
    print('Lab04_C3 Top n:')
    x3 = np.array([1, 0, 3, 5, 7, 3, 2, 8, 9, 2, 8])
    print('The 3 largest values are: ', top_n(x3, n=3), '\n')

    # Lab04_C4 pythagorean
    print('Lab04_C4 pythagorean:')
    x4 = np.array([[3, 4], [5, 12]])
    print(pythagorean(x4))

    try:
        pythagorean(np.array([12]))
        print('If you see this line, you may not check the input array', '\n')
    except:
        print('\n')

    # Lab04_C5 replace_me
    print('Lab04_C5 replace_me:')
    x5 = np.array([1, 2, 3])
    print(replace_me(x5, 2, 4, 5), '\n')


if __name__ == "__main__":
    main()