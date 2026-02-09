import numpy as np
import math as mt
import src.transformations as tn

class Camera:
    __position: np.ndarray[float]
    __yaw: float
    __pitch: float
    __roll: float
    __right: np.ndarray[float]
    __up: np.ndarray[float]
    __forward: np.ndarray[float]
    is_static: bool
    moving_speed: float
    rotation_speed: float
    h_fov: float
    v_fov: float
    near_plane: float
    far_plane: float

    def __init__(self, renderer):
        self.__renderer = renderer
        self.__position = np.array([-5, 6, -55, 1.0])
        self.__yaw = 0
        self.__pitch = 0
        self.__roll = 0
        self.__right = np.array([1, 0, 0, 1])
        self.__up = np.array([0, 1, 0, 1])
        self.__forward = np.array([0, 0, 1, 1])
        self.moving_speed = 0.3
        self.rotation_speed = 0.015
        self.is_static = False
        self.near_plane = 0.1
        self.far_plane = 100
        self.set_fov(mt.pi / 3)

    def projection_matrix(self):
        right = mt.tan(self.h_fov / 2)
        top = mt.tan(self.v_fov / 2)

        m00 = 1 / right
        m11 = 1 / top
        m22 = (self.far_plane + self.near_plane) / (self.far_plane - self.near_plane)
        m32 = -2 * self.near_plane * self.far_plane / (self.far_plane - self.near_plane)

        matrix = np.matrix([
            [m00, 0, 0, 0],
            [0, m11, 0, 0],
            [0, 0, m22, 1],
            [0, 0, m32, 0]
        ])
        return matrix

    def screen_matrix(self):
        hw = self.__renderer.window_width / 2
        hh = self.__renderer.window_height / 2

        matrix = np.matrix([
            [hw, 0, 0, 0],
            [0, -hh, 0, 0],
            [0, 0, 1, 0],
            [hw, hh, 0, 1]
        ])
        return matrix

    def set_fov(self, h_fov: float):
        self.h_fov = h_fov
        self.v_fov = h_fov * (self.__renderer.window_height / self.__renderer.window_width)
    
    def set_position(self, x: float = None, y: float = None, z: float = None):
        if x is not None:
            self.__position[0] = x
        if y is not None:
            self.__position[1] = y
        if z is not None:
            self.__position[2] = z

    def move_left(self):
        self.__position -= self.__right * self.moving_speed

    def move_right(self):
        self.__position += self.__right * self.moving_speed

    def move_down(self):
        self.__position -= self.__up * self.moving_speed

    def move_up(self):
        self.__position += self.__up * self.moving_speed

    def move_backward(self):
        self.__position -= self.__forward * self.moving_speed

    def move_forward(self):
        self.__position += self.__forward * self.moving_speed

    def yaw_down(self):
        self.__yaw -= self.rotation_speed
        
    def yaw_up(self):
        self.__yaw += self.rotation_speed
        
    def pitch_down(self):
        self.__pitch -= self.rotation_speed
        
    def pitch_up(self):
        self.__pitch += self.rotation_speed
        
    def roll_down(self):
        self.__roll -= self.rotation_speed
        
    def roll_up(self):
        self.__roll += self.rotation_speed

    def fov_up(self):
        self.set_fov(self.h_fov - 0.05)
    
    def fov_down(self):
        self.set_fov(self.h_fov + 0.05)

    def update_axis(self):
        rotate = tn.rotate_x(self.__pitch) @ tn.rotate_y(self.__yaw) @ tn.rotate_z(self.__roll)
        self.__forward = np.array([0, 0, 1, 1]) @ rotate
        self.__right = np.array([1, 0, 0, 1]) @ rotate
        self.__up = np.array([0, 1, 0, 1]) @ rotate

    def camera_matrix(self) -> np.matrix:
        self.update_axis()
        return self.translate_matrix() @ self.rotate_matrix()
    
    def translate_matrix(self) -> np.matrix:
        x, y, z, w = self.__position
        return np.matrix([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [-x, -y, -z, 1]
        ])

    def rotate_matrix(self) -> np.matrix:
        rx, ry, rz, w = self.__right
        fx, fy, fz, w = self.__forward
        ux, uy, uz, w = self.__up
        return np.matrix([
            [rx, ux, fx, 0],
            [ry, uy, fy, 0],
            [rz, uz, fz, 0],
            [0, 0, 0, 1]
        ])