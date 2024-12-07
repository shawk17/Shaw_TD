import pygame as pg
from pygame.math import Vector2
import math
from importlib import reload

class Enemy(pg.sprite.Sprite):
    def __init__(self, level, waypoints, enemy_data):
        pg.sprite.Sprite.__init__(self)
        
        self.waypoints = waypoints
        self.pos = Vector2(waypoints[0])
        self.target_waypoint = 1
        self.enemy_data = enemy_data

        self.level = level
        self.speed = self.enemy_data["level"][self.level-1].get('speed')
        self.health = self.enemy_data["level"][self.level-1].get('health')
        self.reward = self.enemy_data["level"][self.level-1].get('reward')
        
        self.angle = 0
        self.original_image = pg.image.load(enemy_data['image']).convert_alpha()

        self.min_size = 3
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.image = pg.transform.scale_by(self.image, math.log10(self.health/5 + self.min_size))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
    
    def update(self, world):
        if self.check_alive(world):
            self.move(world)
            self.rotate()
        
    
    def move(self, world):
        # define target waypoint
        self.image = pg.transform.scale_by(self.image, math.log10(self.health/5 + self.min_size))
        if self.target_waypoint < len(self.waypoints):
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target - self.pos
        else:
            world.health -= 1
            world.missed_enemies += 1
            self.kill()

        # Calculate distance to target
        dist = self.movement.length()
        if dist >= (self.speed * world.game_speed):
            self.pos += (self.speed * world.game_speed) * self.movement.normalize()
        else:
            if dist != 0:
                self.pos += dist * self.movement.normalize()
            self.target_waypoint += 1

    def rotate(self):
        dist = self.target - self.pos
        self.angle = math.degrees(math.atan2(-dist[1], dist[0]))
        
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.image = pg.transform.scale_by(self.image, math.log10(self.health/5 + self.min_size))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def check_alive(self, world):
        if self.health <= 0:
            world.money += self.reward
            world.killed_enemies += 1
            self.kill()
            return False
        return True

    def deal_damage(self, damage):
        self.health -= damage
        
        if self.enemy_data.get('dash'):
            self.speed *= self.enemy_data['level'][self.level-1].get('dash_boost')
        if self.enemy_data.get('armored'):
            self.health += self.enemy_data['level'][self.level-1].get('armored_amount')
        if self.enemy_data.get('consistent'):
            self.health += damage
            self.health -= self.enemy_data['damage']
            























