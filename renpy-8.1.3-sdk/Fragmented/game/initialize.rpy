label initialize:
    python:
        import random

        class Character():
            def __init__(self, name, label, hp, mana, friend_code, moveset):
                self.name = name
                self.label = label
                self.hp = hp
                self.moveset = moveset
                self.mana = mana
                self.friend_code = friend_code
            def append_move(self, move):
                self.moveset.append(move)
            def set_target(self, turn_system):
                # if is temp target for enemies, can create other classes that inherit
                # from Character in order to give different behavior to different npcs...
                # ie, see wolf class below

                # else has the full targeting system for the player
                if self.name != "player":
                    for i in turn_system.order:
                        if i.name == "player":
                            self.target_character = i
                else:
                    #Renpy ask and choice menu
                    narrator("Who would you like to target?", interact=False)
                    tempList = []
                    if self.selected_move.type == "enemy":
                        for i in turn_system.order:
                            if i.friend_code != self.friend_code:
                                tempList.append((i.label, i.name))
                    elif self.selected_move.type == "friendly":
                        for i in turn_system.order:
                            if i.friend_code == self.friend_code:
                                tempList.append((i.label, i.name))
                    elif self.selected_move.type == "self":
                        tempList.append((self.label, self.name))

                    tempInput = renpy.display_menu(tempList)

                    for x in turn_system.order:
                        if tempInput == x.name:
                            self.target_character = x

                    # self.target_character = target
            def use_move(self):
                if self.selected_move == None:
                    pass
                else:
                    self.selected_move.use_move(self.target_character)
            def pick_move_player(self):
                tempString = "Available Moves: "
                for i in self.moveset:
                    tempString += i.name + " "
                narrator(tempString)

                #Renpy ask and choice menu
                narrator("What move would you like to use?", interact=False)
                tempList = []
                for i in self.moveset:
                    tempList.append((i.label, i.name))
                tempInput = renpy.display_menu(tempList)

                for x in self.moveset:
                    if tempInput == x.name:
                        self.selected_move = x
                        break
            def pick_move_npc(self):
                if len(self.moveset) == 0:
                    self.selected_move = None  
                else:
                    self.selected_move = random.choice(self.moveset)
            def check(self, turn_order):
                return False

        class Wolf(Character):
            def __init__(self, name, label, hp, mana, friend_code, moveset):
                super().__init__(name, label, hp, mana, friend_code, moveset)
            def set_target(self, turn_system):
                if self.name != "player":
                    for i in turn_system.order:
                        if i.name == "player":
                            self.target_character = i
            def check(self, turn_order):
                if self.hp < 50 and len(turn_order) <= 2:
                    narrator("Suddenly, the wolf leaps towards you, jaw wide open ready to rip out your throat.")
                    return True
                return False

        
        class Spider(Character):
            def __init__(self, name, label, hp, mana, friend_code, moveset):
                super().__init__(name, label, hp, mana, friend_code, moveset)
            def set_target(self, turn_system):
                if self.name != "player":
                    for i in turn_system.order:
                        if i.name == "player":
                            self.target_character = i


        class Move():
            def __init__(self, name, label, value, mana, type):
                self.name = name
                self.label = label
                self.value = value
                self.mana = mana
                self.type = type

        class Attack(Move):
            def __init__(self, name, label, value, mana, type):
                super().__init__(name, label, value, mana, type)
            def use_move(self, target):
                global active_character
                if active_character.mana < self.mana:
                    print("Move Fails, Not Enough Mana")
                else:
                    target.hp = target.hp - self.value

        class Heal(Move):
            def __init__(self, name, label, value, mana, type):
                super().__init__(name, label, value, mana, type)
            def use_move(self, target):
                global active_character
                if active_character.mana < self.mana:
                    print("Move Fails, Not Enough Mana")
                else:
                    target.hp = target.hp + self.value

        class Turn():
            def __init__(self, order):
                self.order = order
                self.end = False
            def change_turn(self): #change_turn written by ChatGPT 3.5
                if len(self.order) <= 1:
                    # No need to shift for lists with 0 or 1 elements
                    pass
                else:
                    # Store the first element in a temporary variable
                    first_element = self.order[0]

                    # Loop through the list and shift each element to the left
                    for i in range(len(self.order) - 1):
                        self.order[i] = self.order[i + 1]

                    # Assign the first element to the last position
                    self.order[-1] = first_element
            def active(self):
                global active_character
                active_character = self.order[0]
            def target(self, target):
                self.target = target
            def any_dead(self):
                for x in self.order:
                    if x.hp <= 0:
                        narrator(x.name + " is defeated")
                        self.order.remove(x)
                        if  (x.name != "player"):
                            renpy.hide(x.name.lower())
                        
            def check_state(self):
                for x in self.order:
                    temp = x.check(self.order)
                    if temp:
                        return True
                return False


        slash = Attack("slash", "Slash", 90, 0, "enemy")
        arrow = Attack("arrow", "Arrow", 90, 0, "enemy")
        bite = Attack("bite", "Bite", 20, 0, "enemy")
        fire_bolt = Attack("fire bolt", "Fire Bolt", 90, 0, "enemy")
        venom = Attack("venom", "Venom", 150, 0, "enemy")
        heal_limb = Heal("heal limb", "Heal Limb", 20, 0, "friendly")
        heal_self = Heal("heal self", "Heal Self", 50, 0, "self")

        player_move_set = []

    return