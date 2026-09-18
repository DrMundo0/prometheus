# 学习条件判断

cars = [ 'audi', 'bmw', 'subaru', 'toyota' ]

for car in cars:
    # 用相等运算符判断是否相等
    if car.lower() == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 or age_1 >= 21)
age_1 = 22
print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 or age_1 >= 21)

# 验证某元素是否在列表中
requested_toppings = [ 'mushrooms', 'onions', 'pineapple' ]
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

banned_users = [ 'andrew', 'carolina', 'david' ]
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

age = 19

if age >= 18:
    print("You are old enough to vote!")

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# 更简洁的版本
age = 12
price = 0
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
price(f"Your admission cost is ${price}.")

age = 12
price = 0
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
price(f"Your admission cost is ${price}")

