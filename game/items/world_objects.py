class WorldObject:
    def __init__(self, name, image, interactive=False, pickable=False):
        self.name = name
        self.dmg = 0
        self.dmg_radius = 0
        self.weight = 0
        self.hp = 0
        self.state = 'stable'
        self.interactive = interactive
        self.pickable = pickable
        self.image = image
        

class Barrel(WorldObject):
    # type options for barrels: Empty, Water, Wine, and Oil 
    def __init__(self, name, cask_type, liquid_type=None, item_weight=0):
        super().__init__(name, interactive=True, pickable=True)
        self.liquid_type = liquid_type
        self.cask_type = cask_type
        if liquid_type == None:
            self.description = 'A ' + cask_type + ' barrel that contains unknown.'
        else:
            self.description = 'A ' + cask_type + ' barrel that contains ' + liquid_type + '.'
        if self.cask_type == 'metal':
            self.hp = 35
            self.weight += 50
        elif self.cask_type == 'wood':
            self.hp = 10
            self.weight += 10
        else:
            self.hp = 5
        if cask_type == 'wood':
            self.flamable = True
            self.explosive = True
            self.conductive = False
        elif cask_type == 'metal' and liquid_type == 'water':
            self.flamable = False
            self.explosive = False
            self.conductive = True
        elif cask_type == 'metal' and (liquid_type == 'oil' or liquid_type == 'wine'):
            self.flamable = False
            self.explosive = True
            self.conductive = True
        else:
            self.flamable = False
            self.explosive = False
            self.conductive = False
        if liquid_type == 'oil':
            self.weight += 50
        elif liquid_type == 'water' or liquid_type == 'wine':
            self.weight += 35
        elif liquid_type == 'empty' or None:
            self.weight += 0
        else:
            self.weight += item_weight

    def add_fire(self):
        if self.flamable:
            self.hp -= 5
            self.dmg += 5
            self.dmg_radius += 1
            self.state = 'burning'
            self.interactive = False
            self.pickable = False
     
    def combust(self):
        if self.explosive and self. hp <= 0:
            self.dmg = 30
            self.dmg_radius += 10
            self.state = 'exploding'
            self.interactive = False
            self.pickable = False

    def add_electricity(self):
        if self.conductive:
            self.dmg += 10
            self.dmg_radius = 1
            self.state = 'electrified'
            self.interactive = False
            self.pickable = False

                
class Chest(WorldObject):
    def __init__(self, name, locked=False, lock_level=0):
        super.__init__(name, interactive=True, pickable=False)
        self.locked = locked
        self.contents = []
        self.description = 'A chest that is ' + locked + '.'
        self.lock_level = lock_level
        self.hp = 1
        
    def add_treasure(self, content=[]):
        for each in content:
            self.contents.append(each)

    def remove_trasure(self, item, to_who):
        to_who.inventory.append(item)
        self.contents.remove(item)

    def unlock(self, method, character=None):
        if method == 'key':
            self.locked = False
        elif method == 'lopckpick' and character != None:
            if character.lockpick >= self.lock_level:
                self.locked = False
            else:
                character.inventory['lockpick'] -= 1
        elif method == 'force' and character != None:
            if character.strength >= self.lock_level and character.strength < self.lock_level + 3:
                self.locked = False
                return 'You managed to get the lock open.'
            elif character.strength < self.lock_level:
                self.locked = True
                return 'The lock is too strong to break.'
            elif character.strenght >= self.lock_level + 3:
                self.locked = True
                return 'You broke the lock but the chest now seems jammed stuck.'
            else:
                return 'Nothing happened.'
            
class Trash(WorldObject):
    def __init__(self, name):
        super.__init__(name, interactive=False, pickable=False)
        self.description = 'A pile of trash, maybe something hidden underneath.'
        self.contents = []
        self.lootable = True

    def loot_trash(self, character):
        for each in self.contents:
            character.inventory.append(each)
            self.contents.remove(each)
        self.lootable = False

class Door(WorldObject):
    def __init__(self, name, type, locked=False, lock_level=0):
        super.__init__(name, interactive=True, pickable=False)
        self.type = type
        self.state = 'closed'
        self.locked = locked
        self.description = 'A door that is ' + locked + '.'
        self.lock_level = lock_level
        if self.type == 'metal':
            self.hp = 500
            self.breakable = True
        elif self.type == 'wood':
            self.hp = 20
            self.breakable = True
        else:
            self.breakable = False

    def open_door(self, method, character=None):    
        if self.locked:
            if method == 'key':
                self.locked = False
            elif method == 'lopckpick' and character != None:
                if character.lockpick >= self.lock_level:
                    self.locked = False
                else:
                    character.inventory['lockpick'] -= 1
            elif method == 'force' and character != None:
                if character.strength >= self.lock_level and character.strength < self.lock_level + 3:
                    self.locked = False
                    return 'You managed to get the lock open.'
                elif character.strength < self.lock_level:
                    self.locked = True
                    return 'The lock is too strong to break.'
                elif character.strenght >= self.lock_level + 3:
                    self.locked = True
                    return 'You broke the lock but the chest now seems jammed stuck.'
                else:
                    return 'Nothing happened.'
        else:
            self.state = 'open'

class Lever(WorldObject):
    def __init__(self, name, state='off'):
        super.__init__(name, interactive=True, pickable=False)
        self.state = state
        self.description = 'A lever that is ' + state + '.'

    def pull_lever(self):
        if self.state == 'off':
            self.state = 'on'
        else:
            self.state = 'off'

class Item(WorldObject):
    def __init__(self, item):
        super.__init__(name, interactive=False, pickable=True)
        self.item = item
        
    def pickup(self, character):
        character.inventory.append(self)    
