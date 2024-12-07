import pygame as pg
from importlib import reload
import random
import enemy_data
reload(enemy_data)
import constants as c
reload(c)


class World():
    def __init__(self, data, map_image, stage_data):
        self.image = map_image
        self.level_data = data
        self.waypoints = []
        self.tile_map = []

        self.game_speed = 1
        self.stage_data = stage_data
        self.health = self.stage_data['health']
        self.money = self.stage_data['money']
        self.level_money = self.stage_data['level_reward']
        self.level_spawn_data = self.stage_data['spawn_data']

        self.level = 1
        self.enemy_list = []
        self.enemy_type_list = []
        self.spawned_enemies = 0
        self.killed_enemies = 0
        self.missed_enemies = 0

    def process_data(self):
        # extract data
        for layer in self.level_data["layers"]:
            if layer["name"] == 'waypoints':
                for obj in layer["objects"]:
                    waypoint_data = obj["polyline"]
                    self.process_waypoints(waypoint_data)
            if layer["name"] == 'tilemap':
                self.tile_map = layer['data']
    
    def process_enemies(self):
        enemies = self.level_spawn_data[self.level - 1]
        for enemy_type in enemies:
            for enemy_level, enemy_num in enumerate(enemies.get(enemy_type)):
                for enemy in range(enemy_num):
                    self.enemy_type_list.append(enemy_type)
                    self.enemy_list.append(enemy_level + 1)
        
        c = list(zip(self.enemy_list, self.enemy_type_list))
        random.shuffle(c)
        self.enemy_list, self.enemy_type_list = zip(*c)
        
    def check_level_complete(self):
        if self.killed_enemies + self.missed_enemies >= len(self.enemy_list):
            self.enemy_list = []
            self.enemy_type_list = []
            self.spawned_enemies = 0
            self.killed_enemies = 0
            self.missed_enemies = 0
            
            self.money += self.level_money
            self.level += 1
            return True
        else:
            return False
    
    def process_waypoints(self, data): 
        # Extract x and y
        for point in data:
            self.waypoints.append((point['x'], point['y']))

    def draw(self,surface):
        surface.blit(self.image, (0,0))

    def reset(self):
        self.health = c.HEALTH
        self.money = c.MONEY

        self.level = 1
        self.enemy_list = []
        self.spawned_enemies = 0
        self.killed_enemies = 0
        self.missed_enemies = 0
        