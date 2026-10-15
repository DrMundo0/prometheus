import sys
from time import sleep

import pygame

from c12s34_settings import Settings
from c12s41_ship import Ship
from c12s82_bullet import Bullet
from c13s21_alien import Alien
from c13s62_game_stats import GameStats

class AlienInvasion:
    """管理游戏资源和行为"""
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        # 窗口模式
        self.screen = pygame.display.set_mode((1200, 800))
        # 全屏游戏
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        # 创建一个用于存储游戏统计信息的实例
        self.stats = GameStats(self)
        # 创建飞船
        self.ship = Ship(self)
        # 存放所有有效的子弹
        self.bullets = pygame.sprite.Group()
        # 外星人编队
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
    
    def run_game(self):
        while True:
            self._check_events()
            # 更新飞船的位置
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_ESCAPE:
            # 按Esc退出游戏
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _create_fleet(self):
        # 创建外星飞船舰队
        alien = Alien(self)
        # 因为size是一个元组，所以可以用两个变量来拆分接收
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height

        # 根据屏幕的高度控制外星舰队的行数
        while current_y < (self.settings.screen_height - 3 * alien_height):
            # 因为外星人的间距与外星人的宽度相同，所以是2倍的外星人宽度
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            # 添加一行外星人后，重置x并递增y值
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """创建一个外星人并将其放到当前行中"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.y = y_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_alien_fleet_edges(self):
        """在外星人到达边缘时采取相应的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                # 每次撞到屏幕边缘后下移每个外星人并改版它们的移动方向
                self._change_alien_fleet_direction()
                break

    def _change_alien_fleet_direction(self):
        """将整个外星舰队向下移动，并改变它们的移动方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.alien_fleet_drop_speed
        self.settings.alien_fleet_direction *= -1

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        # 设置屏幕背景色
        self.screen.fill(self.settings.bg_color)

        # 先绘制子弹，以防子弹出现在飞机上
        for bullet in self.bullets:
            bullet.draw_bullet()

        # 绘制飞船
        self.ship.blitme()
        # 绘制外星人
        self.aliens.draw(self.screen)
        
        # 刷新绘制区域
        pygame.display.flip()

    def _update_bullets(self):
        """更新子弹的位置并删除已消失的子弹"""
        # 更新子弹的位置
        self.bullets.update()

        # 删除已消失的子弹，节约内存
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """响应子弹和外星人的碰撞"""
        # 检查是否有子弹击中了外星人，如果是，就删除相应的子弹和外星人
        # collide是碰撞的意思，检测两个Group的碰撞
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        # 每次击落外星人之后检查外星人队列是否为空，空了则创建新的外星舰队
        if not self.aliens:
            # 删除现有的子弹并创建一个新的外星舰队
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """更新外星舰队中所有外星人的位置"""
        self._check_alien_fleet_edges()
        self.aliens.update()

        # 检测外星人和飞船之间的碰撞
        # 检测一个Sprite和Group的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _ship_hit(self):
        """响应飞船和外星人的碰撞"""
        # 将ships_left减一
        self.stats.ships_left -= 1
        # 清空外星人列表和子弹列表
        self.bullets.empty()
        self.aliens.empty()
        # 创建一个新的外星舰队，并将飞船放在屏幕底部的中央
        self._create_fleet()
        self.ship.center_ship()
        # 暂停
        sleep(1.5)

    def _fire_bullet(self):
        """发射子弹"""
        # 限制可发射的子弹的数量
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
