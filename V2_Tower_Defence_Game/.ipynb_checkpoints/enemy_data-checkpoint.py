# Each Dictionary in the list is a level
# Each list says how many of each level and guy you want (No more than 4 levels currently, can add more)
stage_data_1 = {
'spawn_data':[
    {'regular':[10]}, #1
    {'dash':[20]}, #1
    {'regular':[0,5], 'speed':[25]}, #1
    {'constant':[0,10]}, #1
    {'armored':[30]}, #1
    {'regular':[15],'dash':[15],'speed':[15],'constant':[15],'armored':[15]}, #1
    {'regular':[0,1],'dash':[0,1],'speed':[0,1],'constant':[0,1],'armored':[0,1]}, #1 
],
    'level_reward':50,
    'money':650,
    'health':20
}
stage_data_balance = {
'spawn_data':[
    {'regular':[20]}, #1
    {'regular':[0,20]}, #1
    {'regular':[0,0,20]}, #1
    {'regular':[0,0,0,20]}, #1
],
    'level_reward':50,
    'money':10000,
    'health':20
}
# To add new enemies, just change here, one place in main, for new attributes also change enemy line 54
ENEMY_DATA_REG = {
    "level":[{"health": 10, "speed": 2,"reward": 5},
             {"health": 25, "speed": 3,"reward": 10},
             {"health": 50, "speed": 4,"reward": 15},
             {"health": 100,"speed": 5,"reward": 20}],
    "image":'Assets/Enemies/enemy_1.png',
    "dash":False,
    #"blink":False, # not implemented
    "armored":False
}
ENEMY_DATA_SPEED = {
    "level":[{"health": 10, "speed": 3,"reward": 5},
             {"health": 15, "speed": 5,"reward": 10},
             {"health": 20, "speed": 6,"reward": 15},
             {"health": 25, "speed": 8,"reward": 20}],
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
    "level":[{"health": 2, "speed": 2,"reward": 5},
             {"health": 4, "speed": 3,"reward": 10},
             {"health": 6, "speed": 4,"reward": 15},
             {"health": 10, "speed": 6,"reward": 20}],
    "image":'Assets/Enemies/enemy_4.png',
    "consistent":True,
    "damage":1
}
ENEMY_DATA_DASH = {
    "level":[{"health": 8, "speed": 2,"dash_boost":1.5,"reward": 5},
             {"health": 16, "speed": 2,"dash_boost":1.75,"reward": 10},
             {"health": 25, "speed": 2,"dash_boost":2,"reward": 15},
             {"health": 35, "speed": 2,"dash_boost":2.25,"reward": 20}],
    "image":'Assets/Enemies/enemy_dash.png',
    "dash":True,
    "dash_boost":1.25
}