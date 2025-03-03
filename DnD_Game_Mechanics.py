import pymysql
import json
import random

Database = pymysql.connect(
    host='localhost',
    user='root',
    password='Goddess0!',
    database='dndgame'
)
#To pull something from db, call Database.cursor(), this is like an instance of the DB and then <cursor>.execute('<SQL QUERY>')
#To close the connection to the db, call Database.close(), this ends the transaction


class Dice:
    def __init__(self,qty,size=4) -> None:
        self.qty = qty
        self.size = size

    def roll(self):
        value = 0
        for die in range(1,self.qty+1):
            value += random.randint(1,self.size)
        #     print(value)
        # print(value)
        return value
    
class Character: #(Database):
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
    POSSIBLE_CLASSES = classes = ["Barbarian","Bard","Cleric","Druid","Fighter","Monk","Paladin","Ranger","Rogue","Sorcerer","Warlock","Wizard"]
    
    def __init__(self,position) -> None:
        self.race = ''
        self.subrace = ''
        self.spec = ''
        self.hp = 0
        self.ac = 10
        self.darkvision = 30
        self.spellslots = 'PUT QUERY TO ACCESS FEATS DATA'
        self.spells = 'PUT QUERY TO ACCESS FEATS DATA'
        self.actions = ['Attack','Move','Sprint','Jump','Shove','Disengage']
        self.weaponskills = 'PUT QUERY TO ACCESS FEATS DATA'
        self.traits = 'PUT QUERY TO ACCESS FEATS DATA'
        self.STR = 'PUT QUERY TO ACCESS FEATS DATA'
        self.DEX = 'PUT QUERY TO ACCESS FEATS DATA'
        self.CON = 'PUT QUERY TO ACCESS FEATS DATA'
        self.WIS = 'PUT QUERY TO ACCESS FEATS DATA'
        self.INT = 'PUT QUERY TO ACCESS FEATS DATA'
        self.CHR = 'PUT QUERY TO ACCESS FEATS DATA'
        self.equipment = 'PUT QUERY TO ACCESS FEATS DATA'
        self.proficiencies = 'PUT QUERY TO ACCESS FEATS DATA'
        self.armorproficiency = 'PUT QUERY TO ACCESS FEATS DATA'
        self.commonweaponproficiency = 'PUT QUERY TO ACCESS FEATS DATA'
        self.martialweaponproficiency = 'PUT QUERY TO ACCESS FEATS DATA'                          
        self.tools = 'PUT QUERY TO ACCESS FEATS DATA'
        self.landVehicles = 'PUT QUERY TO ACCESS FEATS DATA'
        self.waterVehicles = 'PUT QUERY TO ACCESS FEATS DATA'
        self.languages = 'PUT QUERY TO ACCESS FEATS DATA'
        self.maxcarryweight = 'PUT QUERY TO ACCESS FEATS DATA'
        self.carryweight = 'PUT QUERY TO ACCESS FEATS DATA'
        self.age = 'PUT QUERY TO ACCESS FEATS DATA'
        self.alignment = 'PUT QUERY TO ACCESS FEATS DATA'
        self.inventory = 'PUT QUERY TO ACCESS FEATS DATA'
        self.feats = 'PUT QUERY TO ACCESS FEATS DATA'
        self.initiative = 0
        self.advantagerolls = {'STR': False, 
                               'DEX': False, 
                               'CON': False, 
                               'WIS': False, 
                               'INT': False, 
                               'CHR': False}
        self.xposition = 'PUT QUERY TO ACCESS FEATS DATA'
        self.yposition = 'PUT QUERY TO ACCESS FEATS DATA'

    def attack(self,enemy):
        pass

    def move(self,position):
        if position <= self.position and position >= -self.position:
            self.position = position
        else:
            pass

    def sprint(self):
        self.movedistance = self.movedistance * 1.5

    def jump(self):
        pass

    def shove(self,enemy):
        pass

    def disengage(self):
        pass
    
    def gain_feat(self,feat):
        # runs query to update feat table for selected feat
        self.feats += feat

    def saving_throw(self,checked_stat,required_roll):
        #check = self.{checked_stat} - required_roll
        if check >= 0:
            return True
        else:
            return False
    

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
        self.ac = armor.ac + self.ac
        self.equipment[self.location] = self

