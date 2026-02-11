# 什么是向量？
# 向量用于描述多维环境中的一个点，拿二维空间来说，有x轴、y轴两个轴，一个点的定义由x轴的量和y轴的量表示，这两个量组成的二维空间点描述被称为向量

# 什么是标量？
# 标量是一个数，整数、小数、分数，都是一个标量

from draw2d import draw
from patch2d import Arrow, Polygon, Points, Segment, add, dino_vectors

# 画出恐龙轮廓的各个点
# 星号是 Python 中的解包运算符，不加星号，会把 dino_vectors tuple list 传入 Points 函数，加了星号则会把 dino_vectors tuple list 中的每个 tuple 挨个传入 Points 函数，这样就会画出每个 Points
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
