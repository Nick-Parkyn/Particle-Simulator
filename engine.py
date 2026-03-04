from Physics import integrators, forces, collisions

class Engine:
    def __init__(self, config):
        self.config = config
    
    def step(self, state, dt, substeps):
        dt_sub = dt/substeps
        
        for _ in range(substeps):
            state = forces.clear_forces(state)
            state = forces.compute_forces(state)
            state = integrators.symplectic_euler(state, dt_sub)
            colls = collisions.detect_collisions(state)
            state = collisions.resolve_collisions(state, colls)
            state = collisions.wall_collisions(state, self.config)
        
        return state