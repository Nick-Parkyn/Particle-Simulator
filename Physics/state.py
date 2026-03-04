
class Particle:
    def __init__(self, position, velocity, mass):
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.radius = 10 * (mass ** 0.5)
        self.forces = [0, 0, 0]

class State:
    def __init__(self, config):
        self.particles = []
        self.time = 0
        self.config = config
    
    def add_particle(self, particle):
        self.particles.append(particle)

def init(config):
    state = State(config)
    state.add_particle(Particle([600, 400, 0], [200, 300, 0], 10))
    state.add_particle(Particle([400, 600, 0], [400, 100, 0], 15))
    return state