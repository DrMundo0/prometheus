# 演示向量 v = (2, 1) 的重复相加
import color
from e0218 import length
from draw2d import draw
from patch2d import Arrow, Polygon, Points, Segment, add, dino_vectors

# 为了更真实的反映出向量相加的过程，改变写法

# 初始向量
v = (2, 1)
# 相加的次数
n = 10
# 将相加n次的结果组合为向量列表
vectors = [ (0, 0) ] + [ (v[0] * i, v[1] * i) for i in range(1, n + 1) ]

# 将向量列表组合为向量对列表
pairs = list(zip(vectors, vectors[1:]))
# 用向量对列表生成箭头列表
arrows = [ Arrow(y, x, color=color.red) for x, y in pairs ]

draw(
    Points(*vectors, color=color.blue),
    *arrows
)
