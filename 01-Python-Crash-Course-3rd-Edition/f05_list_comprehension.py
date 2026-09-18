# 学习列表推导式

# 对列表中的每个元素都执行相同的操作
squares = [ value ** 2 for value in range(1, 10) ]
print(squares)

# https://stackoverflow.com/a/613218
x = { 7: 8, 1: 2, 9: 10, 3: 4, 5: 6 }
# 列表推导式外面用大括号括起来它就是字典，用中括号它就是列表
x2 = { k: v for k, v in sorted(x.items(), key=lambda i: i[1]) }
print(x)
print(x2)
