import color
from draw2d import draw
from patch2d import Arrow, Polygon, Points, Segment, add, dino_vectors

# 三个点，演示向量的加法
vectors = [ (-1, 1), (4, 3), (3, 4) ]

draw(
    Points(*vectors),
    # 第一个向量
    Arrow((-1, 1)),
    # 第二个向量
    Arrow((4, 3)),
    # 这两个向量相加之后的向量
    Arrow((3, 4)),
    # 用箭头表示两个向量相加的首尾加法
    Arrow((3, 4), (4, 3), color=color.blue)
)
