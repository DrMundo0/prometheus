# 学习重构

from pathlib import Path
import json

def get_stored_username(path: Path):
    """如果存储了用户名，就获取它"""
    if path.exists():
        contents = path.read_text(encoding='utf-8')
        username = json.loads(contents)
        return username
    else:
        return None

# 一个函数只负责干一件事
def get_new_username(path: Path):
    username = input("What is your name?")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    path = Path('username.json')
    username = get_stored_username(path)

    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

if __name__ == "__main__":
    greet_user()
