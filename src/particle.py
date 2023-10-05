import numpy as np

class Particle:
    def __init__(self, mass, position):
        self.mass = mass
        self.position = position


    def update_position(self, time_step, size):
        step = np.random.uniform(-1, 1, 2)* self.mass * time_step
        if max(self.position + step * time_step) > size[1] or \
            min(self.position + step * time_step) < size[0]:
            pass
        else:
            self.position += step