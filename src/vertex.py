import numpy as np

class Vertex:
    x: int
    y: int
    z: int

    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def to_matrix(self) -> np.matrix:
        return np.matrix([self.x, self.y, self.z])