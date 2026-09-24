# 学习重构

from pathlib import Path
import json

def greet_user():
    path = Path('username.json')
    if path.exists():
        contents = path.read_text(encoding='utf-8')
        username = json.loads(contents)
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name?")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")

if __name__ == "__main__":
    greet_user()
