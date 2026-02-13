import color
from draw2d import draw
from Fig0207 import dino_vectors
from Fig0213 import add
from patch2d import Arrow, Polygon, Points, Segment

# 图2-17：将向量(4, 3)分解为(4, 0)与(0, 3)之和
if __name__ == "__main__":
    a = (4, 0)
    b = (0, 3)
    c = add(a, b)

    draw(
        Points(*[ a, b, c ]),
        Arrow(a, color=color.blue),
        Arrow(c, a, color=color.green),
        Arrow(c)
    )
