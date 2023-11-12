label initialize_screens:
    python:
        person = None
        
        bar1_currenthp = 1000
        bar1_maxhp = 1000
        bar1_x = 0.1
        bar1_y = 0.7
        bar1_xmaximum = 500
        bar1_name = "Player"

        bar2_currenthp = 500
        bar2_maxhp = 500
        bar2_x = 0.5
        bar2_y = 0.5
        bar2_xmaximum = 250
        bar2_name = "Enemy"

        bar3_currenthp = 500
        bar3_maxhp = 500
        bar3_x = 0.5
        bar3_y = 0.8
        bar3_xmaximum = 250
        bar3_name = "Enemy"

        def change_bar1_values(a, b, c, d, name):
            global bar1_currenthp
            global bar1_maxhp
            global bar1_x
            global bar1_y
            global bar1_xmaximum
            global bar1_name

            bar1_currenthp = a
            bar1_maxhp = b
            bar1_x = c
            bar1_y = d
            bar1_xmaximum = bar1_maxhp / 2
            bar1_name = name
        
        def change_bar2_values(a, b, c, d, name):
            global bar2_currenthp
            global bar2_maxhp
            global bar2_x
            global bar2_y
            global bar2_xmaximum
            global bar2_name

            bar2_currenthp = a
            bar2_maxhp = b
            bar2_x = c
            bar2_y = d
            bar2_xmaximum = bar2_maxhp / 2
            bar2_name = name

        def change_bar3_values(a, b, c, d, name):
            global bar3_currenthp
            global bar3_maxhp
            global bar3_x
            global bar3_y
            global bar3_xmaximum
            global bar3_name

            bar3_currenthp = a
            bar3_maxhp = b
            bar3_x = c
            bar3_y = d
            bar3_xmaximum = bar3_maxhp / 2
            bar3_name = name

    screen bar1:
        tag bar1
        vbox:
            spacing 20
            xalign bar1_x
            yalign bar1_y
            xmaximum 500
            frame:
                text "[bar1_name]: [bar1_currenthp] / [bar1_maxhp]"
            bar value bar1_currenthp range bar1_maxhp

    screen bar2:
        tag bar2
        vbox:
            spacing 20
            xalign bar2_x
            yalign bar2_y
            xmaximum 500
            frame:
                text "[bar2_name]: [bar2_currenthp] / [bar2_maxhp]"
            bar value bar2_currenthp range bar2_maxhp

    screen bar3:
        tag bar3
        vbox:
            spacing 20
            xalign bar3_x
            yalign bar3_y
            xmaximum 500
            frame:
                text "[bar3_name]: [bar3_currenthp] / [bar3_maxhp]"
            bar value bar3_currenthp range bar3_maxhp

    screen display_mana:
        tag display_mana
        frame:
            xalign 0.38
            yalign 0.72
            vbox:
                text "Mana: [person.mana]"

    screen display_arrows:
        tag display_arrows
        frame:
            xalign 0.53
            yalign 0.72
            vbox:
                text "Arrows: [arrow_count]"
