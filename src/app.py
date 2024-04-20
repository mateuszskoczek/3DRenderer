from src.renderer import Renderer
from src.object_builder import ObjectBuilder

class App:
    renderer : Renderer

    def __init__(self):
        self.renderer = Renderer(1280, 720)
        self.renderer.caption = "Virtual camera"

    def main(self):
        obj_builder1 = ObjectBuilder()
        va = obj_builder1.add_vertex(-1, 1,  1)
        vb = obj_builder1.add_vertex( 1, 1,  1)
        vc = obj_builder1.add_vertex( 1, 3,  1)
        vd = obj_builder1.add_vertex(-1, 3,  1)
        ve = obj_builder1.add_vertex(-1, 1, -1)
        vf = obj_builder1.add_vertex( 1, 1, -1)
        vg = obj_builder1.add_vertex( 1, 3, -1)
        vh = obj_builder1.add_vertex(-1, 3, -1)
        obj_builder1.add_vertices_connection(va, vb)
        obj_builder1.add_vertices_connection(va, vd)
        obj_builder1.add_vertices_connection(vd, vc)
        obj_builder1.add_vertices_connection(vb, vc)
        obj_builder1.add_vertices_connection(ve, vf)
        obj_builder1.add_vertices_connection(ve, vh)
        obj_builder1.add_vertices_connection(vh, vg)
        obj_builder1.add_vertices_connection(vf, vg)
        obj_builder1.add_vertices_connection(va, ve)
        obj_builder1.add_vertices_connection(vb, vf)
        obj_builder1.add_vertices_connection(vd, vh)
        obj_builder1.add_vertices_connection(vc, vg)
        self.renderer.add_object(obj_builder1.build())

        obj_builder2 = ObjectBuilder()
        wa = obj_builder2.add_vertex(-2, 0,  2)
        wb = obj_builder2.add_vertex( 2, 0,  2)
        wc = obj_builder2.add_vertex( 2, 4,  2)
        wd = obj_builder2.add_vertex(-2, 4,  2)
        we = obj_builder2.add_vertex(-2, 0, -2)
        wf = obj_builder2.add_vertex( 2, 0, -2)
        wg = obj_builder2.add_vertex( 2, 4, -2)
        wh = obj_builder2.add_vertex(-2, 4, -2)
        obj_builder2.add_vertices_connection(wa, wb)
        obj_builder2.add_vertices_connection(wa, wd)
        obj_builder2.add_vertices_connection(wd, wc)
        obj_builder2.add_vertices_connection(wb, wc)
        obj_builder2.add_vertices_connection(we, wf)
        obj_builder2.add_vertices_connection(we, wh)
        obj_builder2.add_vertices_connection(wh, wg)
        obj_builder2.add_vertices_connection(wf, wg)
        obj_builder2.add_vertices_connection(wa, we)
        obj_builder2.add_vertices_connection(wb, wf)
        obj_builder2.add_vertices_connection(wd, wh)
        obj_builder2.add_vertices_connection(wc, wg)
        self.renderer.add_object(obj_builder2.build())
        
        obj_builder3 = ObjectBuilder()
        ua = obj_builder3.add_vertex(-14, 0,  10)
        ub = obj_builder3.add_vertex(-8,  0,  10)
        uc = obj_builder3.add_vertex(-8,  8,  10)
        ud = obj_builder3.add_vertex(-14, 8,  10)
        ue = obj_builder3.add_vertex(-14, 0, -2)
        uf = obj_builder3.add_vertex(-8,  0, -2)
        ug = obj_builder3.add_vertex(-8,  8, -2)
        uh = obj_builder3.add_vertex(-14, 8, -2)
        obj_builder3.add_vertices_connection(ua, ub)
        obj_builder3.add_vertices_connection(ua, ud)
        obj_builder3.add_vertices_connection(ud, uc)
        obj_builder3.add_vertices_connection(ub, uc)
        obj_builder3.add_vertices_connection(ue, uf)
        obj_builder3.add_vertices_connection(ue, uh)
        obj_builder3.add_vertices_connection(uh, ug)
        obj_builder3.add_vertices_connection(uf, ug)
        obj_builder3.add_vertices_connection(ua, ue)
        obj_builder3.add_vertices_connection(ub, uf)
        obj_builder3.add_vertices_connection(ud, uh)
        obj_builder3.add_vertices_connection(uc, ug)
        self.renderer.add_object(obj_builder3.build())

        obj_builder4 = ObjectBuilder()
        za = obj_builder4.add_vertex(-2, 0, 10)
        zb = obj_builder4.add_vertex( 2, 0, 10)
        zc = obj_builder4.add_vertex( 2, 0,  6)
        zd = obj_builder4.add_vertex(-2, 0,  6)
        ze = obj_builder4.add_vertex( 0, 8,  8)
        obj_builder4.add_vertices_connection(za, zb)
        obj_builder4.add_vertices_connection(za, zd)
        obj_builder4.add_vertices_connection(zd, zc)
        obj_builder4.add_vertices_connection(zb, zc)
        obj_builder4.add_vertices_connection(za, ze)
        obj_builder4.add_vertices_connection(zb, ze)
        obj_builder4.add_vertices_connection(zc, ze)
        obj_builder4.add_vertices_connection(zd, ze)
        self.renderer.add_object(obj_builder4.build())

        self.renderer.run()