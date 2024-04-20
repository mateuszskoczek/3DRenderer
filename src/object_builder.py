from src.object import Object
from src.vertex import Vertex

class ObjectBuilder:
    __vertices: list[Vertex]
    __lines: list[(Vertex, Vertex)]

    def __init__(self):
        self.__vertices = []
        self.__lines = []

    def add_vertex(self, x: int, y: int, z: int) -> Vertex:
        v = Vertex(x, y, z)
        self.__vertices.append(v)
        return v

    def add_vertices_connection(self, vertex1: Vertex, vertex2: Vertex):
        self.__lines.append((vertex1, vertex2))

    def build(self) -> Object:
        return Object(self.__vertices, self.__lines)