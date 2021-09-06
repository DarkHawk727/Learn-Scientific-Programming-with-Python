import math
import random

class Polymer:
    """ A class representing a random-flight polymer in solution. """
    def __init__(self, N, a):
        """
        Initialize a Polymer object with N segments, each of length a.

        """

        self.N, self.a = N, a
        # self.xyz holds the segment position vectors as tuples
        self.xyz = [(None, None, None)] * N
        # End-to-end vector
        self.R = None
        # Make our polymer by assigning segment positions
        self.make_polymer()


    def make_polymer(self):
        """
        Calculate the segment positions, centre of mass and end-to-end
        distance for a random-flight polymer.

        """

        # Start our polymer off at the origin, (0,0,0).
        self.xyz[0] = x, y, z = cx, cy, cz = 0., 0., 0.
        for i in range(1, self.N):
            # Pick a random orientation for the next segment.
            theta = math.acos(2 * random.random() - 1)
            phi = random.random() * 2. * math.pi
            # Add on the corresponding displacement vector for this segment.
            x += self.a * math.sin(theta) * math.cos(phi)
            y += self.a * math.sin(theta) * math.sin(phi)
            z += self.a * math.cos(theta)
            # Store it, and update or centre of mass sum.
            self.xyz[i] = x, y, z
            cx, cy, cz = cx + x, cy + y, cz + z
        # Calculate the position of the centre of mass.
        cx, cy, cz = cx / self.N, cy / self.N, cz / self.N
        # The end-to-end vector is the position of the last
        # segment, since we started at the origin.
        self.R = x, y, z

        # Finally, re-centre our polymer on the centre of mass.
        for i in range(self.N):
            self.xyz[i] = self.xyz[i][0]-cx,self.xyz[i][1]-cy,self.xyz[i][2]-cz 

            
    def calc_Rg(self):
        """
        Calculates and returns the radius of gyration, Rg. The polymer
        segment positions are already given relative to the centre of
        mass, so this is just the rms position of the segments.

        """

        self.Rg = 0.
        for x,y,z in self.xyz:
            self.Rg += x**2 + y**2 + z**2
        self.Rg = math.sqrt(self.Rg / self.N)
        return self.Rg

    
    def save_SVG(self, svg_name='C:/Users/arjun/Learn-Scientific-Programming-with-Python-Solutions/Section 4.6/P4.6.2/polymer_svg.svg'):
        canvas_height = 500
        canvas_width = 500
        f = open(svg_name, 'w')
        print("""<?xml version="1.0" encoding="utf-8"?>
                 <svg xmlns="http://www.w3.org/2000/svg"
                      xmlns:xlink="http://www.w3.org/1999/xlink"
                      width="{}" height="{}" style="background: {}">""".format(
                        canvas_width, canvas_height, '#ffffff'), file=f)

        ccx = canvas_width / 2
        ccy = canvas_height / 2

        scale = 10

        x, y, z = zip(*self.xyz)

        x_min = min(x)
        x_max = max(x)
        y_min = min(y)
        y_max = max(y)

        d_max = max(x_max - x_min, y_max - y_min)

        scale = min(canvas_height, canvas_height) / d_max

        for i in range(1, self.N):
            x1 = x[i-1] * scale + ccx
            y1 = y[i-1] * scale + ccy
            x2 = x[i] * scale + ccx
            y2 = y[i] * scale + ccy
            print('<line x1="{:.1f}" y1="{:.1f}" x2="{:.1f}" y2="{:.1f}"'
                        ' style="stroke: {:s}; stroke-width: {:d};"/>'.format(
                   x1, y1, x2, y2, 'black', 2), file=f)
        print('</svg>', file=f)


