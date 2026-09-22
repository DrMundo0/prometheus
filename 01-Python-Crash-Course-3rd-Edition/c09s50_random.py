# 学习标准库，如何生成随机数

from random import randint, choice

# 返回1到6之间的整数
print(randint(1, 6))

players = [ 'charles', 'martina', 'michael', 'florence', 'eli' ]
# 随机返回列表中的一个元素
first_up = choice(players)
print(first_up)
