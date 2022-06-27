import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

eph_names = ["earth", "mars", "jupiter", "saturn", "uranus", "voyager2"]


def get_eph_data(filepath):
    """
    Get the orbital data for the given ephemeris.
    """

    def parse_line(line):
        """Parse a single line of the data file, returning position, (x,y,z)."""
        sx, sy, sz = line[4:26], line[30:52], line[56:78]
        return float(sx), float(sy), float(sz)

    dates, xyz = [], []
    with open(filepath) as fi:
        while not fi.readline().strip() == "$$SOE":
            pass
        while True:
            line = fi.readline().rstrip()
            if line == "$$EOE":
                break
            if "A.D." in line:
                date = line[25:36]
                if date.startswith("1988-Jul"):
                    break
                dates.append(date)
            elif line.startswith(" X ="):
                xyz.append(parse_line(line))
    return dates, np.array(xyz).T


class Ephemeris:
    def __init__(self, r, c, trajectory):
        self.r = r
        self.c = c
        self.date_series, self.traj = trajectory

    def get_xy(self, i=None):
        """
        Get the x, y position of the object. If i is None, return the entire
        trajectory in an array, otherwise return the position at index i.
        """
        if i is None:
            return self.traj[:2]
        return self.traj[0][i], self.traj[1][i]


ephemerides = {
    "earth": Ephemeris(
        0.3,
        "tab:blue",
        get_eph_data(
            "C:/Users/Arjun Sarao/Learn-Scientific-Programming-with-Python-Solutions/LSPwP_accompanying_files/earth.txt"
        ),
    ),
    "mars": Ephemeris(
        0.3,
        "tab:red",
        get_eph_data(
            "C:/Users/Arjun Sarao/Learn-Scientific-Programming-with-Python-Solutions/LSPwP_accompanying_files/mars.txt"
        ),
    ),
    "jupiter": Ephemeris(
        0.6,
        "tab:orange",
        get_eph_data(
            "C:/Users/Arjun Sarao/Learn-Scientific-Programming-with-Python-Solutions/LSPwP_accompanying_files/jupiter.txt"
        ),
    ),
    "saturn": Ephemeris(
        0.5,
        "brown",
        get_eph_data(
            "C:/Users/Arjun Sarao/Learn-Scientific-Programming-with-Python-Solutions/LSPwP_accompanying_files/saturn.txt"
        ),
    ),
    "uranus": Ephemeris(
        0.4,
        "tab:green",
        get_eph_data(
            "C:/Users/Arjun Sarao/Learn-Scientific-Programming-with-Python-Solutions/LSPwP_accompanying_files/uranus.txt"
        ),
    ),
    "voyager2": Ephemeris(
        0.2,
        "w",
        get_eph_data(
            "C:/Users/Arjun Sarao/Learn-Scientific-Programming-with-Python-Solutions/LSPwP_accompanying_files/voyager2.txt"
        ),
    ),
}

fig, ax = plt.subplots()
fig.patch.set_facecolor("k")
ax.axis("off")


e_objects = []
for name, eph in ephemerides.items():
    if name != "voyager2":
        ax.plot(*eph.get_xy(), c=eph.c, lw=0.5)
    # Circles represent each of the objects; start in initial positions.
    e_circ = Circle(xy=eph.get_xy(0), radius=eph.r, fc=eph.c, zorder=10)
    ax.add_patch(e_circ)
    e_objects.append(e_circ)
(e_line,) = ax.plot([], [], c=ephemerides["voyager2"].c, lw=0.5)
e_objects.append(e_line)
label = ax.text(15, 15, "", c="w")
e_objects.append(label)


def init():
    for i, ephemeris in enumerate(ephemerides.values()):
        e_objects[i].center = ephemeris.get_xy(0)
    e_line.set_data([], [])
    return e_objects


def reformat_date(date):
    """
    Reverse date string from YYYY-Mon-DD to DD-Mon-YYYY.
    """
    return "-".join(date.split("-")[::-1])


def animate(j):
    """
    Advance the animation by one time step.
    """
    for i, ephemeris in enumerate(ephemerides.values()):
        e_circ = e_objects[i]
        e_circ.set_center(ephemeris.get_xy(j))
        e_line.set_data(ephemeris.traj[0][:j], ephemeris.traj[1][:j])
    e_line.set_data(
        ephemerides["voyager2"].traj[0][:j], ephemerides["voyager2"].traj[1][:j]
    )
    label.set_text(reformat_date(ephemerides["voyager2"].date_series[j]))

    return e_objects


lim = 25
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)
ani = animation.FuncAnimation(fig, animate, interval=1, init_func=init, blit=True)
plt.show()
