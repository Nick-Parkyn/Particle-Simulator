def clear_forces(state):
    for particle in state.particles:
        particle.forces = [0, 0, 0]
    
    return state

def compute_forces(state):
    return state