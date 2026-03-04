from Physics import integrators, forces, collisions

class Engine:
    def __init__(self, state, config, integrator):
        self.state = state
        self.config = config
        self.integrator = integrator
    
    # set up integrator before sim starts running frames
    def initialise(self):
        self.integrator.initialise(self.state)
    
    # apply particle motion each frame
    def step(self, state, dt, substeps):

        # divide default timestep for higher accuracy
        dt_sub = dt/substeps
        
        # run integrator, detect and resolve collisions
        for _ in range(substeps):
            state = self.integrator.step(state, dt_sub, self.config)
            colls = collisions.detect_collisions(state)
            state = collisions.resolve_collisions(state, colls)
            state = collisions.wall_collisions(state, self.config)
        
        return state