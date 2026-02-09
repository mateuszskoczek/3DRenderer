import pygame as pg
import numpy as np
from math import *
from src.camera import Camera
from src.object import Object

class Renderer:
    __clock: pg.time.Clock
    screen: pg.Surface
    fps: int
    caption: str
    camera: Camera
    window_width: int
    window_height: int
    objects: list[Object]

    def __init__(self, window_width: int, window_height: int):
        self.__clock = pg.time.Clock()
        self.screen = pg.display.set_mode((window_width, window_height))
        self.window_width = window_width
        self.window_height = window_height
        self.fps = 60
        self.caption = "window"
        self.camera = Camera(self)
        self.objects = []

    def __quit(self):
        pg.quit()
        exit()

    def __handle_event(self, event: pg.event.Event):
        if event.type == pg.QUIT:
            self.__quit()
        if not self.camera.is_static:
            key = pg.key.get_pressed()
            if key[pg.K_w]:
                self.camera.move_forward()
            if key[pg.K_s]:
                self.camera.move_backward()
            if key[pg.K_a]:
                self.camera.move_left()
            if key[pg.K_d]:
                self.camera.move_right()
            if key[pg.K_SPACE]:
                self.camera.move_up()
            if key[pg.K_LSHIFT]:
                self.camera.move_down()
            if key[pg.K_EQUALS]:
                self.camera.fov_up()
            if key[pg.K_MINUS]:
                self.camera.fov_down()
            if key[pg.K_r]:
                self.camera.pitch_down()
            if key[pg.K_f]:
                self.camera.pitch_up()
            if key[pg.K_q]:
                self.camera.yaw_down()
            if key[pg.K_e]:
                self.camera.yaw_up()
            if key[pg.K_z]:
                self.camera.roll_down()
            if key[pg.K_c]:
                self.camera.roll_up()

    def __update(self):
        self.screen.fill((255,255,255))
        for o in self.objects:
            o.draw()
        pg.display.update()

    def add_object(self, object: Object):
        object.attach_renderer(self)
        self.objects.append(object)

    def run(self):
        pg.display.set_caption(self.caption)
        while True:
            for event in pg.event.get():
                self.__handle_event(event)
            self.__update()
            self.__clock.tick(self.fps)