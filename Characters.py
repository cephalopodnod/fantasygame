class Spec:
    def __init__(self):
        self.STR = 0
        self.AGI = 0
        self.CON = 0
        self.WIS = 0
        self.INT = 0
        self.LUK = 0
        self.weapon_types = []
        self.armor_types = []
        self.skills = []
        self.spells = []

    def get_stats(self):
        return {"STR":self.STR,
                "AGI":self.AGI,
                "CON":self.CON,
                "WIS":self.WIS,
                "INT":self.INT,
                "LUK":self.LUK}

    def skill_list(self):
        return self.skills

    def spell_list(self):
        return self.spells    
        
class Warrior(Spec):
    SKILL_DICT = {1:{'Name':'Slash','Damage':10,'Effect': '','Damage Type':'Slashing'},
                  3:{'Name':'Slash','Damage':10,'Effect': '','Damage Type':'Slashing'},
                  5:{'Name':'Slash','Damage':10,'Effect': '','Damage Type':'Slashing'},
                  7:{'Name':'Slash','Damage':10,'Effect': '','Damage Type':'Slashing'},
                  9:{'Name':'Slash','Damage':10,'Effect': '','Damage Type':'Slashing'},
                  11:{'Name':'Slash','Damage':10,'Effect': '','Damage Type':'Slashing'}}
    
    def __init__(self):
        super().__init__()      
        self.STR = 8
        self.AGI = 5
        self.CON = 7
        self.WIS = 4
        self.INT = 4
        self.LUK = 2
        self.weapon_types = ['sword','club','great sword','dagger','mace','spear']
        self.armor_types = ['cloth','leather','chainmail','plate']
        
    def add_skill(self,level):
        if level in Warrior.SKILL_DICT:
            self.skills.append(Warrior.SKILL_DICT[level])

class Character:
    def __init__(self,name,spec):
        self.level = 1
        self.name = name
        self.spec = spec
        self.inventory = {}
        self.currency = 0
        self.equipment = {'head':{},'chest':{},'legs':{},'weapon':{},'off-hand':{}}

    def level_up(self):
        self.level += 1
        self.spec.add_skill(self.level)


tom = Character('Tom',Warrior())
print(tom)
