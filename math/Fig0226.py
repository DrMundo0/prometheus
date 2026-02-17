import color
from draw2d import draw
from Fig0207 import dino_vectors
from Fig0213 import add
from Fig0221 import multiply
from Fig0224 import subtract
from patch2d import Arrow, Polygon, Points, Segment

# 图2-26：距w=(2,2)等距离的几个点
if __name__ == "__main__":
    v = (-1, 3)
    w = (2, 2)
    a = (-1, 1)
    b = (3, 5)
    c = (3, -1)

    draw(
        Points(*[ v, w, a, b, c ]),
        Segment(v, w, color=color.red),
        Segment(a, w, color=color.blue),
        Segment(b, w, color=color.green),
        Segment(c, w, color=color.purple)
    )
