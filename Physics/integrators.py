def compute_forces(state):
    return state

def clear_forces(state):
    for particle in state.particles:
        particle.forces = [0, 0, 0]
    
    return state

def symplectic_euler(state, dt):
    for particle in state.particles:
        for i in range(3):
            particle.position[i] += particle.velocity[i] * dt
            particle.velocity[i] += particle.forces[i] * dt
    state.time += dt

    return state