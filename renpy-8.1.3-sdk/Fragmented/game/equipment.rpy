label equipment:
    hide screen my_screen
    show inventory with fade
    
    python:
        inventory.list_items()
        narrator("Would you like to adjust your equipment?", interact=False)
        e_choice = renpy.display_menu([("Yes",True), ("No",False)])
        if e_choice:
            narrator("What would you like to adjust?", interact=False)
            e_choice = renpy.display_menu([("Weapon", "weapon"), ("Armor", "armor"), ("Ring", "ring"), ("Necklace", "necklace"), ("Back", "back")])
            if e_choice != "back":
                e = renpy.display_menu(inventory.list_equipment(e_choice))
                equipment.equip(e.name, e_choice)
        else:
            pass   
        
    hide inventory with fade
    show screen my_screen
    return