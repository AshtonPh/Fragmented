define mc = Character("????")
define duchess = Character("The Duchess", color = "#d71542ee")

label journey_to_castle:
    scene snowy_path
    with fade

    "You decide it's time to part ways with Illyria and head towards the castle that looms in the distance. The path is treacherous, and the snow grows deeper with every step."

    "The castle, a silhouette against the grey sky, stands as a testament to a time before the alchemist's curse. Its towers now appear as jagged teeth against the horizon."

    "As you trudge through the snow, the quiet is unsettling. The only sound is the crunch of your footsteps and the occasional distant howl."

    "Suddenly, a flurry of movement catches your eye. Shadows flit through the air, silent but for the whisper of wings."
    
    show bat1 at my_left
    with fade
    show bat2 at my_right
    with fade

    "A group of bats, their eyes glowing with an unnatural hue, descend upon you. They're not ordinary bats; their size and the malice in their eyes speak of the alchemist's touch."



    "You ready your weapon, knowing that the path to answers lies beyond these twisted creatures."


    jump bats_combat

label bats_combat:
    

    play music "combat.ogg" loop
    "You engage in a fierce battle with the creatures. Your every move is a dance between life and death."

    

    $ combat = "bats"

    $ change_bar1_values(player.maxhp, player.maxhp, 0.1, 0.7, "Player")
    $ change_bar2_values(100, 100, 0.2, 0.0, "Bat1")
    $ change_bar3_values(100, 100, 0.7, 0.0, "Bat2")
    show screen bar1
    show screen bar2
    show screen bar3
    jump combat



label castle_gates:
    scene castle_exterior
    with fade
    play music "ambient.ogg" loop

    "With the bats defeated, you continue on your path to the castle, wary of what other horrors the alchemist's curse has spawned."

    "The gates of the castle loom before you, the ironwork twisted and the wood splintered. It's clear that few have entered here since the curse took hold."

    "You push open the gates, their creaking groan echoing through the empty courtyard beyond."

    "Stepping inside, you wonder what awaits you in the heart of this once-great stronghold."

    jump duchess_encounter

label duchess_encounter:
    scene throne_room
    with fade

    "The throne room is vast, the high ceilings lost in shadows. At the far end, upon a throne that has seen better days, sits the duchess."

    show duchess

    "Her gaze is weary but determined, and she rises as you approach."
    "She has dark emerald eyes that are fierce– piercing even– but with a touch of softness."
    "She looks to be around her late 50’s, still beautiful and regal, but time and stress are beginning to leave their mark on her face." 
    "She steps down towards you, and her dark mahogany dress seems to glimmer and sparkle as she makes her way to face you." 
    "As she gets closer, her presence draws warmth and light to the room, making you feel as if you’re finally home. "

    duchess " 'So, another survivor braves the wilderness to seek my audience. Speak, what brings you to my crumbling court?'"

    mc "‘I awoke on an altar not far from here with no memory of who I am or where I came from. All that I can remember is something about an alchemist and his connection to the creatures that roam the dark. What happened here?’"

    "The throne room, once a symbol of regal authority, now stands as a hollow echo of its former glory. The duchess begins to unravel the tale of her land's downfall."

    duchess " 'It began as a time of prosperity. Our lands were fertile, and our people happy. But in our midst, a darkness grew, one we did not recognize until it was too late.'"

    "She pauses, her eyes reflecting the flicker of torchlight, shadows dancing across her face."

    duchess " 'The alchemist, once a man of science and a friend to the crown, delved into forbidden arts. His obsession with eternal life twisted his mind and soul.'"

    menu:
        "What exactly did the alchemist do?":
            duchess " 'He experimented with the very essence of life, blending alchemy and dark magic. He promised miracles: crops that would never wither, loved ones returned from the grip of death.'"
            duchess " 'But with each experiment, the land began to wither, and the dead returned not as themselves but as twisted aberrations.'"

        "How did it affect your people?":
            duchess " 'At first, it was subtle. A blight here, a strange illness there. But soon, our children began to vanish, and creatures of nightmare prowled in the dark.'"
            duchess " 'Families were torn apart, not just by loss, but by the monstrosities that some of their loved ones became.'"

        "Why didn't anyone stop him sooner?":
            duchess " 'Pride and greed blinded us. The promise of power, of defying death itself—it was too alluring. By the time we realized the truth, it was too late.'"

    "The duchess stands, her silhouette a stark contrast against the vast emptiness of the room."

    duchess " 'I sent my husband, the duke, with a contingent of our best knights to confront the alchemist. They have yet to return. I was left to mourn and to rule over a dying land.'"

    menu:
        "Tell me about the duke and your knights.":
            duchess " 'They were brave and noble, the finest this duchy had to offer. Their loyalty was unwavering, their courage unassailable.'"
            duchess " 'But against the alchemist's dark creations, even they stood little chance. They are presumed perished, though their bodies were never recovered.'"

        "What happened to the alchemist?":
            duchess " 'Some say he achieved his goal and became an immortal being, a lich, perhaps. Others believe his creations turned on him and destroyed him.'"
            duchess " 'But his legacy of horror remains, a curse upon the land that was once his home.'"

        "Is there any way to reverse what's been done?":
            duchess " 'There surely must be some information left in the tatters of the alchemist’s lair– one can feel the dark energy radiate from deep within it from leagues away. But I would imagine anything of import is hidden, and many dangers lie between us and it.'"

    "The duchess's gaze meets yours, a silent plea for help that needs no words."

    duchess " 'You are not the first to come seeking answers, nor, I fear, will you be the last. But if you have the will to brave the perils, I will tell you all I know.'"

    "Tell me more about the alchemist’s lair."            
    duchess " 'It is deep in the foothills, among the most dangerous and dense concentration of the aberrations. You could try to explore it on your own, but if you’d like assistance, I know that the alchemist’s assistant now lives in the nearest village swallowing his sorrows in the tavern.’"
    duchess " ‘I don’t blame him for helping the alchemist– all of us were blinded by greed and tricked by his silver tongue. I’ve known the boy since he lost his mother, and he would never seek to harm the duchy or its people. The townspeople, however, hold him in much lower regard. He is shunned and blamed for the deaths of their children, so he mostly keeps to himself and his drink.'"

    jump duchess_options

label duchess_options:
  
    "The duchess watches you with a mixture of hope and resignation, a silent testament to the suffering of her people and the land."
    return
