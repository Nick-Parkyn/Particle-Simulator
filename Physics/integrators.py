import numpy
from Physics import forces

def symplectic_euler(state, dt):
    for particle in state.particles:
        particle.position += particle.velocity * dt
        particle.velocity += particle.forces
    state.time += dt

    return state

class Velocity_verlet:
    
    def initialise(self, state, config):
        state = forces.clear_forces(state)
        state = forces.compute_forces(state, config)

        for particle in state.particles:
            particle.acceleration = particle.forces / particle.mass
        
        return state
    
    def step(self, state, dt, config):

        for particle in state.particles:
            particle.acceleration = particle.forces / particle.mass
            particle.position = particle.position + particle.velocity * dt + 0.5 * particle.forces / particle.mass * dt * dt
            
        state = forces.clear_forces(state)
        state = forces.compute_forces(state, config)

        for particle in state.particles:
            new_accel = particle.forces / particle.mass
            particle.velocity = particle.velocity + 0.5 * (particle.acceleration + new_accel) * dt
            particle.acceleration = new_accel
        state.time += dt
        
        return state

    
