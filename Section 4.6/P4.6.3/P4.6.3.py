import math
import sys
import Star

stars = []

try:
    constellation = sys.argv[1]
except IndexError:
    print('Constellation is unrecognized!')

with open('C:/Users/arjun/Learn-Scientific-Programming-with-Python-Solutions/LSPwP accompanying files/bsc5.dat') as data:
    for line in data.readlines():
        if line[11:14] != constellation:
            continue
        name = line[4:14]

        try:
            magnitude = float(line[102:107])
        except ValueError:
            continue

    right_ascension_hours, right_ascension_minutes, right_ascension_seconds = [float(x) for x in (line[75:77], line[77:79], line[79:83])]
    declination_degrees, declination_minutes, declination_seconds = [float(x) for x in (line[83:86], line[86:88], line[88:90])]

    right_ascension = math.radians((right_ascension_hours + right_ascension_minutes / 60 + right_ascension_seconds / 3600) * 15.0)
    declination = math.radians(declination_degrees + declination_minutes / 60 + declination_seconds / 3600)

    stars.append(Star(name, magnitude, right_ascension, declination))

if len(stars) == 0:
    print('Constellation not found!')
else:
    print('Found {:d} stars in the constellation {:s}.'.format(len(stars), constellation))

right_ascension_0 = sum([Star.right_asension for star in stars]) / len(stars)
declination_0 = sum([Star.declination for star in stars]) / len(stars)

x, y = [None] * len(stars), [None] * len(stars)

for i, star in enumerate(stars):
    x[i], y[i] = Star.project_orthographic(right_ascension_0, declination_0)
    x_min = min(x)
    x_max = max(x)
    y_min = min(y)
    y_max = max(y)
    aspect_ratio = (x_max - x_min) / (y_max - y_min)

padding = 50
height = 500
width = int(height * aspect_ratio)

with open('C:/Users/arjun/Learn-Scientific-Programming-with-Python-Solutions/Section 4.6/P4.6.3/{:s}.svg'.format(constellation), 'w') as image:
    print('<?xml version="1.0" encoding="utf-8"?>', file=image  )
    print('<svg xmlns="http://www.w3.org/2000/svg"', file=image)
    print('     xmlns:xlink="http://www.w3.org/1999/xlink"', file=image)
    print('     width="{:d}" height="{:d}" style="background: #000000">'.format(width + 2*padding, height + 2*padding), file=image)

    for star in stars:
        rx = (star.x - x_min) / (x_max - x_min)
        ry = (star.y - y_min) / (y_max - y_min)
        cx = padding + (1-rx) * (width - 2*padding)
        cy = padding + (1-ry) * (height - 2*padding)
        print('<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}"'
              ' stroke="none" fill="#ffffff" name="{name:s}"/>'.format(
              cx=cx, cy=cy, r=max(1,5-star.mag), name=star.name), file=image)
    print('</svg>', file=image)