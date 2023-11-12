define mc = Character("????")
define ranger = Character("Ranger", color = "#276927")
define Illyria = Character("Illyria", color = "#276927")
label start:
    call initialize_screens
    # Scene starts with the snow-covered wasteland.
    scene bg_wasteland
    with fade

    play music "ambient.ogg" loop

    "You wake up with a start. Your vision is blurry, but after blinking your eyes and adjusting to the light, you look around, revealing a snow-covered wasteland. The wind howls eerily, its mournful wails echoing across the vast expanse of white. The relentless snowstorm rages on, each flake dancing whimsically before merging into the blanket beneath. The air is thick with the scent of frost and desolation."

    scene altar with dissolve
    
    "A massive stone altar stands defiantly amidst the sea of snow. Chains dangle from its sides, their ends embedded in the frozen ground. At the center of the altar lays you, surrounded by intricate, glowing runes carved into the stone."

    "Your vision is still hazy, and a sharp, pulsating pain thunders behind your eyes. Your body feels heavy, and an overwhelming cold numbs your senses. As your eyes adjust, the world around you starts to take form."

    mc "Wh... where am I?"

    "Your voice sounds foreign to your own ears, echoing back to you from the surrounding wasteland. You try to move, but your limbs feel sluggish, as though they've been weighed down."

    #show bg_wasteland_pan with dissolve
    "You look beyond the altar, revealing an endless stretch of snow-covered plains, with the ruins of ancient buildings jutting out like skeletal fingers trying to grasp at the heavens. The sky overhead is a bleak shade of grey, with no sun in sight."

    "From the distance, you hear a faint growl, followed by the sound of shuffling feet. Shadows move beyond the curtain of the snowstorm and dance behind the treeline."

    "The wind carries whispers of lament, stories of a land once vibrant, now reduced to a frozen hellscape. The Alchemist's experiments, they murmur, turned paradise into purgatory. You can't remember who you are or how you got here, but something remains in your memory. The Alchemist."

    #show statue with dissolve
    "On your left, half buried in snow, lies a broken statue of a child, its face twisted in a silent scream. On your right, a tattered flag flutters weakly – an emblem of a kingdom or clan, perhaps, but its insignia has been weathered away."

    "As you attempt to stand, memories rush back, fragmented and disjointed. Flashes of a lavish chamber, shimmering vials filled with glowing liquids, and the echoing laughter of a man consumed by his obsession."

    mc "Who am I? What has happened here?"

    #show bg_castle with dissolve
    "To the North, the snow begins to disperse, revealing a path leading to a dilapidated castle, its spires and towers gnawed away by time and neglect. But there's a magnetic pull, an instinctive need to move towards it."

    "The growls grow louder, more insistent."

    play music "combat.ogg" loop

    transform my_left:
        xalign 0.3
    transform my_right:
        xalign 0.7
    scene bg_wasteland
    show wolf1 at my_left
    show wolf2 at my_right
    
    "The remnants of the Alchemist's creations lurk in the shadows, souls trapped in monstrous forms, forever damned by their creator's insatiable thirst to live beyond death."

    "Emerging from the snowstorm, you see the grotesque figures of the failed experiments. Some resemble beasts with twisted human features, while others are more humanoid but with limbs and features grotesquely out of proportion. Their eyes, however, tell a story of pain, confusion, and anger."

    "Without thinking, your hand moves to your side, fingers wrapping around the hilt of a weapon you didn't know you possessed. It feels right, familiar."

    mc "I need to defend myself. But... I need answers. First, this castle. It beckons."

    call initialize

    menu:
        "Choose your weapon:"
        "A short sword":
            $ weapon = "short sword"
            $ player_move_set.append(slash)
            mc "I feel the weight of a short sword by my side. It's sharp and ready for combat."
        "A Long Bow":
            $ weapon = "long bow"
            $ player_move_set.append(arrow)
            mc "A long bow is strapped to my back, with a quiver full of arrows. It's perfect for long-range attacks."
        "A mage's staff":
            $ weapon = "mage's staff"
            $ player_move_set.append(fire_bolt)
            mc "A mage's staff is in my hand. It pulses with arcane energy, ready to unleash its power."
    
    $ combat = "wolf"
    $ change_bar2_values(100, 100, 0.2, 0.0)
    $ change_bar3_values(100, 100, 0.7, 0.0)
    show screen bar1
    show screen bar2
    show screen bar3
    jump combat

