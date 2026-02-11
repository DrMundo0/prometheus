# 练习2.19（小项目）：假定 z = (-1, 1) 和 v = (1, 1)，而 r 和 s 是实数，并且假设 -3 < r < 3 且 -1 < s < 1。在平面上，向量 r * z + s * v 可能的终点是哪里？

# r * z 是把 z 向量移动 r 个单位，s * v 是把 v 向量移动 s 个单位，然后两个结果向量的加法

from random import uniform

u = (-1, 1)
v = (1, 1)

def random_r():
    return uniform(-3, 3)

def random_s():
    return uniform(-1, 1)

possibilities = [ add(scale(random_r(), u), scale(random_s(), v)) for i in range(0, 500)]

draw(Points(*possibilities))