class Barabarian:
    def __init__(self):
        self.skills = {1: {"Rage": "Enter a rage as a bonus action, gaining advantage on Strength checks and saving throws, bonus damage on melee weapon attacks, and resistance to bludgeoning, piercing, and slashing damage. Lasts for 1 minute or until you’re knocked unconscious or your turn ends without attacking or taking damage.",
                                "Unarmored Defense": "When not wearing armor, your AC is 10 + Dexterity modifier + Constitution modifier."},
                            2: {"Reckless Attack": "When you make your first attack on your turn, you can decide to attack recklessly, gaining advantage on melee weapon attack rolls using Strength for the turn. Attacks against you also gain advantage until your next turn.",
                                "Danger Sense": "You have advantage on Dexterity saving throws against effects you can see, such as traps and spells, as long as you are not blinded, deafened, or incapacitated."},
                            3: {"Primal Path": "Choose a Primal Path (Path of the Berserker or Path of the Totem Warrior), gaining features at 3rd, 6th, 10th, and 14th levels."},
                            4: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                            5: {"Extra Attack": "You can attack twice, instead of once, whenever you take the Attack action on your turn.",
                                "Fast Movement": "Your speed increases by 10 feet while you aren’t wearing heavy armor."},
                            6: {"Path Feature": "Gain a feature from your Primal Path."},
                            7: {"Feral Instinct": "You have advantage on initiative rolls. Additionally, if you are surprised at the beginning of combat and aren’t incapacitated, you can act normally on your first turn if you enter your rage before doing anything else on that turn."},
                            8: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                            9: {"Brutal Critical": "You can roll one additional weapon damage die when determining the extra damage for a critical hit with a melee attack. This increases at higher levels."},
                            10: {"Path Feature": "Gain a feature from your Primal Path."},
                            11: {"Relentless Rage": "If you drop to 0 HP while raging and don’t die outright, make a DC 10 Constitution saving throw. If you succeed, you drop to 1 HP instead. Each time you use this feature, the DC increases by 5. It resets after a short or long rest."},
                            12: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                            13: {"Brutal Critical (2 dice)": "You can roll two additional weapon damage dice when determining the extra damage for a critical hit with a melee attack."},
                            14: {"Path Feature": "Gain a feature from your Primal Path."},
                            15: {"Persistent Rage": "Your rage only ends early if you fall unconscious or choose to end it."},
                            16: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                            17: {"Brutal Critical (3 dice)": "You can roll three additional weapon damage dice when determining the extra damage for a critical hit with a melee attack."},
                            18: {"Indomitable Might": "If your total for a Strength check is less than your Strength score, you can use your Strength score in place of the total."},
                            19: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                            20: {"Primal Champion": "Your Strength and Constitution scores increase by 4 (maximum of 24), and you gain an unlimited number of rages."}}
        self.featlevels = [4,8,12,16,19]
        self.proficiencies = ['Light Armor','Medium Armor','Shields','Simple Weapons','Martial Weapons']
        self.savingthrowproficiency = ['STR','CON']
        self.bonuspickcount = 2
        self.bonusproficiencyoptions = ['Animal Handling','Athletics','Intimidation','Nature','Perception','Survival']

class Bard:
    def __init__(self):
        self.skills = {1: {"Spellcasting": "You can cast bard spells using Charisma as your spellcasting ability. You know two cantrips and four 1st-level spells at this level.",
                            "Bardic Inspiration": "As a bonus action, give a creature within 60 feet an inspiration die (1d6) to add to one ability check, attack roll, or saving throw within the next 10 minutes."},
                        2: {"Jack of All Trades": "Add half your proficiency bonus, rounded down, to any ability check that doesn’t already include your proficiency bonus.",
                            "Song of Rest": "During a short rest, you can use soothing music or oration to help allies regain hit points. Each creature that hears you regains an extra 1d6 HP when using Hit Dice to heal."},
                        3: {"Bard College": "Choose a Bard College (College of Lore or College of Valor), which grants additional features at levels 3, 6, and 14.",
                            "Expertise": "Choose two of your skill proficiencies, or one of your skill proficiencies and your proficiency with one musical instrument. Your proficiency bonus is doubled for any ability check you make with the chosen proficiencies."},
                        4: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        5: {"Bardic Inspiration (d8)": "Your Bardic Inspiration die increases to a d8."},
                        6: {"Countercharm": "As an action, you can start a performance that lasts until the end of your next turn. During that time, you and any friendly creatures within 30 feet have advantage on saving throws against being frightened or charmed.",
                            "College Feature": "Gain an additional feature from your chosen Bard College."},
                        7: {"Font of Inspiration": "You regain all expended uses of Bardic Inspiration when you finish a short or long rest."},
                        8: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        9: {"Song of Rest (d8)": "The extra healing from your Song of Rest increases to 1d8."},
                        10: {"Bardic Inspiration (d10)": "Your Bardic Inspiration die increases to a d10.",
                             "Expertise": "Choose two more skill proficiencies, or one skill proficiency and one musical instrument. Your proficiency bonus is doubled for any ability check you make with the chosen proficiencies.",
                             "Magical Secrets": "Choose two spells from any class, including the bard spell list. The chosen spells count as bard spells for you."},
                        11: {"Spellcasting (6th-level spells)": "You gain access to 6th-level spells."},
                        12: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        13: {"Song of Rest (d10)": "The extra healing from your Song of Rest increases to 1d10.",
                             "Spellcasting (7th-level spells)": "You gain access to 7th-level spells."},
                        14: {"Bardic Inspiration (d12)": "Your Bardic Inspiration die increases to a d12.",
                             "Magical Secrets": "Choose two more spells from any class, including the bard spell list. The chosen spells count as bard spells for you.",
                             "College Feature": "Gain an additional feature from your chosen Bard College."},
                        15: {"Spellcasting (8th-level spells)": "You gain access to 8th-level spells."},
                        16: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        17: {"Song of Rest (d12)": "The extra healing from your Song of Rest increases to 1d12.",
                             "Spellcasting (9th-level spells)": "You gain access to 9th-level spells."},
                        18: {"Magical Secrets": "Choose two more spells from any class, including the bard spell list. The chosen spells count as bard spells for you."},
                        19: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        20: {"Superior Inspiration": "When you roll initiative and have no uses of Bardic Inspiration left, you regain one use."}}
        self.featlevels = [4,8,12,16,19]
        self.proficiencies = ['Light Armor','Simple Weapons','Hand Crossbows','Longswords','Rapiers','Shortswords','Tools (Musical Insturment)']
        self.savingthrowproficiency = ['DEX','CHR']
        self.bonuspickcount = 3
        self.bonusproficiencyoptions = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature","Perception","Performance","Persuasion","Religion","Sleight of Hand","Stealth", "Survival"]

