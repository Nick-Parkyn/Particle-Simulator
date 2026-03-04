import numpy, math

# set forces on all particles to 0
def clear_forces(state):
    for particle in state.particles:
        particle.forces = numpy.array([0, 0, 0])
    
    return state

# calculate forces applies to each particle from all sources
def compute_forces(state, config):
    state = gravity(state, config)
    return state

# calculate force of gravity acting on each particle
def gravity(state, config):
    e = 0.01

    # loop through each pair of particles
    for i, p_i in enumerate(state.particles):
        for j, p_j in enumerate(state.particles[i + 1:]):

            # get direction of force and distance between particles
            normal = p_j.position - p_i.position
            dist = math.sqrt(math.dist(p_j.position, p_i.position) + e ** 2)
            normal = normal / dist

            # calculate forces acting on each particle
            mass_prod = p_i.mass * p_j.mass
            p_i.forces = config.grav * mass_prod * normal / dist ** 2
            p_j.forces = -config.grav * mass_prod * normal / dist ** 2
    
    return state