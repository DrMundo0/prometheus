# 存储游戏设置
class Settings:
    def __init__(self):
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 子弹的宽度
        self.bullet_width = 3000
        # 子弹的高度
        self.bullet_height = 15
        # 子弹的颜色
        self.bullet_color = (60, 60, 60)
        # 子弹的数量
        self.bullets_allowed = 3
        # 玩家有几条命
        self.ship_limit = 3
        # 外星人下落速度
        self.alien_fleet_drop_speed = 50
        # 以什么速度加快游戏的节奏
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    # 初始化动态设置
    def initialize_dynamic_settings(self):
        """初始化游戏进行而变化的设置"""
        # 飞船速度
        self.ship_speed = 6
        # 子弹的速度
        self.bullet_speed = 2.5
        # 外星人的移动速度
        self.alien_speed = 1.0
        # 外星人移动方向，1表示向右，-1表示向左
        self.alien_fleet_direction = 1

    def increase_speed(self):
        """提高速度设置的值"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
