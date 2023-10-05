import numpy as np
from src.particle import Particle

class Simulation:
    def __init__(self, size):
        self.particles = []
        self.size = size

    
    def add_particle(self, particle):
        self.particles.append(particle)

    def create_particles(self, num_particles):
        for particle in range(num_particles):
            part = Particle(mass=np.random.uniform(-5, 5), 
                     position=np.random.uniform(-20, 20, 2))
            self.add_particle(part)

    def simulate(self):
        for particle in self.particles:
            particle.update_position(self.size)