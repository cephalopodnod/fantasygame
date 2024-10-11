class Character:
    def __init__(self):
        pass     

    # item related code
    def useItem(self,item,target):
        pass
        

    def addItem(self,item,amount=1):
        pass

    def removeItem(self,item,amount=1):
        pass

    def shopItem(self,item,cost,quantitity,buy):
        pass

    def makeKeyItem(self,item):
        pass

    # ability/skills related code
    def gainAbility(self,ability):
        pass

    def move(self):
        pass

    def interact(self,target):
        pass

    def updateHealth(self,amount):
        pass

    def updateMana(self,amount):
        pass

    def levelUp(self):
        pass

    def death(self):
        pass

    def revive(self,toHealth):
        pass