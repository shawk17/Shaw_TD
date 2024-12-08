import constants as c
# Target types: defualt (longest alive), strong, weak, fast, slow, all
TURRET_DATA = {'level':[
    {"cost":150,"reach":90, "cooldown":1500, "damage": 5,"sprites":"Assets/Turret/turret_1.png"},
    {"cost":250,"reach":110, "cooldown":1200,"damage": 10,"sprites":"Assets/Turret/turret_2.png"},
    {"cost":500,"reach":150, "cooldown":900,"damage": 15,"sprites":"Assets/Turret/turret_3.png"},
    {"cost":None,"reach":170, "cooldown":700, "damage": 20,"sprites":"Assets/Turret/turret_4.png"}],
               "cost":100,
              'image':"Assets/Turret/cursor_turret.png", 'button_x':c.SCREEN_WIDTH + 2, 'button_y':400,
              "description":"Regular Turret",
              "target_type":"default"}
FAST_TURRET_DATA = {'level':[
    {"cost":175,"reach":90, "cooldown":500,"damage":2, "sprites":"Assets/Turret/turret_fast_1.png"},
    {"cost":300,"reach":110, "cooldown":300,"damage":3,  "sprites":"Assets/Turret/turret_fast_2.png"},
    {"cost":500,"reach":125, "cooldown":100,"damage":4,  "sprites":"Assets/Turret/turret_fast_3.png"},
    {"cost":None,"reach":150,"cooldown":0,"damage":5,"sprites":"Assets/Turret/turret_fast_4.png"}],
                    "cost":150,
                    "image":"Assets/Turret/cursor_turret_fast.png",'button_x':c.SCREEN_WIDTH + 102, 'button_y':400,
                    "description":"Fast Turret",
                    "target_type":"weak"
                   }
SLOW_TURRET_DATA = {'level':[
    {"cost":150,"reach":100, "cooldown":3000, "damage": 10, "sprites":"Assets/Turret/turret_slow_1.png"},
    {"cost":200,"reach":150, "cooldown":2800,"damage": 15,  "sprites":"Assets/Turret/turret_slow_2.png"},
    {"cost":200,"reach":200, "cooldown":2600,"damage": 20,  "sprites":"Assets/Turret/turret_slow_3.png"},
    {"cost":None,"reach":250, "cooldown":2500, "damage": 25,"sprites":"Assets/Turret/turret_slow_4.png"}],
                    "cost":200,
                   "image":"Assets/Turret/cursor_turret_slow.png",'button_x':c.SCREEN_WIDTH + 202, 'button_y':400,
                   "description":"High Damage Slow Turret",
                   "target_type":"strong"}
EMP_TURRET_DATA = {'level':[
    {"cost":150,"reach":100, "cooldown":1400, "damage": 1,"sprites":"Assets/Turret/turret_1.png"},
    {"cost":200,"reach":110, "cooldown":1200,"damage": 3,"sprites":"Assets/Turret/turret_2.png"},
    {"cost":250,"reach":120, "cooldown":1000,"damage": 4,"sprites":"Assets/Turret/turret_3.png"},
    {"cost":None,"reach":130, "cooldown":800, "damage": 5,"sprites":"Assets/Turret/turret_4.png"}],
                   "cost":100,
                  "image":"Assets/Turret/cursor_turret.png",'button_x':c.SCREEN_WIDTH + 2, 'button_y':500,
                  "description":"Multitarget Turret",
                  "target_type":"all"}
# Placeholder Turrets Make sure to change the 3 places in main (unless you are fine with the name)
OTHER_TURRET_DATA = {'level':[
    {"cost":150,"reach":100, "cooldown":1400, "damage": 1,"sprites":"Assets/Turret/turret_1.png"},
    {"cost":200,"reach":110, "cooldown":1200,"damage": 3,"sprites":"Assets/Turret/turret_2.png"},
    {"cost":250,"reach":120, "cooldown":1000,"damage": 4,"sprites":"Assets/Turret/turret_3.png"},
    {"cost":None,"reach":130, "cooldown":800, "damage": 5,"sprites":"Assets/Turret/turret_4.png"}],
                   "cost":100,
                  "image":"Assets/Turret/cursor_turret.png",'button_x':c.SCREEN_WIDTH + 102, 'button_y':500,
                  "description":"Multitarget Turret",
                  "target_type":"all"}
ANOTHER_TURRET_DATA = {'level':[
    {"cost":150,"reach":100, "cooldown":1400, "damage": 1,"sprites":"Assets/Turret/turret_1.png"},
    {"cost":200,"reach":110, "cooldown":1200,"damage": 3,"sprites":"Assets/Turret/turret_2.png"},
    {"cost":250,"reach":120, "cooldown":1000,"damage": 4,"sprites":"Assets/Turret/turret_3.png"},
    {"cost":None,"reach":130, "cooldown":800, "damage": 5,"sprites":"Assets/Turret/turret_4.png"}],
                   "cost":100,
                  "image":"Assets/Turret/cursor_turret.png",'button_x':c.SCREEN_WIDTH + 202, 'button_y':500,
                  "description":"Multitarget Turret",
                  "target_type":"all"}