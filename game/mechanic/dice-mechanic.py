import random
'''
Each instance of Dice will create a number of die of a certain size, you must generate new instances of dice for each different size of dice (ex 6 sided dice vs 8 sided dice need 2 different Dice)
The "roll" function will roll x(qty) amount of dice of y(sides) size.
'''
class Dice:
    def __init__(self,qty,sides=4) -> None:
        self.qty = qty
        self.sides = sides

    def roll(self):
        value = 0
        for die in range(1,self.qty+1):
            value += random.randint(1,self.sides)
        #     print(value)
        # print(value)
        return value