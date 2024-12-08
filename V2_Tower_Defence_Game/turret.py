import pygame as pg
import constants as c
import math
from importlib import reload

class Turret(pg.sprite.Sprite):
    def __init__(self, tile_x, tile_y, turret_data):
        pg.sprite.Sprite.__init__(self)
        # Stats Variables
        self.level = 1
        self.turret_data = turret_data
        self.upgrade_cost = self.turret_data['level'][self.level-1].get('cost')
        self.cooldown = self.turret_data['level'][self.level-1].get('cooldown')
        self.reach = self.turret_data['level'][self.level-1].get('reach')
        self.damage = self.turret_data['level'][self.level-1].get('damage')
        
        self.target_type = self.turret_data['target_type']
        self.target_types = ['default', 'weak', 'strong', 'slow', 'fast']
        self.max_level = len(self.turret_data['level'])
        self.selected = False
        self.last_shot = pg.time.get_ticks()
        self.target = None

        # Posistion Variables
        self.tile_x = tile_x
        self.tile_y = tile_y
        self.x = (self.tile_x +0.5) * c.TILE_SIZE
        self.y = (self.tile_y +0.5) * c.TILE_SIZE

        # Animation Variables
        self.animation_images = []
        self.load_animation()
        self.frame_index = 0
        self.update_time = pg.time.get_ticks()
        
        # Image Variables
        self.angle = 90
        self.original_image = self.animation_images[self.frame_index]
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        

        # range image
        self.range_image = pg.Surface((self.reach*2, self.reach*2))
        self.range_image.fill((0,0,0))
        self.range_image.set_colorkey((0,0,0))
        pg.draw.circle(self.range_image, ('grey100'), (self.reach, self.reach), self.reach)
        self.range_image.set_alpha(100)
        self.range_rect = self.range_image.get_rect()
        self.range_rect.center = self.rect.center
    
    def load_animation(self):
        # populate animaiton images
        sprite_sheet = pg.image.load(self.turret_data['level'][self.level - 1].get('sprites'))
        size = sprite_sheet.get_height()
        self.animation_images = []
        for i in range(c.ANIMATION_STEPS):
            self.animation_images.append(sprite_sheet.subsurface(i*size, 0, size, size))
        
    def update(self, enemy_group, world):
        if self.target:
            self.play_animation(world)
        else:
            if pg.time.get_ticks() - self.last_shot >= (self.cooldown / world.game_speed):
                self.pick_target(enemy_group)

    def upgrade(self):
        if self.level < len(self.turret_data['level']):
            self.level += 1
            self.upgrade_cost = self.turret_data['level'][self.level-1].get('cost')
            self.cooldown = self.turret_data['level'][self.level-1].get('cooldown')
            self.reach = self.turret_data['level'][self.level-1].get('reach')
            self.damage = self.turret_data['level'][self.level-1].get('damage')
            # range image upgrade
            self.range_image = pg.Surface((self.reach*2, self.reach*2))
            self.range_image.fill((0,0,0))
            self.range_image.set_colorkey((0,0,0))
            pg.draw.circle(self.range_image, ('grey100'), (self.reach, self.reach), self.reach)
            self.range_image.set_alpha(100)
            self.range_rect = self.range_image.get_rect()
            self.range_rect.center = self.rect.center

            self.load_animation()
            self.original_image = self.animation_images[self.frame_index]
        else:
            print('It is at max level already')

    def play_animation(self, world):
        self.original_image = self.animation_images[self.frame_index]
        if pg.time.get_ticks() - self.update_time > c.ANIMATION_DELAY/world.game_speed:
            self.frame_index = self.frame_index + 1
            self.update_time = pg.time.get_ticks()
            
        if self.frame_index >= c.ANIMATION_STEPS:
            self.frame_index = 0
            self.last_shot = pg.time.get_ticks()
            self.target = None

    def draw(self, screen):
        self.image = pg.transform.rotate(self.original_image, self.angle-90)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        
        screen.blit(self.image, self.rect)
        if self.selected:
            screen.blit(self.range_image, self.range_rect)
        
    def pick_target(self, enemy_group):
        enemy_possible = []
        for enemy in enemy_group:
            if enemy.health > 0:
                x_dist, y_dist = self.calc_dist(enemy)
                dist = ( x_dist**2 + y_dist**2 )**0.5
                if dist < self.reach:
                    enemy_possible.append(enemy)

        # Choose target based on targeting type             
        if len(enemy_possible) > 0:
            self.target = enemy_possible[0]
            if self.target_type == 'slow':
                for enemy in enemy_possible:
                    if enemy.speed < self.target.speed:
                        self.target = enemy
            elif self.target_type == 'fast':
                for enemy in enemy_possible:
                    if enemy.speed > self.target.speed:
                        self.target = enemy
            elif self.target_type == 'weak':
                for enemy in enemy_possible:
                    if enemy.health < self.target.health:
                        self.target = enemy
            elif self.target_type == 'strong':
                for enemy in enemy_possible:
                    if enemy.health > self.target.health:
                        self.target = enemy
            elif self.target_type == 'all':
                for enemy in enemy_possible:
                    enemy.deal_damage(self.damage)
            # Rotate and deal damage         
            if not self.target_type == 'all': 
                self.target.deal_damage(self.damage)
                x_dist, y_dist = self.calc_dist(self.target)
                self.angle = math.degrees(math.atan2(-y_dist, x_dist))
                    
    def calc_dist(self, enemy):
        return enemy.pos[0]-self.x, enemy.pos[1]-self.y

    def change_target_type(self):
        if not self.target_type == 'all':
            self.target_type = self.target_types[(self.target_types.index(self.target_type) + 1) % len(self.target_types)]







