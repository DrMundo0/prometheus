# 演示列表的用法
# https://jupyter.org/try-jupyter/lab/

bicycles = [ 'trek', 'cannondale', 'redline', 'specialized' ]
print(bicycles)

# 访问列表中的元素，索引从0开始
print(bicycles[0])
print(bicycles[0].title())

# Python 支持负数索引，将从结尾开始算，结尾第一个元素的下标是-1，以此类推
print(bicycles[-1])
print(bicycles[-2])

motorcycles = [ 'honda', 'yamaha', 'suzuki' ]
print(motorcycles)

# 修改第一个元素的指
motorcycles[0] = 'ducati'
print(motorcycles)

# 在列表末尾添加元素
motorcycles.append('ducati')
print(motorcycles)

# 插入元素
motorcycles.insert(0, 'Haojue')
print(motorcycles)

# 使用del语句删除第一个元素
del motorcycles[0]
print(motorcycles)

# 使用del语句删除第二个元素
del motorcycles[1]
print(motorcycles)

# 弹出列表中最后一个元素并保存
popped_motorcycle = motorcycles.pop()
# 打印会发现列表变短
print(motorcycles)
# 打印出弹出的元素
print(popped_motorcycle)

# pop中还可以填下标，所以能弹出第一个元素
first_owned = motorcycles.pop(0)
print(motorcycles)
print(first_owned)

# 根据值来删除元素
motorcycles.remove('honda')
print(motorcycles)

cars = [ 'bmw', 'audi', 'toyota', 'subaru' ]
print(f"before: {cars}")
# 调用列表的sort()函数讲对列表永久排序
cars.sort()
print(f"after: {cars}")

# 倒排
cars.sort(reverse=True)
print(cars)

# 临时排序
print(sorted(cars))

# 临时倒排
print(sorted(cars, reverse=True))

# 反转列表
cars.reverse()
print(cars)

# 计算列表的长度
print(len(cars))

# 通过 __sizeof__() 函数查看列表所占的内存空间，单位字节
# 列表通过预先分配内存来提高操作效率print(cars.__sizeof__())
print(cars.__sizeof__())

# 计算某个元素出现的次数
print(cars.count("bmw"))

# 查找某个元素出现的下标
print(cars.index("bmw"))

magicians = [ 'alice', 'david', 'carolina' ]

# 遍历列表
# Python中是用缩进来表示代码块的，没有大括号
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    # print函数执行完成后自己就会换行，再加个换行符就是两行
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")

# -m timeit 可精确测量小段 Python 代码的执行时间
# !python3 -m timeit 'x=(1,2,3,4,5,6)'

# [Python性能分析利器：timeit 模块深度解析](https://hot.dawoai.com/posts/2025/python-performance-analysis-timeit-module-in-depth-analysis)
# [Python 3 时间测试神器：轻松掌握 timeit 模块高效用法](https://www.oryoy.com/news/python-3-shi-jian-ce-shi-shen-qi-qing-song-zhang-wo-timeit-mo-kuai-gao-xiao-yong-fa.html)
import timeit

code = "x=[1,2,3,4,5,6]"
print(timeit.timeit(stmt=code, number=20000000))

keys = [x for x in range(0, 100000)]
vals = [x for x in range(200000, 300000)]
list0 = list(zip(keys, vals))