class Cleric:
    def __init__(self):
        self.skills = {1: {"Spellcasting": "You can cast cleric spells using Wisdom as your spellcasting ability. You know three cantrips and can prepare a number of spells equal to your Wisdom modifier + cleric level.",
                            "Divine Domain": "Choose a Divine Domain (such as Life, Light, or Trickery) that grants additional features at levels 1, 2, 6, 8, and 17."},
                        2: {"Channel Divinity": "You can use Channel Divinity once per short or long rest to perform effects determined by your Divine Domain, such as Turn Undead.",
                            "Divine Domain Feature": "Gain an additional feature from your chosen Divine Domain."},
                        3: {"Spellcasting (2nd-level spells)": "You gain access to 2nd-level spells."},
                        4: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        5: {"Destroy Undead (CR 1/2)": "When using Channel Divinity: Turn Undead, any undead of CR 1/2 or lower are instantly destroyed if they fail their saving throw.",
                            "Spellcasting (3rd-level spells)": "You gain access to 3rd-level spells."},
                        6: {"Channel Divinity (2/rest)": "You can use Channel Divinity twice per short or long rest.",
                            "Divine Domain Feature": "Gain an additional feature from your chosen Divine Domain."},
                        7: {"Spellcasting (4th-level spells)": "You gain access to 4th-level spells."},
                        8: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20.",
                            "Destroy Undead (CR 1)": "When using Channel Divinity: Turn Undead, any undead of CR 1 or lower are instantly destroyed if they fail their saving throw.",
                            "Divine Domain Feature": "Gain an additional feature from your chosen Divine Domain."},
                        9: {"Spellcasting (5th-level spells)": "You gain access to 5th-level spells."},
                        10: {"Divine Intervention": "Call upon your deity for aid, with an effect determined by the DM. The chance for success is a roll equal to or lower than your cleric level on a d100. If successful, you cannot use this feature again for 7 days."},
                        11: {"Destroy Undead (CR 2)": "When using Channel Divinity: Turn Undead, any undead of CR 2 or lower are instantly destroyed if they fail their saving throw.",
                            "Spellcasting (6th-level spells)": "You gain access to 6th-level spells."},
                        12: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        13: {"Spellcasting (7th-level spells)": "You gain access to 7th-level spells."},
                        14: {"Destroy Undead (CR 3)": "When using Channel Divinity: Turn Undead, any undead of CR 3 or lower are instantly destroyed if they fail their saving throw."},
                        15: {"Spellcasting (8th-level spells)": "You gain access to 8th-level spells."},
                        16: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        17: {"Destroy Undead (CR 4)": "When using Channel Divinity: Turn Undead, any undead of CR 4 or lower are instantly destroyed if they fail their saving throw.",
                            "Divine Domain Feature": "Gain an additional feature from your chosen Divine Domain.",
                            "Spellcasting (9th-level spells)": "You gain access to 9th-level spells."},
                        18: {"Channel Divinity (3/rest)": "You can use Channel Divinity three times per short or long rest."},
                        19: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        20: {"Divine Intervention Improvement": "When you use Divine Intervention, it succeeds automatically. After a successful use, you cannot use this feature again for 7 days."}}
        self.featlevels = [4,8,12,16,19]
        self.proficiencies = ['Light Armor','Medium Armor','Shields','Simple Weapons','Hand Crossbows','Longswords','Rapiers','Shortswords','Tools (Musical Insturment)']
        self.savingthrowproficiency = ['WIS','CHR']
        self.bonuspickcount = 2
        self.bonusproficiencyoptions = ['History','Insight','Medicine','Persuasion','Religion']

