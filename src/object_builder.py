from object import Object
from vertex import Vertex

class ObjectBuilder:
    vertices: list[Vertex]
    lines: list[(Vertex, Vertex)]

    def __init__(self):
        self.vertices = []

    def add_vertex(self, x: int, y: int, z: int) -> Vertex:
        v = Vertex(x, y, z)
        self.vertices.append(v)
        return v

    def add_vertices_connection(self, vertex1: Vertex, vertex2: Vertex):
        self.lines.append((vertex1, vertex2))

    def build(self) -> Object:
        pass