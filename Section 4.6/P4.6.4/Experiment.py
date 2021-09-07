import numpy as np

class Experiment():
    def __init__(self, description):
        self.description = description

        self.x = np.array([])
        self.y = np.array([])

        self.m = None
        self.c = None

    def load_data(self, filepath):
        