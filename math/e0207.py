# 什么是向量？
# 向量用于描述多维环境中的一个点，拿二维空间来说，有x轴、y轴两个轴，一个点的定义由x轴的量和y轴的量表示，这两个量组成的二维空间点描述被称为向量

# 什么是标量？
# 标量是一个数，整数、小数、分数，都是一个标量

from draw2d import draw
from patch2d import Arrow, Polygon, Points, Segment, add

# 恐龙二维向量集合
dino_vectors = [ (6, 4), (3, 1), (1, 2), (-1, 5), (-2, 5), (-3, 4), (-4, 4), (-5, 3), (-5, 2), (-2, 2), (-5, 1), (-4, 0), (-2, 1), (-1, 0), (0, -3), (-1, -4), (1, -4), (2, -3), (1, -2), (3, -1), (5, 1) ]

# 将需要直接执行的代码写在 main 函数里面是 Python 的最佳实践，在 import 时，会执行所有被 import py 文件中的所有顶层代码，如果把 draw 放在外面则会被执行，而写在 main 函数中只有当启动 e0207.py 时才会执行 main 函数中的内容
if __name__ == "__main__":
    # 画出恐龙轮廓的各个点
    # 星号是 Python 中的解包运算符，不加星号，会把 dino_vectors tuple list 传入 Points 函数，加了星号则会把 dino_vectors tuple list 中的每个 tuple 挨个传入 Points 函数，这样就会画出每个 Points
    draw(Points(*dino_vectors))
