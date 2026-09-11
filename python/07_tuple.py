# 元组与列表很像，但是用小括号包围，同样是逗号分隔，但无法修改元组中的元素
dimensions = (200, 50)
# 取元组中元素的方法和列表一样，也是下标
print(dimensions[0])
print(dimensions[1])

# 怎么定义只有一个元素的元组？
my_t = (3,)
print(my_t)

# 遍历元组中的元素
for dimension in dimensions:
    print(dimension)
