class Character():
    def __init__(self,name):
        self.name = name
        self.hp = 25   

    # ability/skills related code
    def gainAbility(self):
        pass

    def move(self):
        pass

    def interact(self):
        pass

    def updateHealth(self,amount:int):
        self.hp += amount

    def updateMana(self):
        pass

    def levelUp(self):
        pass

    def death(self):
        pass

    def revive(self):
        


jon = Character('Jon')
print(jon.hp)