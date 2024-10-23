class Dice:
    import random
    def __init__(self,qty,size=4) -> None:
        self.qty = qty
        self.size = size

    def roll(self):
        import random
        value = 0
        for die in range(1,self.qty+1):
            value += random.randint(1,self.size)
        return value
    
class Character:
    INITIAL_STAT_POINTS = 27

    def __init__(self,race,spec) -> None:
        self.race = race
        self.spec = spec
        self.hp = 0
        self.ac = 10
        self.spellslots = {"0":0,
                           "1":0,
                           "2":0,
                           "3":0,
                           "4":0,
                           "5":0,
                           "6":0,
                           "7":0,
                           "8":0,
                           "9":0}
        self.spells = []
        self.actions = ['Attack','Move','Sprint','Jump','Shove','Disengage']
        self.weaponskills = []
        self.stats = {"STR":8,
                      "DEX":8,
                      "CON":8,
                      "WIS":8,
                      "INT":8,
                      "CHR":8}
        self.equipment = {'Head':None,
                          "Chest":None,
                          "Legs":None,
                          "Hands":None,
                          "Back":None,
                          "Main Hand":None,
                          "Off Hand":None,
                          "Neck":None,
                          "Ring 1":None,
                          "Ring 2":None}
        self.proficiencies = {"Acrobatics": 0,
                              "Animal Handling": 0,
                              "Arcana": 0,
                              "Athletics": 0,
                              "Deception": 0,
                              "History": 0,
                              "Insight": 0,
                              "Intimidation": 0,
                              "Investigation": 0,
                              "Medicine": 0,
                              "Nature": 0,
                              "Perception": 0,
                              "Performance": 0,
                              "Persuasion": 0,
                              "Religion": 0,
                              "Sleight of Hand": 0,
                              "Stealth": 0,
                              "Survival": 0,
                              "Light Armor": 0,
                              "Medium Armor": 0,
                              "Heavy Armor": 0,
                              "Shields": 0,
                              "Simple Weapons": 0,
                              "Martial Weapons": 0}
        self.tools = {"Tools (Artisan’s tools)": 0,
                      "Tools (Disguise Kit)": 0,
                      "Tools (Forgery Kit)": 0,
                      "Tools (Gaming Set)": 0,
                      "Tools (Herbalism Kit)": 0,
                      "Tools (Musical Instrument)": 0,
                      "Tools (Navigator’s Tools)": 0,
                      "Tools (Poisoner’s Kit)": 0,
                      "Tools (Thieves' Tools)": 0}
        self.vehicles = {"Vehicles (Land)": 0,
                         "Vehicles (Water)": 0}
        self.languages = {"Languages (Common)": 0,
                          "Languages (Elvish)": 0,
                          "Languages (Dwarvish)": 0,
                          "Languages (Gnomish)": 0,
                          "Languages (Halfling)": 0,
                          "Languages (Orc)": 0,
                          "Languages (Goblin)": 0,
                          "Languages (Draconic)": 0,
                          "Languages (Abyssal)": 0,
                          "Languages (Infernal)": 0,
                          "Languages (Celestial)": 0,
                          "Languages (Sylvan)": 0,
                          "Languages (Primordial)": 0}
        self.maxcarryweight = self.stats['STR'] * 15
        self.carryweight = 0
        if self.race == 'Halflings' or self.race == 'Dwarves' or self.race == 'Gnomes':
            self.movedistance = 25
        else:
            self.movedistance = 30

    def buy_stat(self,stat):
        points = Character.INITIAL_STAT_POINTS
        if self.stats[stat] == 14 and points < 9:
            points = points - 9
            self.stats[stat] = self.stats[stat] + 1
        elif self.stats[stat] == 13 and points > 7:
            points = points - 7
            self.stats[stat] = self.stats[stat] + 1
        elif self.stats[stat] == 12 and points > 5:
            points = points - 5
            self.stats[stat] = self.stats[stat] + 1
        elif self.stats[stat] == 11 and points > 4:
            points = points - 4
            self.stats[stat] = self.stats[stat] + 1
        elif self.stats[stat] == 10 and points > 3:
            points = points - 3
            self.stats[stat] = self.stats[stat] + 1
        elif self.stats[stat] == 9 and points > 2:
            points = points - 2
            self.stats[stat] = self.stats[stat] + 1
        elif self.stats[stat] == 8 and points > 1:
            points = points - 1
            self.stats[stat] = self.stats[stat] + 1

    def check_weight(self):
        if self.carryweight >= self.stats['STR'] * 10:
            self.movedistance = self.movedistance - 20
        elif self.carryweight >= self.stats['STR'] * 5:
            self.movedistance = self.movedistance - 10
        else:
            pass

class Weapon:
    #DMGTYPES = ['Bludgeoning','Slashing','Piercing']
    def __init__(self,name,dmgtype,bonus=None,qty=1,size=4) -> None:
        self.name = name
        self.dmgtype = dmgtype
        self.bonus = bonus
        self.damage = {'Quantity':qty,'Size':size}     

class Armor:
    #ARMORTYPES = ['Clothing','Light','Medium','Heavy']
    def __init__(self,armortype,position,ac=10,bonus=None) -> None:
        self.ac = ac
        self.armortype = armortype
        self.position = position
        self.bonus = bonus

    def equip(self,character):
        character.ac = character.ac + self.ac
        character.equipment[self.position] = self

class Consumable:
    def __init__(self) -> None:
        pass

class OffHand:
    def __init__(self) -> None:
        pass


jon = Character()
print(jon.stats)
jon.buy_stat('STR')
print(jon.stats)
