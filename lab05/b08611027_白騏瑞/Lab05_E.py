from numpy import sin, cos
from collections import deque
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

G = 9.8  # acceleration due to gravity, in m/s^2
L1 = 1.0  # length of pendulum 1 in m
L2 = 1.0  # length of pendulum 2 in m
M1 = 1.0  # mass of pendulum 1 in kg
M2 = 1.0  # mass of pendulum 2 in kg
history1_len = 20  # number of points in the first trace
history2_len = 50  # number of points in the second trace
num_transparencies = 10  # number of transparency values used in the trace


def derivs(state, t):

    dydx = np.zeros_like(state)
    dydx[0] = state[1]

    delta = state[2] - state[0]
    den1 = (M1+M2) * L1 - M2 * L1 * cos(delta) * cos(delta)
    dydx[1] = ((M2 * L1 * state[1] * state[1] * sin(delta) * cos(delta)
                + M2 * G * sin(state[2]) * cos(delta)
                + M2 * L2 * state[3] * state[3] * sin(delta)
                - (M1+M2) * G * sin(state[0]))
               / den1)

    dydx[2] = state[3]

    den2 = (L2/L1) * den1
    dydx[3] = ((- M2 * L2 * state[3] * state[3] * sin(delta) * cos(delta)
                + (M1+M2) * G * sin(state[0]) * cos(delta)
                - (M1+M2) * L1 * state[1] * state[1] * sin(delta)
                - (M1+M2) * G * sin(state[2]))
               / den2)

    return dydx

# create a time array from 0..100 sampled at 0.05 second steps
dt = 0.05
t = np.arange(0, 20, dt)

# th1 and th2 are the initial angles (degrees)
# w10 and w20 are the initial angular velocities (degrees per second)
th1 = 120.0
w1 = 0.0
th2 = -10.0
w2 = 0.0

# initial state
state = np.radians([th1, w1, th2, w2])

# integrate your ODE using scipy.integrate.
y = integrate.odeint(derivs, state, t)

x1 = L1*sin(y[:, 0])
y1 = -L1*cos(y[:, 0])

x2 = L2*sin(y[:, 2]) + x1
y2 = -L2*cos(y[:, 2]) + y1

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
ax.set_aspect('equal')
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
pendulum1_trace = [ax.plot([], [], ',-', color='g', lw=1, alpha=a)[0]
                       for a in np.linspace(1, 0, num_transparencies)]
pendulum2_trace = [ax.plot([], [], ',-', color='#FF7F0E', lw=1, alpha=a)[0]
                       for a in np.linspace(1, 0, num_transparencies)]
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

# create an array to store the trajectories
history1_x = deque(maxlen=history1_len)
history1_y = deque(maxlen=history1_len)
history2_x = deque(maxlen=history2_len)
history2_y = deque(maxlen=history2_len)



def animate(i):
    curr_x = [0, x1[i], x2[i]]
    curr_y = [0, y1[i], y2[i]]

    if i == 0:
        history1_x.clear()
        history1_y.clear()

        history2_x.clear()
        history2_y.clear()

    history1_x.appendleft(curr_x[1])
    history1_y.appendleft(curr_y[1])

    history2_x.appendleft(curr_x[2])
    history2_y.appendleft(curr_y[2])

    line.set_data(curr_x, curr_y)

    h1x = list(history1_x)
    h1y = list(history1_y)
    k = history1_len // num_transparencies
    for idx, trace in enumerate(pendulum1_trace):
        p = h1x[idx * k: (idx + 1) * k + 1]
        q = h1y[idx * k: (idx + 1) * k + 1]
            # trace.set_data(p, q)

    h2x = list(history2_x)
    h2y = list(history2_y)
    k = history2_len // num_transparencies
    for idx, trace in enumerate(pendulum2_trace):
        p = h2x[idx * k: (idx + 1) * k + 1]
        q = h2y[idx * k: (idx + 1) * k + 1]
        trace.set_data(p, q)
    time_text.set_text(f'time = {i * dt:.1f} s')
    return line, pendulum1_trace, *pendulum2_trace, time_text

ani = animation.FuncAnimation(fig, animate, range(1, len(y)),
                                   interval=1000 * dt, blit=False)

plt.show()