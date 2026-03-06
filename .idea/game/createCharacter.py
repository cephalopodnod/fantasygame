#createCharacter.py
class Character():
    SKILLS_LIST = ['Acrobatics','Animal Handling','Arcana','Athletics','Deception','History','Insight','Intimidation','Investigation','Medicine','Nature','Perception','Performance','Persuasion','Religion','Sleight of Hand','Stealth','Survival']
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
        self.armor_train = []
        self.traits = []
        self.skills = []
        

    def add_inv(self,item,qty):
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
        if race == 1 or race.lower() == 'aasimar':
            self.race = 'Aasimar'
        elif race == 2 or race.lower() == 'dragonborn':
            subrace = input("Select your dragonborns dranconic ancestory: Black, Blue, Brass, Bronze, Copper, Gold, Green, Red, Silver, or White")
            if subrace == 1 or subrace.lower() == 'black':
                self.race = 'Black Dragonborn'
            elif subrace == 2 or subrace.lower() == 'blue':
                self.race = 'Blue Dragonborn'
            elif subrace == 3 or subrace.lower() == 'brass':
                self.race = 'Brass Dragonborn'
            elif subrace == 4 or subrace.lower() == 'bronze':
                self.race = 'Bronze Dragonborn'
            elif subrace == 5 or subrace.lower() == 'copper':
                self.race = 'Copper Dragonborn'
            elif subrace == 6 or subrace.lower() == 'gold':
                self.race = 'Gold Dragonborn'
            elif subrace == 7 or subrace.lower() == 'green':
                self.race = 'Green Dragonborn'
            elif subrace == 8 or subrace.lower() == 'red':
                self.race = 'Red Dragonborn'
            elif subrace == 9 or subrace.lower() == 'silver':
                self.race = 'Silver Dragonborn'
            elif subrace == 10 or subrace.lower() == 'white':
                self.race = 'White Dragonborn'
        elif race == 3 or race.lower() == 'dwarf':
            self.race = 'Dwarf'
        elif race == 4 or race.lower() == 'elf':
            subrace = input("Select your elves lineage: Drow, High Elf, or Wood Elf")
            if subrace == 1 or subrace.lower() == 'drow':
                self.race = 'Drow'
            elif subrace == 2 or subrace.lower() == 'high elf':
                self.race = 'High Elf'
            elif subrace == 3 or subrace.lower() == 'wood elf':
                self.race = 'Wood Elf'
        elif race == 5 or race.lower() == 'gnome':
            subrace = input("Select your gnome's lineage: Forest or Rock")
            if subrace == 1 or subrace.lower() == 'forest':
                self.race = 'Forest Gnome'
            elif subrace == 2 or subrace.lower() == 'rock':
                self.race = 'Rock Gnome'
        elif race == 6 or race.lower() == 'goliath':
            subrace = input("Select your goliath's lineage: Cloud, Fire, Frost, Hill, Stone, or Storm")
            if subrace == 1 or subrace.lower() == 'cloud':
                self.race = 'Cloud Goliath'
            elif subrace == 2 or subrace.lower() == 'fire':
                self.race = 'Fire Goliath'
            elif subrace == 3 or subrace.lower() == 'frost':
                self.race = 'Frost Goliath'
            elif subrace == 4 or subrace.lower() == 'hill':
                self.race = 'Hill Goliath'
            elif subrace == 5 or subrace.lower() == 'stone':
                self.race = 'Stone Goliath'
            elif subrace == 6 or subrace.lower() == 'storm':
                self.race = 'Storm Goliath'
        elif race == 7 or race.lower() == 'halfling':
            self.race = 'Halfling'
        elif race == 8 or race.lower() == 'human':
            self.race = 'Human'
        elif race == 9 or race.lower() == 'orc':
            self.race = 'Orc'
        elif race == 10 or race.lower() == 'tiefling':
            subrace = input("Select your tieflings fiendish lineage: Abyssal, Chthonic, or Infernal")
            if subrace == 1 or subrace.lower() == 'abyssal':
                self.race = 'Abyssal Tiefling'
            elif subrace == 2 or subrace.lower() == 'chthonic':
                self.race = 'Chthonic Tiefling'
            elif subrace == 3 or subrace.lower() == 'infernal':
                self.race = 'Infernal Tiefling'

    def set_background(self):
        BACKGROUNDS = [
            {"Type":"Acolyte",
             "Ability Scores":["INT","WIS","CHR"],
             "Feat":"Magic Initiate (Cleric)",
             "Skill Proficiencies":["Insight","Religion"],
             "Tool Proficiency":["Calligrapher's Supplies"],
             "Equipment":["Calligrapher's Supplies","Book (prayers)","Holy Symbol","Parchment (10 Sheets)","Robe","8 GP"]},
            {"Type":"Artisan",
             "Ability Scores":["STR","DEX","INT"],
             "Feat":"Crafter",
             "Skill Proficiencies":["Investigation","Persuasion"],
             "Tool Proficiency":"Artisan Tool",
             "Equipment":["Artisan Tool","2 Pouches","Traveler's Clothes","32 GP"]},
            {"Type":"Charlatan",
             "Ability Scores":["DEX","CON","CHR"],
             "Feat":"SKilled",
             "Skill Proficiencies":["Deception","Sleight of Hand"],
             "Tool Proficiency":["Forgery Kit"],
             "Equipment":["Forgery Kit","Costume","Fine Clothes","15 GP"]},
            {"Type":"Criminal",
             "Ability Scores":["DEX","CON","INT"],
             "Feat":"Alert",
             "Skill Proficiencies":["Stealth","Sleight of Hand"],
             "Tool Proficiency":["Thieves' Tools"],
             "Equipment":["Thieves' Tools","2 Daggers","Crowbar","2 Pouches","Traveler's Clothes","16 GP"]},
            {"Type":"Entertainer",
             "Ability Scores":["STR","DEX","CHR"],
             "Feat":"Musician",
             "Skill Proficiencies":["Acrobatics","Performance"],
             "Tool Proficiency":["Musical Instrument"],
             "Equipment":["Musical Instrument","2 Costumes","Mirror","Perfume","Traveler's Clothes","11 GP"]},
            {"Type":"Farmer",
             "Ability Scores":["STR","WIS","CON"],
             "Feat":"Tough",
             "Skill Proficiencies":["Animal Handling","Nature"],
             "Tool Proficiency":["Carpenter's Tools"],
             "Equipment":["Carpenter's Tools","Sickle","Healer's Kit","Iron Pot","Shovel","Traveler's Clothes","30 GP"]},
            {"Type":"Guard",
             "Ability Scores":["INT","WIS","STR"],
             "Feat":"Alert",
             "Skill Proficiencies":["Athletics","Perception"],
             "Tool Proficiency":["Gaming Set"],
             "Equipment":["Spear","Light Crossbow","20 Bolts","Gaming Set","Hooded Lantern","Manacles","Quiver","Traveler's Clothes","12 GP"]},
            {"Type":"Guide",
             "Ability Scores":["DEX","WIS","CON"],
             "Feat":"Magic Initiate (Druid)",
             "Skill Proficiencies":["Stealth","Survival"],
             "Tool Proficiency":["Cartographer's Tools"],
             "Equipment":["Cartographer's Tools","Shortbow","20 Arrows","Bedroll","Quiver","Tent","Traveler's Clothes","3 GP"]},
            {"Type":"Hermit",
             "Ability Scores":["CON","WIS","CHR"],
             "Feat":"Healer",
             "Skill Proficiencies":["Medicine","Religion"],
             "Tool Proficiency":["Herbalism Kit"],
             "Equipment":["Herbalism Kit","Quarterstaff","Bedroll","Book (philosophy)","Lamp","Oil (3 flasks)","Traveler's Clothes","16 GP"]},
            {"Type":"Merchant",
             "Ability Scores":["CON","INT","CHR"],
             "Feat":"Lucky",
             "Skill Proficiencies":["Animal Handling","Persuasion"],
             "Tool Proficiency":["Navigator's Tools"],
             "Equipment":["Navigator's Tools","2 Pouches","Traveler's Clothes","22 GP"]},
            {"Type":"Noble",
             "Ability Scores":["STR","INT","CHR"],
             "Feat":"Skilled",
             "Skill Proficiencies":["History","Persuasion"],
             "Tool Proficiency":["Gaming Set"],
             "Equipment":["Gaming Set","Perfume","Fine Clothes","29 GP"]},
            {"Type":"Sage",
             "Ability Scores":["CON","WIS","INT"],
             "Feat":"Magic Initiate (Wizard)",
             "Skill Proficiencies":["Arcana","History"],
             "Tool Proficiency":["Calligrapher's Supplies"],
             "Equipment":["Calligrapher's Supplies","Quarterstaff","Book (history)","Parchment (8 Sheets)","Robe","8 GP"]},
            {"Type":"Sailor",
             "Ability Scores":["STR","WIS","DEX"],
             "Feat":"Tavern Brawler",
             "Skill Proficiencies":["Acrobatics","Perception"],
             "Tool Proficiency":["Navigator's Tools"],
             "Equipment":["Navigator's Tools","Dagger","Rope","Traveler's Clothes","20 GP"]},
            {"Type":"Scribe",
             "Ability Scores":["DEX","INT","WIS"],
             "Feat":"Skilled",
             "Skill Proficiencies":["Investigation","Perception"],
             "Tool Proficiency":["Calligrapher's Supplies"],
             "Equipment":["Calligrapher's Supplies","Fine Clothes","Lamp","Oil (3 flasks)","Parchment (12 sheets)","23 GP"]},
            {"Type":"Soldier",
             "Ability Scores":["STR","DEX","CON"],
             "Feat":"Savage Attacker",
             "Skill Proficiencies":["Athletics","Intimidation"],
             "Tool Proficiency":["Gaming Set"],
             "Equipment":["Gaming Set","Spear","Short Bow","20 Arrows","Healer's Kit","Quiver","Traveler's Clothes","14 GP"]},
            {"Type":"Wayfarer",
             "Ability Scores":["DEX","WIS","CHR"],
             "Feat":"Lucky",
             "Skill Proficiencies":["Insight","Stealth"],
             "Tool Proficiency":["Thieves' Tools"],
             "Equipment":["Thieves' Tools","2 Daggers","Gaming Set","Bedroll","2 Pouches","Traveler's Clothes","16 GP"]}
        ]
        selection = input("What is your background: Acolyte, Artisan, Charlatan, Criminal, Entertainer, Farmer, Guard, Guide, Hermit, Merchant, Noble, Sage, Sailor, Scribe, Soldier, Wayfarer").lower()  
        if selection == "acolyte" or selection == 1:
            for select in BACKGROUNDS:
                if select['Type'] == 'Acolyte':
                    self.background = select
                    self.inventory.append(select['Equipment'])
        elif selection == "artisan" or selection == 2:
            for select in BACKGROUNDS:
                if select['Type'] == 'Artisan':
                    self.background = select
                    self.inventory.append(select['Equipment'])
        elif selection == "charlatan" or selection == 3:
            for select in BACKGROUNDS:
                if select['Type'] == 'Charlatan':
                    self.background = select
                    self.inventory.append(select['Equipment'])
        elif selection == "criminal" or selection == 4:
            for select in BACKGROUNDS:
                if select['Type'] == 'Criminal':
                    self.background = select
                    self.inventory.append(select['Equipment'])
        elif selection == "entertainer" or selection == 5:
            for select in BACKGROUNDS:
                if select['Type'] == 'Entertainer':
                    self.background = select
                    self.inventory.append(select['Equipment'])
        elif selection == "farmer" or selection == 6:
            for select in BACKGROUNDS:
                if select['Type'] == 'Farmer':
                    self.background = select
                    self.inventory.append(select['Equipment'])
        elif selection == "guard" or selection == 7:
            for select in BACKGROUNDS:
                if select['Type'] == 'Guard':
                    self.background = select
                    self.inventory.append(select['Equipment'])
        elif selection == "guide" or selection == 8:
            for select in BACKGROUNDS:
                if select['Type'] == 'Guide':
                    self.background = select
                    self.inventory.append(select['Equipment'])
        elif selection == "hermit" or selection == 9:
            for select in BACKGROUNDS:
                if select['Type'] == 'Hermit':
                    self.background = select
                    self.inventory.append(select['Equipment'])
        elif selection == "merchant" or selection == 10:
            for select in BACKGROUNDS:
                if select['Type'] == 'Merchant':
                    self.background = select
                    self.inventory.append(select['Equipment'])
        elif selection == "noble" or selection == 11:
            for select in BACKGROUNDS:
                if select['Type'] == 'Noble':
                    self.background = select
                    self.inventory.append(select['Equipment'])
        elif selection == "sage" or selection == 12:
            for select in BACKGROUNDS:
                if select['Type'] == 'Sage':
                    self.background = select
                    self.inventory.append(select['Equipment'])
        elif selection == "sailor" or selection == 13:
            for select in BACKGROUNDS:
                if select['Type'] == 'Sailor':
                    self.background = select
                    self.inventory.append(select['Equipment'])
        elif selection == "scribe" or selection == 14:
            for select in BACKGROUNDS:
                if select['Type'] == 'Scribe':
                    self.background = select
                    self.inventory.append(select['Equipment'])
        elif selection == "soldier" or selection == 15:
            for select in BACKGROUNDS:
                if select['Type'] == 'Soldier':
                    self.background = select
                    self.inventory.append(select['Equipment'])
        elif selection == "wayfarer" or selection == 16:
            for select in BACKGROUNDS:
                if select['Type'] == 'Wayfarer':
                    self.background = select
                    self.inventory.append(select['Equipment'])
        else:
            print("No option was selected, try again!")
            self.set_background()

    def set_class(self):
        mainclass = input("What class are you: Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard").lower()
        if mainclass == 'barbarian' or mainclass == 1:
            self.player_class = 'Barbarian'
            self.armor_train.append('Light')
            self.armor_train.append('Medium')
            self.armor_train.append('Shield')
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
        elif mainclass == 'bard' or mainclass == 2:
            self.player_class = 'Bard'
            self.armor_train.append('Light')
            self.hpdie = 8
            self.primary_stat = 'CHR'
            self.saving_throws.append('DEX')
            self.saving_throws.append('CHR')
        elif mainclass == 'cleric' or mainclass == 3:
            self.player_class = 'Cleric'
            self.armor_train.append('Simple')
            self.armor_train.append('Martial')
            self.hpdie = 12
            self.primary_stat = 'STR'
            self.saving_throws.append('STR')
            self.saving_throws.append('CON')
        elif mainclass == 'druid' or mainclass == 4:
            self.player_class = 'Druid'
            self.armor_train.append('Simple')
            self.armor_train.append('Martial')
            self.hpdie = 12
            self.primary_stat = 'STR'
            self.saving_throws.append('STR')
            self.saving_throws.append('CON')
        elif mainclass == 'fighter' or mainclass == 5:
            self.player_class = 'Fighter'
            self.armor_train.append('Simple')
            self.armor_train.append('Martial')
            self.hpdie = 12
            self.primary_stat = 'STR'
            self.saving_throws.append('STR')
            self.saving_throws.append('CON')
        elif mainclass == 'monk' or mainclass == 6:
            self.player_class = 'Monk'
            self.armor_train.append('Simple')
            self.armor_train.append('Martial')
            self.hpdie = 12
            self.primary_stat = 'STR'
            self.saving_throws.append('STR')
            self.saving_throws.append('CON')
        elif mainclass == 'paladin' or mainclass == 7:
            self.player_class = 'Paladin'
            self.armor_train.append('Simple')
            self.armor_train.append('Martial')
            self.hpdie = 12
            self.primary_stat = 'STR'
            self.saving_throws.append('STR')
            self.saving_throws.append('CON')
        elif mainclass == 'ranger' or mainclass == 8:
            self.player_class = 'Ranger'
            self.armor_train.append('Simple')
            self.armor_train.append('Martial')
            self.hpdie = 12
            self.primary_stat = 'STR'
            self.saving_throws.append('STR')
            self.saving_throws.append('CON')
        elif mainclass == 'rogue' or mainclass == 9:
            self.player_class = 'Rogue'
            self.armor_train.append('Simple')
            self.armor_train.append('Martial')
            self.hpdie = 12
            self.primary_stat = 'STR'
            self.saving_throws.append('STR')
            self.saving_throws.append('CON')
        elif mainclass == 'sorcerer' or mainclass == 10:
            self.player_class = 'Sorcerer'
            self.armor_train.append('Simple')
            self.armor_train.append('Martial')
            self.hpdie = 12
            self.primary_stat = 'STR'
            self.saving_throws.append('STR')
            self.saving_throws.append('CON')
        elif mainclass == 'warlock' or mainclass == 11:
            self.player_class = 'Warlock'
            self.armor_train.append('Simple')
            self.armor_train.append('Martial')
            self.hpdie = 12
            self.primary_stat = 'STR'
            self.saving_throws.append('STR')
            self.saving_throws.append('CON')
        elif mainclass == 'wizard' or mainclass == 12:
            self.player_class = 'Wizard'
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
