"""
Stats:
    - ATK: attack
    - ARM: armor
    - MR: magic resist
    - MAG: magic attack
    - HP: health
    - MP: mana
    - CRT: critical chance


"""

class BlackMage:
    # gains skills by visiting elemental shrines. 
    def __init__(self):
        self.spec = 'Elemental Mage'
        self.main_stat = 'MAG'
        self.secondary_stat = 'MP'
        self.skills = {1:"fire",3:"water",5:"air",6:"ice",6:"lightning",7:"earth",9:"dark",11:"light",13:"decrepify",15:"arefire",16:"arewater",17:"areair",18:"areice",19:"arelightning",20:"areearth",25:"aredark",25:"arelight",25:"aredecrepify",30:"meteor",40:"cosmic storm",50:"armageddon"}

class WhiteMage:
    # gains skills through visiting healers.
    def __init__(self):
        self.spec = 'Healer Mage'
        self.main_stat = 'MP'
        self.secondary_stat = 'MAG'
        self.skills = {1:"heal",3:"pray",5:"depoison",7:"condem",9:"deblind",11:"revive",13:"desilence",15:"banish",16:"seraphim blessing",17:"halo",18:"excercission",19:"angels fury",20:"angels grace",25:"hand of god",30:"epiphany",40:"rebirth",50:"judgement day"}

class RedMage:
    # gains skills through epicrurian digest(must consume blood from certain amount of enemies).
    def __init__(self):
        self.spec = 'Blood Mage'
        self.main_stat = 'HP'
        self.secondary_stat = 'MAG'
        self.skills = {1:"slice",3:"transfuse",5:"drain",7:"hemonalysis",9:"bleed",11:"blood infection",13:"viral perfume",15:"charm",16:"aredrain",17:"arebleed",18:"blood whip",19:"splatter",20:"macabre shield",25:"vengeful whisper",30:"blood twin",40:"become one",50:"blood moon"}

class BlueMage:
    # gains skills by killing creatures that have used the ability.
    def __init__(self):
        self.spec = 'Beast Mage'
        self.main_stat = 'ARM'
        self.secondary_stat = 'MR'
        self.skills = {}

class Hunter:
    # gains skills by leveling and taming creatures.
    def __init__(self):
        self.spec = 'Hunter'
        self.main_stat = 'ATK'
        self.secondary_stat = 'CRT'
        self.skills = {1:"shoot",3:"snare",5:"trap",7:"snipe",9:"tame",15:"beast fury",20:"teamwork",25:"invigoration",35:"call for friends",40:"eagle eye shot",50:"run with the bulls"}

class Pirate:
    # gains skills by collecting tales of sea, collect 'cards' to add special skills in play the cards
    def __init__(self):
        self.spec = 'Pirate'
        self.main_stat = 'CRT'
        self.secondary_stat = 'ATK'
        self.skills = {1:"slice",3:"shoot",5:"sip juice",7:"play the cards",9:"slip into the shadows",12:"shank",15:"stack the deck",17:"turn the tides",20:"rusty coating",25:"ink spray",31:"perfect hand",40:"calypsos rage",50:"leviathan's maelstrom"}

class Jester:
    # gains skills by collecting tales of sea, collect 'cards' to add special skills in play the cards
    def __init__(self):
        self.spec = 'Jester'
        self.main_stat = 'CRT'
        self.secondary_stat = 'MP'
        self.skills = {1:"slice",3:"shoot",5:"sip juice",7:"play the cards",9:"slip into the shadows",12:"shank",15:"stack the deck",17:"turn the tides",20:"rusty coating",25:"ink spray",31:"perfect hand",40:"calypsos rage",50:"leviathan's maelstrom"}
