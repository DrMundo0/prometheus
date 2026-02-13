from draw2d import draw
from Fig0207 import dino_vectors
from patch2d import Arrow, Polygon, Points, Segment

if __name__ == "__main__":
    # 画恐龙的聪明版本，利用多边形对象
    # 画出恐龙的点和线
    draw(Points(*dino_vectors), Polygon(*dino_vectors))
