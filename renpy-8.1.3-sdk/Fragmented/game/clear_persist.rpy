label clear_persistant:
    menu:
        "Are you sure you want to clear persistant data?"
        "Yes":
            $ persistent.timesdied = 0
            $ persistent.healthupgrade = 0
            $ persistent.damageupgrade = 0
            $ persistent.manaupgrade = 0
            $ persistent.upgradecounter = 0
            $ persistent.tutorial = True
            "Persistant data has been cleared."
        "No":
            pass
    
    $ bullshit = True
    $ renpy.set_return_stack([])
    $ MainMenu()