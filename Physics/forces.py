import numpy, math

def clear_forces(state):
    for particle in state.particles:
        particle.forces = [0, 0, 0]
    
    return state

def compute_forces(state, config):
    state = gravity(state, config)
    return state

def gravity(state, config):
    e = 0.01
    for i, p_i in enumerate(state.particles):
        for j, p_j in enumerate(state.particles[i + 1:]):
            normal = numpy.array(p_j.position) - numpy.array(p_i.position)
            dist = math.sqrt(math.dist(p_j.position, p_i.position) + e ** 2)
            normal = normal / dist
            mass_prod = p_i.mass * p_j.mass
            p_i.forces = config.grav * mass_prod * normal / dist ** 2
            p_j.forces = -config.grav * mass_prod * normal / dist ** 2
    
    return state