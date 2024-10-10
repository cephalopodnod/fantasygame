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
        # Need to fix this up.
        self.defense = spec.CON + self.equipment

    def level_up(self):
        self.level += 1
        self.spec.add_skill(self.level)
    
    def add_item(self,amount=1,item={}):
        self.inventory.append({'Item':item,'Quantity':amount})

    def equip_item(self,position='',item={}):
        if self.equipment[position] == {}:
            self.equipment[position] = item
            self.inventory.remove(item)
        else:
            self.inventory.append(self.equipment[position])
            self.equipment[position] = item
            self.inventory.remove(item)
         
    def attack(self,target):
        attack = (atk + weapon_atk) - target.defense
        crit_multiplier = 0.10 * (self.LCK * 0.04)
        target.hp = target.hp - attack * crit_multiplier
         
class Enemy:
    def __init__(self,hp=0,mp=100,armor=0,mr=0,atk=0) -> None:
        self.hp = hp
        self.mp = mp
        self.armor = armor
        self.mr = mr
        self.atk = atk
        self.abilities = []

    def attack(self,target):
        attack = self.atk - target.defense
        target.hp = target.hp - attack