init python:
    class Game():
        current_item = None
        inventory = [None] * 40
        
        ingredients = {}
        tilesets = {}
        
        # Tools
        
        
        @staticmethod
        def addIngredient(id, item):
            Game.ingredients[id] = item
            
        @staticmethod
        def setItem(index,item):
            Game.inventory[index] = item
            
        @staticmethod
        def addItem(item):
            for i in range(len(Game.inventory)):
                if not Game.inventory[i]:
                    Game.inventory[i] = item
                    return
        
        @staticmethod
        def loadTileset(name, path, sprite_size, tile_counts):
            
            Game.tilesets[name] = []
            
            for x in range(tile_counts[0]):
                Game.tilesets[name].append([])
                
                for y in range(tile_counts[1]):
                    tile = im.Crop(path, (x * sprite_size[0], y * sprite_size[1], sprite_size[0], sprite_size[1]))
                    Game.tilesets[name][x].append(tile)
                    

