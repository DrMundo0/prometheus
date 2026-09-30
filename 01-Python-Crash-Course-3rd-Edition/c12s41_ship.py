import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # 加载图像，类型为surface
        self.image = pygame.image.load('img/ship.png')
        self.rect = self.image.get_rect()
        # 飞船的底部中间与屏幕的底部中间对齐
        self.rect.midbottom = self.screen_rect.midbottom
        # 浮点让飞船的移动更平滑
        self.x = float(self.rect.x)
        # 向右移动标志
        self.moving_right = False
        # 向左移动标志
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """更新飞船的位置"""
        # 最右不能超过屏幕的右边
        if self.moving_right and self.rect.right < self.screen_rect.right + self.rect.width / 2:
            self.x += self.settings.ship_speed
        # 把elif改成if可以支持斜着移动
        if self.moving_left and self.rect.left > 0 - self.rect.width / 2:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.ship_speed
        
        self.rect.x = self.x
