#createCharacter.py
class Character():
    SKILLS_LIST = ['Acrobatics','Animal Handling','Arcana','Athletics','Deception','History','Insight','Intimidation','Investigation','Medicine','Nature','Perception','Performance','Persuasion','Religion','Sleight of Hand','Stealth','Survival']
    START_EQUIP = [{'Main Class':'Barbarian',
                    'Inventory':[{"Name":"Greataxe","Qty":1},{"Name":"Handaxe","Qty":4},{"Name":"Explorer's Pack","Qty":1},{"Name":"GP","Qty":15}]},
                    {'Main Class':'Bard',
                    'Inventory':[{"Name":"Leather Armor","Qty":1},{"Name":"Dagger","Qty":2},{"Name":"Musical Instrument","Qty":1},{"Name":"Entertainer's Pack","Qty":1},{"Name":"GP","Qty":19}]},
                    {'Main Class':'Cleric',
                    'Inventory':[{"Name":"Chain Shirt","Qty":1},{"Name":"Shield","Qty":1},{"Name":"Mace","Qty":1},{"Name":"Holy Symbol","Qty":1},{"Name":"Priest's Pack","Qty":1},{"Name":"GP","Qty":7}]},
                    {'Main Class':'Druid',
                    'Inventory':[{"Name":"Leather Armor","Qty":1},{"Name":"Sickle","Qty":1},{"Name":"Shield","Qty":1},{"Name":"Druidic Focus (Quarterstaff)","Qty":1},{"Name":"Herbalism Kit","Qty":1},{"Name":"Explorer's Pack","Qty":1},{"Name":"GP","Qty":9}]},
                    {'Main Class':'Fighter (STR)',
                    'Inventory':[{"Name":"Greatsword","Qty":1},{"Name":"Chain Mail","Qty":1},{"Name":"Flail","Qty":1},{"Name":"Javelin","Qty":8},{"Name":"Dungoneer's Pack","Qty":1},{"Name":"GP","Qty":4}]},
                    {'Main Class':'Fighter (DEX)',
                    'Inventory':[{"Name":"Studded Leather Armor","Qty":1},{"Name":"Scimitar","Qty":1},{"Name":"Short Sword","Qty":1},{"Name":"Longbow","Qty":1},{"Name":"Arrows","Qty":20},{"Name":"Quiver","Qty":1},{"Name":"Dungeoneer's Pack","Qty":1},{"Name":"GP","Qty":11}]},
                    {'Main Class':'Monk',
                    'Inventory':[{"Name":"Spear","Qty":1},{"Name":"Dagger","Qty":5},{"Name":"Explorer's Pack","Qty":1},{"Name":"GP","Qty":11}]},
                    {'Main Class':'Paladin',
                    'Inventory':[{"Name":"Chain Mail","Qty":1},{"Name":"Shield","Qty":1},{"Name":"Longsword","Qty":1},{"Name":"Javelin","Qty":6},{"Name":"Holy Symbol","Qty":1},{"Name":"Priest's Pack","Qty":1},{"Name":"GP","Qty":9}]}, 
                    {'Main Class':'Ranger',
                    'Inventory':[{"Name":"Chain Mail","Qty":1},{"Name":"Shield","Qty":1},{"Name":"Longsword","Qty":1},{"Name":"Javelin","Qty":6},{"Name":"Holy Symbol","Qty":1},{"Name":"Priest's Pack","Qty":1},{"Name":"GP","Qty":9}]}, 
                    {'Main Class':'Rogue',
                    'Inventory':[{"Name":"Leather Armor","Qty":1},{"Name":"Dagger","Qty":2},{"Name":"Thieves' Tools","Qty":1},{"Name":"Explorer's Pack","Qty":1},{"Name":"GP","Qty":19}]}, 
                    {'Main Class':'Sorcerer',
                    'Inventory':[{"Name":"Chain Mail","Qty":1},{"Name":"Shield","Qty":1},{"Name":"Longsword","Qty":1},{"Name":"Javelin","Qty":6},{"Name":"Holy Symbol","Qty":1},{"Name":"Priest's Pack","Qty":1},{"Name":"GP","Qty":9}]}, 
                    {'Main Class':'Warlock',
                    'Inventory':[{"Name":"Chain Mail","Qty":1},{"Name":"Shield","Qty":1},{"Name":"Longsword","Qty":1},{"Name":"Javelin","Qty":6},{"Name":"Holy Symbol","Qty":1},{"Name":"Priest's Pack","Qty":1},{"Name":"GP","Qty":9}]}, 
                    {'Main Class':'Wizard',
                    'Inventory':[{"Name":"Chain Mail","Qty":1},{"Name":"Shield","Qty":1},{"Name":"Longsword","Qty":1},{"Name":"Javelin","Qty":6},{"Name":"Holy Symbol","Qty":1},{"Name":"Priest's Pack","Qty":1},{"Name":"GP","Qty":9}]}, 
                    ]
    def __init__(self,name):
        self.name = name
        self.player_class = ''
        self.sub_class = ''
        self.race = ''
        self.inventory = []
        self.background = {}
        self.primary_stat = ''
        self.hpdie = 0
        self.saving_throws = []
        self.weapon_prof = []
        self.tool_prof = []
        self.armor_train = []
        self.traits = []
        self.skills = []
        
    def caps_first_letter(self,string):
        return string[0].upper() + string[1:]
    
    def add_inv(self,item,qty):
        if any(d.get("Name") == item for d in self.inventory):
            for d in self.inventory:
                if d.get("Name") == item:
                    d["Qty"] += qty
                    break
        else:
            self.inventory.append({"Name":item,"Qty":qty})

    def sub_inv(self,item,qty):
        for items in self.inventory:
            if items["Name"] == item:
                items["Qty"] -= qty
            else:
                print(f"No Item {item} exisists in {self.name}'s Inventory.")
                return None

        for items in self.inventory:
            if items["Qty"] == 0:
                self.inventory.remove(items)

    def set_race(self):
        race = input("Select Race: Aasimar, Dragonborn, Dwarf, Elf, Gnome, Goliath, Halfling, Human, Orc, or Tiefling ")
        race = self.caps_first_letter(race)
        if race == 'Aasimar':
            self.race = 'Aasimar'
        elif race == 'Dragonborn':
            subrace = input("Select your dragonborns dranconic ancestory: Black, Blue, Brass, Bronze, Copper, Gold, Green, Red, Silver, or White")
            subrace = self.caps_first_letter(subrace)
            if subrace == 'Black':
                self.race = 'Black Dragonborn'
            elif subrace == 'Blue':
                self.race = 'Blue Dragonborn'
            elif subrace == 'Brass':
                self.race = 'Brass Dragonborn'
            elif subrace == 'Bronze':
                self.race = 'Bronze Dragonborn'
            elif subrace == 'Copper':
                self.race = 'Copper Dragonborn'
            elif subrace == 'Gold':
                self.race = 'Gold Dragonborn'
            elif subrace == 'Green':
                self.race = 'Green Dragonborn'
            elif subrace == 'Red':
                self.race = 'Red Dragonborn'
            elif subrace == 'Silver':
                self.race = 'Silver Dragonborn'
            elif subrace == 'White':
                self.race = 'White Dragonborn'
        elif race == 'Dwarf':
            self.race = 'Dwarf'
        elif race == 'Elf':
            subrace = input("Select your elves lineage: Drow, High Elf, or Wood Elf")
            subrace = self.caps_first_letter(subrace)
            if subrace == 'Drow':
                self.race = 'Drow'
            elif subrace == 'High Elf':
                self.race = 'High Elf'
            elif subrace == 'Wood Elf':
                self.race = 'Wood Elf'
        elif race == 'Gnome':
            subrace = input("Select your gnome's lineage: Forest or Rock")
            subrace = self.caps_first_letter(subrace)
            if subrace == 'Forest':
                self.race = 'Forest Gnome'
            elif subrace == 'Rock':
                self.race = 'Rock Gnome'
        elif race == 'Goliath':
            subrace = input("Select your goliath's lineage: Cloud, Fire, Frost, Hill, Stone, or Storm")
            subrace = self.caps_first_letter(subrace)
            if subrace == 'Cloud':
                self.race = 'Cloud Goliath'
            elif subrace == 'Fire':
                self.race = 'Fire Goliath'
            elif subrace == 'Frost':
                self.race = 'Frost Goliath'
            elif subrace == 'Hill':
                self.race = 'Hill Goliath'
            elif subrace == 'Stone':
                self.race = 'Stone Goliath'
            elif subrace == 'Storm':
                self.race = 'Storm Goliath'
        elif race == 'Halfling':
            self.race = 'Halfling'
        elif race == 'Human':
            self.race = 'Human'
        elif race == 'Orc':
            self.race = 'Orc'
        elif race == 'Tiefling':
            subrace = input("Select your tieflings fiendish lineage: Abyssal, Chthonic, or Infernal")
            subrace = self.caps_first_letter(subrace)
            if subrace == 'Abyssal':
                self.race = 'Abyssal Tiefling'
            elif subrace == 'Chthonic':
                self.race = 'Chthonic Tiefling'
            elif subrace == 'Infernal':
                self.race = 'Infernal Tiefling'

    def set_background(self):
        BACKGROUNDS = [
            {"Type":"Acolyte",
             "Ability Scores":["INT","WIS","CHR"],
             "Feat":"Magic Initiate (Cleric)",
             "Skill Proficiencies":["Insight","Religion"],
             "Tool Proficiency":["Calligrapher's Supplies"],
             "Equipment":[{"Name":"Calligrapher's Supplies","Qty":1},
                          {"Name":"Book (prayers)","Qty":1},
                          {"Name":"Holy Symbol","Qty":1},
                          {"Name":"Parchment","Qty":10},
                          {"Name":"Robe","Qty":1},
                          {"Name":"GP","Qty":8}]},
            {"Type":"Artisan",
             "Ability Scores":["STR","DEX","INT"],
             "Feat":"Crafter",
             "Skill Proficiencies":["Investigation","Persuasion"],
             "Tool Proficiency":"Artisan Tool",
             "Equipment":[{"Name":"Artisan Tool","Qty":1},
                          {"Name":"Pouch","Qty":2},
                          {"Name":"Traveler's Clothes","Qty":1},
                          {"Name":"GP","Qty":32}]},
            {"Type":"Charlatan",
             "Ability Scores":["DEX","CON","CHR"],
             "Feat":"SKilled",
             "Skill Proficiencies":["Deception","Sleight of Hand"],
             "Tool Proficiency":["Forgery Kit"],
             "Equipment":[{"Name":"Forgery Kit","Qty":1},
                          {"Name":"Costume","Qty":1},
                          {"Name":"Fine Clothes","Qty":1},
                          {"Name":"GP","Qty":15}]},
            {"Type":"Criminal",
             "Ability Scores":["DEX","CON","INT"],
             "Feat":"Alert",
             "Skill Proficiencies":["Stealth","Sleight of Hand"],
             "Tool Proficiency":["Thieves' Tools"],
             "Equipment":[{"Name":"Thieves' Tools","Qty":1},
                          {"Name":"Dagger","Qty":2},
                          {"Name":"Crowbar","Qty":1},
                          {"Name":"Pouch","Qty":2},
                          {"Name":"Traveler's Clothes","Qty":1},
                          {"Name":"GP","Qty":16}]},
            {"Type":"Entertainer",
             "Ability Scores":["STR","DEX","CHR"],
             "Feat":"Musician",
             "Skill Proficiencies":["Acrobatics","Performance"],
             "Tool Proficiency":["Musical Instrument"],
             "Equipment":[{"Name":"Musical Instrument","Qty":1},
                          {"Name":"Costume","Qty":2},
                          {"Name":"Mirror","Qty":1},
                          {"Name":"Perfume","Qty":1},
                          {"Name":"Traveler's Clothes","Qty":1},
                          {"Name":"GP","Qty":11}]},
            {"Type":"Farmer",
             "Ability Scores":["STR","WIS","CON"],
             "Feat":"Tough",
             "Skill Proficiencies":["Animal Handling","Nature"],
             "Tool Proficiency":["Carpenter's Tools"],
             "Equipment":[{"Name":"Carpenter's Tools","Qty":1},
                          {"Name":"Sickle","Qty":1},
                          {"Name":"Healer's Kit","Qty":1},
                          {"Name":"Iron Pot","Qty":1},
                          {"Name":"Shovel","Qty":1},
                          {"Name":"Traveler's Clothes","Qty":1},
                          {"Name":"GP","Qty":30}]},
            {"Type":"Guard",
             "Ability Scores":["INT","WIS","STR"],
             "Feat":"Alert",
             "Skill Proficiencies":["Athletics","Perception"],
             "Tool Proficiency":["Gaming Set"],
             "Equipment":[{"Name":"Spear","Qty":1},
                          {"Name":"Light Crossbow","Qty":1},
                          {"Name":"Bolts","Qty":20},
                          {"Name":"Gaming Set","Qty":1},
                          {"Name":"Hooded Lantern","Qty":1},
                          {"Name":"Manacles","Qty":1},
                          {"Name":"Quiver","Qty":1},
                          {"Name":"Traveler's Clothes","Qty":1},
                          {"Name":"GP","Qty":12}]},
            {"Type":"Guide",
             "Ability Scores":["DEX","WIS","CON"],
             "Feat":"Magic Initiate (Druid)",
             "Skill Proficiencies":["Stealth","Survival"],
             "Tool Proficiency":["Cartographer's Tools"],
             "Equipment":[{"Name":"Cartographer's Tools","Qty":1},
                          {"Name":"Shortbow","Qty":1},
                          {"Name":"Arrows","Qty":20},
                          {"Name":"Bedroll","Qty":1},
                          {"Name":"Quiver","Qty":1},
                          {"Name":"Tent","Qty":1},
                          {"Name":"Traveler's Clothes","Qty":1},
                          {"Name":"GP","Qty":3}]},
            {"Type":"Hermit",
             "Ability Scores":["CON","WIS","CHR"],
             "Feat":"Healer",
             "Skill Proficiencies":["Medicine","Religion"],
             "Tool Proficiency":["Herbalism Kit"],
             "Equipment":[{"Name":"Herbalism Kit","Qty":1},
                          {"Name":"Quarterstaff","Qty":1},
                          {"Name":"Bedroll","Qty":1},
                          {"Name":"Book (philosophy)","Qty":1},
                          {"Name":"Lamp","Qty":1},
                          {"Name":"Oil","Qty":3},
                          {"Name":"Traveler's Clothes","Qty":1},
                          {"Name":"GP","Qty":16}]},
            {"Type":"Merchant",
             "Ability Scores":["CON","INT","CHR"],
             "Feat":"Lucky",
             "Skill Proficiencies":["Animal Handling","Persuasion"],
             "Tool Proficiency":["Navigator's Tools"],
             "Equipment":[{"Name":"Navigator's Tools","Qty":1},
                          {"Name":"Pouch","Qty":2},
                          {"Name":"Traveler's Clothes","Qty":1},
                          {"Name":"GP","Qty":22}]},
            {"Type":"Noble",
             "Ability Scores":["STR","INT","CHR"],
             "Feat":"Skilled",
             "Skill Proficiencies":["History","Persuasion"],
             "Tool Proficiency":["Gaming Set"],
             "Equipment":[{"Name":"Gaming Set","Qty":1},
                          {"Name":"Perfume","Qty":1},
                          {"Name":"Fine Clothes","Qty":1},
                          {"Name":"GP","Qty":29}]},
            {"Type":"Sage",
             "Ability Scores":["CON","WIS","INT"],
             "Feat":"Magic Initiate (Wizard)",
             "Skill Proficiencies":["Arcana","History"],
             "Tool Proficiency":["Calligrapher's Supplies"],
             "Equipment":[{"Name":"Calligrapher's Supplies","Qty":1},
                          {"Name":"Quarterstaff","Qty":1},
                          {"Name":"Book (history)","Qty":1},
                          {"Name":"Parchment","Qty":8},
                          {"Name":"Robe","Qty":1},
                          {"Name":"GP","Qty":8}]},
            {"Type":"Sailor",
             "Ability Scores":["STR","WIS","DEX"],
             "Feat":"Tavern Brawler",
             "Skill Proficiencies":["Acrobatics","Perception"],
             "Tool Proficiency":["Navigator's Tools"],
             "Equipment":[{"Name":"Navigator's Tools","Qty":1},
                          {"Name":"Dagger","Qty":1},
                          {"Name":"Rope","Qty":1},
                          {"Name":"Traveler's Clothes","Qty":1},
                          {"Name":"GP","Qty":20}]},
            {"Type":"Scribe",
             "Ability Scores":["DEX","INT","WIS"],
             "Feat":"Skilled",
             "Skill Proficiencies":["Investigation","Perception"],
             "Tool Proficiency":["Calligrapher's Supplies"],
             "Equipment":[{"Name":"Calligrapher's Supplies","Qty":1},
                          {"Name":"Fine Clothes","Qty":1},
                          {"Name":"Lamp","Qty":1},
                          {"Name":"Oil","Qty":3},
                          {"Name":"Parchment","Qty":12},
                          {"Name":"GP","Qty":23}]},
            {"Type":"Soldier",
             "Ability Scores":["STR","DEX","CON"],
             "Feat":"Savage Attacker",
             "Skill Proficiencies":["Athletics","Intimidation"],
             "Tool Proficiency":["Gaming Set"],
             "Equipment":[{"Name":"Gaming Set","Qty":1},
                          {"Name":"Spear","Qty":1},
                          {"Name":"Short Bow","Qty":1},
                          {"Name":"Arrows","Qty":20},
                          {"Name":"Healer's Kit","Qty":1},
                          {"Name":"Quiver","Qty":1},
                          {"Name":"Traveler's Clothes","Qty":1},
                          {"Name":"GP","Qty":14}]},
            {"Type":"Wayfarer",
             "Ability Scores":["DEX","WIS","CHR"],
             "Feat":"Lucky",
             "Skill Proficiencies":["Insight","Stealth"],
             "Tool Proficiency":["Thieves' Tools"],
             "Equipment":[{"Name":"Thieves' Tools","Qty":1},
                          {"Name":"Dagger","Qty":2},
                          {"Name":"Gaming Set","Qty":1},
                          {"Name":"Bedroll","Qty":1},
                          {"Name":"Pouch","Qty":2},
                          {"Name":"Traveler's Clothes","Qty":1},
                          {"Name":"GP","Qty":16}]}
        ]
        selection = input("What is your background: Acolyte, Artisan, Charlatan, Criminal, Entertainer, Farmer, Guard, Guide, Hermit, Merchant, Noble, Sage, Sailor, Scribe, Soldier, Wayfarer")
        selection = self.caps_first_letter(selection)
        
        if selection in [background['Type'] for background in BACKGROUNDS]:
            self.background = selection
            for select in BACKGROUNDS:
                if select['Type'] == selection:
                    for each in select["Equipment"]:
                        self.inventory.append(each)
        else:
            print("No option was selected, try again!")
            self.set_background()

    def set_class(self):
        mainclass = input("What class are you: Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard").lower()
        mainclass = self.caps_first_letter(mainclass)
        self.player_class = mainclass
        if mainclass == 'Barbarian':
            self.armor_train.append('Light')
            self.armor_train.append('Medium')
            self.armor_train.append('Shields')
            self.weapon_prof.append('Simple')
            self.weapon_prof.append('Martial')
            self.hpdie = 12
            self.primary_stat = 'STR'
            self.saving_throws.append('STR')
            self.saving_throws.append('CON')
            options = ['Animal Handling','Athletics','Intimidation','Nature','Perception','Survival']
            firstselect = input(f'Select one from {options}.')
            self.skills.append(firstselect)
            if firstselect != '':
                options.remove(firstselect)
            secondselect = input(f'Select your second skill from {options}')
            self.skills.append(secondselect)
        elif mainclass == 'Bard':
            self.armor_train.append('Light')
            self.weapon_prof.append('Simple')
            self.tool_prof.append('Instruments')
            self.hpdie = 8
            self.primary_stat = 'CHR'
            self.saving_throws.append('DEX')
            self.saving_throws.append('CHR')
            instrument = input('Which instrument do you want to start with: Bagpipes, Drum, Dulcimer, Flute, Horn, Lute, Lyre, Pan flute, Shawm, or Viol? ').lower()
            self.inventory.append(instrument)
            skills_to_learn = []
            skillscopy = self.SKILLS_LIST
            while len(skills_to_learn) < 3:
                addskill = input(f'Select one of the skills to learn: {skillscopy}')
                skills_to_learn.append(addskill)
                skillscopy.remove(addskill)
            for each in skills_to_learn:
                self.skills.append(each)
        elif mainclass == 'Cleric':
            self.armor_train.append('Light')
            self.armor_train.append('Medium')
            self.armor_train.append('Shields')
            self.weapon_prof.append('Simple')
            self.hpdie = 8
            self.primary_stat = 'WIS'
            self.saving_throws.append('WIS')
            self.saving_throws.append('CHR')
            options = ['History','Insight','Medicine','Persuasion','Religion']
            firstselect = input(f'Select one from {options}.')
            self.skills.append(firstselect)
            options.remove(firstselect)
            secondselect = input(f'Select your second skill from {options}')
            self.skills.append(secondselect)
        elif mainclass == 'Druid':
            self.armor_train.append('Light')
            self.armor_train.append('Shields')
            self.weapon_prof.append('Simple')
            self.tool_prof.append('Herbalism Kit')
            self.hpdie = 8
            self.primary_stat = 'WIS'
            self.saving_throws.append('WIS')
            self.saving_throws.append('INT')
            options = ['Arcana','Animal Handling','Insight','Medicine','Nature','Perception','Religion','Survival']
            firstselect = input(f'Select one from {options}.')
            self.skills.append(firstselect)
            options.remove(firstselect)
            secondselect = input(f'Select your second skill from {options}')
            self.skills.append(secondselect)
        elif mainclass == 'Fighter':
            self.weapon_prof.append('Simple')
            self.weapon_prof.append('Martial')
            self.armor_train.append('Light')
            self.armor_train.append('Medium')
            self.armor_train.append('Heavy')
            self.armor_train.append('Shields')
            self.hpdie = 10
            self.saving_throws.append('STR')
            self.saving_throws.append('CON')
            pick = input('Do you want to be a strength or dexterity based fighter? ').lower()
            if pick == 'strength':
                self.primary_stat = 'STR'
            elif pick == 'dexterity':
                self.primary_stat = 'DEX'
        elif mainclass == 'Monk':
            self.weapon_prof.append('Simple')
            self.weapon_prof.append('Martial')
            self.armor_train.append('None')
            self.hpdie = 8
            self.primary_stat = 'DEX WIS'
            self.saving_throws.append('STR')
            self.saving_throws.append('DEX')
            options = ['Acrobatics','Athletics','History','Insight','Religion','Stealth']
            firstselect = input(f'Select one from {options}.')
            self.skills.append(firstselect)
            options.remove(firstselect)
            secondselect = input(f'Select your second skill from {options}')
            self.skills.append(secondselect)
            tools = ["Alchemist's Supplies", "Calligrapher's Supplies", "Carpenter's Tools", "Cartographer's Tools", "Cobblers Tools", "Cook's Utensils", "Glassblower's Tools", "Jeweler's Tools", "Leatherworker's Tools", "Mason's Tools", "Painter's Supplies", "Potter's Tools", "Smith's Tools", "Tinker's Tools", "Weaver's Tools", "Woodcarver's Tools","Bagpipes", "Drum", "Dulcimer", "Flute", "Horn", "Lute", "Lyre", "Pan flute", "Shawm", "Viol"]
            toolselect = input(f'Select one tool proficiency from {tools}.')
            toolselect = self.caps_first_letter(toolselect)
            self.tool_prof.append(toolselect)
            self.inventory.append({"Name":toolselect,"Qty":1})
        elif mainclass == 'Paladin':
            self.armor_train.append('Light')
            self.armor_train.append('Medium')
            self.armor_train.append('Heavy')
            self.armor_train.append('Shields')
            self.weapon_prof.append('Simple')
            self.weapon_prof.append('Martial')
            self.hpdie = 10
            self.primary_stat = 'STR CHR'
            self.saving_throws.append('WIS')
            self.saving_throws.append('CHR')
            options = ['Athletics','Insight','Intimidation','Medicine','Persuasion','Religion']
            firstselect = input(f'Select one from {options}.')
            self.skills.append(firstselect)
            options.remove(firstselect)
            secondselect = input(f'Select your second skill from {options}')
            self.skills.append(secondselect)
        elif mainclass == 'Ranger':
            self.armor_train.append('Light')
            self.armor_train.append('Medium')
            self.armor_train.append('Shields')
            self.weapon_prof.append('Simple')  
            self.weapon_prof.append('Martial')
            self.hpdie = 10
            self.primary_stat = 'DEX WIS'
            self.saving_throws.append('STR')
            self.saving_throws.append('DEX')
            options = ['Animal Handling','Athletics','Insight','Investigation','Nature','Perception','Stealth','Survival']
            firstselect = input(f'Select one from {options}.')
            self.skills.append(firstselect)
            options.remove(firstselect)
            secondselect = input(f'Select your second skill from {options}')
            self.skills.append(secondselect)
            options.remove(secondselect)
            thirdselect = input(f'Select your third skill from {options}')
            self.skills.append(thirdselect)
        elif mainclass == 'Rogue':
            self.armor_train.append('Simple')
            self.armor_train.append('Martial')
            self.hpdie = 12
            self.primary_stat = 'STR'
            self.saving_throws.append('STR')
            self.saving_throws.append('CON')
        elif mainclass == 'Sorcerer':
            self.armor_train.append('Simple')
            self.armor_train.append('Martial')
            self.hpdie = 12
            self.primary_stat = 'STR'
            self.saving_throws.append('STR')
            self.saving_throws.append('CON')
        elif mainclass == 'Warlock':
            self.armor_train.append('Simple')
            self.armor_train.append('Martial')
            self.hpdie = 12
            self.primary_stat = 'STR'
            self.saving_throws.append('STR')
            self.saving_throws.append('CON')
        elif mainclass == 'Wizard':
            self.armor_train.append('Simple')
            self.armor_train.append('Martial')
            self.hpdie = 12
            self.primary_stat = 'STR'
            self.saving_throws.append('STR')
            self.saving_throws.append('CON')
        else:
            pass

Tim = Character('Tim')
# print(Tim.name)
# Tim.add_inv('Gold',2)
# print(Tim.inventory)
# Tim.sub_inv('Gold',1)
# print(Tim.inventory)
# Tim.sub_inv('Gold',1)
# print(Tim.inventory)
Tim.set_class()
print(Tim.skills)

