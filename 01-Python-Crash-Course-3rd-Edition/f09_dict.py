# 学习字典

# 声明一个字典，有点像一个对象，但是它没有字段模板
alien_0 = { 'color': 'green', 'points': 5 }
# 访问字典中的成员
print(alien_0['color'])
new_points = alien_0['points']
print(f"You jusst earned {new_points} points!")

# 向字典中添加元素直接写字段名称就行
alien_0['x_position'] = 0
alien_0['y_position'] = 25
# 打印时保持了定义时元素的顺序
print(alien_0)

# 空字典
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

alien_0 = { 'color': 'green' }
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

alien_0 = { 'x_position': 0, 'y_position': 25, 'speed': 'medium' }
print(f"Original position: {alien_0['x_position']}")
x_increment = 0

def run():
    if alien_0['speed'] == 'slow':
        x_increment = 1
    elif alien_0['speed'] == 'medium':
        x_increment = 2
    else:
        x_increment = 3

    alien_0['x_position'] = alien_0['x_position'] + x_increment
    print(f"New position: {alien_0['x_position']}")

run()
alien_0['speed'] = 'fast'
run()

alien_0 = { 'color': 'green', 'points': 5 }
print(f"删除前：{alien_0}")
del alien_0['points']
print(f"删除后：{alien_0}")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# 用get函数根据一个不存在的key取value时并不会报异常，第一个参数是key的名字，第二个参数是当key不存在时返回的默认值
point_value = alien_0.get('points2', 'No points2 value assigned.')
print(point_value)

user_0 = {
    'username': 'efermi',
    'first': 'enrice',
    'last': 'fermi',
}

# items()返回一个键值对列表，同样使用for-in语句，用key接收键，用value接收值
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# 用来接键值对列表的两个变量名字可以随意定义，符合实际用途，使代码更具可读性
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# 如果只遍历键，可以用keys()
for name in favorite_languages.keys():
    print(name.title())

# 这种方式也可以只遍历键
for name in favorite_languages:
    print(name.title())

friends = [ 'phil', 'sarah' ]

# 结合for和if的一个例子
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# 如果一个元素不在字典的key列表中
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# 使用sorted函数对字典的键做临时排序，并不影响字典本来的存放顺序
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
print(favorite_languages.keys())

# 遍历字典中的值
for language in favorite_languages.values():
    print(language.title())

# 用set函数可以过滤掉值中的重复项
for language in set(favorite_languages.values()):
    print(language.title())

alien_1 = { 'color': 'yellow', 'points': 10 }
alien_2 = { 'color': 'red', 'points': 15 }
# 将三个字典放入列表中
aliens = [ alien_0, alien_1, alien_2 ]
for alien in aliens:
    print(alien)

aliens = []
# 批量自动创建多个字典填充列表
for alien_number in range(30):
    new_alien = { 'color': 'green', 'points': 5, 'speed': 'slow' }
    aliens.append(new_alien)

# 使用列表的切片操作，取前五个字典元素
for alien in aliens[:5]:
    print(alien)
print("...")
# 用len函数
print(f"Total number of aliens: {len(aliens)}")

# 修改前三个字典的字段值
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# 打印前五个字典的内容
for alien in aliens[:5]:
    print(alien)
print("...")

# 列表作为字典的value
pizza = {
    'crust': 'thick',
    'toppings': [ 'mushrooms', 'extrachesse' ],
}
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")

# 每个value都是列表的的字典
favorite_languages = {
    'jen': [ 'python', 'rust' ],
    'sarah': [ 'c' ],
    'edward': [ 'rust', 'go' ],
    'phil': [ 'python', 'haskell' ]
}
for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is {languages[0]}")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")

# 字典里面套字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

