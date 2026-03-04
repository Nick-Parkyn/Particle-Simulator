import pygame as py

# initialise pygame display and clock objects, and set sim to run
def init(config):
    py.init()
    screen = py.display.set_mode(config.size, py.RESIZABLE)
    py.display.set_caption("Particle Simulator V3")
    clock = py.Clock()
    running = True
    return screen, clock, running
    
# draw the current state to the display
def loop(state, screen, running):

    # clear display after every frame
    screen.fill("black")

    # stop sim if the window is closed
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    
    # draw each particle on screen each frame
    for particle in state.particles:
        py.draw.circle(screen, (255, 255, 255), (particle.position[0], particle.position[1]), particle.radius)
    
    py.display.flip()
    
    return running