import pygame as pg
import numpy as np
from math import *
import src.constants as cn
import transformation as tm
from src.object_builder import ObjectBuilder
from src.object import Object
from src.camera import Camera



class App:
    clock: pg.time.Clock
    screen: pg.Surface
    camera: Camera
    objects = list[Object]

    def __init__(self):
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode(cn.WINDOW_SIZE)
        self.objects = []
        self.camera = Camera(-5, 6, -55)
        self.create_objects()

    def create_objects(self):
        obj_builder = ObjectBuilder()
        va = obj_builder.add_vertex(-1, -1,  1)
        vb = obj_builder.add_vertex( 1, -1,  1)
        vc = obj_builder.add_vertex( 1,  1,  1)
        vd = obj_builder.add_vertex(-1,  1,  1)
        ve = obj_builder.add_vertex(-1, -1, -1)
        vf = obj_builder.add_vertex( 1, -1, -1)
        vg = obj_builder.add_vertex( 1,  1, -1)
        vh = obj_builder.add_vertex(-1,  1, -1)
        obj_builder.add_vertices_connection(va, vb)
        obj_builder.add_vertices_connection(va, vd)
        obj_builder.add_vertices_connection(vd, vc)
        obj_builder.add_vertices_connection(vb, vc)
        obj_builder.add_vertices_connection(ve, vf)
        obj_builder.add_vertices_connection(ve, vh)
        obj_builder.add_vertices_connection(vh, vg)
        obj_builder.add_vertices_connection(vf, vg)
        obj_builder.add_vertices_connection(va, ve)
        obj_builder.add_vertices_connection(vb, vf)
        obj_builder.add_vertices_connection(vd, vh)
        obj_builder.add_vertices_connection(vc, vg)
        self.objects.append(obj_builder.build())

    def main(self):
        self.setup()
        while True:
            self.clock.tick(cn.FPS)
            for event in pg.event.get():
                self.handle_event(event)
            self.update()

    def handle_event(self, event: pg.event.Event):
        match event.type:
            case pg.QUIT:
                self.quit()
            case pg.KEYDOWN:
                match event.key:
                    case pg.K_ESCAPE:
                        self.quit()
                    case pg.K_s:
                        self.camera.move_backward()
                    case pg.K_w:
                        self.camera.move_forward()
                    case pg.K_d:
                        self.camera.move_right()
                    case pg.K_a:
                        self.camera.move_left()
                    case pg.K_SPACE:
                        self.camera.move_up()
                    case pg.K_LSHIFT:
                        self.camera.move_down()

    def transform(self, transformation_matrix: np.matrix):
        for key in self.points.keys():
            point = self.points[key]
            self.points[key] = np.dot(transformation_matrix, point.reshape((3,1)))
    
    def setup(self):
        pg.display.set_caption("Virtual camera")

    def update(self):
        self.screen.fill((255,255,255))
        for obj in self.objects:
            obj.draw()
        pg.display.update()

    def quit(self):
        pg.quit()
        exit()
        

"""
        projected_points = {}

        for point_key in self.points.keys():
            point = self.points[point_key]
            projected_2D = np.dot(self.projection_matrix, point.reshape((3, 1)))

            x = int(projected_2D[0][0] * self.scale) + (1280 / 2)
            y = int(projected_2D[1][0] * self.scale) + (720 / 2)

            pg.draw.circle(self.screen, (255, 0, 0), (x, y), 5)

            projected_points[point_key] = (x, y)
        
        for line in self.lines:
            point_a = projected_points[line[0]]
            point_b = projected_points[line[1]]
            pg.draw.line(self.screen, (0,0,0), point_a, point_b)
"""