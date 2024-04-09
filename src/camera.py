import numpy as np
import transformation as tm

class Camera:
    moving_speed: float
    rotation_speed: float
    position: np.ndarray[float]

    def __init__(self, x: float, y: int, z: int):
        self.moving_speed = 0.3
        self.rotation_speed = 0.015
        self.position = np.array([x, y, z, 1.0])

    def move_forward(self):
        self.position += tm.forward_array * self.moving_speed

    def move_backward(self):
        self.position -= tm.forward_array * self.moving_speed

    def move_right(self):
        self.position += tm.right_array * self.moving_speed

    def move_left(self):
        self.position -= tm.right_array * self.moving_speed

    def move_up(self):
        self.position += tm.up_array * self.moving_speed

    def move_down(self):
        self.position -= tm.up_array * self.moving_speed