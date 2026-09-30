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
            self._check_events()
            self.ship.update()
            self._update_screen()
            # 设置帧率每秒60
            self.clock.tick(60)

    # 辅助方法以下划线开头，只在类中调用，不在类外调用
    def _check_events(self):
        """响应按键和鼠标事件"""
        # 判断事件类型
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # 监听按键按下事件
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # 监听按键弹起事件
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        # 右方向键向右移动
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        # 左方向键向左移动
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        # 设置屏幕背景色
        self.screen.fill(self.settings.bg_color)
        # 绘制飞船
        self.ship.blitme()
        # 刷新绘制区域
        pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