label introduction_ranger:

    hide wolf1
    hide wolf2
    scene snowy_forest
    with fade
    play music "ambient.ogg" loop
    show ranger at my_left
    with moveinright

    "Just as the situation seems dire, an arrow whizzes past, striking the wolf squarely in the head. It collapses, mere inches away."

    ranger " 'Looks like you could use some help.'"
    "You turn to look at your savior and see a young woman running toward you, bow in hand. Her attire is rugged, designed for mobility and camouflage against the snow and trees. A hood partially obscures her face, and she nocks another arrow as she approaches you."
    "As she nears you she lowers her hood to reveal her face. Her eyes hold a depth of experience and a hint of sorrow. Her hair, a mix of dark browns and greens, is tied back to keep it out of her face, and her skin bears the marks and scars of a life lived in the wilderness."

    menu:
        "Thank you. I had it under control, but I appreciate the assist.":
            jump gratitude_response

        "Who are you? You're skilled with that bow.":
            jump curiosity_response

        "I'm grateful. That was too close for comfort.":
            jump comfort_response

label gratitude_response:
    ranger " 'Sure you did. But out here, even the strongest can be overwhelmed. It's not just about skill; it's about survival. I'm Illyria. I'd prefer to meet you under better circumstances both those are few and far between around here these days.'"
    jump common_followup

label curiosity_response:
    ranger " 'I've had a lot of practice. When your life depends on it, you get good fast. I'm Illyria, by the way.'"
    jump common_followup

label comfort_response:
    ranger " 'You're welcome. These woods have become more dangerous by the day. You need to be on guard at all times. It's nice to meet you-- I'm Illyria'"
    jump common_followup

label common_followup:
    # Common dialogue after initial choice
    mc " 'Seems like you've had your fair share of survival.'"
    ranger " 'More than I'd like. Ever since the alchemist turned this place into a death trap, every day is a fight to see tomorrow. Who are you? I've not seen you around before but you seem to know how to handle yourself and a weapon which is rare around these parts.'"
    

    menu:
        "I'm just trying to figure that out myself.":
            jump identity_crisis

        "A traveler, lost in more ways than one.":
            jump lost_traveler

        "Someone who owes you one now.":
            jump debt_of_gratitude

label identity_crisis:
    Illyria " 'Aren't we all? This place... it changes you. Makes you question everything.'"
    mc " 'You sound like you've lost a lot.'"
    Illyria " 'Everything. My family, my home... Now, I wander these woods, haunted by memories and fighting to survive.'"
    jump mark_conversation

label lost_traveler:
    Illyria " 'I know the feeling. This land used to be familiar, now it's like a distant memory, twisted and dark.'"
    mc " 'What twisted it?'"
    Illyria " 'The alchemist's experiments. He tried to play god, and we're living in his failed creation. A world of monsters, curses, and endless winter.'"
    jump mark_conversation

label debt_of_gratitude:
    Illyria " 'No debt needed. We survivors need to stick together. The wilderness doesn't take sides.'"
    mc " 'How have you survived this long?'"
    Illyria " 'By learning from the beasts. You either become the predator, or you're the prey. And I refuse to be hunted down.'"
    jump mark_conversation

label mark_conversation:
    "While conversing with her, her cloak shifts, revealing a faint purple mark rising up her fingertips."

    menu:
        "What's that mark on your hand?":
            jump curse_explanation

        "Cursed wasteland? What happened here?":
            jump wasteland_story

        "You seem to know your way around. Can you help me?":
            jump guidance_offer

