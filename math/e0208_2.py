from draw2d import draw
from e0207 import dino_vectors
from patch2d import Arrow, Polygon, Points, Segment, add

# 画恐龙的聪明版本，利用多边形对象
draw(Polygon(*dino_vectors))

# 画出恐龙的点和线
draw(Points(*dino_vectors), Polygon(*dino_vectors))
