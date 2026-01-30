# 什么是向量？
# 向量用于描述多维环境中的一个点，拿二维空间来说，有x轴、y轴两个轴，一个点的定义由x轴的量和y轴的量表示，这两个量组成的二维空间点描述被称为向量

# 什么是标量？
# 标量是一个数，整数、小数、分数，都是一个标量

from draw_matplotlib import draw
from patch import Arrow, Polygon, Points, Segment

# 恐龙二维向量集合
dino_vectors = [ (6, 4), (3, 1), (1, 2), (-1, 5), (-2, 5), (-3, 4), (-4, 4), (-5, 3), (-5, 2), (-2, 2), (-5, 1), (-4, 0), (-2, 1), (-1, 0), (0, -3), (-1, -4), (1, -4), (2, -3), (1, -2), (3, -1), (5, 1) ]
# 画出恐龙轮廓的各个点
draw(Points(*dino_vectors))

# 绘制队列，用点坐标初始化
objs = [ Points(*dino_vectors) ]

# 将要绘制的线段加入绘制队列中
for i in range(0, len(dino_vectors)):
    if i < len(dino_vectors) - 1:
        # 从第一个点，到最后一个点，每一个线段都是从自己到下一个点
        print(i, dino_vectors[i], dino_vectors[i + 1])
        objs.append(Segment(dino_vectors[i], dino_vectors[i + 1]))
    elif i == len(dino_vectors) - 1:
        # 第20个点，从最后一个向量指向第一个向量
        print(i, dino_vectors[i], dino_vectors[0])
        objs.append(Segment(dino_vectors[i], dino_vectors[0]))
    else:
        # 第21个点，从最后一个向量指向前一个向量
        print(i, dino_vectors[i - 1], dino_vectors[i])
        objs.append(Segment(dino_vectors[i - 1], dino_vectors[i]))

# 画恐龙的点和线（笨版本）
draw(*objs)

# 画恐龙的聪明版本，利用多边形对象
draw(Polygon(*dino_vectors))

# 画出恐龙的点和线
draw(Points(*dino_vectors), Polygon(*dino_vectors))

# 定义向量加法运算函数，向量的加法就是组成向量的两个成员分别相加，组成新的向量
# 加法可以理解为向量的移动，先向 x 轴的左边或者右边移动，再向 y 轴的上边或者下边移动
def add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

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
