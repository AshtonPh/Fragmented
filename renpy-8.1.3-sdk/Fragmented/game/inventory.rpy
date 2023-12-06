init python:
    class Inventory():
        def __init__(self, items, no_items):
            self.items = items
            self.no_items = no_items

        # Adding an item to the inventory
        def add_item(self, item):
            if item in self.items:
                pass
            else:
                self.items.append(item)
                self.no_items += 1
                self.check_for_item()

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

        # Make the inventory iterable
        def __iter__(self):
            return iter(self.items)
        
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

        # Empty inventory
        def empty(self):
            self.items.clear()
            self.no_items = 0


        def check_for_item(self):
            for item in self.items: 
                if item.name == "Minor Health Potion" and item.count >= 1 and drink_minor_health_potion not in player_move_set:
                    player_move_set.append(drink_minor_health_potion)
                    pass
                if item.name == "Agility Potion" and item.count >= 1 and drink_agility_potion not in player_move_set:
                    player_move_set.append(drink_agility_potion)
                    pass
                if item.name == "Throwing Knives" and item.count >= 1 and throw_knife not in player_move_set:
                    player_move_set.append(throw_knife)
                    pass
                if item.name == "Standard Health Potion" and item.count >= 1 and drink_standard_health_potion not in player_move_set:
                    player_move_set.append(drink_standard_health_potion)
                    pass
                if item.name == "Greater Elixir" and item.count >= 1 and drink_greater_elixir not in player_move_set:
                    player_move_set.append(drink_greater_elixir)
                    pass
                else:
                    pass
                        
                        

                

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
        
        def update_count(self, count):
            self.count = count 

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

        def list_equipment(self):
            narrator("You have the following equipment:")
            if self.armor != None:
                narrator("Armor: " + self.armor.name)
            if self.weapon != None:
                narrator("Weapon: " + self.weapon.name)
            if self.necklace != None:
                narrator("Necklace: " +self.necklace.name)
            if self.ring != None:
                narrator("Ring: " + self.ring.name)

        def unequip(self, slot):
            if slot == "armor":
                narrator("You unequipped the " + self.armor.name + ".")
                self.armor = None
            elif slot == "weapon":
                narrator("You unequipped the " + self.weapon.name + ".")
                self.weapon = None
                player_move_set.clear()
            elif slot == "necklace":
                narrator("You unequipped the " + self.necklace.name + ".")
                self.necklace = None
            elif slot == "ring":
                narrator("You unequipped the " + self.ring.name + ".")
                self.ring = None
            else:
                narrator("That is not a valid slot.")
        
        def __iter__(self):
            equipment = [self.armor, self.weapon, self.necklace, self.ring]
            return iter(equipment)
        
    def adjust_moveset(equipment):
        player_move_set.clear()
        if equipment == short_sword:
            slash.update_value(equipment.value)
            player_move_set.append(slash)
        if equipment == long_bow:
            arrow.update_value(equipment.value)
            player_move_set.append(arrow)
        if equipment == mage_staff:
            smash.update_value(round(equipment.value/2))
            player_move_set.append(smash)

            fire_bolt.update_value(round(equipment.value * 1.5))
            player_move_set.append(fire_bolt)

            heal_self.update_value(round(equipment.value * 1.5))
            player_move_set.append(heal_self)
        if equipment == hunter_bow:
            arrow.update_value(equipment.value)
            player_move_set.append(arrow)
        if equipment == magic_sword:
            magic_thrust.update_value(equipment.value)
            player_move_set.append(magic_thrust)

            fire_bolt.update_value(round(equipment.value * 1.2))
            player_move_set.append(fire_bolt)
        
        if equipment == arcane_staff:
            smash.update_value(round(equipment.value/2))
            player_move_set.append(smash)

            magic_blast.update_value(round(equipment.value * 1.5))
            player_move_set.append(magic_blast)


        else:
            pass 
        player_move_set.append(unarmed_attack)

        

    # Stackable items 
    gold = Items("Gold", "Shiny gold coins", 0, "gold", 0)
    arrows = Items("Arrows", "Ammunition of the bow", 0, "arrows", 0)
    minor_health_potion = Items("Minor Health Potion", "A potion that heals a small amount of health", 0, "consumable", 100)
    agility_potion = Items("Agility Potion", "Faster than the wind", 0, "consumable", 30)
    throwing_knives = Items("Throwing Knives", "Small but deadly", 0, "consumable", 100)
    standard_health_potion = Items("Standard Health Potion", "A potion that heals a moderate amount of health", 0, "consumable", 300)
    greater_elixir = Items("Greater Elixir", "A potion that heals a large amount of health", 0, "consumable", 800)
    strength_potion = Items("Strength Potion", "A potion that increases your strength two fold", 0, "consumable", 2)

    # Non-stackable items (unique items)
    short_sword = Items("Short Sword", "An old short sword that may still have some uses", 1, "melee_weapon", 90)
    long_bow = Items("Long Bow", "A old long bow that still have some shots left in it", 1, "ranged_weapon", 90)
    mage_staff = Items("Mage's Staff", "An old staff with some basic spells", 1, "magic_weapon", 80)
    hunter_bow = Items("Hunter's Bow", "One of Illyria's many trusty bows", 1, "ranged_weapon", 100)
    magic_sword = Items("Magic Sword", "A sword that has been imbued with magic", 1, "melee_weapon", 150)
    arcane_staff = Items("Arcane Staff", "A staff that has been imbued with magic", 1, "magic_weapon", 120) 

    # Test equipment
    simple_clothes = Items("Simple Clothes", "Simple clothes that are easy to move in", 1, "simple_armor", 10)
    ring_of_vitality = Items("Ring of Vitality", "A ring that increases your health", 1, "health_ring", 10)
    necklace_of_energy = Items("Necklace of Energy", "A necklace that increases your energy", 1, "energy_necklace", 10)

