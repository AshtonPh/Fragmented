label combat:
    python:
        import random

        player = Character("player", "Player",1000, 50, 1, player_move_set, 1)
        wolf1 = Wolf("wolf1", "Wolf1",100, 50, 2, [slash, bite], 2)
        wolf2 = Wolf("wolf2", "Wolf2",100, 50, 2, [slash, bite, bite], 3)
        spider = Spider("spider", "Spider", 500, 50, 3, [venom], 2)
        bat1 = Bat("bat1", "Bat1", 100, 50, 2, [blood_suck, bite], 2)
        bat2 = Bat("bat2", "Bat2", 100, 50, 2, [blood_suck, bite], 3)

        
        if combat == "wolf":
            turn = Turn([wolf1, wolf2, player])
        elif combat == "spider":
            turn = Turn([spider, player])
        elif combat == "bats":
            turn = Turn([bat1, bat2, player])
        

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
                if turn.check_state() == True:
                    break
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
        if combat == "wolf":
            renpy.hide_screen("bar1")
            renpy.hide_screen("bar2")
            renpy.hide_screen("bar3")
            renpy.jump("introduction_ranger")
        elif combat == "spider":
            renpy.hide_screen("bar1")
            renpy.hide_screen("bar2")
            renpy.jump("post_spider_fight")
        elif combat == "bats":
            renpy.hide_screen("bar1")
            renpy.hide_screen("bar2")
            renpy.hide_screen("bar3")
            renpy.jump("castle_gates")

                
    