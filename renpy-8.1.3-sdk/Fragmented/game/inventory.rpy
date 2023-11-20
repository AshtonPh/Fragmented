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

    # Stackable items 
    gold = Items("Gold", "Shiny gold coins", 0, "gold", 0)
    arrows = Items("Arrows", "Ammunition of the bow", 0, "arrows", 0)



    # Non-stackable items (unique items)
    short_sword = Items("Short Sword", "A short sword", 0, "short_sword", 0)
