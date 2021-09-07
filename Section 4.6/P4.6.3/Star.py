from typing import Match


import math

class Star():

    def __init__(self, name, magnitude, right_ascension, declination):
        self.name = name
        self.magnitude = magnitude
        self.right_ascension = right_ascension
        self.declination = declination


    def project_orthographic(self, right_ascension_0, declination_0):

        delta_right_ascension = self.right_ascension - right_ascension_0
        self.x = math.cos(self.declination) * math.sin(delta_right_ascension)
        self.y = math.sin(self.declination) * math.cos(declination_0) / math.cos(self.declination) * math.cos(delta_right_ascension) * math.sin(declination_0)

        return self.x, self.y
