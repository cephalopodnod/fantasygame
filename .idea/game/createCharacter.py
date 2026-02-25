#createCharacter.py
class Character():
    def __init__(self,name):
        self.name = name
        self.player_class = ''
        self.race = ''
        self.inventory = []

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

    # def setup(self):
    #     self.set_race()
    #     self.set_background()

Tim = Character('Tim')
# print(Tim.name)
# Tim.add_inv('Gold',2)
# print(Tim.inventory)
# Tim.sub_inv('Gold',1)
# print(Tim.inventory)
# Tim.sub_inv('Gold',1)
# print(Tim.inventory)
Tim.set_race()
print(Tim.race)