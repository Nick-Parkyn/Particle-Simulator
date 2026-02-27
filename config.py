dt = 1/60
substeps = 4
size = (1200, 800)

class Config:
    def __init__(self, dt, substeps, size):
        self.dt = dt
        self.substeps = substeps
        self.size = size


def init():
    return Config(dt, substeps, size)