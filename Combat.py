class Combat:    
    def __init__(self,allies,enemies,neutrals=[]):
        self.goodguys = allies
        self.badguys = enemies
        self.neutrals = neutrals
        self.incombat = True
        self.fightsize = len(self.goodguys) + len(self.badguys) + len(self.neutrals)
        self.fightorder = {}
        self.currentturn = 1

    def roll_initiative(self):
        dice = Dice()
        dicerolls = {}
        for each in self.goodguys:
            initiative = dice.roll(1,20)
            dicerolls[each] = initiative
        for each in self.badguys:
            initiative = dice.roll(1,20)
            dicerolls[each] = initiative  
        for each in self.neutrals:
            initiative = dice.roll(1,20)
            dicerolls[each] = initiative 
        self.fightorder = dict(sorted(dicerolls.items(),key=lambda item: item[1]))

    def end_turn(self):
        if self.currentturn != self.fightsize:
            self.currentturn += 1
        else:
            self.currentturn = 1

    def opportunity_attack(self,attacker,target):
        if target.position <= attacker.position + 3:
            attacker.actions['attack']
