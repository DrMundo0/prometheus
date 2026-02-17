import color
from draw2d import draw
from Fig0207 import dino_vectors
from Fig0213 import add
from Fig0221 import multiply
from patch2d import Arrow, Polygon, Points, Segment

# 向量的减法
def subtract(x, y):
    return (x[0] - y[0], x[1] - y[1])

# 图2-24：v-w的结果是从w头部到v头部的箭头
if __name__ == "__main__":
    v = (-1, 3)
    w = (2, 2)
    a = subtract(v, w)
    draw(
        Points(*[ v, w, a ]),
        Arrow(v, color=color.red),
        Arrow(w, color=color.blue),
        Arrow(a, color=color.green),
        Arrow(v, w, color=color.purple)
    )
