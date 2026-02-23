class Combat:    
    from game.mechanic.dice_mechanic import Dice
    def __init__(self,allies,enemies,neutrals=[]):
        self.goodguys = allies
        self.badguys = enemies
        self.neutrals = neutrals
        self.incombat = True
        self.fightsize = len(self.goodguys) + len(self.badguys) + len(self.neutrals)
        self.fightorder = {}
        self.currentturn = 0

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

    def opportunity_attack(self,attacker,target):
        if target.position <= attacker.position + 3:
            attacker.actions['attack']

    def dmg_roll(self,dice=1,side=4,modifier=0):
        dmg = Dice(dice,sides) + modifier
        return dmg

    def atk_roll(self,dice=1,sides=20,modifier=0):
        dice = Dice(dice,sides) 
        if dice == 20:
            # crit hit
            return True
        else:
            atk = dice + modifier
            return atk_value

    def attack(self,target):
        # attack rolls are done with a d20 + modifiers, if the roll is higher than the target's AC then the attack hits.
        # damage rolls are done with a d6 + modifiers, if the roll is higher than the target's HP then the target is dead.
        atk = self.atk_roll()
        if atk > target.ac:
            dmg = self.dmg_roll()
            target.hp -= dmg
        elif atk == True:
            dmg = self.dmg_roll() * 2
            target.hp -= dmg
        else:
            return 'miss'






