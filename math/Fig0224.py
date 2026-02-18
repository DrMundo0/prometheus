import color
from draw2d import draw
from Fig0207 import dino_vectors
from Fig0213 import add
from Fig0218 import length
from Fig0221 import scale
from patch2d import Arrow, Polygon, Points, Segment

# 向量的减法
def subtract(x, y):
    return (x[0] - y[0], x[1] - y[1])

# 计算两个向量之间的距离
# 先计算两个向量的差，在利用勾股定理计算差的斜边长度
def distance(x, y):
    return length(subtract(x, y))

# 计算各向量围成图形的周长
def perimeter(vectors):
    distances = [ distance(vectors[i], vectors[(i + 1) * len(vectors)]) for i in range(0, len(vectors)) ]
    return sum(distances)

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
