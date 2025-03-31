class Dungeon:
    def __init__(self, name, level):
        self.active = False
        self.name = name
        self.level = level
        self.rooms = []
        self.current_room = None
        self.entrance_exit = (0,0)
        self.players = []

    def enter(self, player):
        self.players.append(player)
        self.active = True
        self.set_current_room("Entrance")
        
    def exit(self, player):
        self.players.remove(player)
        
    def add_room(self, room):
        self.rooms.append(room)
    
    def get_room(self, room_name):
        for room in self.rooms:
            if room.name == room_name:
                return room
        return None

    def set_current_room(self, room_name):
        self.current_room = self.get_room(room_name)

    def get_current_room(self):
        return self.current_room

    def get_room_names(self):
        return [room.name for room in self.rooms]
    

class Room:
    # name options for rooms in a dungeon: Entrance, Hall, Stairs, Boss, Locked, Treasure, and Junk
    def __init__(self):
        self.name = ''
        self.x = 0
        self.y = 0
        self.connectors = {'Top':False, 'Bottom':False, 'Left':False, 'Right':False}
        self.characters = []
        self.objects = []
        self.enemies = []
        self.background = None
        self.interactives = []
        self.description = self.name + str(self.background) + "pos_" + str(self.x) + "_" + str(self.y)

    def build_room(self, type, x, y, background, connectors=[], objects=[], enemies=[], interactives=[]):
        self.name = type
        self.x = x
        self.y = y
        self.background = background
        for each in connectors:
            self.connectors[each] = True
        for each in objects:
            self.objects.append(each) 
        for each in enemies:
            self.enemies.append(each)   
        for each in interactives:    
            self.interactives.append(each)

    def add_character(self, character):
        self.characters.append(character)

    def remove_character(self, character):
        self.characters.remove(character)

    def add_object(self, room):
        self.objects.append(room)

    def remove_object(self, object):
        self.objects.remove(object) 
   
    def add_enemy(self, enemy):
        self.enemies.append(enemy)    
    
    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    def add_interactive(self, interactive):
        self.interactives.append(interactive)
    
    def remove_interactive(self, interactive):
        self.interactives.remove(interactive)   
        

