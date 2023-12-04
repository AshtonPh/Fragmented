label equipment:
    hide screen inventory_screen
    show inventory with fade
    
    python:
        inventory.list_items()
        narrator("Would you like to adjust your equipment?", interact=False)
        e_choice = renpy.display_menu([("Yes",True), ("No",False)])
        if e_choice:
            narrator("What would you like to adjust?", interact=False)
            e_choice = renpy.display_menu([("Weapon", "weapon"), ("Armor", "armor"), ("Ring", "ring"), ("Necklace", "necklace"), ("Back", "back")])
            if e_choice != "back":
                # Create an empty list to store the tuples
                item_list = []

                # Loop through the inventory
                for item in inventory.__iter__():
                    # Check if the item has the key e_choice in its key value
                    if e_choice in item.key:
                        # Add the item to the list as a tuple with the name and the item itself
                        item_list.append((item.name, item))
                if not item_list:
                    narrator("You have no items of that type.")
                else:
                    e = renpy.display_menu(item_list)
                    equipment.equip(e, e_choice)
            else:
                pass
        else:
            pass   
        
    hide inventory with fade
    show screen inventory_screen
    return