import color
from draw2d import draw
from Fig0207 import dino_vectors
from Fig0213 import add
from Fig0221 import multiply
from Fig0224 import subtract
from patch2d import Arrow, Polygon, Points, Segment

# 图2-25：平面内两点之间的距离
if __name__ == "__main__":
    v = (-1, 3)
    w = (2, 2)
    draw(
        Points(*[ v, w ]),
        Segment(v, w)
    )
