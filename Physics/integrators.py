def symplectic_euler(state, dt):
    for particle in state.particles:
        for i in range(3):
            particle.position[i] += particle.velocity[i] * dt
            particle.velocity[i] += particle.forces[i] / particle.mass * dt
    state.time += dt

    return state