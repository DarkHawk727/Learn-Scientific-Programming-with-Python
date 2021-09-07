from typing import Match


import math

class Star():

    def __init__(self, name, magnitude, right_ascention, declination) -> None:
        self.name = name
        self.magnitude = magnitude
        self.right_ascention = right_ascention
        self.declination = declination

    def project_orthographic(self, right_ascention_0, declination_0):

        delta_right_ascention = self.right_ascention - self.right_ascention_0
        self.x = math.cos(self.declination) * math.sin(self.delta_right_ascention)
        self.y = math.sin(self.declination) * math.cos(declination_0) / math.cos(self.declination) * math.cos(delta_right_ascention) * math.sin(declination_0)

        return self.x, self.y
