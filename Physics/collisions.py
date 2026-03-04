import math, numpy

# detect collisions between each pair of particles
def detect_collisions(state):

    collisions = []
    e = 0.01

    for i in range(len(state.particles)):

        for j in range(i + 1, len(state.particles)):
             
             p_i = state.particles[i]
             p_j = state.particles[j]

             # check if particles are close enough to be colliding
             dist = math.sqrt(math.dist(p_i.position, p_j.position) ** 2 + e ** 2)
             if dist <= p_i.radius + p_j.radius:
                  
                  # add particle indices and direction of collision
                  normal = (numpy.array(p_j.position) - numpy.array(p_i.position)) / dist
                  collisions.append([i, j, normal])
    
    return collisions

# apply impulses to resolve collisions between particles
def resolve_collisions(state, collisions):

    for i, j, normal in collisions:

        p_i = state.particles[i]
        p_j = state.particles[j]

        # get relative velocity along the direction of impact
        rel_vel = numpy.array(p_j.velocity) - numpy.array(p_i.velocity)
        vel_normal = numpy.dot(rel_vel, normal)

        # only apply collision if particles are moving towards each other
        if vel_normal > 0:
            continue

        # elasticity, currently perfectly elastic
        e = 1
        
        # calculate impulse
        j_imp = - (1 + e) * vel_normal / (1/p_i.mass + 1/p_j.mass)
        impulse = j_imp * normal

        # apply impulse to particles 
        p_i.velocity -= impulse / p_i.mass
        p_j.velocity += impulse / p_j.mass
    
    return state

def wall_collisions(state, config):
    for particle in state.particles:

        if particle.position[0] + particle.radius > config.size[0] or particle.position[0] - particle.radius < 0:
            particle.velocity[0] *= -1

        if particle.position[1] + particle.radius > config.size[1] or particle.position[1] - particle.radius < 0:
            particle.velocity[1] *= -1
    
    return state