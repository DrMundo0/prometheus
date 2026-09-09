name = "ada lovelace"

# 首字母大写
print(name.title())

# 全大写
print(name.upper())

# 全小写
print(name.lower())

first_name = "ada"
last_name = "lovelace"
# 占位符，格式化字符串，f是format的意思
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}")

favorite_language = " python "
# 去除右边的空格
print(favorite_language.rstrip())
# 去除左边的空格
print(favorite_language.lstrip())
# 去除左右两边的空格
print(favorite_language.strip())

nostarch_url = "https://www.baidu.com"
print(nostarch_url)
# 去除前缀
print(nostarch_url.removeprefix("https://"))
