import color
from draw2d import draw
from Fig0207 import dino_vectors
from Fig0213 import add, add2, translate
from Fig0218 import length
from Fig0221 import scale
from Fig0224 import subtract, distance
from Fig0256 import to_cartesian, to_polar, rotate
from Fig0257 import regular_polygon
from patch2d import Arrow, Polygon, Points, Segment, ArcX
from math import tan, pi, sin, cos, asin, sqrt, acos, atan2
from random import uniform

# 图2-58：先平移再旋转恐龙
if __name__ == "__main__":
    vectors01 = translate((8, 8), dino_vectors)
    vectors02 = rotate(5 * pi / 3, vectors01)

    c01 = [ (8, 8) ]
    c02 = rotate(5 * pi / 3, c01)

    draw(
        Points(*dino_vectors),
        Polygon(*dino_vectors),
        Points(*vectors01),
        Polygon(*vectors01, color=color.red),
        Points(*vectors02),
        Polygon(*vectors02, color=color.green),
        Points(*(c01 + c02)),
        Arrow(c01[0]),
        Arrow(c02[0]),
        ArcX(start_point=c01[0], end_point=c02[0])
    )
