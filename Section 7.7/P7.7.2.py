import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

w = h = 10.0
dx = dy = 0.1
D = 4.0

T_cool, T_hot = 300, 700

nx, ny = int(w / dx), int(h / dy)

dx2, dy2 = dx * dx, dy * dy
dt = dx2 * dy2 / (2 * D * (dx2 + dy2))

u_0 = T_cool * np.ones((nx, ny))
u = u_0.copy()

r, cx, cy = 2, 5, 5
r2 = r**2
for i in range(nx):
    for j in range(ny):
        p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
        if p2 < r2:
            u_0[i, j] = T_hot


def do_timestep(u_0: np.array, u: np.array) -> tuple:
    """
    Propagate with forward-difference in time, central-difference in space
    """ 
    u[1:-1, 1:-1] = u_0[1:-1, 1:-1] + D * dt * (
        (u_0[2:, 1:-1] - 2 * u_0[1:-1, 1:-1] + u_0[:-2, 1:-1]) / dx2
        + (u_0[1:-1, 2:] - 2 * u_0[1:-1, 1:-1] + u_0[1:-1, :-2]) / dy2
    )

    u_0 = u.copy()
    return u_0, u



num_steps = 500
fig = plt.figure()
ax = fig.add_subplot()

im = ax.imshow(
    u_0, cmap=plt.get_cmap("magma"), vmin=T_cool, vmax=T_hot, interpolation="bicubic"
)
ax.set_axis_off()
ax.set_title("0.0 ms")

fig.subplots_adjust(right=0.85)
cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
cbar_ax.set_xlabel("$T$ / K", labelpad=20)
fig.colorbar(im, cax=cbar_ax)


def animate(i: int) -> None:
    """
    Animate the ith frame.
    """
    global u_0, u
    u_0, u = do_timestep(u_0, u)
    ax.set_title(f"{i * dt * 1000:.1f} ms")
    im.set_data(u.copy())


interval = 10

ani = animation.FuncAnimation(fig, animate, frames=num_steps, interval=interval)
plt.show()
