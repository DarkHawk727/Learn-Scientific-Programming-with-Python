import math
import sys

def haversin(alpha):
    return math.sin(alpha / 2) ** 2

R = 6378.1

phi_1 = math.radians(float(sys.argv[1].split(',')[0]))
lambda_1 = math.radians(float(sys.argv[1].split(',')[1]))

phi_2 = math.radians(float(sys.argv[2].split(',')[0]))
lambda_2 = math.radians(float(sys.argv[2].split(',')[1]))

dLon = phi_2 - phi_1
dLat = lambda_2 - lambda_1

d = 2 * R * math.atan(math.sqrt(haversin(dLon) + math.cos(phi_1) * math.cos(phi_2) * haversin(dLat)))


print('{:.2f} km.'.format(d))