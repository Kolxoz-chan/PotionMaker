init python:
    Game.loadTileset("ingredients", "images/gameplay/ingredients.png", (64, 64), (10, 10))
    
    # Loading ingredients
    Game.addIngredient("ING_ROMASHKA", Ingredient("Ромашка", Game.tilesets["ingredients"][0][0], 1, 1, 0, 0))
    
    # Inventory filling
    Game.addItem(Game.ingredients["ING_ROMASHKA"])
    Game.addItem(Game.ingredients["ING_ROMASHKA"])
    Game.addItem(Game.ingredients["ING_ROMASHKA"])
 
init:
    image blue = "#077"

label start:

    scene blue
    call screen LaboratoryMainScreen
    
    "Добавьте сюжет, изображения и музыку и отправьте её в мир!"

    return
