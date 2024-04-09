from vertex import Vertex

class Object:
    vertices: list[Vertex]
    lines = list[(Vertex, Vertex)]

    def __init__(self, vertices: list[Vertex], lines: list[(Vertex, Vertex)]):
        self.vertices = vertices
        self.lines = lines

    def draw():
        pass