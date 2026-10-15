# 存储游戏设置
class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 6
        # 子弹的速度
        self.bullet_speed = 2.5
        # 子弹的宽度
        self.bullet_width = 3000
        # 子弹的高度
        self.bullet_height = 15
        # 子弹的颜色
        self.bullet_color = (60, 60, 60)
        # 子弹的数量
        self.bullets_allowed = 3
        # 外星人的移动速度
        self.alien_speed = 1.0
        # 玩家有几条命
        self.ship_limit = 3
        # 外星人下落速度
        self.alien_fleet_drop_speed = 50
        # 外星人移动方向，1表示向右，-1表示向左
        self.alien_fleet_direction = 1