class Druid:
    def __init__(self):
        self.skills = {1: {"Spellcasting": "You can cast druid spells using Wisdom as your spellcasting ability. You know two cantrips and can prepare a number of spells equal to your Wisdom modifier + druid level.",
                            "Druidic": "You know Druidic, the secret language of druids. You can use it to leave hidden messages that only other druids can understand."},
                        2: {"Wild Shape": "As an action, you can transform into a beast you've seen before. You can use this twice per short or long rest. Restrictions apply based on level.",
                            "Druid Circle": "Choose a Druid Circle (such as Circle of the Land or Circle of the Moon), which grants additional features at levels 2, 6, 10, and 14."},
                        3: {"Spellcasting (2nd-level spells)": "You gain access to 2nd-level spells."},
                        4: {"Wild Shape Improvement": "You can transform into a beast with a CR of 1/2 or lower and can swim.",
                            "Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        5: {"Spellcasting (3rd-level spells)": "You gain access to 3rd-level spells."},
                        6: {"Druid Circle Feature": "Gain an additional feature from your chosen Druid Circle."},
                        7: {"Spellcasting (4th-level spells)": "You gain access to 4th-level spells."},
                        8: {"Wild Shape Improvement": "You can transform into a beast with a CR of 1 and can fly.",
                            "Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        9: {"Spellcasting (5th-level spells)": "You gain access to 5th-level spells."},
                        10: {"Druid Circle Feature": "Gain an additional feature from your chosen Druid Circle."},
                        11: {"Spellcasting (6th-level spells)": "You gain access to 6th-level spells."},
                        12: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        13: {"Spellcasting (7th-level spells)": "You gain access to 7th-level spells."},
                        14: {"Druid Circle Feature": "Gain an additional feature from your chosen Druid Circle."},
                        15: {"Spellcasting (8th-level spells)": "You gain access to 8th-level spells."},
                        16: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        18: {"Timeless Body": "You suffer none of the frailty of old age, and you can’t be aged magically. You still die of old age, however.",
                            "Beast Spells": "You can cast druid spells in Wild Shape, but only spells that don’t require material components."},
                        19: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        20: {"Archdruid": "You can use Wild Shape an unlimited number of times. Additionally, you can ignore the verbal and somatic components of druid spells and material components that don’t have a cost."}}
        self.featlevels = [4,8,12,16,19]
        self.proficiencies = ['Light Armor','Medium Armor','Shields','Clubs','Daggers','Darts','Javelins','Maces','Quarterstaffs','Scimitars','Sickles','Slings','Spears','Tools (Herbalism Kit)']
        self.savingthrowproficiency = ['INT','WIS']
        self.bonuspickcount = 2
        self.bonusproficiencyoptions = ['Arcana','Animal Handling','Insight','Medicine','Nature','Perception','Religion','Survival']        

class Fighter:
    def __init__(self):
        self.skills = {1: {"Fighting Style": "Choose a fighting style from options like Archery, Defense, Dueling, Great Weapon Fighting, Protection, or Two-Weapon Fighting. Each grants a specific combat advantage.",
                            "Second Wind": "You can use a bonus action to regain hit points equal to 1d10 + your Fighter level. This feature can be used once per short or long rest."},
                        2: {"Action Surge": "You can take one additional action on your turn. This feature can be used once per short or long rest."},
                        3: {"Martial Archetype": "Choose a Martial Archetype, such as Battle Master or Champion. Each archetype grants unique features at levels 3, 7, 10, 15, and 18."},
                        4: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        5: {"Extra Attack": "You can attack twice, instead of once, whenever you take the Attack action on your turn."},
                        6: {"Martial Archetype Feature": "Gain an additional feature from your chosen Martial Archetype."},
                        7: {"Remarkable Athlete": "You gain proficiency in Athletics, or if already proficient, double your proficiency bonus for checks with that skill. You can also add half your proficiency bonus to any Strength, Dexterity, or Constitution check not already using proficiency."},
                        8: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        9: {"Indomitable": "You can reroll a failed saving throw. You must use the new roll. You can use this feature once per long rest."},
                        10: {"Martial Archetype Feature": "Gain an additional feature from your chosen Martial Archetype."},
                        11: {"Extra Attack (2)": "You can attack three times, instead of twice, whenever you take the Attack action on your turn."},
                        12: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        13: {"Indomitable (2/rest)": "You can use Indomitable twice per long rest."},
                        14: {"Martial Archetype Feature": "Gain an additional feature from your chosen Martial Archetype."},
                        15: {"Superior Critical": "Your weapon attacks score a critical hit on a roll of 19 or 20."},
                        16: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        17: {"Action Surge (2/rest)": "You can use Action Surge twice per short or long rest."},
                        18: {"Martial Archetype Feature": "Gain an additional feature from your chosen Martial Archetype."},
                        19: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        20: {"Extra Attack (3)": "You can attack four times, instead of three, whenever you take the Attack action on your turn."}}
        self.featlevels = [4,6,8,12,14,16,19]
        self.proficiencies = ['Light Armor','Medium Armor','Heavy Armor','Shields','Simple Weapons','Martial Weapons']
        self.savingthrowproficiency = ['STR','CON']
        self.bonuspickcount = 2
        self.bonusproficiencyoptions = ['Acrobatics', 'Animal Handling', 'Athletics', 'History', 'Insight', 'Intimidation', 'Perception', 'Survival']

class Monk:
    def __init__(self):
        self.skills = {1: {"Unarmored Defense": "While not wearing armor or wielding a shield, your AC equals 10 + your Dexterity modifier + your Wisdom modifier.",
                            "Martial Arts": "You can use Dexterity instead of Strength for the attack and damage rolls of your unarmed strikes and monk weapons. You can also make an unarmed strike as a bonus action when you take the Attack action using an unarmed strike or monk weapon."},
                        2: {"Ki": "You have a pool of Ki points equal to your Monk level. You can use Ki to perform various special abilities like Step of the Wind, Patient Defense, and Dodge action as a bonus action, or Dash and Disengage.",
                            "Unarmored Movement": "Your speed increases by 10 feet while not wearing armor or wielding a shield."},
                        3: {"Monastic Tradition": "Choose a Monastic Tradition, such as Way of the Open Hand, Way of Shadow, or Way of the Four Elements. Each grants unique features at levels 3, 6, 11, and 17.",
                            "Deflect Missiles": "As a reaction, you can deflect or catch a missile that hits you, reducing the damage by 1d10 + your Dexterity modifier + your Monk level."},
                        4: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        5: {"Extra Attack": "You can attack twice, instead of once, whenever you take the Attack action on your turn.",
                            "Unarmored Movement (Improved)": "Your speed increases by an additional 10 feet (total 20 feet increase)."},
                        6: {"Ki Empowered Strikes": "Your unarmed strikes count as magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage."},
                        7: {"Evasion": "When you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on the saving throw, and only half damage if you fail."},
                        8: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        9: {"Stillness of Mind": "As an action, you can end one effect on yourself that is causing you to be charmed or frightened."},
                        10: {"Purity of Body": "You are immune to disease and poison."},
                        11: {"Tongue of the Sun and Moon": "You can understand and speak all languages."},
                        12: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        13: {"Unarmored Movement (Improved)": "Your speed increases by an additional 30 feet (total 40 feet increase)."},
                        14: {"Diamond Soul": "You gain proficiency in all saving throws. If you are already proficient in a saving throw, you can add your Wisdom modifier to the roll."},
                        15: {"Timeless Body": "You suffer none of the frailty of old age, and you can’t be aged magically. You still die of old age, however."},
                        16: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        17: {"Empty Body": "You can use 4 Ki points to become invisible and have resistance to all damage except force damage for 1 minute."},
                        18: {"Unarmored Movement (Improved)": "Your speed increases by an additional 40 feet (total 50 feet increase)."},
                        19: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        20: {"Perfect Self": "When you roll for initiative and have no Ki points remaining, you regain 4 Ki points."}}
        self.featlevels = [4,8,12,16,19]
        self.proficiencies = ['Simple Weapons','Shortswords']
        #Monk gets to pick one from the bonus tool options list to add to their proficiencies
        self.bonustooloptions = ["Tools (Artisan’s tools)", "Tools (Disguise Kit)", "Tools (Forgery Kit)", "Tools (Gaming Set)", "Tools (Herbalism Kit)", "Tools (Musical Instrument)", "Tools (Navigator’s Tools)", "Tools (Poisoner’s Kit)", "Tools (Thieve's Tools)"]
        self.savingthrowproficiency = ['STR','DEX']
        self.bonuspickcount = 2
        self.bonusproficiencyoptions = ['Acrobatics','Athletics','History','Insight','Religion','Stealth']

class Paladin:
    def __init__(self):
        self.skills = { 1: {"Divine Sense": "As an action, you can detect the presence of celestial, fiend, and undead creatures within 60 feet of you. You can use this feature a number of times equal to 1 + your Charisma modifier (a minimum of once), regaining expended uses after a long rest.",
                            "Lay on Hands": "You can heal a creature you touch by expending points from a pool equal to 5 times your Paladin level. As an action, you can restore hit points to a creature, or cure diseases or poison."},
                        2: {"Divine Smite": "When you hit a creature with a melee weapon attack, you can expend a spell slot to deal radiant damage in addition to the weapon's damage.",
                            "Spellcasting": "You gain the ability to cast Paladin spells using Charisma as your spellcasting ability. You know two 1st-level spells and can prepare a number of spells equal to your Charisma modifier + half your Paladin level (rounded down)."},
                        3: {"Sacred Oath": "Choose a Sacred Oath, such as the Oath of Devotion, Oath of the Ancients, or Oath of Vengeance. Each grants unique features at levels 3, 7, 15, and 20.",
                            "Channel Divinity": "You gain one use of Channel Divinity. At 3rd level, you can use your Channel Divinity to either turn undead or use your Oath's specific Channel Divinity feature."},
                        4: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        5: {"Extra Attack": "You can attack twice, instead of once, whenever you take the Attack action on your turn."},
                        6: {"Aura of Protection": "You and friendly creatures within 10 feet of you gain a bonus to all saving throws equal to your Charisma modifier (with a minimum bonus of +1)."},
                        7: {"Sacred Oath Feature": "Gain an additional feature from your Sacred Oath."},
                        8: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        9: {"Aura of Courage": "You and friendly creatures within 10 feet of you can’t be frightened while you are conscious."},
                        10: {"Divine Intervention": "You can call upon your deity to intervene on your behalf. You can ask for divine assistance and roll a percentile die; if you roll a number equal to or lower than your Paladin level, the deity intervenes."},
                        11: {"Improved Divine Smite": "Your Divine Smite feature now deals an extra 1d8 radiant damage on every melee hit."},
                        12: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        13: {"Aura of Health": "You and friendly creatures within 10 feet of you are immune to disease."},
                        14: {"Cleansing Touch": "As an action, you can end one effect causing a creature you touch to be charmed or frightened, or you can end one disease or poison affecting the creature."},
                        15: {"Sacred Oath Feature": "Gain an additional feature from your Sacred Oath."},
                        16: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        17: {"Aura of Devotion": "You and friendly creatures within 10 feet of you are immune to being charmed while you are conscious."},
                        18: {"Sacred Oath Feature": "Gain an additional feature from your Sacred Oath."},
                        19: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        20: {"Avatar of Battle": "You gain the ability to become a paragon of combat. You can cast the *holy weapon* spell without expending a spell slot, and your attacks with that weapon deal an extra 2d8 radiant damage."}}
        self.featlevels = [4,8,12,16,19]
        self.proficiencies = ['Light Armor','Medium Armor','Heavy Armor','Shields','Simple Weapons','Martial Weapons']
        self.savingthrowproficiency = ['WIS','CHR']
        self.bonuspickcount = 2
        self.bonusproficiencyoptions = ['Athletics','Insight','Intimidation','Medicine','Persuasion','Religion']

class Ranger:
    def __init__(self):
        self.skills = {1: {"Favored Enemy": "You gain a favored enemy, which grants advantages in tracking and knowledge about a specific type of creature (e.g., beasts, dragons). You also gain proficiency with Survival to track them.",
                            "Natural Explorer": "You are proficient in navigating through specific terrains, gaining bonuses like faster travel and easier tracking in certain environments. You also gain advantage on checks to forage and avoid getting lost.",
                            "Ranger's Prey": "You can choose a favored enemy and, once per turn, deal additional damage to it when you hit it with a weapon attack.",
                            "Spellcasting": "You gain the ability to cast Ranger spells, with Wisdom as your spellcasting modifier. You know two 1st-level spells and can prepare a number of spells equal to your Wisdom modifier + half your Ranger level (rounded down)."},
                        2: {"Fighting Style": "Choose a fighting style, such as Archery, Defense, or Two-Weapon Fighting. Each grants a combat benefit like a bonus to ranged attacks or defense while wielding a shield.",
                            "Primeval Awareness": "You can choose a type of terrain (such as forest, desert, etc.) and gain advantages when traveling through that terrain or tracking creatures associated with that environment."},
                        3: {"Ranger Archetype": "Choose an archetype, such as Hunter, Beast Master, or Gloom Stalker. Each grants unique abilities at levels 3, 7, 11, and 15.",
                            "Hunter's Mark": "As a bonus action, mark a target and deal extra damage to it when you hit with a weapon attack. You can only have one Hunter's Mark at a time, and it lasts for an hour or until the target drops to 0 hit points."},
                        4: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        5: {"Extra Attack": "You can attack twice, instead of once, whenever you take the Attack action on your turn.",
                            "Spellcasting (Improved)": "You gain access to additional spells as you level up, such as 2nd-level spells at this level."},
                        6: {"Hunter's Prey": "You gain the ability to choose a special combat technique to enhance your effectiveness in combat, such as Colossus Slayer, Giant Killer, or Horde Breaker."},
                        7: {"Ranger Archetype Feature": "Gain an additional feature from your chosen Ranger archetype."},
                        8: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        9: {"Nimble Escape": "You gain the ability to take the Dash or Disengage action as a bonus action. This allows you to move quickly through combat and avoid damage."},
                        10: {"Hunter's Mark (Improved)": "You can mark a second target simultaneously with Hunter's Mark, allowing you to deal extra damage to two different creatures at once."},
                        11: {"Ranger Archetype Feature": "Gain an additional feature from your chosen Ranger archetype."},
                        12: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        13: {"Camouflage": "You can use the Hide action even when you are only lightly obscured by natural elements, such as foliage or fog."},
                        14: {"Feral Sense": "You can sense the presence of creatures within 30 feet of you that are invisible or hidden, giving you an advantage against them."},
                        15: {"Ranger Archetype Feature": "Gain an additional feature from your chosen Ranger archetype."},
                        16: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        17: {"Slayer's Endurance": "You gain resistance to damage from the favored enemy types and automatically succeed on saving throws against effects they cause."},
                        18: {"Land's Stride": "You can move through difficult terrain without slowing your pace, and you can pass through plants and underbrush without being slowed or hindered."},
                        19: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        20: {"Ranger's Mastery": "You gain the ability to take a bonus action to deal additional damage to creatures you’ve marked with Hunter's Mark, and you also gain immunity to poison and disease."}}
        self.featlevels = [4,8,12,16,19]
        self.proficiencies = ['Light Armor','Medium Armor','Shields','Simple Weapons','Martial Weapons']
        self.savingthrowproficiency = ['STR','DEX']
        self.bonuspickcount = 3
        self.bonusproficiencyoptions = ['Animal Handling','Athletics','Insight','Investigation','Nature','Perception','Stealth','Survival']

class Rogue:
    def __init__(self):
        self.skills = {1: {"Sneak Attack": "Once per turn, you can deal extra damage with a finesse or ranged weapon attack if you have advantage on the attack roll, or if another enemy of the target is within 5 feet of it and isn't incapacitated. The extra damage starts at 1d6 and increases as you level up.",
                            "Thieves' Cant": "You learn a secret language known only to other Rogues and those who know the Thieves' Cant. You can use it to communicate in code with other thieves.",
                            "Proficiency": "You gain proficiency with light armor, simple weapons, hand crossbows, longswords, rapiers, shortswords, thieves' tools, and two skills of your choice."},
                        2: {"Cunning Action": "You can take a bonus action on each of your turns in combat to Dash, Disengage, or Hide."},
                        3: {"Roguish Archetype": "Choose an archetype, such as Thief, Assassin, or Arcane Trickster. Each grants unique abilities at levels 3, 9, 13, and 17.",
                            "Sneak Attack (Improved)": "Your Sneak Attack damage increases to 2d6, and it continues to increase with your Rogue level."},
                        4: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        5: {"Uncanny Dodge": "When an attacker that you can see hits you with an attack, you can use your reaction to halve the damage."},
                        6: {"Expertise": "Choose two of your skill proficiencies. Your proficiency bonus is doubled for any ability check you make that uses either of the chosen proficiencies."},
                        7: {"Evasion": "When you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on the saving throw, and only half damage if you fail."},
                        8: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        9: {"Roguish Archetype Feature": "Gain an additional feature from your chosen Rogue archetype."},
                        10: {"Sneak Attack (Improved)": "Your Sneak Attack damage increases to 3d6, and it continues to increase with your Rogue level."},
                        11: {"Reliable Talent": "Whenever you make an ability check that lets you add your proficiency bonus, you can treat a roll of 9 or lower as a 10."},
                        12: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        13: {"Roguish Archetype Feature": "Gain an additional feature from your chosen Rogue archetype."},
                        14: {"Blindsense": "If you are able to hear, you can sense the location of any creature within 10 feet of you that is hidden, invisible, or otherwise out of sight."},
                        15: {"Sneak Attack (Improved)": "Your Sneak Attack damage increases to 4d6, and it continues to increase with your Rogue level."},
                        16: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        17: {"Roguish Archetype Feature": "Gain an additional feature from your chosen Rogue archetype."},
                        18: {"Elusive": "No attack roll has advantage against you while you aren't incapacitated."},
                        19: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        20: {"Stroke of Luck": "If you miss with an attack roll, you can turn the miss into a hit. Alternatively, if you fail an ability check, you can treat the roll as a 20."}}
        self.featlevels = [4,8,10,12,16,19]
        self.proficiencies = ['Light Armor','Simple Weapons','Hand Crossbows','Longswords','Rapiers','Shortswords',"Tools (Thieve's Tools)"]
        self.savingthrowproficiency = ['DEX','INT']
        self.bonuspickcount = 4
        self.bonusproficiencyoptions = ['Acrobatics', 'Athletics', 'Deception', 'Insight', 'Intimidation', 'Investigation', 'Perception', 'Performance', 'Persuasion', 'Sleight of Hand', 'Stealth']

class Sorcerer:
    def __init__(self):
        self.skills = {1: {"Sorcerer's Spellcasting": "You can cast spells using Charisma as your spellcasting modifier. You know a number of cantrips and 1st-level spells, and can cast spells using spell slots. You prepare spells based on your Charisma modifier and level.",
                            "Sorcerer's Origin": "Choose a Sorcerer's Origin (Draconic Bloodline, Wild Magic, or other homebrew origins) that gives you unique abilities at level 1 and further as you level up.",
                            "Font of Magic": "You gain Sorcery Points, which allow you to convert them into spell slots or use them to fuel Metamagic. At 1st level, you have a pool of Sorcery Points equal to your Sorcerer level."},
                        2: {"Metamagic": "You gain the ability to modify your spells with Metamagic options. At level 2, you can choose two Metamagic options, such as Quickened Spell (casting as a bonus action) or Twinned Spell (targeting an additional creature)."},
                        3: {"Sorcerer's Origin Feature": "Gain an additional feature from your chosen Sorcerer's Origin (e.g., Draconic Resilience, Wild Magic Surge, or other abilities from the chosen Origin).",
                            "Spellcasting (Improved)": "At this level, you gain access to 2nd-level spells and can prepare more spells."},
                        4: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        5: {"Sorcery Points (Improved)": "You gain additional Sorcery Points and can convert them into higher-level spell slots.",
                            "Metamagic (Improved)": "You can select a third Metamagic option, allowing you more flexibility in casting spells."},
                        6: {"Sorcerer's Origin Feature": "Gain an additional feature from your chosen Sorcerer's Origin."},
                        7: {"Spellcasting (Improved)": "You gain access to 3rd-level spells and can prepare more spells."},
                        8: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        9: {"Sorcerer's Origin Feature": "Gain an additional feature from your chosen Sorcerer's Origin."},
                        10: {"Metamagic (Improved)": "You can select a fourth Metamagic option."},
                        11: {"Spellcasting (Improved)": "You gain access to 5th-level spells and can prepare more spells."},
                        12: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        13: {"Sorcerer's Origin Feature": "Gain an additional feature from your chosen Sorcerer's Origin."},
                        14: {"Spellcasting (Improved)": "You gain access to 7th-level spells and can prepare more spells."},
                        15: {"Metamagic (Improved)": "You can select a fifth Metamagic option."},
                        16: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        17: {"Sorcerer's Origin Feature": "Gain an additional feature from your chosen Sorcerer's Origin."},
                        18: {"Spellcasting (Improved)": "You gain access to 9th-level spells and can prepare more spells."},
                        19: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        20: {"Sorcerous Restoration": "You regain 4 Sorcery Points when you finish a short rest. This allows you to regain your magical resources more quickly."}}
        self.featlevels = [4,8,12,16,19]
        self.proficiencies = ['Daggers','Darts','Slings','Quarterstaffs','Light Crossbows']
        self.savingthrowproficiency = ['CON','CHR']
        self.bonuspickcount = 2
        self.bonusproficiencyoptions = ['Arcana', 'Deception', 'Insight', 'Intimidation', 'Persuasion', 'Religion']

class Warlock:
    def __init__(self):
        self.skills = {1: {"Otherworldly Patron": "Choose a patron that grants you power, such as The Archfey, The Fiend, or The Great Old One. This grants you additional abilities at level 1 and further at higher levels.",
                            "Spellcasting": "You can cast spells using Charisma as your spellcasting modifier. You know two 1st-level spells, and you can cast using spell slots. You can also prepare more spells as you gain levels.",
                            "Pact Magic": "Warlocks have a unique spellcasting system called Pact Magic. You have a limited number of spell slots that you can use for Warlock spells. At level 1, you have one 1st-level spell slot that can be used for any Warlock spell.",
                            "Eldritch Blast": "You know the Eldritch Blast cantrip, which allows you to deal force damage at range. This cantrip scales with your Warlock level, dealing more damage as you progress."},
                        2: {"Pact Boon": "At level 3, you choose a Pact Boon (Pact of the Chain, Pact of the Blade, or Pact of the Tome). This grants you an additional ability at level 2, which is specific to the Pact you chose. For example, Pact of the Chain allows you to summon a familiar, while Pact of the Blade lets you create a magical weapon.",
                            "Invocations": "At level 2, you gain access to Eldritch Invocations, special magical abilities that enhance your Warlock powers. You can choose two invocations from a list, such as Agonizing Blast (which adds your Charisma modifier to Eldritch Blast damage)."},
                        3: {"Otherworldly Patron Feature": "Gain a feature from your chosen patron, such as the Archfey’s Fey Presence or the Fiend’s Dark One’s Blessing. These abilities are specific to the patron you select and become available at level 3."},
                        4: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        5: {"Invocations (Improved)": "At level 5, you can select another Eldritch Invocation, giving you more customization of your Warlock abilities."},
                        6: {"Otherworldly Patron Feature (Improved)": "Gain another feature from your chosen patron. This could grant new powers, like the Fiend’s Dark One’s Own Luck or the Great Old One’s Entropic Ward."},
                        7: {"Spellcasting (Improved)": "At level 7, you gain access to 3rd-level spells and can prepare more spells. You also have a 2nd-level spell slot available."},
                        8: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        9: {"Otherworldly Patron Feature (Improved)": "Gain another feature from your chosen patron, which further enhances your relationship with the entity you serve."},
                        10: {"Invocations (Improved)": "At level 10, you can choose another Eldritch Invocation, further enhancing your powers."},
                        11: {"Mystic Arcanum": "At level 11, you gain access to a Mystic Arcanum, which is a powerful spell that you can cast once per long rest. This spell is typically a 6th-level spell."},
                        12: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        13: {"Otherworldly Patron Feature (Improved)": "Gain another feature from your patron at level 13. This feature is often an enhancement to your combat or spellcasting capabilities."},
                        14: {"Mystic Arcanum (Improved)": "At level 14, you gain a second Mystic Arcanum, which allows you to cast another powerful spell once per long rest. This one is typically a 7th-level spell."},
                        15: {"Invocations (Improved)": "At level 15, you gain access to another Eldritch Invocation, further customizing your Warlock abilities."},
                        16: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        17: {"Mystic Arcanum (Improved)": "At level 17, you gain a third Mystic Arcanum, which allows you to cast an 8th-level spell once per long rest."},
                        18: {"Otherworldly Patron Feature (Final)": "At level 18, you gain the final feature from your chosen patron. This feature is often a very powerful or game-changing ability."},
                        19: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        20: {"Mystic Arcanum (Final)": "At level 20, you gain a fourth Mystic Arcanum, which allows you to cast a 9th-level spell once per long rest."}}
        self.featlevels = [4,8,12,16,19]
        self.proficiencies = ['Light Armor','Simple Weapons']
        self.savingthrowproficiency = ['WIS','CHR']
        self.bonuspickcount = 2
        self.bonusproficiencyoptions = ['Arcana', 'Deception', 'History', 'Intimidation', 'Investigation', 'Nature', 'Religion']

class Wizard:
    def __init__(self):
        self.skills = { 1: {"Spellcasting": "You can cast spells using Intelligence as your spellcasting modifier. You know a number of cantrips and 1st-level spells, and you can prepare more spells based on your Intelligence modifier and Wizard level.",
                            "Arcane Recovery": "Once per day after a short rest, you can recover spell slots equal to half your Wizard level (rounded up), with a maximum of 5th-level spell slots."},
                        2: {"Arcane Tradition": "At level 2, you choose an Arcane Tradition (a school of magic) such as Evocation, Necromancy, or Transmutation. This grants you an additional feature at level 2, which is specific to the tradition you choose.",
                            "Spellcasting (Improved)": "At this level, you gain access to 2nd-level spells and can prepare more spells."},
                        3: {"Arcane Tradition Feature": "Gain an additional feature from your chosen Arcane Tradition (e.g., Evocation’s Sculpt Spells, or Divination’s Portent).",
                            "Spellcasting (Improved)": "You gain access to 3rd-level spells and can prepare more spells."},
                        4: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        5: {"Spellcasting (Improved)": "At this level, you gain access to 3rd-level spells and can prepare more spells. You also gain an additional 3rd-level spell slot.",
                            "Arcane Tradition Feature (Improved)": "Gain another feature from your chosen Arcane Tradition."},
                        6: {"Arcane Tradition Feature (Improved)": "You gain an additional feature from your chosen Arcane Tradition."},
                        7: {"Spellcasting (Improved)": "You gain access to 4th-level spells and can prepare more spells."},
                        8: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        9: {"Arcane Tradition Feature (Improved)": "Gain another feature from your chosen Arcane Tradition."},
                        10: {"Spellcasting (Improved)": "You gain access to 5th-level spells and can prepare more spells."},
                        11: {"Spellcasting (Improved)": "At level 11, you gain access to 6th-level spells and can prepare more spells. You can now cast more powerful spells and have access to additional spell slots.",
                            "Arcane Tradition Feature (Improved)": "Gain another feature from your chosen Arcane Tradition."},
                        12: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        13: {"Spellcasting (Improved)": "You gain access to 7th-level spells and can prepare more spells."},
                        14: {"Arcane Tradition Feature (Improved)": "Gain another feature from your chosen Arcane Tradition."},
                        15: {"Spellcasting (Improved)": "You gain access to 8th-level spells and can prepare more spells."},
                        16: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        17: {"Spellcasting (Improved)": "At level 17, you gain access to 9th-level spells and can prepare more spells. This includes the most powerful spells in the game, such as Wish.",
                            "Arcane Tradition Feature (Improved)": "Gain another feature from your chosen Arcane Tradition."},
                        18: {"Spellcasting (Improved)": "You gain access to additional spell slots for 9th-level spells. This gives you more options in combat and exploration.",
                            "Arcane Tradition Feature (Improved)": "Gain another feature from your chosen Arcane Tradition."},
                        19: {"Ability Score Improvement": "Increase one ability score by 2, or two ability scores by 1 each. You cannot increase an ability score above 20."},
                        20: {"Archmage": "At level 20, you become an Archmage, gaining access to the ability to cast 1st-level spells without expending spell slots (rechargeable on a long rest) and further improving your Arcane Tradition abilities."}}
        self.featlevels = [4,8,12,16,19]
        self.proficiencies = ['Daggers','Darts','Slings','Quarterstaffs','Light Crossbows']
        self.savingthrowproficiency = ['INT','WIS']
        self.bonuspickcount = 2
        self.bonusproficiencyoptions = ['Arcana','History','Insight','Investigation','Medicine','Religion']

class Item:
    def __init__(self,type,name,qty,weight):
        self.item_type = type
        self.name = name
        self.quantity = qty
        self.weight = weight


class Weapon:
    #DMGTYPES = ['Bludgeoning','Slashing','Piercing']
    def __init__(self,dmgtype,bonus=None,qty=1,size=4) -> None:
        self.dmgtype = dmgtype
        self.bonus = bonus
        self.damage = {'Quantity':qty,
                       'Size':size}  

class Armor:
    #ARMORTYPES = ['Clothing','Light','Medium','Heavy']
    def __init__(self,armortype,position,ac=10,bonus=None) -> None:
        self.ac = ac
        self.armortype = armortype
        self.position = position
        self.bonus = bonus

class Consumable:
    def __init__(self,stacksize=99,stat='',amount=0,status='') -> None:
        self.stacksize = stacksize
        self.effect = {'Stat':stat,
                       'Increase':amount}
        self.status = status

class OffHand:
    def __init__(self,ac=0,bonus='',stat='',amount=0) -> None:
        self.ac = ac
        self.bonus = bonus
        self.effect = {'Stat':stat,
                       'Increase':amount}

class Event:
    def __init__(self,reward=[]):
        self.state = True
        self.reward = []
        
    def complete(self,character):
        self.state = False
        for item in self.reward:
            character.inventory.appened(item)


