import sys
import pygame

class AlienInvasion:
    """管理游戏资源和行为"""
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (230, 230, 230)
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # 设置屏幕背景色
            self.screen.fill(self.bg_color)
            # 刷新绘制区域
            pygame.display.flip()
            # 设置帧率每秒60
            self.clock.tick(60)


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
