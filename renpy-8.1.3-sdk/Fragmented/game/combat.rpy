label combat:
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
            def check(self):
                pass

        class Wolf(Character):
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
                    x.check()

        slash = Attack("slash", "Slash", 90, 0, "enemy")
        bite = Attack("bite", "Bite", 20, 0, "enemy")
        heal_limb = Heal("heal limb", "Heal Limb", 20, 0, "friendly")
        heal_self = Heal("heal self", "Heal Self", 50, 0, "self")
        player = Character("player", "Player",1000, 50, 1, [slash, bite, heal_limb, heal_self])
        wolf1 = Wolf("wolf1", "Wolf1",100, 50, 2, [slash, bite])
        wolf2 = Wolf("wolf2", "Wolf2",100, 50, 2, [slash, bite, bite])
        turn = Turn([wolf1, wolf2, player])

        def combat_loop():
            while True:
                # update the active character
                turn.active()

                if active_character.name == "player":
                    narrator("Player turn", interact=False)
                    active_character.pick_move_player()
                    active_character.set_target(turn)
                    narrator(active_character.name + " uses " + active_character.selected_move.name + " on " + active_character.target_character.name)
                    active_character.use_move()
                else:
                    narrator("enemy turn")
                    active_character.pick_move_npc()
                    active_character.set_target(turn)
                    narrator(active_character.name + " uses " + active_character.selected_move.name + " on " + active_character.target_character.name)
                    active_character.use_move()

                # check state for each chracter
                turn.check_state()
                # print hp totals
                for x in turn.order:
                    narrator(x.name + " has " + str(x.hp) + " hp remaining.")
                # checks to see if any character is dead
                turn.any_dead()
                if player not in turn.order:
                    "You died, GAME OVER!"
                    break
                elif len(turn.order) == 1 and player in turn.order:
                    "You win!!!"
                    break
                else:
                    pass

                # change the turn
                turn.change_turn()


        combat_loop()
    hide wolf1
    hide wolf2
    jump introduction_ranger