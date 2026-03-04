import ui, engine, config
from Physics import state, integrators

def main():

    #initialise each part of the sim architecture
    settings = config.init()
    screen, clock, running = ui.init(settings)
    sim_state = state.init(settings)
    integrator = integrators.Velocity_verlet()
    sim_engine = engine.Engine(sim_state, settings, integrator)

    # get physics dt and initialise physics/render accumulator correction
    phys_dt = settings.dt
    accumulator = 0

    while running:

        # frame dt and accumulator
        frame_dt = clock.tick()/1000
        accumulator += frame_dt

        # run physics engine
        while accumulator >= frame_dt:
            sim_state = sim_engine.step(sim_state, phys_dt, settings.substeps)
            accumulator -= phys_dt
        
        # draw ui
        running = ui.loop(sim_state, screen, running)

if __name__ == "__main__":
    main()