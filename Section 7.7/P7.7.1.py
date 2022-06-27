import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.special import ellipk

m, L, g = 1, 1, 9.81

theta_0, v_0 = np.radians(60), 0

T_harm = 2 * np.pi * np.sqrt(L / g)

dt = 0.001

theta, v = [theta_0], [v_0]

old_theta = theta_0


def get_coords(th: float) -> tuple:
    """
    Return the (x, y) coordinates of the bob at angle th.
    """
    return L * np.sin(th), -L * np.cos(th)


def animate(i: int) -> None:
    """
    Animate the bob at the ith frame.
    """
    x, y = get_coords(theta[i])
    line.set_data([0, x], [0, y])
    circle.set_center((x, y))


i = 0
while True:
    i += 1
    t = i * dt
    old_theta, old_velocity = theta[-1], v[-1]
    omega = old_velocity / L
    new_theta = old_theta - omega * dt

    acceleration = g * np.sin(old_theta)
    new_velocity = old_velocity + acceleration * dt

    if t > T_harm and new_velocity * old_velocity < 0:
        break
    theta.append(new_theta)
    v.append(new_velocity)
num_steps = len(theta)
T = num_steps * dt
print(f"Calculated period, T = {T} s")
print(f"Estimated small-displacement angle period, Tharm = {T_harm} s")
k = np.sin(theta_0 / 2)
print(f"SciPy calculated period, T = {2 * T_harm / np.pi * ellipk(k**2)} s")


fig = plt.figure()
ax = fig.add_subplot(aspect="equal")

x_0, y_0 = get_coords(theta_0)
(line,) = ax.plot([0, x_0], [0, y_0], lw=3, c="k")

bob_radius = 0.08
circle = ax.add_patch(plt.Circle(get_coords(theta_0), bob_radius, fc="r", zorder=3))

ax.set_xlim(-L * 1.5, L * 1.5)
ax.set_ylim(-L * 1.5, L * 1.5)

num_frames = num_steps
interval = dt * 1000
ani = animation.FuncAnimation(
    fig, animate, frames=num_frames, repeat=True, interval=interval
)
plt.show()
