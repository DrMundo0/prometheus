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

# add((-1.5, -2.5), v) for v in dino_vectors 是一个列表推导式
# 由两部分构成，先看后面，for v in dino_vectors 循环取出数组 dino_vectors 中的每一个向量
# 再看前面的部分，add((-1.5, -2.5), v) 是对循环取出的每一个向量要做的操作，这个表达式中的 v 就是后面循环语句中指代每个向量所使用的 v
# 这两部分加起来之后，将会返回21个都加了 (-1.5, -2.5) 的向量，用中括号括起来，让他们组成一个新的向量数组
# dino_vectors 中每个向量都加 (-1.5, -2.5) 相当于左移 1.5，再下移 2.5
dino_vectors2 = [ add((-1.5, -2.5), v) for v in dino_vectors ]
draw(Points(*dino_vectors2), Polygon(*dino_vectors))

# 向量加法的第二个版本，支持传入任意多个向量，使用了列表推导式
def add2(*vs):
    return (sum([v[0] for v in vs]), sum([v[1] for v in vs]))
