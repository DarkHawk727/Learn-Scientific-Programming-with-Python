import os
import math

def create_coords_x(angle):
    x = 200 * math.sin(2 * math.pi * angle / 360) + 250
    return x

def create_coords_y(angle):
    y = 200 * math.cos(2 * math.pi * angle / 360) + 250
    return y

for i in range(21):
    angle = (360 / 20) * i
    file_name = 'C:/Users/arjun/Desktop/SVGFiles/fig{0:02d}.svg'.format(i)
    svg_file = open(file_name,'x')
    
    with open('C:/Users/arjun/Desktop/SVGFiles/svgcode.txt', 'r') as svg_code:
        for line in svg_code.readlines():
            svg_file.writelines(line)
        svg_file.write('<circle cx="{0:0.1f}" cy="{1:0.1f}" r="20" style="stroke: red; fill: red;"/>'.format(create_coords_x(angle), create_coords_y(angle)))
        svg_file.write('</svg>')