# 切片操作
players = [ 'charlees', 'martina', 'michael', 'florence', 'eli' ]

# 冒号前是起始下标，冒号后是结束下标
print(players[0:3])
print(players[1:3])

# 冒号前的起始下标可以省略，则会从0开始
print(players[:4])

# 同理，冒号后的结束下标也可以省略
print(players[2:])

# 列表下标可以用负数，切片同样也能用负数，取最后三个元素
print(players[-3:])

# 遍历前三个元素
print("here are the first thre players on my team:")

for player in players[:3]:
    print(player.title())

# 复制列表可以使用不指定起始下标和结束下标的切片写法
my_foods = [ 'pizza', 'falafel', 'carrot cake' ]
friend_foods = my_foods[:]
print(f"My favorite foods are: {my_foods}")
print(f"My friend's favorite foods are: {friend_foods}")
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(f"My favorite foods are: {my_foods}")
print(f"My friend's favorite foods are: {friend_foods}")
