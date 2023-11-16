define mc = Character("????")
define duchess = Character("The Duchess", color = "#d71542ee")
define sir_henrick = Character("Sir Henrick", color = "#d76c15ee")

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
    "She steps down towards you, and her dark violet dress seems to glimmer and sparkle as she makes her way to face you." 
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

    "The duchess draws closer, her silhouette a stark contrast against the vast emptiness of the room."

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
menu:
    "Tell me more about the alchemist’s lair."            
    duchess " 'It is deep in the foothills, among the most dangerous and dense concentration of the aberrations. You could try to explore it on your own, but if you’d like assistance, I know that the alchemist’s assistant now lives in the nearest village swallowing his sorrows in the tavern.’"
    duchess " ‘I don’t blame him for helping the alchemist– all of us were blinded by greed and tricked by his silver tongue. I’ve known the boy since he lost his mother, and he would never seek to harm the duchy or its people."
     "The townspeople, however, hold him in much lower regard. He is shunned and blamed for the deaths of their children, so he mostly keeps to himself and his drink.'"

    jump duchess_options

label duchess_options:
  
    "The duchess watches you with a mixture of hope and resignation, a silent testament to the suffering of her people and the land."

    menu:
        "Is there anything else I can do to help you or your people?":
            jump offer_help

        "I'll head to the town first. Perhaps the alchemist's assistant can shed more light on this situation.":
            jump visit_town

        "I'm ready to explore the secrets of the alchemist’s lair.":
            jump alchemists_lair


label offer_help:
    duchess " 'Your willingness to aid us is a balm to our weary spirits. Many need help—orphans, wounded, those still fighting against the darkness.'"

    "She gestures to a side door, where her aide awaits."

    duchess " 'Speak with Sir Henrick at the door. He coordinates our efforts and will guide you to where your skills are most needed.'"

    "You nod, turning to the door to seek out Sir Hendrick."

    jump Sir_Hendrick

label visit_town:
    "The duchess nods in approval."

    duchess " 'A wise decision. Knowledge is as powerful a weapon as any blade or spell.’  "

    "She hands you a sealed letter."

    duchess " 'Take this. It bears my seal and will help ensure his cooperation. Be cautious; he is a man driven by fear and guilt.'"

    "You tuck the letter safely into your cloak."
 
    $ seal = True
    jump main_village


label alchemists_lair:
    "A shadow of concern crosses the duchess's face."

    duchess " 'You are brave, indeed. The lair is a place of great evil, a blight upon our land. If you are to go, be prepared for anything.'"

    "She rises, moving to a large, ornate chest. From within, she retrieves a small, crystal vial filled with a swirling, luminescent liquid."

    duchess " 'Take this. It is a potion of clarity. It will protect your mind from the alchemist's dark illusions.'"

    "Gratefully, you accept the vial, feeling its power pulse in your palm."

    $ Potion_of_clarity = True
  
    jump path_to_hell


label Sir_Hendrick:

    scene royal_barrack with fade
    "You approach Sir Henrick, a man whose stern visage is softened by the weariness in his eyes. He stands by the door, a list of tasks clutched in his hand."

    sir_henrick " 'I was told you'd come. We have much to do and too few hands to do it. Here are the pressing matters at hand."
     "We could use help repairing an overrun village; hunting a particularly nasty monster that’s been terrorizing the farmers; or investigating what happened to our most recent supply shipment. '"

    menu:
        "Help fortify the defenses of the Duchy.":
            "Sir Henrick nods solemnly."
            sir_henrick " 'Our walls have suffered from the constant attacks. Your aid in strengthening them could be the difference between life and death for many. A local village has been overrun and some of its walls destroyed. We would’ve just evacuated but there are too many elderly, children, and disabled to be able to move them far away enough to safety. We’ll need you to go help defend and try and rebuild what you can'"
            "He hands you a map and a hammer, and sends you on your way."
            jump fortify_defenses


        "Help with the missing supplies.":
            "Sir Hendrick looks relieved."
            sir_hendrick " 'Your assistance is crucial. The empire seldom responds to our requests for assistance, but their yearly supply delivery was supposed to arrive two weeks ago. Our last confirmation that the supply train was safe was the village before Greenfield– something must have happened to the wagon train on its way to or in Greenfield. We’ll need you to go investigate so that we can find the supplies we desperately need, but the path is overrun with dangers. You'll need to be cautious and swift.'"
            "He hands you a list of the supplies and a small pouch of gold for any expenses."
            "You nod and prepare to leave for Greenfield."
            $ gold += 100 
            jump supply_run_preparation


label fortify_defenses:

    scene village_road with fade
    "The village in need is not far, but time is of the essence."

    "As you study the map, you notice two paths leading to the village. One is the main road, well-traveled and safer, but longer. The other is a shortcut, hastily scratched into the map, promising a quicker route but potentially more dangerous."

    menu:
        "Take the well-traveled path.":
            "Deciding that safety is paramount, especially considering the villagers' plight, you choose the well-traveled path. It may take longer, but the risk of unexpected dangers is less."
            jump arrive_at_village_main_path

        "Take the shortcut.":
            "Time is of the essence, and every moment counts. You decide to take the risk and follow the shortcut, hoping it will save precious time."
            "The shortcut leads you through dense woods and overgrown trails. The silence is eerie, and you can't shake the feeling of being watched."
             "As you exit the forest, ahead of you is a long stretch of snowy plains, the sunset reflecting off of the whiteness and creating a dazzling display of warm colors across the horizon."
            "You consult with your map, and the shortcut goes across the plain and back into another copse of trees."
             "Your steps squeak and crunch as you cross the plains and every rustle of a squirrel or god knows what beneath the snow sends your heart into your throat."
            jump arrive_at_village_shortcut

 label arrive_at_village_shortcut:
    "Leaving the snowy field behind, you step into the dense forest, the shortcut's path barely visible under the overgrowth. The stark contrast between the open, white expanse and the dark, enclosing woods is disorienting."

    "The trees loom overhead, their branches like gnarled hands reaching out to the sky. The silence of the forest is unnerving, broken only by the crunch of your footsteps on the snow-covered ground."

    "As you delve deeper, the light fades, the thick canopy above blocking out the sun. The air grows colder, and a sense of foreboding settles over you. You can't shake the feeling that you're not alone in these woods."

    "Suddenly, a chilling scream pierces the silence. You spin around, coming face to face with a horrifying creature. It's like nothing you've ever seen before: a mass of writhing limbs, each one ending in sharp, claw-like appendages."
     "In the center of this monstrosity is a face, twisted in agony, resembling a screaming baby."

    "The creature lunges at you, its limbs flailing wildly. You barely have time to react, dodging and weaving through the trees, trying to escape this nightmare."
##add combat where the creature runs away at low health##
    "After what feels like an eternity, the creature finally retreats, disappearing into the depths of the forest as quickly as it appeared. You're left panting, heart racing, the adrenaline still coursing through you."

    "Shaken but determined, you press on, the encounter serving as a grim reminder of the dangers that lurk in these lands. The village needs you, now more than ever."

    "Emerging from the forest, the sight of the village brings a sense of relief. The shortcut was risky, but you've made it, and now it's time to help these people rebuild their lives."
    jump fortify_village_walls














