class Warrior():
    SKILL_DICT = {1: {'Name': 'Slash', 'Damage': 10, 'Effect': '', 'Damage Type': 'Slashing'},
                  3: {'Name': 'Smash', 'Damage': 15, 'Effect': '', 'Damage Type': 'Bludgeon'},
                  5: {'Name': 'Slash', 'Damage': 10, 'Effect': '', 'Damage Type': 'Slashing'},
                  7: {'Name': 'Slash', 'Damage': 10, 'Effect': '', 'Damage Type': 'Slashing'},
                  9: {'Name': 'Slash', 'Damage': 10, 'Effect': '', 'Damage Type': 'Slashing'},
                  11: {'Name': 'Slash', 'Damage': 10, 'Effect': '', 'Damage Type': 'Slashing'}}

    def __init__(self):
        self.STR = 8
        self.AGI = 5
        self.CON = 7
        self.WIS = 4
        self.INT = 4
        self.LUK = 2
        self.weapon_types = ['sword', 'club', 'great sword', 'dagger', 'mace', 'spear']
        self.armor_types = ['cloth', 'leather', 'chainmail', 'plate']
        self.skills = [{'Name': 'Slash', 'Damage': 10, 'Effect': '', 'Damage Type': 'Slashing'}]
        self.spells = []
    def add_skill(self, level=0):
        if level in Warrior.SKILL_DICT.keys():
            self.skills.append(Warrior.SKILL_DICT[level])
        else:
            pass

    def get_stats(self):
        return {"STR": self.STR,"AGI": self.AGI,"CON": self.CON,"WIS": self.WIS,"INT": self.INT,"LUK": self.LUK}

    def skill_list(self):
        return self.skills

    def spell_list(self):
        return self.spells

class Character:
    def __init__(self, name, spec):
        self.level = 1
        self.name = name
        self.spec = spec
        self.inventory = []
        self.currency = 0
        self.equipment = {'head': {}, 'chest': {}, 'legs': {}, 'weapon': {}, 'off-hand': {}}

    def level_up(self):
        self.level += 1
        self.spec.add_skill(self.level)
    def add_item(self,amount,item):
        self.inventory.append({'Item':item,'Quantity':amount})

class Consumable:
    def __int__(self,name,stat='',increase=0):
        self.name = name
        self.stat = stat
        self.increase = increase

class Armor:
    def __init__(self,position,type,armor=0,mr=0,bonus={}):
        self.slot = position
        self.type = type
        self.stats = {'Armor':armor,'Magic Resist':mr}
        self.bonus_trait = bonus

class Weapon:
    def __init__(self,type,hands=1,damage=0,atkspd=0,bonus={}):
        self.type = type
        self.hands = hands
        self.stats = {'Damage':damage,'Attack Speed':atkspd}
        self.bonus_trait = bonus        

class OffHand:
    '''
    brace -> enhance melee 2 hander
    shield -> 1 hand defensive with 1 hand melee or caster
    ammo -> enhances ranged weapon
    bauble -> enhances mage with 1 hand melee or caster
    off-hand -> enhance melee with 1 hand melee or caster
    '''
    OFFHAND_TYPES = ['brace','shield','ammo','bauble','off-hand']
    
    def __init__(self,type,stats={},bonus={}):
        self.type = type
        self.stats = stats
        self.bonus_trait = bonus   