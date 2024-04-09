import numpy as np
from math import *

rotation_x = lambda angle: np.matrix([
    [1, 0,          0          ],
    [0, cos(angle), -sin(angle)],
    [0, sin(angle), cos(angle) ],
])

rotation_y = lambda angle: np.matrix([
    [cos(angle),    0,  sin(angle)],
    [0,             1,  0         ],
    [-sin(angle),   0,  cos(angle)],
])

rotation_z = lambda angle: np.matrix([
    [cos(angle),    -sin(angle),    0],
    [sin(angle),    cos(angle),     0],
    [0,             0,              1],
])