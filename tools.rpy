init 1 python:
    class Tool():
        potion = None
            
        def reset(self):
            self.potion = Potion(0, 0, 0, 0)
            self.potion.icon = Game.tilesets["ingredients"][1][1]
        
        def getPotion(self):
            potion = self.potion
            self.reset()
            return potion
        
    class Cauldron(Tool):
        def __init__(self):
            self.reset()
        
        def addIngredient(item):
            self.potion.power += item.power
            self.potion.speed += item.speed
            self.potion.health += item.health
            self.potion.mind += item.mind
        
