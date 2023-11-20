init python:
    class Inventory():
        def __init__(self, items, no_items):
            self.items = items
            self.no_items = no_items

        def add_item(self, item):
            self.items.append(item)
            self.no_items += 1

        def remove_item(self, item):
            self.items.remove(item)
            self.no_items -= 1

        def list_items(self):
            if len(self.items) < 1:
                narrator("You have no items in your inventory.")
            else:
                narrator("You have " + str(len(self.items)) + " items in your inventory:")
                for item in self.items:
                    narrator(f"{item.name} - {item.description} - x{item.count}.")
                

    class Items():
        def __init__(self, name, description, count, key, value):
            self.name = name
            self.description = description
            self.count = count
            self.key = key
            self.value = value

        def describe(self):
            narrator(self.description)
        
        def add_count(self, count):
            self.count += count

        def use(self, count):
            self.count -= count

    
    gold = Items("Gold", "Shiny gold coins", 0, "gold", 0)
    arrows = Items("Arrows", "Ammunition of the bow", 0, "arrows", 0)
    
