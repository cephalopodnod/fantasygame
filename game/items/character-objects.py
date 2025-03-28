class Item:
    def __init__(self, name, use, consumable, image, statsEffected={}, cost=0):
        self.name = name                    #str
        self.use = use                      #str
        self.consumable = consumable        #bool
        self.statsEffected = statsEffected  #dict
        self.cost = cost                    #int
        self.image = image                  #image
        
    def setEffect(self, effect):
        self.use = effect

    def applyStatChange(self, stat, qty):
        tempDict = {stat:qty}
        self.statsEffected.update(tempDict)

    def setCost(self, cost):
        self.cost = cost

class Equipment:
    def __init__(self, name, equip_type, image):
        self.name = name
        self.type = equip_type
        self.stats = {}
        self.bonus_trait = {}
        self.iamge = image
    
    def setArmorStats(self, armor=0, mr=0, dodge=0, bonus={}):
        self.stats = {"armor":armor,"magic_resist":mr,"dodge_chance":dodge}
        self.bonus_trait = bonus

    def setWeaponStats(self, atk=0, crit=0, bonus={}):
        self.stats = {'atk':atk,'crit_chance':crit}
        self.bonus_trait = bonus

    def setOffHandStats(self, stats={}, bonus={}):
        self.stats = stats
        self.bonus_trait = bonus
    
class Consumable:
    def __int__(self, name, stat='', increase=0):
        self.name = name
        self.stat = stat
        self.increase = increase

class Armor:
    def __init__(self, name, position, type, armor=0, mr=0, bonus={}):
        self.name = name
        self.slot = position
        self.type = type
        self.stats = {'Armor':armor,'Magic Resist':mr}
        self.bonus_trait = bonus

class Weapon:
    ONEHAND_WEAPON_TYPES = ['sword',]
    
    def __init__(self, type, hands=1, damage=0, atkspd=0, bonus={}):
        self.type = type
        self.hands = hands
        self.stats = {'Damage':damage,'Attack Speed':atkspd}
        self.bonus_trait = bonus        

class OffHand:
    '''
    brace -> enhance melee 2 hander
    shield -> 1 hand defensive with 1 hand melee or caster
    ammo -> enhances ranged weapon
    bauble -> enhances mage with 1 hand melee or caster
    off-hand -> enhance melee with 1 hand melee or caster
    '''
    OFFHAND_TYPES = ['brace','shield','ammo','bauble','off-hand']
    
    def __init__(self, type, stats={}, bonus={}):
        self.type = type
        self.stats = stats
        self.bonus_trait = bonus   

