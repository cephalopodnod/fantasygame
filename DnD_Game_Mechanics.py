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
    POSSIBLE_FEATS = {
    "Actor": "Gain +1 to Charisma. Advantage on Deception and Performance checks when trying to pass as a different person. Can mimic voices after hearing them.",
    "Athlete": "Gain +1 to Strength or Dexterity. Climbing doesn’t cost extra movement, standing up from prone costs only 5 feet of movement.",
    "Alert": "Gain +5 to initiative, cannot be surprised while conscious, and other creatures don’t gain advantage on attack rolls against you from being hidden.",
    "Charger": "If you Dash, you can make a melee attack or shove with a +5 bonus to the damage if you move at least 10 feet in a straight line.",
    "Crossbow Expert": "Ignore the loading property of crossbows you’re proficient with, no disadvantage on ranged attacks within 5 feet, and can use a bonus action for a second crossbow attack.",
    "Defensive Duelist": "If you’re wielding a finesse weapon, you can use your reaction to add your proficiency bonus to AC against one melee attack.",
    "Dual Wielder": "Gain +1 to AC when dual-wielding, can use non-light melee weapons in each hand, and draw two weapons at once.",
    "Dungeon Delver": "Advantage on Perception and Investigation checks to detect traps, resist effects of traps, and find hidden doors.",
    "Durable": "Gain +1 to Constitution. When you roll a hit die to regain HP, treat any roll as a minimum of your Constitution modifier.",
    "Elemental Adept": "Choose a damage type (acid, cold, fire, lightning, or thunder). Damage of that type ignores resistance, and rolls of 1 on that type of damage are treated as 2.",
    "Grappler": "Gain advantage on attack rolls against creatures you’re grappling, and you can restrain a creature you're grappling (with mutual restraint).",
    "Great Weapon Master": "On a critical hit or a kill, make a bonus action melee attack. Take a -5 penalty to hit for a +10 bonus to damage on a melee attack.",
    "Healer": "Use a healer's kit to restore 1d6 + 4 HP + target’s level. Stabilize creatures at 1 HP instead of 0 when using a healer’s kit.",
    "Heavily Armored": "Gain proficiency with heavy armor, and +1 to Strength.",
    "Heavy Armor Master": "Gain +1 to Strength. While in heavy armor, reduce bludgeoning, piercing, and slashing damage by 3.",
    "Inspiring Leader": "Give a 10-minute speech to grant temporary HP equal to your level + Charisma modifier to allies within 30 feet.",
    "Keen Mind": "Gain +1 to Intelligence. Always know which way is north, the number of hours until sunset, and can recall anything seen or heard in the past month.",
    "Lightly Armored": "Gain proficiency with light armor and +1 to Strength or Dexterity.",
    "Linguist": "Gain +1 to Intelligence. Learn three languages and can create written ciphers that others need proficiency in Intelligence to decode.",
    "Lucky": "Gain 3 luck points per long rest. Spend one to reroll an attack, ability check, or saving throw (take your choice of roll).",
    "Mage Slayer": "When a creature within 5 feet casts a spell, you can use your reaction to make a melee attack. Also, give disadvantage to creatures you damage on their Concentration checks.",
    "Magic Initiate": "Choose a class (Bard, Cleric, Druid, Sorcerer, Warlock, or Wizard) to learn two cantrips and one 1st-level spell that can be cast once per long rest.",
    "Martial Adept": "Learn two maneuvers and gain one superiority die (d6), which can be used once per short rest.",
    "Medium Armor Master": "Stealth is not disadvantaged in medium armor, and the armor's Dexterity bonus increases to +3 instead of +2.",
    "Mobile": "Gain +10 to movement speed, and when you make a melee attack against a creature, it can’t make opportunity attacks against you that turn.",
    "Moderately Armored": "Gain proficiency with medium armor and shields, and +1 to Strength or Dexterity.",
    "Mounted Combatant": "Advantage on melee attacks against unmounted creatures smaller than your mount, and can redirect attacks targeting your mount to yourself.",
    "Observant": "Gain +1 to Intelligence or Wisdom. Gain a +5 bonus to passive Perception and Investigation and can read lips if you know the language.",
    "Polearm Master": "Can make a melee weapon attack as a bonus action with the opposite end of a polearm. Gain opportunity attacks when creatures enter your reach.",
    "Resilient": "Gain +1 to one ability score of your choice, and gain proficiency in saving throws with that score.",
    "Ritual Caster": "Learn two 1st-level spells with the ritual tag from any class, and add new ritual spells to your list if you find spell scrolls.",
    "Savage Attacker": "Once per turn, reroll the damage of a melee weapon attack and choose the higher result.",
    "Sentinel": "Creatures you hit with opportunity attacks have their speed reduced to 0, and you can make an opportunity attack on creatures that attack others within 5 feet.",
    "Sharpshooter": "Ignore disadvantage on long-range attacks, ignore half and three-quarters cover, and take a -5 penalty to hit for a +10 bonus to damage on ranged attacks.",
    "Shield Master": "Use your shield as a bonus action to shove. Gain a bonus to Dexterity saving throws equal to your shield’s AC bonus and protect against effects of successful saves.",
    "Skilled": "Gain proficiency in any combination of three skills or tools.",
    "Skulker": "Hide when lightly obscured, miss with ranged weapon attacks without revealing your position, and see in dim light as if it were bright light.",
    "Spell Sniper": "Double the range of your spell attacks, ignore half and three-quarters cover, and learn a cantrip that requires an attack roll from any spellcasting class.",
    "Tavern Brawler": "Gain +1 to Strength or Constitution, proficiency with improvised weapons, and can make an unarmed strike as a bonus action after an attack.",
    "Tough": "Your maximum HP increases by +2 per level.",
    "War Caster": "Advantage on Constitution saves to maintain concentration, can cast spells instead of making opportunity attacks, and can perform somatic components with weapons or shields.",
    "Weapon Master": "Gain proficiency with four weapons of your choice and +1 to Strength or Dexterity."}

    def __init__(self,position) -> None:
        self.race = ''
        self.subrace = ''
        self.spec = ''
        self.hp = 0
        self.ac = 10
        self.darkvision = 30
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
        self.traits = []
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
                              "Shields": 0,
                              "Simple Weapons": 0,
                              "Martial Weapons": 0}
        self.armorproficiency = {'Clothing':True,
                                'Light Armor':False,
                                'Medium Armor':False,
                                'Heavy Armor':False}
        self.commonweaponproficiency = {"Club": False,
                                "Dagger": False,    
                                "Greatclub": False,    
                                "Handaxe": False,    
                                "Javelin": False,    
                                "Light Hammer": False,    
                                "Mace": False,    
                                "Quarterstaff": False,    
                                "Sickle": False,
                                "Spear": False,    
                                "Light Crossbow": False,    
                                "Dart": False,    
                                "Shortbow": False,    
                                "Sling": False}
        self.martialweaponproficiency = {"Battleaxe": False,
                                "Flail": False,
                                "Glaive": False,
                                "Greataxe": False,
                                "Greatsword": False,    
                                "Halberd": False,    
                                "Lance": False,    
                                "Longsword": False,    
                                "Maul": False,    
                                "Morningstar": False,    
                                "Pike": False,
                                "Rapier": False,    
                                "Scimitar": False,    
                                "Shortsword": False,    
                                "Trident": False,    
                                "War Pick": False,    
                                "Warhammer": False,    
                                "Whip": False,    
                                "Blowgun": False,
                                "Hand Crossbow": False,    
                                "Heavy Crossbow": False,    
                                "Longbow": False,    
                                "Net": False}                            
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
                          "Languages (Primordial)": 0,
                          "Languages (Undercommon)":0,
                          "Languages (Deep Speech)":0}
        self.maxcarryweight = self.stats['STR'] * 15
        self.carryweight = 0
        if self.race == 'Halflings' or self.race == 'Dwarves' or self.race == 'Gnomes':
            self.movedistance = 25
        else:
            self.movedistance = 30
        self.age = 0
        self.alignment = ''
        self.inventory = []
        self.feats = [{"Actor": False},
                      {"Athlete": False},
                      {"Alert": False},
                      {"Charger": False},
                      {"Crossbow Expert": False},
                      {"Defensive Duelist": False},
                      {"Dual Wielder": False},
                      {"Dungeon Delver": False},
                      {"Durable": False},
                      {"Elemental Adept": False},
                      {"Grappler": False},
                      {"Great Weapon Master": False},
                      {"Healer": False},
                      {"Heavily Armored": False},
                      {"Heavy Armor Master": False},
                      {"Inspiring Leader": False},
                      {"Keen Mind": False},
                      {"Lightly Armored": False},
                      {"Linguist": False},
                      {"Lucky": False},
                      {"Mage Slayer": False},
                      {"Magic Initiate": False},
                      {"Martial Adept": False},
                      {"Medium Armor Master": False},
                      {"Mobile": False},
                      {"Moderately Armored": False},
                      {"Mounted Combatant": False},
                      {"Observant": False},
                      {"Polearm Master": False},
                      {"Resilient": False},
                      {"Ritual Caster": False},
                      {"Savage Attacker": False},
                      {"Sentinel": False},
                      {"Sharpshooter": False},
                      {"Shield Master": False},
                      {"Skilled": False},
                      {"Skulker": False},
                      {"Spell Sniper": False},
                      {"Tavern Brawler": False},
                      {"Tough": False},
                      {"War Caster": False},
                      {"Weapon Master": False}]
        self.initiative = 0
        self.advantagerolls = {'STR': False, 
                               'DEX': False, 
                               'CON': False, 
                               'WIS': False, 
                               'INT': False, 
                               'CHR': False}
        self.athlete = ''

    def str_saving_throw(self):
        pass

    def dex_saving_throw(self):
        pass

    def int_saving_throw(self):
        pass

    def wis_saving_throw(self):
        pass

    def con_saving_throw(self):
        pass

    def chr_saving_throw(self):
        pass        

    def gainfeat_actor(self):
        self.feat['Actor'] = True

    def gainfeat_athlete(self,choice):
        self.feat['Athlete'] = True
        if choice.upper() == 'DEX':

        elif choice.upper() == 'STR':
            self.stats['STR'] = self.stats['STR'] + 1


    def gainfeat_alert(self):
        self.feat['Alert'] = True

    def gainfeat_charger(self):
        pass

    def set_age(self,age=0):
        self.age = age

    def set_race(self):
        race = input('Select your race: Dragonborn, Dwarf, Elf, Gnome, Half-Elf, Halfling, Half-Orc, Human, Tiefling. ').lower()
        if race == 'dragonborn' or race == 'half-elf' or race == 'half-orc' or race == 'human' or race == 'tiefling':
            self.race = race
        elif race == 'dwarf':
            subrace = input('Are you Hill or Mountain Dwarf? ').lower()
            self.race = race
            self.subrace = subrace
        elif race == 'elf':
            subrace = input('Are you High, Wood, or a Dark Elf (Drow)? ').lower()
            self.race = race
            self.subrace = subrace
        elif race == 'gnome':
            subrace = input('Are you a Forest or Rock Gnome? ').lower()
            self.race = race
            self.subrace = subrace
        elif race == 'halfling':
            subrace = input('Are you a Lightfoot or Stout Halfling)? ').lower()
            self.race = race
            self.subrace = subrace    
        else:
            print('Please try again!')
            self.set_race()

    def set_alignment(self):
        alignments = ['Lawful Good','Neutral Good','Chaotic Good','Lawful Neutral','Neutral','Chaotic Neutral','Lawful Evil','Neutral Evil','Chaotic Evil']
        print('Please select your alignment:')
        for each in alignments:
            print(each)
        pick = input('Which alignment do you choose? ').lower()
        self.alignment = pick
    
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

    def use_item(self,item):
        self.inventory[item] = self.inventory[item] - 1

    def add_item(self,item,qty=1):
        self.inventory[item] = qty

    def equip_weapon(self,weapon):
        self.equipment['Main Hand'] = weapon
        self.inventory[weapon] = self.inventory[weapon] - 1

    def equip_armor(self,armor,location):
        self.equipment[location] = armor
        self.inventory[armor] = self.inventory[armor] - 1

    def gain_feat(self,name,updates):
        pass

    def use_item(self,item):
        self.inventory[item] = self.inventory[item] - 1

    def add_item(self,item,qty=1):
        self.inventory[item] = qty

    def equip_weapon(self,weapon):
        self.equipment['Main Hand'] = weapon
        self.inventory[weapon] = self.inventory[weapon] - 1

    def equip_armor(self,armor,location):
        self.equipment[location] = armor
        self.inventory[armor] = self.inventory[armor] - 1

    def gain_feat(self,name,updates):
        pass

    def use_item(self,item):
        self.inventory[item] = self.inventory[item] - 1

    def add_item(self,item,qty=1):
        self.inventory[item] = qty

    def equip_weapon(self,weapon):
        self.equipment['Main Hand'] = weapon
        self.inventory[weapon] = self.inventory[weapon] - 1

    def equip_armor(self,armor,location):
        self.equipment[location] = armor
        self.inventory[armor] = self.inventory[armor] - 1
        self.ac = armor.ac + self.ac
        self.equipment[self.location] = self


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

class Consumable:
    def __init__(self,name,stacksize=99,stat='',amount=0,status='') -> None:
        self.name = name
        self.stacksize = stacksize
        self.effect = {'Stat':stat,'Increase':amount}
        self.status = status

class OffHand:
    def __init__(self,ac=0,bonus='',stat='',amount=0) -> None:
        self.ac = ac
        self.bonus = bonus
        self.effect = {'Stat':stat,'Increase':amount}

class Event:
    def __init__(self,reward=[]):
        self.state = True
        self.reward = []
        
    def complete(self,character):
        self.state = False
        for item in self.reward:
            character.inventory.appened(item)

jon = Character()
jon.set_alignment()
print(jon.alignment)
