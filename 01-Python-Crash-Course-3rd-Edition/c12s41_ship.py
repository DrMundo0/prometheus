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

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
