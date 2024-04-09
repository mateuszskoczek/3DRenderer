import pygame
import numpy as np
from math import *
import src.transformation_matrices as tm



class App:
    clock: pygame.time.Clock
    screen: pygame.Surface
    scale: int
    points: dict[str, np.matrix]
    lines: list[str]
    projection_matrix: np.matrix
    angle_x: float

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1280, 720))
        self.scale = 100
        self.angle = 0.05
        self.points = {
            "A": np.matrix([-1, -1,  1]),
            "B": np.matrix([ 1, -1,  1]),
            "C": np.matrix([ 1,  1,  1]),
            "D": np.matrix([-1,  1,  1]),
            "E": np.matrix([-1, -1, -1]),
            "F": np.matrix([ 1, -1, -1]),
            "G": np.matrix([ 1,  1, -1]),
            "H": np.matrix([-1,  1, -1]),
        }
        self.lines = [
            "AB",
            "AD",
            "DC",
            "BC",
            "EF",
            "EH",
            "HG",
            "FG",
            "AE",
            "BF",
            "DH",
            "CG"
        ]
        self.projection_matrix = np.matrix([
            [1, 0, 0],
            [0, 1, 0]
        ])

    def main(self):
        self.setup()
        while True:
            self.clock.tick(60)
            for event in pygame.event.get():
                self.handle_event(event)
            self.update()

    def handle_event(self, event: pygame.event.Event):
        match event.type:
            case pygame.QUIT:
                self.quit()
            case pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        self.quit()
                    case pygame.K_s:
                        self.transform(tm.rotation_x(self.angle))
                    case pygame.K_w:
                        self.transform(tm.rotation_x(-self.angle))
                    case pygame.K_d:
                        self.transform(tm.rotation_y(self.angle))
                    case pygame.K_a:
                        self.transform(tm.rotation_y(-self.angle))
                    case pygame.K_q:
                        self.transform(tm.rotation_z(self.angle))
                    case pygame.K_e:
                        self.transform(tm.rotation_z(-self.angle))


    def transform(self, transformation_matrix: np.matrix):
        for key in self.points.keys():
            point = self.points[key]
            self.points[key] = np.dot(transformation_matrix, point.reshape((3,1)))
    
    def setup(self):
        pygame.display.set_caption("Virtual camera")

    def update(self):
        self.screen.fill((255,255,255))

        projected_points = {}

        for point_key in self.points.keys():
            point = self.points[point_key]
            projected_2D = np.dot(self.projection_matrix, point.reshape((3, 1)))

            x = int(projected_2D[0][0] * self.scale) + (1280 / 2)
            y = int(projected_2D[1][0] * self.scale) + (720 / 2)

            pygame.draw.circle(self.screen, (255, 0, 0), (x, y), 5)

            projected_points[point_key] = (x, y)
        
        for line in self.lines:
            point_a = projected_points[line[0]]
            point_b = projected_points[line[1]]
            pygame.draw.line(self.screen, (0,0,0), point_a, point_b)


        pygame.display.update()

    def quit(self):
        pygame.quit()
        exit()