label curse_explanation:
    Illyria " 'This? It's a curse, or so I believe. A constant reminder of the cost of survival out here. The things I've had to do... they come with a price.'"
    mc " 'A curse? From what?'"
    Illyria " 'From consuming the essence of the monsters. It was either that or starve. But now, this mark spreads, and with it, a darkness grows inside me.'"
    jump final_choice

label wasteland_story:
    Illyria " 'It started with the alchemist's experiments. His quest for power turned our home into a nightmare. Now, we live among the consequences.'"
    mc " 'And you've been fighting these... consequences?'"
    Illyria " 'Every day. The alchemist's creations roam these lands, and I hunt them, trying to undo at least some of his horrors.'"
    jump final_choice

label guidance_offer:
    Illyria " 'I can. But be warned, it's not just the direction you choose, but the dangers you face along the way.'"
    mc " 'I'll take my chances. I need to understand this place.'"
    Illyria " 'Then follow me, but keep your weapon ready. Danger lurks behind every tree in this cursed forest.'"
    jump final_choice

label final_choice:
    Illyria " 'I'm heading out to track one of them down. It's personal. You're welcome to join me if you're up for it.'"

    menu:
        "I could use the company, and I want to help.":
            jump join_hunt

        "I need to find my own way, but thank you.":
            jump parting_ways

label join_hunt:
    mc " 'What's our first move?'"
    Illyria " 'We'll start by tracking a beast I've been following. It's dangerous, but I believe we can take it down together.'"
    jump quest_start
 

label parting_ways:
    mc " 'Maybe our paths will cross again.'"
    Illyria " 'Perhaps they will. Until then, may your arrows fly true and your steps be silent.'"
 
    jump journey_to_castle


label quest_start:
    scene snowy_forest_path
    with fade

    "She heads to a rugged, snow-laden path leading deeper into the forest. The trees stand tall, their branches heavy with snow, casting long, eerie shadows across the ground."

    show ranger with dissolve
    "Illyria moves with a purpose, her eyes scanning the horizon. Her bow is at the ready, an arrow nocked but not drawn."

    Illyria "The beast we're tracking... it's not far now. Stay close and stay quiet."

    menu:
        "How do you know these woods so well?":
            Illyria "I grew up here, with my parents. They taught me how to read the land, the tracks... before they were taken by the alchemist's creations."
            Illyria "This land wasn't always a wasteland. It used to be vibrant, full of life. But then, the alchemist began his experiments."

        "What kind of experiments?":
            Illyria "He was obsessed with immortality, with power. He started with animals, then children from the villages began to disappear."
            "She points over at remnants of a once-thriving village, now just broken structures and memories."
            Illyria "Parents woke up to empty beds. Cries echoed through the night. Fear gripped the land. That's when the Duchess tried to intervene."

    Illyria "She rules the duchy, or what's left of it. A widow, left to fend for her people against horrors she couldn't imagine."
    "The path leads to a clearing, where the remnants of a massive creature's passage are evident."
    Illyria "The Duchess sent her best men, but none returned. We're on our own out here. The empire has long forgotten us."

    menu:
        "And the alchemist?":
            Illyria "He vanished. Some say he achieved his goal, others believe his creations turned on him. All I know is, he left us with this... nightmare."
            "Illyria stops, kneeling to inspect some tracks."
            Illyria "These are fresh. The beast is close. We must be ready for anything."

        "How do we stop it?":
            Illyria "With cunning and strength. These creatures are powerful, but they're not invincible."
            "The wind picks up, howling through the trees, as if mourning the tragedies of the past."
            Illyria "I hunt them, not just for survival, but for vengeance. For my parents, for the lost children... for a chance to reclaim some semblance of peace."

    Illyria "Stay sharp. In these woods, danger is always just a step away. But together, we might just make it."
    jump Spider_combat

