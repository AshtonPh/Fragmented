init python:
    class Inventory():
        def __init__(self, items, no_items):
            self.items = items
            self.no_items = no_items

        # Adding an item to the inventory
        def add_item(self, item):
            self.items.append(item)
            self.no_items += 1

        # Remove an item from the inventory
        def remove_item(self, item):
            self.items.remove(item)
            self.no_items -= 1

        # List all the items in the inventory
        def list_items(self):
            if len(self.items) < 1:
                narrator("You have no items in your inventory.")
            else:
                narrator("You have " + str(len(self.items)) + " items in your inventory:")
                for item in self.items:
                    narrator(f"{item.name} - {item.description} - x{item.count}.")
        
        def list_equipment(self, type):
            e_list = []
            if (type == "armor"):
                for item in self.items:
                    if "armor" in item.key:
                        e_list.append(item)
            elif (type == "weapon"):
                for item in self.items:
                    if "weapon" in item.key:
                        e_list.append(item)
            elif (type == "necklace"):
                for item in self.items:
                    if "necklace" in item.key:
                        e_list.append(item)
            elif (type == "ring"):
                for item in self.items:
                    if "ring" in item.key:
                        e_list.append(item)

                        
                        

                

    class Items():

        # name is the name of the item
        # description is the description of the item
        # count is the number of the item (stackable items only)
        # key is the type of the item, used to identify it
        # value is the value of the effect of the item (if any). For example, a potion of healing would have a value of 10, as it heals 10 health points 

        def __init__(self, name, description, count, key, value):
            self.name = name
            self.description = description
            self.count = count
            self.key = key
            self.value = value

        # Give a description of the item
        def describe(self):
            narrator(self.description)
        
        # Add to the count of the item (stackable items only)
        def add_count(self, count):
            self.count += count

        # Remove from the count of the item (stackable items only)
        def use(self, count):
            self.count -= count


    class Equipment:
        def __init__(self):
            self.armor = None
            self.weapon = None
            self.necklace = None
            self.ring = None

        def equip(self, item, slot):
            if slot == "armor":
                if "armor" in item.key:
                    narrator("You equipped the " + item.name + ".")
                    self.armor = item
                    
                else:
                    narrator("You can't equip that item in that slot.")
            elif slot == "weapon":
                if "weapon" in item.key:
                    self.weapon = item
                    adjust_moveset(item)
                    narrator("You equipped the " + item.name + ".")
                    
                else:
                    narrator("You can't equip that item in that slot.")
                self.weapon = item
            elif slot == "necklace":
                if "necklace" in item.key:
                    narrator("You equipped the " + item.name + ".")
                    self.necklace = item
                else:
                    narrator("You can't equip that item in that slot.")
            elif slot == "ring":
                if "ring" in item.key:
                    narrator("You equipped the " + item.name + ".")
                    self.ring = item
                else:
                    narrator("You can't equip that item in that slot.")
            else:
                narrator("That is not a valid slot.")
            

        def get_value(self, slot):
            if slot == "armor":
                return self.armor
            elif slot == "weapon":
                return self.weapon
            elif slot == "necklace":
                return self.necklace

        
    def adjust_moveset(equipment):
        player_move_set = []
        if equipment == short_sword:
            player_move_set.append(slash)
        if equipment == long_bow:
            player_move_set.append(arrow)
        if equipment == mage_staff:      
            player_move_set.append(smash)
            player_move_set.append(fire_bolt)
            player_move_set.append(heal_self)      

        

    # Stackable items 
    gold = Items("Gold", "Shiny gold coins", 0, "gold", 0)
    arrows = Items("Arrows", "Ammunition of the bow", 0, "arrows", 0)
    minor_health_potion = Items("Minor Health Potion", "A potion that heals a small amount of health", 0, "consumable", 100)



    # Non-stackable items (unique items)
    short_sword = Items("Short Sword", "An old short sword that may still have some uses", 1, "melee_weapon", 90)
    long_bow = Items("Long Bow", "A old long bow that still have some shots left in it", 1, "ranged_weapon", 90)
    mage_staff = Items("Mage's Staff", "An old staff with some basic spells", 1, "magic_weapon", 80)
    hunter_bow = Items("Hunter's Bow", "One of Illyria's many trusty bows", 1, "ranged_weapon", 100)


    # Test equipment
    simple_clothes = Items("Simple Clothes", "Simple clothes that are easy to move in", 1, "simple_armor", 10)
    ring_of_vitality = Items("Ring of Vitality", "A ring that increases your health", 1, "health_ring", 10)
    necklace_of_energy = Items("Necklace of Energy", "A necklace that increases your energy", 1, "energy_necklace", 10)

