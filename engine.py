from Physics import integrators

class Engine:
    def __init__(self, config):
        self.config = config
    
    def step(self, state, dt, substeps):
        dt_sub = dt/substeps
        
        for _ in range(substeps):
            state = integrators.compute_forces(state)
            state = integrators.symplectic_euler(state, dt_sub)
            state = integrators.clear_forces(state)
        
        return state