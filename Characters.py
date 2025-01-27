class Enemy:
    def __init__(self,image,hp=0,armor=0,mr=0,atk=0) -> None:
        self.image = image
        self.movement = 30
        self.hp = hp
        self.armor = armor
        self.mr = mr
        self.atk = atk
        self.skills = []
        self.spells = []
        self.actions = ['Move','Attack','Jump','Sprint','Shove','Disengage']
        

    def attack(self,target):
        attack = self.atk - target.defense
        target.hp = target.hp - attack