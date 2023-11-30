label combat:
    hide screen inventory_screen
    python:
        import random
        import time

        player = Character("player", "Player", 1000 + persistent.healthupgrade, 100 + persistent.manaupgrade, 1, player_move_set, 1)
        person = player
        if mana_aware:
            renpy.show_screen("display_mana")
        renpy.show_screen("display_arrows")
        wolf1 = Wolf("wolf1", "Wolf1",100, 50, 2, [enemySlash, bite], 2)
        wolf2 = Wolf("wolf2", "Wolf2",100, 50, 2, [enemySlash, bite], 3)
        spider = Spider("spider", "Spider", 500, 50, 3, [venom], 2)
        bat1 = Bat("bat1", "Bat1", 100, 50, 2, [blood_suck, bite], 2)
        bat2 = Bat("bat2", "Bat2", 100, 50, 2, [blood_suck, bite], 3)

        bandit1 = Bandit("bandit1", "Bandit1", 200, 50, 2, [stab, enemySlash], 2)
        bandit2 = Bandit("bandit2", "Bandit2", 200, 50, 2, [stab, enemySlash], 3)



        
        if combat == "wolf":
            turn = Turn([player, wolf1, wolf2])
        elif combat == "spider":
            turn = Turn([spider, player])
        elif combat == "bats":
            turn = Turn([bat1, bat2, player])
        elif combat == "bandits":
            turn = Turn([bandit1, bandit2, player])

        

        def combat_loop():
            first_load = True
            while True:
                # update the active character
                turn.active()

                # check state for each chracter, if first turn ignore this
                if first_load == True:
                    first_load = False
                else:
                    if turn.check_state() == True:
                        break

                if active_character.name == "player":
                    # narrator("Player turn", interact=False)
                    active_character.pick_move_player()
                    active_character.set_target(turn)
                    active_character.use_move()
                else:
                    # narrator("enemy turn")
                    active_character.pick_move_npc()
                    active_character.set_target(turn)
                    active_character.use_move()

                # check state for each chracter
                if turn.check_state() == True:
                    break
                # print hp totals
                for x in turn.order:
                    # narrator(x.name + " has " + str(x.hp) + " hp remaining.")
                    pass
                # checks to see if any character is dead
                turn.any_dead()
                if player not in turn.order:
                    renpy.hide_screen("bar1")
                    renpy.hide_screen("bar2")
                    renpy.hide_screen("bar3")
                    renpy.hide_screen("display_mana")
                    renpy.hide_screen("display_arrows")
                    renpy.jump("persist")
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
            renpy.hide_screen("display_mana")
            renpy.hide_screen("display_arrows")
            renpy.jump("introduction_ranger")
        elif combat == "spider":
            renpy.hide_screen("bar1")
            renpy.hide_screen("bar2")
            renpy.hide_screen("display_mana")
            renpy.hide_screen("display_arrows")
            renpy.jump("post_spider_fight")
        elif combat == "bats":
            renpy.hide_screen("bar1")
            renpy.hide_screen("bar2")
            renpy.hide_screen("bar3")
            renpy.hide_screen("display_mana")
            renpy.hide_screen("display_arrows")
            renpy.jump("castle_gates")
        elif combat == "bandits":
            renpy.hide_screen("bar1")
            renpy.hide_screen("bar2")
            renpy.hide_screen("bar3")
            renpy.hide_screen("display_mana")
            renpy.hide_screen("display_arrows")
            renpy.jump("bandit_aftermath")
    
    show screen inventory_screen