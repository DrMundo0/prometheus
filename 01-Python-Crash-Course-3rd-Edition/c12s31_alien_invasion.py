import sys
import pygame

from c12s34_settings import Settings
from c12s41_ship import Ship

class AlienInvasion:
    """管理游戏资源和行为"""
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
    
    def run_game(self):
        while True:
            # 判断事件类型
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # 设置屏幕背景色
            self.screen.fill(self.settings.bg_color)
            # 绘制飞船
            self.ship.blitme()
            # 刷新绘制区域
            pygame.display.flip()
            # 设置帧率每秒60
            self.clock.tick(60)

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
