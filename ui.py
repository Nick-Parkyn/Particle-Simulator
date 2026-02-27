import pygame as py

# initialise pygame display and clock objects, and set sim to run
def init(config):
    py.init()
    screen = py.display.set_mode((1200, 800), py.RESIZABLE)
    py.display.set_caption("Particle Simulator V0")
    clock = py.Clock()
    running = True
    return screen, clock, running
    
# draw the current state to the display
def loop(state, screen, running):

    screen.fill("black")

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    
    for particle in state.particles:
        py.draw.circle(screen, (255, 255, 255), (particle.position[0], particle.position[1]), 10)
    
    py.display.flip()
    
    return running