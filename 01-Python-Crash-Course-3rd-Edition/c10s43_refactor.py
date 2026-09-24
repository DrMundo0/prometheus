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

def greet_user():
    path = Path('username.json')
    username = get_stored_username(path)
    
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name?")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")

if __name__ == "__main__":
    greet_user()
