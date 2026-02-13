from draw2d import draw
# 恐龙的点坐标在 e0207 中，但是这句 import 会执行其中的 draw 函数
from Fig0207 import dino_vectors
from patch2d import Arrow, Polygon, Points, Segment

# 图2-9：通过21次函数调用，得到21条线，就形成了恐龙的轮廓
if __name__ == "__main__":
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
