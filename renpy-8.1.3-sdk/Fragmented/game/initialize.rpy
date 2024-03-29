﻿label initialize:
    python:
        import random

        class Character():
            def __init__(self, name, label, hp, mana, friend_code, moveset, healthbarnumber):
                self.name = name
                self.label = label
                self.hp = hp
                self.maxhp = hp
                self.moveset = moveset
                self.mana = mana
                self.friend_code = friend_code
                self.healthbarnumber = healthbarnumber
            def append_move(self, move):
                self.moveset.append(move)
            def empty_moveset(self):
                self.moveset = []
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
                """
                tempString = "Available Moves: "
                for i in self.moveset:
                    tempString += i.name + " "
                narrator(tempString)
                """

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
            def __init__(self, name, label, hp, mana, friend_code, moveset, healthbarnumber):
                super().__init__(name, label, hp, mana, friend_code, moveset, healthbarnumber)
            def set_target(self, turn_system):
                if self.name != "player":
                    for i in turn_system.order:
                        if i.name == "player":
                            self.target_character = i
            def check(self, turn_order):
                if len(turn_order) <= 2:
                    narrator("Suddenly, the wolf leaps towards you, jaw wide open ready to rip out your throat. {i}Click to continue...{/i}")
                    return True
                return False

        
        class Spider(Character):
            def __init__(self, name, label, hp, mana, friend_code, moveset, healthbarnumber):
                super().__init__(name, label, hp, mana, friend_code, moveset, healthbarnumber)
            def set_target(self, turn_system):
                if self.name != "player":
                    for i in turn_system.order:
                        if i.name == "player":
                            self.target_character = i


        class Bat(Character):
            def __init__(self, name, label, hp, mana, friend_code, moveset, healthbarnumber):
                super().__init__(name, label, hp, mana, friend_code, moveset, healthbarnumber)
            def set_target(self, turn_system):
                if self.name != "player":
                    for i in turn_system.order:
                        if i.name == "player":
                            self.target_character = i

        class Bandit(Character):
            def __init__(self, name, label, hp, mana, friend_code, moveset, healthbarnumber):
                super().__init__(name, label, hp, mana, friend_code, moveset, healthbarnumber)
            def set_target(self, turn_system):
                if self.name != "player":
                    for i in turn_system.order:
                        if i.name == "player":
                            self.target_character = i

        class Monster(Character):
            def __init__(self, name, label, hp, mana, friend_code, moveset, healthbarnumber):
                super().__init__(name, label, hp, mana, friend_code, moveset, healthbarnumber)
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
                    narrator("Move Fails, Not Enough Mana" + "{w=0.5}{nw}")
                else:
                    narrator(active_character.name + " uses " + active_character.selected_move.name + " on " + active_character.target_character.name + "{w=0.5}{nw}")
                    target.hp = target.hp - self.value
                    active_character.mana -= self.mana
                    renpy.show_screen("bar1")
                    renpy.with_statement(vpunch)
            def update_value(self, new_value):
                self.value = new_value

        class Arrow(Move):
            def __init__(self, name, label, value, mana, type):
                super().__init__(name, label, value, mana, type)
            def use_move(self, target):
                global active_character
                arrow_count = arrows.count
                if active_character.mana < self.mana:
                    narrator("Move Fails, Not Enough Mana" + "{w=0.5}{nw}")
                if arrow_count <= 0:
                    narrator("Move Fails, Out of Arrows" + "{w=0.5}{nw}")
                else:
                    narrator(active_character.name + " uses " + active_character.selected_move.name + " on " + active_character.target_character.name + "{w=0.5}{nw}")
                    target.hp = target.hp - self.value
                    renpy.show_screen("bar1")
                    renpy.with_statement(vpunch)
                    arrows.use(1)
            def update_value(self, new_value):
                self.value = new_value

        class Bloodsuck(Move):
            def __init__(self, name, label, value, mana, type):
                super().__init__(name, label, value, mana, type)
            def use_move(self, target):
                global active_character
                if active_character.mana < self.mana:
                    narrator("Move Fails, Not Enough Mana" + "{w=0.5}{nw}")
                else:
                    narrator(active_character.name + " uses " + active_character.selected_move.name + " on " + active_character.target_character.name + "{w=0.5}{nw}")
                    active_character.mana -= self.mana
                    target.hp = target.hp - self.value
                    if (active_character.hp + self.value > active_character.maxhp):
                        active_character.hp = active_character.maxhp
                    else:
                        active_character.hp = active_character.hp + self.value

        class Heal(Move):
            def __init__(self, name, label, value, mana, type):
                super().__init__(name, label, value, mana, type)
            def use_move(self, target):
                global active_character
                if active_character.mana < self.mana:
                    narrator("Move Fails, Not Enough Mana" + "{w=0.5}{nw}")
                else:
                    narrator(active_character.name + " uses " + active_character.selected_move.name + " on " + active_character.target_character.name + "{w=0.5}{nw}")
                    active_character.mana -= self.mana
                    if (target.hp + self.value > target.maxhp):
                        target.hp = target.maxhp
                    else:
                        target.hp = target.hp + self.value
            def update_value(self, new_value):
                self.value = new_value
        
        class Health_potion(Move):
            def __init__(self, name, label, value, mana, type):
                super().__init__(name, label, value, mana, type)
            def use_move(self, target):
                global active_character

                narrator("You healed for " + str(self.value) + " health" )
                if (target.hp + self.value > target.maxhp):
                    target.hp = target.maxhp
                else:
                    target.hp = target.hp + self.value
                
                # loop through inventory and use the item matching name with self.cost
                for i in inventory.__iter__():
                    if i.name == self.mana.name:
                        i.use(1)
                        break
                if (self.mana.count <= 0):
                    for i in player.moveset:
                        if i.name == self.mana.name:
                            player.moveset.remove(i)
                            break
            def update_value(self, new_value):
                self.value = new_value

        class Agility_potion(Move):
            def __init__(self, name, label, value, mana, type):
                super().__init__(name, label, value, mana, type)
            def use_move(self, target):
                global active_character
                global agile
                global counter
                agile = True
                counter = 2
                agility_potion.use(1)
                if (agility_potion.count <= 0):
                    # Remove drink_agility_potion from player's moveset 
                    for i in player.moveset:
                        if i.name == "agility potion":
                            player.moveset.remove(i)
                            break
            def update_value(self, new_value):
                self.value = new_value
        
        class Strength_potion(Move):
            def __init__(self, name, label, value, mana, type):
                super().__init__(name, label, value, mana, type)
            def use_move(self, target):
                global active_character
                
                global strength
                for i in player.moveset:
                    if isinstance(i, Attack):
                        i.update_value(round(i.value *2))
                strength = True
                strengh_potion.use(1)
                if (strenth_potion.count <= 0):
                    # Remove drink_agility_potion from player's moveset 
                    for i in player.moveset:
                        if i.name == "strength potion":
                            player.moveset.remove(i)
                            break
            def update_value(self, new_value):
                self.value = new_value

        class Use_item(Move):
            def __init__(self, name, label, value, mana, type):
                super().__init__(name, label, value, mana, type)
            def use_move(self, target):
                global active_character
                
        class Throw_knife(Move):
            def __init__(self, name, label, value, mana, type):
                super().__init__(name, label, value, mana, type)
            def use_move(self, target):
                global active_character
                
                target.hp = target.hp - self.value
                
                throwing_knives.use(1)
                if (throwing_knives <= 0):
                    # Remove drink_minor_health_potion from player's moveset 
                    for i in player.moveset:
                        if i.name == "throw knife":
                            player.moveset.remove(i)
                            break
            def update_value(self, new_value):
                self.value = new_value        

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
                        # narrator(x.name + " is defeated")
                        self.order.remove(x)
                        if  (x.name != "player"):
                            renpy.hide(x.name)
                            renpy.with_statement(dissolve, always=False)
                        if (x.healthbarnumber == 1):
                            renpy.hide_screen("bar1")
                            renpy.with_statement(dissolve, always=False)
                        if (x.healthbarnumber == 2):
                            renpy.hide_screen("bar2")
                            renpy.with_statement(dissolve, always=False)
                        if (x.healthbarnumber == 3):
                            renpy.hide_screen("bar3")
                            renpy.with_statement(dissolve, always=False)
                        
            def check_state(self):
                global bar1_currenthp
                global bar1_maxhp
                global bar2_currenthp
                global bar2_maxhp
                global bar3_currenthp
                global bar3_maxhp

                # health bar updates
                for x in self.order:
                    if (x.healthbarnumber == 1):
                        if x.hp <= 0:
                            bar1_currenthp = 0
                        else:
                            bar1_currenthp = x.hp
                    if (x.healthbarnumber == 2):
                        if x.hp <= 0:
                            bar2_currenthp = 0
                        else:
                            bar2_currenthp = x.hp
                    if (x.healthbarnumber == 3):
                        if x.hp <= 0:
                            bar3_currenthp = 0
                        else:
                            bar3_currenthp = x.hp
                renpy.pause(0.5)

                # checks to see if the combat loop needs to break
                for x in self.order:
                    temp = x.check(self.order)
                    if temp:
                        return True
                return False

        unarmed_attack = Attack("unarmed", "Unarmed attack", 25 + persistent.damageupgrade, 0, "enemy")
        slash = Attack("slash", "Slash", 90 + persistent.damageupgrade , 0, "enemy")
        enemySlash = Attack("slash", "Slash", 90, 0, "enemy")
        arrow = Arrow("arrow", "Arrow", 90 + persistent.damageupgrade, 0, "enemy")
        bite = Attack("bite", "Bite", 20, 0, "enemy")
        smash = Attack("smash", "Smash", 20 + persistent.damageupgrade, 0, "enemy")
        fire_bolt = Attack("fire bolt", "Fire Bolt", 80 + persistent.damageupgrade, 30, "enemy")
        venom = Attack("venom", "Venom", 150, 0, "enemy")
        heal_limb = Heal("heal limb", "Heal Limb", 20, 0, "friendly")
        heal_self = Heal("heal self", "Heal Self", 150, 50, "self")
        blood_suck = Bloodsuck("blood suck", "Blood Suck", 50, 10, "enemy")
        stab = Attack("stab", "Stab", 100, 0, "enemy")
        drink_minor_health_potion = Health_potion("Minor Health Potion", "Drink Minor Health Potion", 100, minor_health_potion, "self")
        drink_standard_health_potion = Health_potion("Standard Health Potion", "Drink Standard Health Potion", 300, standard_health_potion, "self")
        drink_greater_elixir = Health_potion("Greater Elixir", "Drink Greater Elixir", 800, greater_elixir, "self")
        drink_agility_potion = Agility_potion("agility potion", "Drink Agility Potion", 0, 0, "self")
        throw_knife = Throw_knife("throw knife", "Throw Knife", 125 + persistent.damageupgrade, 0, "enemy")
        drink_strength_potion = Strength_potion("strength potion", "Drink Strength Potion", 0, 0, "self")
        magic_thrust = Attack("Magic thrust", "Magic Thrust", 100 + persistent.damageupgrade, 0, "enemy")
        magic_blast = Attack("Magic blast", "Magic Blast", 200 + persistent.damageupgrade, 15 , "enemy")

        suck = Attack("Suck", "Suck", 69, 10, "enemy")
        blow = Attack("Lick", "Lick", 420, 0, "enemy")
        #player = Character("player", "Player",1000, 100, 1, player_move_set, 1)

        enemyMagicBlast = Attack("Magic blast", "Magic Blast", 200, 15 , "enemy")
    return