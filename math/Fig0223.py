import color
from draw2d import draw
from Fig0207 import dino_vectors
from Fig0213 import add
from Fig0221 import multiply
from patch2d import Arrow, Polygon, Points, Segment

# 图2-23：向量v=(-4,3)及其负向量-v=(4,-3)
# 向量乘以-1将得到向量的反向量
if __name__ == "__main__":
    v = (-4, 3)
    v2 = multiply(v, -1)
    draw(
        Points(*[ v, v2 ]),
        Arrow(v, color=color.red),
        Arrow(v2, color=color.blue)
    )
