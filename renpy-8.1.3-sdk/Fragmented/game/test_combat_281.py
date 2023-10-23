import random

class Character():
    def __init__(self, name, hp, mana, moveset):
        self.name = name
        self.hp = hp
        self.moveset = moveset
        self.mana = mana
    def append_move(self, move):
        self.moveset.append(move)
    def set_target(self, target):
        self.target_character = target
    def use_move(self):
        if self.selected_move == None:
            pass
        else:
            self.selected_move.use_move(self.target_character)
    def pick_move_player(self):
        tempString = "Available Moves: "
        for i in self.moveset:
            tempString += i.name + " "
        print(tempString)
        print("What move would you like to use?")
        tempInput = input()
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


class Move():
    def __init__(self, name, value, mana):
        self.name = name
        self.value = value
        self.mana = mana

class Attack(Move):
    def __init__(self, name, value, mana):
        super().__init__(name, value, mana)
    def use_move(self, target):
        global active_character
        if active_character.mana < self.mana:
            print("Move Fails, Not Enough Mana")
        else:
            target.hp = target.hp - self.value

class Heal(Move):
    def __init__(self, name, value, mana):
        super().__init__(name, value, mana)
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
                print(x.name + " is defeated")
                self.order.remove(x)
    def check_state(self):
        for x in self.order:
            x.check()

slash = Attack("slash", 10, 0)
bite = Attack("bite", 20, 0)
player = Character("player", 100, 50, [slash, bite])
test_enemy = Character("test_enemy", 100, 50, [slash, bite])
test_enemy2 = Character("test_enemy2", 100, 50, [slash, bite, bite])
turn = Turn([test_enemy, test_enemy2, player])

def combat_loop():
    while True:
        # update the active character
        turn.active()

        if active_character.name == "player":
            print("player turn")
            active_character.pick_move_player()
            active_character.set_target(test_enemy)
            print(active_character.name + " uses " + active_character.selected_move.name + " on " + active_character.target_character.name)
            active_character.use_move()
        else:
            print("enemy turn")
            active_character.pick_move_npc()
            active_character.set_target(player)
            print(active_character.name + " uses " + active_character.selected_move.name + " on " + active_character.target_character.name)
            active_character.use_move()

        # check state for each chracter
        turn.check_state()
        # print hp totals
        for x in turn.order:
            print(x.name + " has " + str(x.hp) + " hp remaining.")
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
