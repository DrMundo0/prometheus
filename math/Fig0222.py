import color
from draw2d import draw
from Fig0207 import dino_vectors
from Fig0213 import add
from Fig0221 import scale
from patch2d import Arrow, Polygon, Points, Segment

# 图2-22：用-1/2乘以向量的标量乘法
if __name__ == "__main__":
    a = (6, 4)
    # 如果向量乘以一个负的标量，不仅改变长度，还会改变方向
    b = scale(a, -0.5)

    draw(
        Points(*[ a, b ]),
        Arrow(a),
        Arrow(b, color=color.blue)
    )
