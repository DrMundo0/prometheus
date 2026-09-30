import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # 加载图像，类型为surface
        self.image = pygame.image.load('img/ship.png')
        self.rect = self.image.get_rect()
        # 飞船的底部中间与屏幕的底部中间对齐
        self.rect.midbottom = self.screen_rect.midbottom
        # 向右移动标志
        self.moving_right = False
        # 向左移动标志
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        # 移动速度
        self.speed = 6

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """更新飞船的位置"""
        if self.moving_right:
            self.rect.x += self.speed
        elif self.moving_left:
            self.rect.x -= self.speed
        elif self.moving_up:
            self.rect.y -= self.speed
        elif self.moving_down:
            self.rect.y += self.speed