label Spider_combat:
    scene snowy_forest

    "The ground trembles slightly, as you feel the sudden, jarring movement of something large and ominous."

    scene mountain_spider

    play music "combat.ogg" loop

    "A massive, grotesque black spider, its body a horrifying amalgamation of twisted limbs and dripping venom, bursts forth from the dense canopy above."
    "Illyria, caught by surprise, barely has time to react. She turns, her bow half drawn, but it's too late."

    "The spider spews a thick, sticky web, ensnaring her in a cocoon-like trap. She struggles fiercely, her movements becoming more frantic as the web tightens."

    Illyria "Get it off me! I... I can't move!"

    "Illyria's expression is one of pure terror."

    menu:
        "Illyria, hold on! I'll get you out!":
            # "The player is now faced with the daunting task of battling the monstrous spider while trying to free Illyria."

            $ combat = "spider"


            $ change_bar2_values(500, 500, 0.5, 0.0)
            show screen bar1
            show screen bar2

            jump combat            

label post_spider_fight:

    "With a final, desperate effort, you manage to land a crippling blow on the spider."

    hide spider
    "You rush to Illyria's side, casting aside all of the thick webbing."

    Illyria "Thank... thank you. I... I was so scared."

    "Are you hurt?"

    Illyria "No, just... shaken. Spiders... they took my parents from me. I've never... never gotten over that fear."

    Illyria "They ambushed us one night... just like this. I was young, too young to help. I could only hide... and watch."
    scene snowy_forest
    with fade

    play music "ambient.ogg" loop
    "Illyria, still shaking from the encounter, sits against a tree. You kneel beside her, offering comfort."

    show ranger
    with fade

    "Her usual stoic demeanor is replaced by vulnerability. Her eyes, usually so full of resolve, now flicker with the shadows of her past."

    menu:
        "You're safe now, Illyria. It's over.":
            Illyria "Yes, but it never really feels over, does it? Every time I close my eyes, I see them... I see that night."
            "I can't imagine what that's like, but I'm here for you. We'll face these challenges together."

        "It's okay to be afraid. You're not alone in this.":
            Illyria "I've always had to be strong, to be fearless. But sometimes in moments like these, I feel that little girl again, hiding, powerless."
            "Strength isn't about never feeling fear. It's about facing it, and you're one of the strongest people I know."

        "Tell me about your parents. It might help to talk about them.":
            Illyria "They were everything to me. Brave, kind... They taught me how to survive, how to live. Losing them... it broke something inside me."
            "They sound like incredible people. They live on through you, in your courage, in your fight."

    "Illyria takes a deep breath, steadying herself; centering herself; finding a moment of peace."

    Illyria "Thank you. Having someone to share this burden... it means more than you know."
    jump Illyria_cabin

label Illyria_cabin:
    scene hidden_cabin
    with fade

    "After the encounter with the spider, Illyria leads you through the dense forest to a small, hidden cabin. The warmth from the fireplace inside is a welcome relief from the cold."

    show ranger

    Illyria "This is my refuge. Not much, but it's safe and warm. You've been a great help, and I want to offer you something in return. She points to the table, on which lies a healing potion, as well as a bow and a quiver full of arrows."

    menu:
        "A healing potion would be useful.":
            "Illyria nods and hands you a small vial filled with a glowing, green liquid."
            Illyria "This should help mend your wounds and restore your strength. Be careful out there."
            $ player_healing_potion = True

        "I could use a bow and some arrows.":
            "Illyria smiles and hands you a well-crafted bow along with a quiver full of arrows."
            Illyria "A good choice for keeping dangers at a distance. There are 24 arrows; use them wisely."
            $ player_bow = True
            $ player_arrows = 24

    "You thank Illyria for her generosity. The comfort of the cabin and the warmth of the fire make it hard to leave, but the journey ahead calls."

    jump journey_to_castle



