import numpy as np
import matplotlib.pyplot as plt


def transition_matrix(n):
    P = np.zeros([n, n], dtype=float)

    a = np.arange(1, (n +1 )//2)
    b = np.arange((n + 1)//2, n - 1)

    # rule1
    P[a, a+1] = 0.6
    P[a, a-1] = 0.35
    P[a, 0] += 0.05

    # rule2
    P[b, b+1] = 0.5
    P[b, b-1] = 0.4
    P[b, 0] += 0.1

    # rule3
    P[0, 0] = 0.4
    P[0, 1] = 0.6

    # rule4
    P[n-1, 0] = 0.1
    P[n-1, -2] = 0.4 
    P[n-1, -1] = 0.5


    return P

def propagate(x0, P, k):
    xk = np.matmul(x0, np.linalg.matrix_power(P, k))

    return xk

def create_sample(s0, P, k, trajectories = None, rng = None):

    if trajectories is None:
        rng = np.random.default_rng()

    if trajectories is None:
        trajectories = np.zeros(k+1)

    trajectories[-k - 1] = s0

    if k == 0:
        return trajectories
    else:
        s1 = rng.choice(P.shape[0], p = P[s0])
    return create_sample(s1, P, k - 1, trajectories = trajectories, rng = rng)
        
def plot_distribution(x):
    plt.plot(x)
    plt.xticks(np.arange(0, len(x), step=1))
    plt.ylim(0, max(x)+0.1)
    plt.xlabel('State (i)')
    plt.ylabel('Probability')
    plt.title('Probability Distribution')
    plt.savefig('Lab04_D3.png', dpi=150)

def plot_histogram(x):
    plt.hist(x, bins=int(max(x)+1), range=(-0.5, int(max(x)+0.5)))
    plt.xticks(np.arange(0, max(x)+1, step=1))
    plt.xlabel('State (i)')
    plt.ylabel('Number of smaple')
    plt.title('State Histogram')
    plt.savefig('Lab04_D7.png', dpi=150)
    
def main():
    
    # TODO_D3, D4, D5,and D7
    # D3
    n = 10
    P = transition_matrix(n)
    print(P)
    x0 = np.zeros(n)
    x0[0] = 1

    x8 = propagate(x0, P, k=8)
    # plot_distribution(x8)

    # D4
    step = 0
    x_step = x0.copy()
    while True:
        if(x_step[9] < 0.01):
            x_step = propagate(x_step, P, 1)
            step += 1
        else:
            break
    print(step)

    # D5
    # y = np.random.random(n)
    # y0 = y/np.sum(y)
    # y8 = propagate(y0, P, k=8)
    # plot_distribution(y8)

    # D7
    last_steps = np.zeros(1000)
    for i in range(1, 1000):
        last_steps[i] = (create_sample(s0=0, P=P, k=8)[-1])
        i+=1
    print("last_steps", last_steps)
    plot_histogram(last_steps)

if __name__ == "__main__":
    main()