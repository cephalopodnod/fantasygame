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
                    'Inventory':[{"Name":"Studded Leather Armor","Qty":1},{"Name":"Scimitar","Qty":1},{"Name":"Longsword","Qty":1},{"Name":"Javelin","Qty":6},{"Name":"Holy Symbol","Qty":1},{"Name":"Priest's Pack","Qty":1},{"Name":"GP","Qty":9}]}, 
                    {'Main Class':'Rogue',
                    'Inventory':[{"Name":"Leather Armor","Qty":1},{"Name":"Dagger","Qty":2},{"Name":"Thieves' Tools","Qty":1},{"Name":"Shortsword","Qty":1},{"Name":"Shortbow","Qty":1},{"Name":"Arrows","Qty":20},{"Name":"Burglar's Pack","Qty":1},{"Name":"GP","Qty":8}]}, 
                    {'Main Class':'Sorcerer',
                    'Inventory':[{"Name":"Spear","Qty":1},{"Name":"Dagger","Qty":2},{"Name":"Arcane Focus (Crystal)","Qty":1},{"Name":"Dungeoneer's Pack","Qty":1},{"Name":"GP","Qty":28}]}, 
                    {'Main Class':'Warlock',
                    'Inventory':[{"Name":"Leather Armor","Qty":1},{"Name":"Sickle","Qty":1},{"Name":"Dagger","Qty":2},{"Name":"Arcane Focus (orb)","Qty":1},{"Name":"Book (occult lore)","Qty":1},{"Name":"Scholar's Pack","Qty":1},{"Name":"GP","Qty":15}]}, 
                    {'Main Class':'Wizard',
                    'Inventory':[{"Name":"Dagger","Qty":2},{"Name":"Arcane Focus (Quarterstaff)","Qty":1},{"Name":"Robe","Qty":1},{"Name":"Spellbook","Qty":1},{"Name":"Scholar's Pack","Qty":1},{"Name":"GP","Qty":5}]}, 
                    ]
    ORIGIN_FEATS = ['Alert','Crafter','Healer','Lucky','Magic Initiate','Musician','Savage Attacker','Skilled','Tavern Brawler','Tough']
    FEATS = [{"Name":"Ability Score Increase","Description":"Your choice of two ability scores increase by 1.","Level Requirement":4},
            {"Name":"Actor","Description":"Skilled at mimicry and dramatics, you can unerringly mimic another person's speech, writing, and behavior. You gain the following benefits: \n-You can cast the *disguise self* spell at will. It doesn't count against your number of spells known.\n-You can mimic the speech of another person or the sounds made by other creatures. You must have heard the person speaking, or heard the creature make the sound, for at least 1 minute. A successful Wisdom (Insight) check contested by your Charisma (Deception) check allows a listener to determine that the effect is faked.","Level Requirement":4},
            {"Name":"Alert","Description":"Always on the lookout for danger, you gain the following benefits: \n-You can't be surprised while you are conscious.\n-Other creatures don't gain advantage on attack rolls against you as a result of being unseen by you.\n-You gain a +5 bonus to initiative.","Level Requirement":4},
            {"Name":"Athlete","Description":"You have undergone extensive physical training to gain the following benefits: \n-You have advantage on Strength (Athletics) checks made to climb, jump, or swim.\n-When you are prone, standing up uses only 5 feet of your movement.\n-You can make a running long jump or a running high jump after moving only 5 feet on foot, rather than 10 feet.","Level Requirement":4,"Stat Requirement":"STR 13+ or DEX 13+"},
            {"Name":"Charger","Description":"When you use your action to Dash, you can use a bonus action to make one melee weapon attack or to shove a creature.","Level Requirement":4},
            {"Name":"Crafter","Description":"You have proficiency with artisan's tools of your choice. You gain the following benefits: \n-When you use your action to craft something, your proficiency bonus is doubled if you are using tools with which you are proficient.\n-You can craft nonmagical items with a cost of 100 gp or fewer in a workweek (6 days of 8 hours crafting).","Level Requirement":4,"Stat Requirement":"INT 13+"},
            {"Name":"Crossbow Expert","Description":"Thanks to extensive practice with the crossbow,you gain the following benefits: \n-You ignore the loading property of crossbows with which you are proficient.\n-Being within 5 feet of a hostile creature doesn't impose disadvantage on your ranged attack rolls.\n-When you use the Attack action and attack with a one-handed weapon, you can use a bonus action to attack with a hand crossbow you are holding.","Level Requirement":4},
            {"Name":"Defensive Duelist","Description":"When you are wielding a finesse weapon, you can use your reaction to add your proficiency bonus to your AC for that attack, potentially causing the attack to miss you.","Level Requirement":4,"Stat Requirement":"DEX 13+"},
            {"Name":"Dual Wielder","Description":"You master fighting with two weapons, gaining the following benefits: \n-You gain a +1 bonus to AC while you are wielding a separate melee weapon in each hand.\n-You can use two-weapon fighting even when the one-handed melee weapons you are wielding aren't light.\n-You can draw or stow two one-handed weapons when you would normally be able to draw or stow only one.","Level Requirement":4},
            {"Name":"Dungeon Delver","Description":"You have significant experience delving into dungeons and other dangerous areas, and you gain the following benefits: \n-You have advantage on Wisdom (Perception) and Intelligence (Investigation) checks made to detect the presence of secret doors.\n-You have advantage on saving throws made to avoid or resist traps.\n-You can search for traps while traveling at a fast pace, and you can search for traps and hidden doors while engaged in combat.","Level Requirement":4},
            {"Name":"Durable","Description":"Your hit point maximum increases by 1, and   whenever you spend Hit Dice to regain hit points, you regain an additional 1 hit point per die.","Level Requirement":4,"Stat Requirement":"CON 13+"},
            {"Name":"Elemental Adept","Description":"When you gain this feat, choose one of the following damage types: acid, cold, fire, lightning, or thunder. \n-Spells you cast ignore resistance to damage of the chosen type.\n- In addition, when you roll damage for a spell you cast that deals damage of that type, you can treat any 1 on a damage die as a 2.","Level Requirement":4,"Stat Requirement":"Spellcasting Ability 13+"},
            {"Name":"Grappler","Description":"You have practiced grappling and pinning your foes, gaining the following benefits: \n-You have advantage on attack rolls against a creature you are grappling.\n- You can use your action to try to pin a creature grappled by you. To do so, make another grapple check. If you succeed, you and the creature are both restrained until the grapple ends.","Level Requirement":4,"Stat Requirement":"STR 13+"},
            {"Name":"Great Weapon Master","Description":"You've learned to put the weight of a weapon to your advantage, letting its momentum empower your strikes. You gain the following benefits: \n- On your turn, when you score a critical hit with a melee weapon or reduce a creature to 0 hit points with one, you can make one melee weapon attack as a bonus action.\n-B Before you make a melee attack with a heavy weapon that you are proficient with, you can choose to take a -5 penalty to the attack roll. If the attack hits, you add +10 to the attack's damage.","Level Requirement":4,"Stat Requirement":"STR 13+"},
            {"Name":"Heavily Armored","Description":"Prerequisite: Proficiency with medium armor\nYour proficiency with medium armor improves. You gain proficiency with heavy armor.","Level Requirement":4,"Stat Requirement":"STR 13+"},
            {"Name":"Heavy Armor Master","Description":"While you are wearing heavy armor, bludgeoning, piercing, and slashing damage that you take from nonmagical weapons is reduced by 3 (to a minimum of 0).","Level Requirement":4,"Stat Requirement":"STR 15+"},
            {"Name":"Inspiring Leader","Description":"You can spend 10 minutes inspiring your companions, shoring up their resolve to fight. When you do so, choose up to six friendly creatures (which can include yourself) within 30 feet of you who can see or hear you and who can understand you. Each creature can gain temporary hit points equal to your level + your Charisma modifier.","Level Requirement":4,"Stat Requirement":"CHR 13+"},
            {"Name":"Keen Mind","Description":"You have a mind that can track time, direction, and detail with uncanny precision. You gain the following benefits: \n-You always know which way is north.\n-You always know the number of hours left before the next sunrise or sunset.\n-You can accurately recall anything you have seen or heard within the past month.","Level Requirement":4},
            {"Name":"Lightly Armored","Description":"Prerequisite: Proficiency with light armor\nYour proficiency with light armor improves. You gain proficiency with medium armor.","Level Requirement":4,"Stat Requirement":"DEX 13+"},
            {"Name":"Linguist","Description":"You have studied languages and codes, gaining the following benefits: \n-You learn three languages of your choice.\n-You can create written ciphers. Others can't decipher a code you create unless you teach them, they succeed on an Intelligence check (DC equal to the number you set when you create the cipher) that uses your Intelligence as a modifier, or they use magic to decipher it.","Level Requirement":4,"Stat Requirement":"INT 13+"},
            {"Name":"Lucky","Description":"You have inexplicable luck that seems to kick in at just the right moment. You have 3 luck points. Whenever you make an attack roll, an ability check, or a saving throw, you can spend one luck point to roll an additional d20. You can choose to spend one of your luck points after you roll the die, but before the outcome is determined. You choose which of the d20s is used for the attack roll, ability check, or saving throw.","Level Requirement":4},
            {"Name":"Mage Slayer","Description":"You have practiced techniques to thwart spellcasters, gaining the following benefits: \n-When a creature within 5 feet of you casts a spell, you can use your reaction to make a melee weapon attack against that creature.\n-When you damage a creature that is concentrating on a spell, that creature has disadvantage on the saving throw it makes to maintain its concentration.\n-You have advantage on saving throws against spells cast by creatures within 5 feet of you.","Level Requirement":4},
            {"Name":"Magic Initiate","Description":"Choose a class: bard, cleric, druid, sorcerer, warlock, or wizard. You learn two cantrips of your choice from that class's spell list. In addition, choose one 1st-level spell from that same list. Using this feat, you can cast the chosen 1st-level spell once at its lowest level. You regain the ability to cast it this way when you finish a long rest. Your spellcasting ability for these spells depends on the class you chose: Charisma for bard, sorcerer, and warlock; Wisdom for cleric and druid; or Intelligence for wizard.","Level Requirement":4},
            {"Name":"Martial Adept","Description":"You have martial training that allows you to perform special combat maneuvers. You gain the following benefits: \n-You learn two maneuvers of your choice from among those available to the Battle Master archetype in the fighter class. If a maneuver you use requires your target to make a saving throw to resist the maneuver's effects, the saving throw DC equals 8 + your proficiency bonus + your Strength or Dexterity modifier (your choice).\n-You gain one superiority die, which is a d6 (this die is added to any superiority dice you have from another source). This die is used to fuel your maneuvers. A superiority die is expended when you use it. You regain your expended superiority die when you finish a short or long rest.","Level Requirement":4,"Stat Requirement":"STR 13+ or DEX 13+"},
            {"Name":"Mask of the Wild","Description":"You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.","Level Requirement":4},
            {"Name":"Mobile","Description":"You are exceptionally speedy and agile. You gain the following benefits: \n-Your speed increases by 10 feet.\n-When you use the Dash action, difficult terrain doesn't cost you extra movement on that turn.\n-When you make a melee attack against a creature, you don't provoke opportunity attacks from that creature for the rest of the turn, whether you hit or not.","Level Requirement":4},
            {"Name":"Moderately Armored","Description":"Prerequisite: Proficiency with light armor\nYour proficiency with light armor improves. You gain proficiency with medium armor and shields.","Level Requirement":4,"Stat Requirement":"STR 13+"},
            {"Name":"Mounted Combatant","Description":"You are a dangerous foe to face while mounted. While you are mounted on a creature, you gain the following benefits: \n-You have advantage on melee attack rolls against unmounted creatures that are smaller than your mount.\n-You can force an attack targeted at your mount to target you instead.\n-If your mount is subjected to an effect that allows it to make a Dexterity saving throw to take only half damage, it instead takes no damage if it succeeds on the saving throw, and only half damage if it fails.","Level Requirement":4},
            {"Name":"Observant","Description":"Quick to notice details of your environment, you gain the following benefits: \n-Increase your Intelligence or Wisdom score by 1, to a maximum of 20.\n-If you can see a creature's mouth while it is speaking a language you understand, you can interpret what it's saying by reading its lips.\n-You have a +5 bonus to your passive Wisdom (Perception) and passive Intelligence (Investigation) scores.","Level Requirement":4},
            {"Name":"Polearm Master","Description":"You can keep your enemies at bay with reach weapons and make opportunity attacks when enemies enter your reach. You gain the following benefits: \n-When you take the Attack action and attack with a glaive, halberd, or quarterstaff, you can use a bonus action to make a melee attack with the opposite end of the weapon. This attack uses the same ability modifier as the primary attack. The weapon's damage die for this attack is a d4, and it deals bludgeoning damage.\n-While you are wielding a glaive, halberd, pike, or quarterstaff, other creatures provoke an opportunity attack from you when they enter your reach.","Level Requirement":4,"Stat Requirement":"STR 13+"},
            {"Name":"Resilient","Description":"Choose one ability score. You gain the following benefits: \n-Your chosen ability score increases by 1, to a maximum of 20.\n-You gain proficiency in saving throws using the chosen ability.","Level Requirement":4},
            {"Name":"Ritual Caster","Description":"Prerequisite: Intelligence or Wisdom 13\nYou have learned a number of spells that you can cast as rituals. These spells are written in a ritual book, which you must have in hand while casting one of these spells. You can use an action to cast one of the ritual spells you know, following the normal rules for spellcasting. The spell's normal casting time is extended by 10 minutes when you cast it as a ritual.\nYou acquire a ritual book holding two 1st-level spells of your choice. You must choose your spells from the bard, cleric, druid, sorcerer, warlock, or wizard spell list, and the spells you choose must have the ritual tag. The spells in your ritual book can't be cast except as rituals.\nWhen you find a magic spell that has the ritual tag, you can add it to your ritual book if the spell's level is equal to or less than half your character level (rounded up) and if you can spare the time to decipher and copy it.","Level Requirement":4,"Stat Requirement":"INT 13+ or WIS 13+"},
            {"Name":"Savage Attacker","Description":"Once per turn when you roll damage for a melee weapon attack, you can reroll the weapon's damage dice and use either total.","Level Requirement":4,"Stat Requirement":"STR 13+"},
            {"Name":"Sentry","Description":"You have keen senses and intuition, which allow you to be on the constant lookout for danger. You gain the following benefits: \n-When you roll initiative and have no creatures hostile to you within 5 feet of you, you can act as if you had rolled a 10 on the initiative die.\n-At the start of each of your turns, you can use your action to make a Wisdom (Perception) check to spot any creature that is invisible or hidden within 10 feet of you.\n-While you are asleep, if you start to slumber and have a creature hostile to you within 5 feet of you, they must make a Wisdom saving throw against your passive Wisdom (Perception) score. On a failed save, the creature wakes you up and doesn't gain advantage on attack rolls against you as a result of being hidden from you.","Level Requirement":4},
            {"Name":"Sharpshooter","Description":"You have mastered ranged weapons and can make shots that others find impossible. You gain the following benefits: \n- Attacking at long range doesn't impose disadvantage on your ranged weapon attack rolls.\n-Your ranged weapon attacks ignore half cover and three-quarters cover.\n-Before you make an attack with a ranged weapon that you are proficient with, you can choose to take a -5 penalty to the attack roll. If the attack hits, you add +10 to the attack's damage.","Level Requirement":4,"Stat Requirement":"DEX 13+"},
            {"Name":"Shield Master","Description":"You use your shield not just for protection but also for offense. You gain the following benefits: \n-If you take the Attack action on your turn, you can use a bonus action to try to shove a creature within 5 feet of you with your shield.\n-If you aren't incapacitated, you can add your shield's AC bonus to any Dexterity saving throw you make against an effect that targets only you.\n-If you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you can use your reaction to take no damage if you succeed on the saving throw, interposing your shield between yourself and the source of the effect.","Level Requirement":4,"Stat Requirement":"STR 13+"},
            {"Name":"Sling Master","Description":"You have mastered the use of the sling, gaining the following benefits: \n-You ignore the loading property of slings with which you are proficient.\n-Being within 5 feet of a hostile creature doesn't impose disadvantage on your ranged attack rolls.\n-When you use the Attack action and attack with a one-handed weapon, you can use a bonus action to attack with a sling you are holding.","Level Requirement":4,"Stat Requirement":"DEX 13+"},
            {"Name":"Spell Sniper","Description":"You have learned techniques to enhance your attacks with certain kinds of spells, gaining the following benefits: \n-When you cast a spell that requires you to make an attack roll, the spell's range is doubled.\n-Your ranged spell attacks ignore half cover and three-quarters cover.\n-Before you make an attack with a spell that requires an attack roll, you can choose to take a -5 penalty to the attack roll. If the attack hits, you add +10 to the attack's damage.","Level Requirement":4,"Stat Requirement":"Spellcasting Ability 13+"},
            {"Name":"Tavern Brawler","Description":"Accustomed to rough-and-tumble fighting using whatever weapons happen to be at hand, you gain the following benefits: \n-You are proficient with improvised weapons and unarmed strikes.\n-Your unarmed strike uses a d4 for damage.\n-When you hit a creature with an unarmed strike or an improvised weapon on your turn, you can use a bonus action to attempt to grapple the target.","Level Requirement":4,"Stat Requirement":"STR 13+"},
            {"Name":"Tough","Description":"Your hit point maximum increases by an amount equal to twice your level when you gain this feat. Whenever you gain a level thereafter, your hit point maximum increases by an additional 2 hit points.","Level Requirement":4,"Stat Requirement":"CON 13+"},
            {"Name":"War Caster","Description":"You have practiced casting spells in the midst of combat, learning techniques that grant you the following benefits: \n-You have advantage on Constitution saving throws that you make to maintain your concentration on a spell when you take damage.\n-You can perform the somatic components of spells even when you have weapons or a shield in one or both hands.\n-When a hostile creature's movement provokes an opportunity attack from you, you can use your reaction to cast a spell at the creature, rather than making an opportunity attack. The spell must have a casting time of 1 action and must target only that creature.","Level Requirement":4,"Stat Requirement":"Spellcasting Ability 13+"}, 
            {"Name":"Weapon Master","Description":"You have practiced extensively with a variety of weapons, gaining the following benefits: \n-You gain proficiency with four weapons of your choice.\n-Each of the weapons you choose must be a simple or a martial weapon.","Level Requirement":4,"Stat Requirement":"STR 13+ or DEX 13+"}
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
            self.weapon_prof.append('Simple')
            self.weapon_prof.append('Martial')
            self.armor_train.append('Light')
            self.hpdie = 8
            self.primary_stat = 'DEX'
            self.saving_throws.append('DEX')
            self.saving_throws.append('INT')
            self.tool_prof.append("Thieves' Tools")
            options = ['Acrobatics','Athletics','Deception','Insight','Intimidation','Investigation','Perception','Persuasion','Sleight of Hand','Stealth']
            firstselect = input(f'Select one from {options}.')
            self.skills.append(firstselect)
            options.remove(firstselect)
            secondselect = input(f'Select your second skill from {options}')
            self.skills.append(secondselect)
            options.remove(secondselect)
            thirdselect = input(f'Select your third skill from {options}')
            self.skills.append(thirdselect)
            options.remove(thirdselect)
            fourthselect = input(f'Select your fourth skill from {options}')
            self.skills.append(fourthselect)
        elif mainclass == 'Sorcerer':
            self.weapon_prof.append('Simple')
            self.hpdie = 6
            self.primary_stat = 'CHR'
            self.saving_throws.append('CHR')
            self.saving_throws.append('CON')
            options = ['Arcana','Deception','Insight','Intimidation','Persuasion','Religion']
            firstselect = input(f'Select one from {options}.')
            self.skills.append(firstselect)
            options.remove(firstselect)
            secondselect = input(f'Select your second skill from {options}')
            self.skills.append(secondselect)
        elif mainclass == 'Warlock':
            self.weapon_prof.append('Simple')
            self.armor_train.append('Light')
            self.hpdie = 8
            self.primary_stat = 'CHR'
            self.saving_throws.append('WIS')
            self.saving_throws.append('CHR')
            options = ['Arcana','Deception','History','Intimidation','Investigation','Nature','Religion']
            firstselect = input(f'Select one from {options}.')
            self.skills.append(firstselect)
            options.remove(firstselect)
            secondselect = input(f'Select your second skill from {options}')
            self.skills.append(secondselect)
        elif mainclass == 'Wizard':
            self.weapon_prof.append('Simple')
            self.hpdie = 6
            self.primary_stat = 'INT'
            self.saving_throws.append('INT')
            self.saving_throws.append('WIS')
            options = ['Arcana','History','Insight','Investigation','Medicine','Nature','Religion']
            firstselect = input(f'Select one from {options}.')
            self.skills.append(firstselect)
            options.remove(firstselect)
            secondselect = input(f'Select your second skill from {options}')
            self.skills.append(secondselect)
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

