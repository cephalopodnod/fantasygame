class Barbarian_NPC:
    def __init__(self):
        self.name = 'enter_barbarians_name'
        self.stats = {"STR": 16, "DEX": 14, "CON": 15, "INT": 8, "WIS": 10, "CHA": 12}
        self.hp = 8
        self.mp = 0
        self.ac = 10
        self.level = 1
        self.xp = 0
        self.armor = {"head": None, "chest": None, "belt": None, "legs": None, "feet": None, "hands": None, "neck": None, "ring1": None, "ring2": None, "mainhand": None, "offhand": None}
        self.inventory = []
        self.position = (0, 0)
        self.age = 0
        self.height = 0
        self.max_carryweight =  100 + 2 * self.stats["STR"]
        self.carryweight = 0
        self.speed = 30
        self.spells = []
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
        self.proficiencies = ['Light Armor','Medium Armor','Shields','Simple Weapons','Martial Weapons','Intimidation','Athletics']
        self.savingthrowproficiency = ['STR','CON']