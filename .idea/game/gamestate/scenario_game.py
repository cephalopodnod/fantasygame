class Event:
    def __init__(self,reward=[]):
        self.state = True
        self.reward = []

    def complete(self,character):
        self.state = False
        for item in self.reward:
            character.inventory.appened(item)
