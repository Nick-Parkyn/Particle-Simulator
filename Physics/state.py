import numpy

class Particle:
    def __init__(self, position, velocity, mass):
        self.position = numpy.array(position)
        self.velocity = numpy.array(velocity)
        self.mass = mass
        self.radius = 10 * (mass ** 0.5)
        self.forces = numpy.array([0, 0, 0])
        self.acceleration = self.forces / self.mass

class State:
    def __init__(self, config):
        self.particles = []
        self.time = 0
        self.config = config
    
    # add another particle to the sim with specified attributes
    def add_particle(self, particle):
        self.particles.append(particle)

# populate sim with default starting particles
def init(config):
    state = State(config)
    state.add_particle(Particle([600, 400, 0], [0, 0, 0], 15))
    state.add_particle(Particle([200, 400, 0], [-50, -300, 0], 5))
    return state