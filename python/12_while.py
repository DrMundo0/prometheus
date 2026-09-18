# 学习while循环

# ------ Fig1 ------
prompt = "\nPlease enter the name of a city you have visited."
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        # 使用break退出while循环
        break
    else:
        print(f"I'd love to go to {city.title()}")

# ------ Fig2 ------
# 打印0到10之间的奇数
current_number = 0

while current_number < 10:
    current_number += 1

    if current_number % 2 == 0:
        # 使用continue跳过循环一次
        continue

    print(current_number)

# ------ Fig3 ------
unconfirmed_users = [ 'alice', 'brian', 'candace' ]
confirmed_users = []

# 列表也可以作为while的条件，当unconfirmed_users为空时是false
while unconfirmed_users:
    # 弹出元素并存起来
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")

for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# ------ Fig4 ------
pets = [ 'dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat' ]
print(pets)

# 删除列表中的所有匹配元素
while 'cat' in pets:
    pets.remove('cat')

print(pets)
