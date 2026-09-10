# 使用range函数快速创建一系列数字，从1开始，到4结束，不会打印5
for value in range(1, 5):
    print(value)

# 用range函数快速创建列表
numbers = list(range(1, 6))
print(numbers)

# 范围1到20-1，步长2，结果是找到这些范围内的偶数
even_numbers = list(range(1, 20, 2))
print(even_numbers)

# 搭配乘方运算符将1到10-1的平方放入一个列表中，简单的功能组合完成复杂的逻辑，这就是程序
squares = []

for value in range(1, 10):
    square = value ** 2
    squares.append(square)

print(squares)

# 找最大值
print(min(squares))

# 找最小值
print(max(squares))

# 求和
print(sum(squares))
