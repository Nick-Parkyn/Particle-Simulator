DT = 1/60
SUBSTEPS = 4
SIZE = (1200, 800)
GRAV = 100


class Config:
    def __init__(self, dt, substeps, size, grav):
        self.dt = dt
        self.substeps = substeps
        self.size = size
        self.grav = grav


def init():
    return Config(DT, SUBSTEPS, SIZE, GRAV)