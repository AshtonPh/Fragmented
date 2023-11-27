label equipment:
    show inventory with fade
    hide screen my_screen
    python:
        inventory.list_items()
        #narrator("You are armed with the" + equipment.get_value("weapon"))
        
    hide inventory with fade
    show screen my_screen
    return