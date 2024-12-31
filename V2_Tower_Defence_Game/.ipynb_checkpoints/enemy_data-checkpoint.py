# To add new enemies, just change here, one place in main, for new attributes also change enemy line 54
ENEMY_DATA_REG = {
    "level":[{"health": 10, "speed": 2,"reward": 5},
             {"health": 25, "speed": 3,"reward": 10},
             {"health": 75, "speed": 4,"reward": 15},
             {"health": 100,"speed": 5,"reward": 20}],
    "image":'Assets/Enemies/enemy_1.png',
    "dash":False,
    #"blink":False, # not implemented
    "armored":False
}
ENEMY_DATA_STRONG = {
    "level":[{"health": 20, "speed": 1,"reward": 5},
             {"health": 50, "speed": 1.5,"reward": 10,},
             {"health": 100, "speed": 2,"reward": 15,},
             {"health": 200, "speed": 2.5,"reward": 20,}],
    "image":'Assets/Enemies/enemy_3.png',
}
ENEMY_DATA_SPEED = {
    "level":[{"health": 10, "speed": 3,"reward": 6},
             {"health": 15, "speed": 5,"reward": 10},
             {"health": 30, "speed": 6,"reward": 15},
             {"health": 50, "speed": 8,"reward": 20}],
    "image":'Assets/Enemies/enemy_2.png'
}
ENEMY_DATA_ARMORED = {
    "level":[{"health": 10, "speed": 1,"reward": 5, 'armored_amount':2},
             {"health": 20, "speed": 2,"reward": 10, 'armored_amount':3},
             {"health": 30, "speed": 3,"reward": 15, 'armored_amount':4},
             {"health": 50, "speed": 4,"reward": 20, 'armored_amount':5}],
    "image":'Assets/Enemies/enemy_3.png',
    "armored":True
}
ENEMY_DATA_CONSTANT = {
    "level":[{"health": 10, "speed": 2,"reward": 5},
             {"health": 20, "speed": 3,"reward": 10},
             {"health": 30, "speed": 4,"reward": 15},
             {"health": 50, "speed": 5,"reward": 20}],
    "image":'Assets/Enemies/enemy_4.png',
    "consistent":True,
    "damage":5
}
ENEMY_DATA_DASH = {
    "level":[{"health": 8, "speed": 2,"dash_boost":1.5,"reward": 5},
             {"health": 15, "speed": 2,"dash_boost":1.75,"reward": 10},
             {"health": 30, "speed": 2,"dash_boost":2,"reward": 15},
             {"health": 50, "speed": 2,"dash_boost":2.25,"reward": 20}],
    "image":'Assets/Enemies/enemy_dash.png',
    "dash":True,
    "dash_boost":1.25
}