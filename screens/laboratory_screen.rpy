screen LaboratoryMainScreen:
    
    # Left inventory
    frame:
        align(0.05, 0.05)
        padding(10, 10)
        grid 4 5:
            spacing 10
            for i in range(20):
                $item = Game.inventory[i]
                button:
                    if item:
                        action Return(1)
                        hovered SetVariable("Game.current_item", item)
                        unhovered SetVariable("Game.current_item", None)
                    
                        frame:
                            add item.icon
                    else:
                        frame:
                            null width 64 height 64
                    
    
    # Right inventory
    frame:
        align(0.95, 0.05)
        padding(10, 10)
        grid 4 5:
            spacing 10
            for i in range(20):
                $item = Game.inventory[i + 20]
                button:
                    if item:
                        action Return(1)
                        hovered SetVariable("Game.current_item", item)
                        unhovered SetVariable("Game.current_item", None)
                    
                        frame:
                            add item.icon
                    else:
                        frame:
                            null width 64 height 64
    
    # Cauldron
    button:
        align(0.5, 0.5)
        action Return(1)
        add "images/gameplay/cauldron.png"
       
    # Tooltipe
    if Game.current_item:
        use TooltipScreen(Game.current_item)
        
        
screen TooltipScreen(item):
    frame:
        padding(10, 10)
        align(0.5, 0.1)
        xsize 300
        
        hbox:
            null width 10
            add item.icon size(64, 64) yalign 0.5
            null width 10
            vbox:
                text "[item.name]"
                text "Здроровье: [item.health]" size 14
                text "Скорость: [item.speed]" size 14
                text "Разум: [item.mind]" size 14
                text "Сила: [item.power]" size 14
                
        
