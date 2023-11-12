label persist:
    scene black with fade
    $ persistent.timesdied += 1
    $ narrator("You have fallen, but you persist.")
    $ renpy.load("most_recent_save")
