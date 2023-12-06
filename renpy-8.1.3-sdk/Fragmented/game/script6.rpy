label path_to_hell:
    "The journey to the alchemist's lair is a descent into a world forgotten by light. The path, shrouded in a perpetual twilight, winds through desolate foothills, each step a defiance against the land's despair."

    "As you navigate the treacherous terrain, the air grows colder, the ground harder. The trees, twisted and bare, claw at the sky like desperate hands. The silence is a heavy cloak, smothering all but the most distant, haunting cries."

    "The path finally opens up to reveal the lair's entrance: a sunken, craggy maw at the base of a towering, ominous mountain. The entrance, framed by jagged rocks, looks like the gaping mouth of some ancient, petrified beast."

    "The entrance to the lair looms before you, a gateway to untold dangers and the promise of a confrontation that could change the fate of the duchy forever."

    "Guarding the entrance is an ice incubus, a creature of nightmares. Its skin is a translucent blue, veins visible beneath like frozen rivers. Its eyes, cold and unblinking, fixate on you with predatory interest. Icicles hang from its elongated limbs, each movement a symphony of chilling whispers."

    "The air around the incubus crackles with a frigid aura, the ground at its feet frosted over, as if its very presence leeches the warmth from the world."

    menu:
        "Face the ice incubus.":
            "Determined to confront the alchemist, you steel yourself for battle against the chilling guardian. The incubus, sensing your resolve, readies itself for combat."
            jump battle_ice_incubus
        "Turn back and reconsider your approach.":
            "The sight of the incubus gives you pause. Perhaps there is wisdom in retreat, to regroup and approach this challenge with a better plan."
            jump main_village
        

label path_to_hell_with_assistant:
    "The journey to the alchemist's lair is a descent into a world forgotten by light. The path, shrouded in a perpetual twilight, winds through desolate foothills, each step a defiance against the land's despair."

    "As you navigate the treacherous terrain, the air grows colder, the ground harder. The trees, twisted and bare, claw at the sky like desperate hands. The silence is a heavy cloak, smothering all but the most distant, haunting cries."

    "The path finally opens up to reveal the lair's entrance: a sunken, craggy maw at the base of a towering, ominous mountain. The entrance, framed by jagged rocks, looks like the gaping mouth of some ancient, petrified beast."

    "The entrance to the lair looms before you, a gateway to untold dangers and the promise of a confrontation that could change the fate of the duchy forever."

    "Guarding the entrance is an ice incubus, a creature of nightmares. Its skin is a translucent blue, veins visible beneath like frozen rivers. Its eyes, cold and unblinking, fixate on you with predatory interest. Icicles hang from its elongated limbs, each movement a symphony of chilling whispers."

    "The air around the incubus crackles with a frigid aura, the ground at its feet frosted over, as if its very presence leeches the warmth from the world."

    menu:
        "Face the ice incubus.":
            "Determined to confront the alchemist, you steel yourself for battle against the chilling guardian. The incubus, sensing your resolve, readies itself for combat."
            jump battle_ice_incubus
        "Turn back and reconsider your approach.":
            "The sight of the incubus gives you pause. Perhaps there is wisdom in retreat, to regroup and approach this challenge with a better plan."
            jump main_village
        "Talk to the Alchemist’s assistant.":
            "The assistant, a hint of fear in his voice, whispers about a hidden path around the back of the mountain, leading to another entrance."
            "You weigh your options, considering the potential risks and rewards of this less direct approach."
            menu:
                "Take the alternate path":
                    jump alternate_path
                "Face the ice incubus.":
                    "Determined to confront the alchemist, you steel yourself for battle against the chilling guardian. The incubus, sensing your resolve, readies itself for combat."
                    jump battle_ice_incubus
                "Turn back and reconsider your approach.":
                    "The sight of the incubus gives you pause. Perhaps there is wisdom in retreat, to regroup and approach this challenge with a better plan."
                    jump main_village

label alternate_path:
    "You both skirt around the edge of the clearing, keeping a wary eye on the incubus. Its icy breath crystallizes in the air, a stark reminder of the danger lurking just yards away."
    "The assistant leads you to a secluded part of the mountain, where the snow and rock seem to blend seamlessly. He brushes away layers of snow, revealing a hidden door, cleverly inset into the mountain itself."
    assistant "Here it is. This door leads to the alchemist's records room. It's where he kept all his research and findings."
    "The door, though unassuming, feels heavy with history. You can sense the secrets it guards, the knowledge it has witnessed."
    assistant "I've only been in here a few times. The things he wrote about... some were fascinating, others deeply troubling."
    "With a nod, you push the door open. It creaks ominously, revealing a dimly lit corridor that leads into the heart of the mountain. You follow along the corridor until it opens up into a small records room."
    "The room is a trove of knowledge. Shelves line the walls, filled with scrolls, books, and various artifacts. The air is thick with the scent of old parchment and ink."
    jump inside_door_1

label battle_ice_incubus:
    "As you step forward, the ice incubus emits a chilling howl, a sound that seems to freeze the very air. Its movements are swift and graceful, each step leaving a trail of frost in its wake."

    "You ready your weapon, your breath visible in the cold air. The incubus lunges, its claws extended, aiming to ensnare you in its icy grasp."

    $ combat = "incubus"
    $ change_bar1_values(player.maxhp, player.maxhp, 0.1, 0.7, "Player")
    $ change_bar2_values(1380, 1380, 0.5, 0.0, "Ice incubus")

    show screen bar1
    show screen bar2

    jump combat

label defeat_ice_incubus:

    "Finally, with a well-placed blow, the incubus shatters into a thousand pieces, its form dissipating like mist. The air around you warms slightly, the oppressive cold lifting as the guardian falls."

    "You stand victorious, the path to the alchemist's lair now open. The defeat of the ice incubus is a testament to your skill and resolve, a crucial step in your quest to confront the alchemist and end his reign of terror."

    "Taking a moment to catch your breath, you steel yourself for the challenges that lie ahead, knowing that the true test still awaits within the depths of the lair."
    jump enter_alchemists_lair

label enter_alchemists_lair:
    "With the ice incubus defeated, you approach the massive door of the alchemist's lair. It looms before you, ancient and foreboding, its surface etched with strange runes."

    "Gathering your strength, you push against the door. It creaks and groans, resisting at first, but eventually gives way to reveal the lair's interior."

    "You step inside, and the door shuts behind you with a resounding thud. The foyer is a vast cavern, its ceiling lost in shadows. Torches with blue flames line the walls, casting an eerie glow over the space."

    "In the center of the cavern stands a winding staircase, spiraling up into the darkness, its destination unknown. Around you, tables are cluttered with vials, potions, and alchemical equipment, a testament to the alchemist's relentless pursuit of knowledge."

    "Four doors, each distinct in design, are set into the walls of the cavern. They beckon with the promise of secrets and dangers untold."

    "On the opposite side of the cavern, another staircase descends into the depths, leading to the basement. The air is thick with the scent of chemicals and the faintest hint of something darker, something hidden."

    "You stand at a crossroads of choices, each path leading to a different aspect of the alchemist's twisted world. The secrets of the lair await, but so do its dangers."
    
    jump alchemists_lair

label alchemists_lair:
    menu:
        "Ascend the winding staircase.":
            "Curiosity piqued, you decide to explore the upper levels of the lair. You ascend the staircase, each step echoing in the cavernous space."
            jump explore_upper_levels

        "Investigate the experimental area.":
            "Drawn to the array of alchemical wonders, you approach the tables laden with vials and potions. The potential knowledge here is vast, but so is the risk."
            jump explore_experimental_area

        "Enter one of the four doors.":
            "Intrigued by the mystery of the doors, you choose to explore what lies beyond. Each door holds its own secrets, and you must choose wisely."
            jump choose_a_door

        "Descend to the basement.":
            "Feeling a pull towards the unknown, you decide to venture into the basement. What lies below could hold the key to understanding the alchemist's true intentions."
            jump explore_basement
        "Return whence you came":
            jump main_village

label explore_experimental_area:
    "As you approach the tables, the sheer variety of alchemical creations before you is staggering. Vials filled with liquids of every conceivable color and consistency are neatly arranged in rows. Some bubble and fizz, while others are eerily still."

    "Among the vials, strange apparatuses sit, their purpose unclear but undoubtedly linked to the alchemist's experiments. Retorts and alembics of all shapes and sizes are connected in a complex network, with gentle vapors rising from some."

    "Scattered among these tools of alchemy are parchments and scrolls, some rolled up, others left open as if abandoned mid-study. The writings are dense, filled with notes, diagrams, and formulas that speak of a mind both brilliant and unhinged."

    "You realize that each item here could hold invaluable information about the alchemist's work, or it could be a trap, a concoction of danger and deceit."

    menu:
        "Examine the vials closely.":
            "Curiosity piqued, you lean in to inspect the vials. The contents range from glowing liquids to dormant, crystalline substances. You carefully pick up a few, examining them for any clues."
            jump examine_vials

        "Read the parchments and scrolls.":
            "Drawn to the written word, you peruse the parchments and scrolls. The handwriting is erratic, the content a mix of genius and madness, revealing insights into the alchemist's methods and motivations."
            jump read_writings

        "Look around the lair":
            jump alchemists_lair


label examine_vials:
    "You carefully pick up each vial, examining its contents and pondering its purpose. The variety is astounding, each one seemingly holding a different mystery." 
##It should stop you from looking at the vials again once you grab each one##
    menu:
        "Vial 1" if vial_1 == False:
            jump vial_1

        "Vial 2" if vial_2 == False:
            jump vial_2

        "Vial 3" if vial_3 == False:
            jump vial_3

        "Vial 4" if vial_4 == False:
            jump vial_4

        "Vial 5" if vial_5 == False:
            jump vial_5

        "Look at other things in the area":
            jump explore_experimental_area

label vial_1:
    "A swirling, silver liquid that seems to dance and shimmer in the light. It has a hypnotic quality, almost alive in its movements."
    menu:
        "Take the vial":
            "You grab the vial and slip it into your bag, hoping it will serve you well."
            $ vial_1 = True
            jump explore_experimental_area

        "Look at the other vials":
            jump examine_vials

label vial_2:
    "A deep, crimson fluid that bubbles slowly. You notice that where it bubbles, tiny sparks of light appear and disappear."
    menu:
        "Take the vial":
            "You grab the vial and slip it into your bag, hoping it will serve you well."
            $ vial_2 = True
            jump explore_experimental_area

        "Look at the other vials":
            jump examine_vials

label vial_3:
    "A clear liquid with a suspended, glowing orb in the center. The orb pulsates gently, emitting a soft, warm light."
    menu:
        "Take the vial":
            "You grab the vial and slip it into your bag, hoping it will serve you well."
            $ vial_3 = True
            jump explore_experimental_area

        "Look at the other vials":
            jump examine_vials

label vial_4:
    "A dark, viscous substance that clings to the sides of the vial. It has an almost gravitational pull, drawing your gaze inward."
    menu:
        "Take the vial":
            "You grab the vial and slip it into your bag, hoping it will serve you well."
            $ vial_4 = True
            jump explore_experimental_area

        "Look at the other vials":
            jump examine_vials

label vial_5:
    "A vial filled with a gas rather than a liquid. The gas shifts colors continuously, creating a mesmerizing kaleidoscope effect."
    menu:
        "Take the vial":
            "You grab the vial and slip it into your bag, hoping it will serve you well."
            $ vial_5 = True
            jump explore_experimental_area

        "Look at the other vials":
            jump examine_vials

label read_writings:
    "You turn your attention to the parchments and scrolls, each one a window into the alchemist's mind."

    menu:
        "Scroll 1":
            jump scroll_1
        "Scroll 2":
            jump scroll_2
        "Scroll 3":
            jump scroll_3
        "Scroll 4":
            jump scroll_4

        "Look at other things in the area":
            jump explore_experimental_area

   
label scroll_1:

    "Week 7 of Experiments"

    "The parchment is aged, the ink faded in places, but the handwriting is meticulous, a testament to the alchemist's dedication."

    "Week 7: The experiments continue to yield fascinating, albeit unpredictable, results. The transmutation of lesser creatures into more formidable beings has proven successful, though not without its share of failures."
    "A particular rat, subject R-12, exhibited remarkable resilience to the process, emerging larger, stronger, yet retaining a semblance of its original form. This success brings me closer to understanding the delicate balance between physical transformation and mental retention."
    jump read_writings

label scroll_2:
    "Week 9 of Experiments"
    "An unexpected development occurred with subject H-05, a human volunteer. Post-experimentation, H-05 exhibited significant memory loss, a side effect not previously encountered. This raises questions about the impact of my methods on the human psyche. Further observation is necessary to determine if this is an isolated incident or a more pervasive issue."
    jump read_writings

label scroll_3:

    "Week 14 of Experiments"

    "The time alteration experiments have shown promise, though the effects are fleeting and unstable. I've theorized that manipulating the flow of time around a subject could, in theory, reverse death itself."

    "However, the process is far from perfected, and the risk of temporal distortion is high. The last attempt resulted in a partial untethering of the subject's soul from their physical form, leading to severe mutations. Caution must be exercised in future trials."
    jump read_writings

label scroll_4:

    "Week 18 of Experiments"

    "The energy emanating from the experiments has attracted something... otherworldly. A force, ancient and forgotten, seems drawn to the soul energy released during the transmutations. I've temporarily sealed it in the basement until I can ascertain its nature and intentions."

    "The discovery of the ancient altars has been a breakthrough. These relics appear to tether the soul to the body, allowing for a return to the moment of tethering upon death. This could be the key to achieving true deathlessness, a goal that has eluded me thus far. The implications are staggering, and the potential for misuse is equally so. Caution and discretion are paramount."

    "The scroll ends with a detailed sketch of the altar, its intricate designs hinting at a forgotten era of alchemy."
    jump read_writings


label choose_a_door:
    "You walk to the edge of the room, where you are faced by four doors of varying shapes, sizes and designs."
    menu:
        "Door 1":
            jump door_1
        "Door 2":
            jump door_2
        "Door 3":
            jump door_3
        "Door 4":
            jump door_4
        "Look around the lair":
            jump alchemists_lair
            
label door_1:

    "As you approach the first door, you notice its surface is unnaturally smooth, almost like polished glass. It reflects the torchlight eerily, creating a mesmerizing effect. You run your hands over its surface, feeling no seams, no handles, no keyholes – nothing to suggest a way to open it."
    "It's as if the door is part of the wall itself. You press and knock, but it remains unyielding, a silent guardian to its secrets. The mystery of this door adds to the enigmatic nature of the lair, hinting at hidden mechanisms or magic at play."
    menu:
        "Check out the other doors":
            jump choose_a_door

label door_2:

    "The second door is a stark contrast to the first. It's adorned with an intricate combination lock, surrounded by an array of gears and mechanical contrivances. The lock itself is a work of art, with delicate engravings that seem to tell a story." 
    "You notice symbols that resemble astrological signs and alchemical elements. Attempting to interact with it, you realize that solving this puzzle would require not only a keen mind but also knowledge of the alchemist's work and perhaps his personal history. The complexity of the lock suggests it guards something of great importance or value."
    menu:
        "Check out the other doors":
            jump choose_a_door
        "Turn to the alchemist's assistant" if assistant == True:
            jump inside_door_2

label door_3:
    "The third door is imposing – a heavy steel door set on large iron hinges. It exudes a sense of foreboding, as if warning those who approach to tread carefully. The door is cold to the touch, and you can feel a faint vibration, like something powerful is at work on the other side." 
    "There's a simple pull handle, but it's clear that opening this door might lead to danger. It's the kind of barrier put in place to keep something in, rather than keep intruders out."
    menu:
        "Open the door":
            jump inside_door_3
        "Check out the other doors":
            jump choose_a_door
label door_4:
    "The final door is surprisingly mundane, a simple wooden door that wouldn't be out of place in any storage room. It's a stark contrast to the grandeur and mystery of the other doors in the lair."
    menu:
        "Open the door":
            jump inside_door_4
        "Check out the other doors":
            jump choose_a_door

label inside_door_1:
    "The room is a veritable archive, filled with shelves of meticulously organized records. Each shelf is labeled with dates and categories, chronicling the alchemist's experiments over the years. The sheer volume of documentation is overwhelming, yet each piece is a fragment of a larger story."
    menu:
        "Search the first shelf":
            jump shelf_1
        "Search the second shelf":
            jump shelf_2
        "Search the third shelf":
            jump shelf_3
        "Search the fourth shelf":
            jump shelf_4
        "Search the fifth shelf":
            jump shelf_5
        "Search the sixth shelf":
            jump shelf_6
        "Search the seventh shelf":
            jump shelf_7
        "Search the eighth shelf":
            jump shelf_8
        "Open the door in front of you":
            jump door_1_exit
    
label door_1_exit:
    "As you pass through the door, it shuts hard behind you automatically, the alchemist's assistant barely dodging out of the way. You turn to look at the door, you notice its surface is unnaturally smooth, almost like polished glass. It reflects the torchlight eerily, creating a mesmerizing effect." 
    "You run your hands over its surface, feeling no seams, no handles, no keyholes – nothing to suggest a way to open it."
    "It's as if the door is part of the wall itself. You press and knock, but it remains unyielding, "
    assistant "Ah.... fuck. I forgot that it did that. We won't be able to get back in without the alchemist, he's the only one who can open that door from the inside."
    jump alchemists_lair

label shelf_1:
    "A Bundle of Letters: Tied with a faded ribbon, these letters offer glimpses into the alchemist's personal and professional relationships. They range from formal requests for rare ingredients to heartfelt pleas from old friends concerned about the alchemist's well-being. One letter, in particular, is filled with worry:"
    "Alaric, your last correspondence was troubling. You speak of breaking barriers never meant to be crossed. Remember, there is a line between genius and madness. Do not lose yourself in your quest."
    jump inside_door_1

label shelf_2:
    "Scroll 3: Week 22 of Experiments"
    "The ink on this scroll is smudged in places, as if the writer was in a hurry or under duress."
    "Week 22: The experiments have taken a toll, both on myself and the subjects. The latest series of transmutations have been successful in terms of physical transformation, but the mental effects are increasingly concerning. Subjects display heightened aggression, confusion, and in some cases, complete loss of self. The balance I sought seems more elusive than ever."
    "The time alteration experiments have yielded some success, but at a great cost. The untethering of the soul from the body has proven more dangerous than anticipated. The mutations are grotesque, a far cry from the controlled changes I envisioned. It's becoming clear that this path may lead to ruin rather than revelation."
    "The environment around the laboratory has become almost alien in nature. Plants and animals affected by the residual alchemical energies have evolved into forms unrecognizable from their original state. This unintended alchemical ecosystem is both a marvel and a warning of the power I wield."
    "The entity in the basement has grown increasingly restless. Its hunger for soul energy seems insatiable, and I fear what might happen should it break free from its confinement. I must find a solution soon, lest it escape and wreak havoc beyond my control."
    "The altars have proven effective in anchoring the soul, but the process is not without its risks. The tethering can be disorienting, and there have been instances where subjects have become lost in time, unable to return to their original moment. The potential for disaster is high, and I must proceed with utmost caution."
    "As I continue my work, I can't help but wonder if the pursuit of immortality is worth the price. The line between genius and madness grows thinner with each passing day, and I fear what I might become should I cross it."
    "The scroll ends abruptly, the final words trailing off into an indecipherable scribble."
    jump inside_door_1


label shelf_3:
    "Week 32 of Experiments"
    "The writing on this scroll is frantic, the ink blots indicating a sense of urgency."
    "Week 36: The experiments have reached a critical juncture. The success rate has improved, but at a cost that weighs heavily on my conscience. The village raids have not gone unnoticed, and the whispers of a 'monster' stealing away the young are spreading like wildfire. I must be cautious, for discovery could mean the end of everything I've worked for."
    "The entity in the basement is a ticking time bomb. Its power grows with each experiment, and I fear what it might become if left unchecked. The containment stones are holding, but for how long, I cannot say. The thought of it breaking free is a nightmare I dare not entertain."
    "My research has led me to a pivotal decision: I must undergo the process myself. To achieve true immortality, I need to be in peak physical condition. The plan is to send my body back 60 years in time, rejuvenating it to its prime. The risks are immense, but the potential reward is the secret to eternal life."
    "The process requires a journey to a secluded altar deep in the woods, surrounded by the altered creatures that roam the area. I will arm myself for protection, as the risk of memory loss is significant. Should I forget who I am, this weapon will be my safeguard."
    "The recipe for the rejuvenation potion is complex, requiring rare ingredients and precise timing. The steps are as follows:"
    "Harvest the heart of a time-altered beast, still beating."
    "Extract the essence of a midnight bloom, a flower that only opens under a full moon."
    "Combine these with the tears of a phoenix, a substance known for its regenerative properties."
    "Perform the ritual at the stroke of midnight, under the light of the full moon, at the ancient altar."
    "The journey will be perilous, but the reward is the culmination of a lifetime's work. I must succeed, for the sake of all I have sacrificed."
    "The scroll includes a detailed map to the altar, along with sketches of the required ingredients."
    jump inside_door_1

label shelf_4:
    "Week 34: The Assistant's Discovery"
    "The air in the laboratory was thick with tension, the kind that precedes a storm. My assistant, always loyal and diligent, had stumbled upon the darker aspects of my work. The revelation hit him like a physical blow, his face a mask of horror and disbelief. I had kept him in the dark, sparing him the moral burden of my more... extreme methods. But now, the truth lay bare between us, an insurmountable chasm."
    "He accused me of monstrosity, of crossing lines no man should ever cross. I tried to explain, to justify my actions with the greater good, but my words fell on deaf ears. He left that night, his departure a silent condemnation of my choices. The loss of his trust and companionship was a blow, but the work must continue. The path to immortality is a solitary one, and sacrifices must be made."
    jump inside_door_1

label shelf_5:
    "Week 36: The Deepening Winter"
    "As the entity in the basement grows in power, its influence seeps into the land. The duchy has fallen into an unending winter, the skies perpetually gray, the air biting cold. The snow blankets the ground in a suffocating embrace, and the once vibrant forests stand silent, their life choked by frost."
    "The villagers speak of an eternal winter, a curse brought upon by my experiments. They do not understand the forces at play, the delicate balance I am trying to maintain. The entity's hunger for soul energy is disrupting the natural order, its power a malignant force against the world's very essence."
    "The changing environment is a grim reminder of the consequences of my actions. The pursuit of knowledge and power comes at a price, and the duchy is paying it in full."
    jump inside_door_1


label shelf_6:
    "Week 38: The Duchess's Discovery and the Duke's Demise"
    "The Duchess, a woman of keen intellect and unwavering determination, has discovered my involvement in the duchy's plight. In a desperate bid to stop me, she dispatched the Duke and his men. They came in force, righteous fury in their eyes, swords drawn, ready to end my 'madness.'"
    "But they were not prepared for what awaited them. The creatures, my creations, descended upon them with a ferocity born of hunger and twisted instinct. The battle was a massacre, the Duke and his men torn asunder, their flesh consumed, their souls absorbed. The ground was soaked with blood, the air filled with screams and the sickening sounds of rending flesh."
    "The Duchess's grief turned to rage, her sorrow to a burning desire for vengeance. I have made an enemy of the one person who could have understood my quest. But there is no turning back now. The path is set, and I must follow it to its end, no matter the cost."
    jump inside_door_1

label shelf_7:
    "Week 40: The Curse of Consumption"
    "My experiments have taken a ghastly turn. Those who consume the flesh and soul of the transmuted creatures are afflicted with a curse, a corruption that eats away at their very being. Their bodies twist and mutate, their minds consumed by an insatiable hunger for blood and flesh."
    "I have observed this transformation with a mix of horror and fascination. The process is irreversible, a descent into madness and monstrosity. In my quest to understand the nature of life and death, I have unleashed a plague upon the land, a curse that turns men into monsters."
    "In a twisted experiment, I forced the transmutations to consume the corpses of their fallen brethren. The result was a horror beyond comprehension. The creatures became more grotesque, more powerful, their hunger for blood and consumption insatiable. They are no longer mere experiments; they are abominations, a testament to my hubris and folly."
    "The weight of my sins grows heavier with each passing day. The path to immortality is paved with the souls of the damned, and I am their architect."
    jump inside_door_1

label shelf_8:
    "Week 42: The time has come to undertake the most crucial experiment of my life. The preparations are complete, and the path to the altar is clear, though fraught with danger. The creatures that roam the woods are a testament to my work's unintended consequences, and they will not take kindly to my intrusion."
    "The entity in the basement has grown more restless, its hunger for soul energy almost palpable. The containment stones are holding, but I sense their power waning. I must complete my experiment before it breaks free and unleashes its fury upon the world. I will never be able to face it in my current state."
    "The potion is ready, the ingredients combined with meticulous care. The ritual at the altar will be the final step, the moment where I either achieve immortality or succumb to the unknown. The thought of losing my memories, of forgetting who I am and what I've done, terrifies me. But the pursuit of knowledge, the quest for eternal life, demands sacrifice."
    "I will transcend. I must transcend. Should I succeed, I will emerge from the ritual reborn, my body restored to its youthful prime. Only then will I have the power to right these wrongs. Should I fail, I entrust this knowledge to whoever finds these scrolls. Use it wisely, for the power they contain is both wondrous and terrifying. May god have mercy on our souls."
    "To whoever reads this, know that my intentions were noble, even if my methods were flawed. I sought to conquer death, to unlock the secrets of the universe. Whether I am remembered as a hero or a monster, know that I did what I believed was necessary for the advancement of alchemy and the betterment of mankind."
    jump inside_door_1

label inside_door_2:
    "Standing before the second door, you are taken aback by its complexity and beauty. The combination lock, an intricate mesh of gears and symbols, appears almost insurmountable. The assistant steps forward, a look of concentration etched on his face."
    assistant "This lock... the alchemist designed it himself. It's not just a barrier; it's a test. He used to say that only those who truly understand his work could access what lies beyond."
    "The assistant carefully examines the lock, his fingers tracing the astrological signs and alchemical elements. He pauses occasionally, muttering to himself as he recalls lessons and conversations with the alchemist."
    "The assistant begins to manipulate the lock, aligning symbols and gears with a practiced hand. He seems to be following a sequence, a pattern known only to him and the alchemist."
    assistant "Each symbol here represents a key aspect of the alchemist's research... and his life. See, this one stands for the celestial alignment under which he made a groundbreaking discovery. And this one here symbolizes the element he believed was the essence of life."
    "As he speaks, the gears of the lock begin to move more smoothly, clicking into place with satisfying precision. The complexity of the puzzle slowly unravels under his deft touch."
    "Finally, with a soft click, the last gear falls into place, and the lock releases. The door swings open, revealing the room beyond."
    assistant "There we go. He always said that understanding was the key to unlocking the world's mysteries. I guess he meant it quite literally in this case."
    "As the door creaks open, you step into a realm that feels detached from the rest of the lair. The room is bathed in a soft, ethereal light, casting gentle shadows across the walls adorned with arcane symbols." 
    "In the center, a stand holds an elegant robe, a staff, and a ring, each item radiating a sense of power and history. Shelves lined with mysterious artifacts and a desk cluttered with magical paraphernalia suggest this room is a personal sanctuary for profound arcane work."
    menu:
        "Examine the Arcane Robe":
            jump robe
        "Inspect the Magical Staff":
            jump staff
        "Look at the Ring":
            jump ring
        "Browse the Personal Grimoire":
            jump book
        "Investigate the Collection of Artifacts":
            jump artifacts
        "Explore the Workbench with Incomplete Projects":
            jump workbenchy
        "Admire the Wall of Achievements":
            jump achievements
        "Return to the Main Chamber":
            jump alchemists_lair
        

label robe:
    "The robe, upon closer inspection, is a masterpiece of magical craftsmanship. The fabric is interwoven with threads of silver and gold, creating patterns that dance and move as if alive. The symbols embroidered on it are from a forgotten language of magic, pulsing with a faint glow. A sense of nostalgia washes over you as you touch the fabric, filling you with warmth and energy."
    menu:
        "Take the Robe":
            $ robe = True
            jump inside_door_2
        "Look back at the room":
            jump inside_door_2

label staff:
    "Picking up the staff, you feel a surge of energy coursing through it. The wood is ancient, possibly from a tree that witnessed centuries. The crystal atop the staff is not just ornamental; it's a focus for magical energies, shimmering with a spectrum of colors. As you hold it, the staff seems to resonate with your touch as arcane power fills every fiber of your being."
    menu:
        "Take the Staff":
            $ staff = True
            jump inside_door_2
        "Look back at the room":
            jump inside_door_2
label ring:
    "The ring is deceptively simple yet elegant. The metal is cool to the touch, and the gemstone set in it is mesmerizing, holding a depth that seems impossible. As you peer into the gem, you feel a connection to the cosmos, a fleeting glimpse of distant stars and unknown worlds. The ring seems to hold a part of its owner's essence."
    menu:
        "Take the Ring":
            $ ring = True
            jump inside_door_2
        "Look back at the room":
            jump inside_door_2
label book:
    "The Grimoire is a dense tome filled with the alchemist's personal notes, spells, and theories. Flipping through the pages, you find annotations, sketches of creatures and symbols, and complex spell formulas. One page details a spell for manipulating time, with notes in the margin expressing concerns about its implications."
    "Flipping the page, you see several entries about the alchemist's experiements:"
    "You start with the earliest records, where the handwriting is vigorous and full of excitement. These logs detail the alchemist's initial experiments with basic transmutations and elixirs. The notes are peppered with sketches of plants, minerals, and intricate apparatus."
    menu:
        "Keep reading":
            jump book_2
        "Look around the room":
            jump inside_door_2

label book_2:
    "You continue leafing through the pages. This Grimoire looks less to be about spells and magic, and more of a personal journal the alchemist kept as a more condensed record of his exploits. It doesn't quite follow the same structured format of his other records, and seems more like a keepsake or a gift meant for someone once he had finished his work."
    menu:
        "Keep reading":
            jump book_3
        "Look around the room":
            jump inside_door_2

label book_3:
    "You turn the page and find a detailed account of turning lead into gold, marked with a triumphant exclamation. The margins are filled with calculations and revisions, showcasing a brilliant, if somewhat obsessive, mind."
    "The next holds a recipe for an elixir that promised to enhance vigor. The notes mention several failed attempts, followed by a breakthrough. A dried flower petal, pressed between the pages, suggests a personal significance to this discovery."
    "Moving to the more recent records, the tone shifts. The handwriting becomes more erratic, the notes more cryptic. Here, the experiments delve into the realms of soul manipulation and time alteration. Diagrams of elaborate circles and arcane symbols cover entire pages."
    menu:
        "Keep reading":
            jump book_4
        "Look around the room":
            jump inside_door_2

label book_4:
    "The next pages include detailed logs of attempts to bind souls to objects, animals, and eventually humans. The notes speak of successes and failures, each entry more desperate than the last."
    "Pages upon pages are filled with theories on reversing the flow of time. Diagrams of hourglasses, celestial alignments, and complex mathematical formulas dominate these records. Margin notes question the ethics and consequences of such power."
    "The diaries and personal notes reveal a mind grappling with the consequences of its actions. The entries become more introspective and filled with doubt."
    "An entry dated about a month before your arrival at the lair speaks of deep regret and a longing for redemption. The alchemist writes of a growing realization that his quest for knowledge and power has led him astray from his original noble intentions."
    "The most recent entry speaks of a final experiment, one that would either restore everything to its rightful path or end in utter ruin. The alchemist writes of preparing to undertake this experiment himself."
    jump inside_door_2

label artifacts:
    "Each artifact on the shelves has its own aura of mystery. A small box contains a set of runes that hum with power, a vial filled with a swirling galaxy-like substance, and a miniature model of a celestial orrery that moves on its own. These items are not just collectibles but tools and trophies of a life spent exploring the boundaries of reality. It's probably best not to touch them."
    jump inside_door_2

label workbenchy:
    "The workbench is cluttered with ongoing experiments and inventions. Among them, a half-assembled device designed to harness elemental energies, and a series of crystalline lenses that seem to alter the fabric of reality when looked through. Notes scattered around suggest these projects were at the heart of the alchemist's current research."
    jump inside_door_2


label achievements:
    "The wall displays a testament to a life of recognition and accomplishment. Each frame holds a certificate, a commendation, or a letter of appreciation from various magical institutions and societies. One particularly ornate certificate is from the Arcanum Magna, honoring the alchemist for groundbreaking research in transmutation."
    jump achievements

label inside_door_3:
    "The steel door's creak is a foreboding overture to the horrors within. As it swings open, a wave of cold, stale air rushes out, carrying with it the echoes of despair and suffering." 
    "The room is a stark contrast to the rest of the lair, devoid of the warmth of scholarly pursuit or the comfort of domesticity. It's a place where the alchemist's quest for knowledge and immortality took a dark and twisted turn. The walls, once pristine, are now marred with stains and scratches, each a silent testament to the room's grim purpose."
    "The room is meticulously organized, reflecting a mind that, despite its descent into madness, clung to the principles of scientific rigor. Tables line the walls, each dedicated to a different aspect of the alchemist's experiments."
    "Some hold rows of vials filled with liquids of varying viscosities and hues, others are cluttered with surgical tools, their blades dulled and stained with blood. In the center, the chair with its restraints stands as a grim monument to human suffering. Above it, mechanical arms equipped with various implements hang ominously, used for procedures of both precision and pain."
    menu:
        "Inspect the examination tables":
            jump exam_tables
        "Inspect the glass containers":
            jump containters
        "Inspect the Chair":
            jump chair
        "Return to the central chamber":
            jump alchemists_lair

label exam_tables:
    "Each examination table tells its own morbid story. One is littered with anatomical sketches, the drawings detailed and precise, yet depicting subjects that defy natural law. Another table holds a series of jars, each containing a preserved organ, grotesquely altered through alchemical processes." 
    "The journal found here is a window into the alchemist's mind, the entries oscillating between clinical detachment and frenzied excitement. The final pages are particularly disturbing, revealing a complete surrender to obsession, the handwriting devolving into barely legible scrawls."
    "Week 29: The experiments have revealed a curious pattern: the younger the subject, the more successful the transmutation. This has led me to the unfortunate necessity of sourcing subjects from nearby villages." 
    "The kidnapping of children and young adults is a reprehensible act, yet I justify it in the name of progress and the greater good. The guilt is a constant companion, but I cannot allow emotions to hinder my work. The end, I tell myself, justifies the means."
    jump inside_door_3

label containers:
    "The containers are like windows into a nightmare realm. One holds a creature that seems to be a fusion of bird and human, its wings grotesquely grafted onto human arms. Another contains a serpentine form, its scales shimmering with an unnatural iridescence, the result of some alchemical mutation."
    "The most unsettling container holds what appears to be a failed attempt at reversing death itself, the subject caught in a perpetual state of decay and regeneration."
    jump inside_door_3

label chair:
    "Approaching the chair, you can almost hear the echoes of the past - the whir of machinery, the clink of metal, the muffled cries of the subjects. The restraints are worn, the leather cracked and stained with the sweat and blood of countless victims. The devices above the chair range from scalpels and saws to more arcane instruments, their purpose unclear but undoubtedly sinister." 
    "A nearby stand holds a collection of syringes, each containing a different colored substance, likely used in the alchemist's attempts to manipulate life and death. You glance down at the table next to the chair and see a series of neat and detailed notes:"
    "Week 15: Progress has been made in refining the transmutation process. The latest batch of subjects, both animal and human, have shown increased stability post-transformation. The key seems to lie in the precise application of alchemical reagents during the procedure. A balance must be struck between the physical and ethereal elements to avoid catastrophic results."
    "Observations of the environment surrounding the laboratory have revealed a gradual but noticeable change. The flora and fauna exhibit signs of alchemical influence, likely a residual effect of the energies released during experimentation. This unintended consequence warrants further study, as it could provide insights into the long-term effects of my work on the natural world."
    "The memory loss in human subjects remains a concern. It appears more prevalent than initially thought, with several subjects exhibiting varying degrees of amnesia. This could be a byproduct of the soul's untethering during the time alteration experiments. The implications are troubling, and I must take care to ensure that my own exposure to these forces does not impair my faculties."
    jump inside_door_3


label inside_door_4:
    "As you step into the storage room, it takes a moment for your eyes to adjust to the dim light. The storage room, a stark contrast to the rest of the alchemist's lair, is a testament to functionality over form. Rows of wooden shelves, sturdy and well-worn, dominate the space. The air is thick with the mingled scents of dried herbs, oils, and the metallic tang of minerals." 
    "The room's meticulous organization speaks of a disciplined mind, while the occasional spill or hastily scribbled label hints at moments of frenzied inspiration." 
    menu:
        "Search the shelves on the left of the room":
            jump left_shelves
        "Search the shelves on the right":
            jump right_shelves
        "Search the Drawers":
            jump drawers
        "Head back into the main cavern":
            jump alchemists_lair

label left_shelves:
    "The shelves are a cornucopia of alchemical ingredients and tools. Each item is carefully labeled, though some labels show signs of age and wear. Among the myriad items, several stand out:"
    "A collection of bottles, each filled with a luminous red liquid that pulses gently, like a heartbeat. The liquid's viscosity and the way it clings to the glass suggest a powerful regenerative property. The label below is smudged but it appears to be an advanced healing potion."
    "Bottles of deep blue liquid, shimmering with an inner light that seems to dance and play. The fluid moves with an almost sentient grace, hinting at the potent magical energies contained within. The label below is smudged but it appears to be an advanced mana potion."
    "Small vials containing a clear, sparkling substance. The liquid appears to constantly shift between liquid and a fine mist. The label below documents it as an advanced agility potion."    
    menu:
        "Take the potions":
            $ advanced_healing_potions = + 3
            $ advanced_mana_potions = + 3
            $ advanced_agility_potions = + 3
            jump inside_door_4
        ##pls help UwU (make sure they can't take them again)##
        "Look back around the room":
            jump inside_door_4

label right_shelves:
    "The ingredients on display are as varied as they are exotic. Some are common in alchemical practices, while others are rare and possibly dangerous. Notable among them are:"
    "Wolfsbane: Bundles of this dark, leafy plant are stored in sealed containers. Known for its potency in repelling malevolent creatures and its use in transformational potions, the wolfsbane here appears to be of an exceptionally high quality."
    "Phoenix Feather: A single, radiant feather, its colors shifting in the light. The feather exudes a warm, comforting energy, suggesting its use in powerful healing potions or perhaps in rituals of rebirth and renewal."
    "Dragon Scale Powder: A small, securely locked box contains this rare ingredient. The scales have been ground into a fine, iridescent powder that seems to absorb and reflect light in mesmerizing patterns. Its uses could range from fire-resistant potions to concoctions granting immense strength or resilience."
    jump inside_door_4

label drawers:
    "Hidden among the more mundane supplies are items of a more personal nature:"
    "An Old Journal: This journal, bound in faded leather, contains detailed notes on various alchemical experiments. The handwriting, initially neat and precise, becomes increasingly erratic as the entries progress. One entry, in particular, stands out:"
    "Experiment #67: The boundaries of life and death blur further. The subject revived, but at what cost? Their eyes, once vibrant, now hold a hollow gaze. I fear I am losing myself in this pursuit."
    "Flipping through its pages, you find detailed notes on experimental procedures. One entry, detailing an experiment on memory transference, is marked with a question in the margin, 'What if I forget who I am?' The handwriting, eerily similar to your own, sends a shiver down your spine."
    "In the drawers you also find a faded photograph, hidden behind a stack of vials. It depicts a young man standing beside the alchemist, both smiling broadly."
    "Next is a collection of letters, some with ink faded by time. They speak of concerns and warnings about the path of the alchemist's research. One unsigned note simply says, 'Remember why you started this journey.'"
    "Tucked into the corner of the furthest drawer, you find a locket."
    "The locket, once elegant, now shows signs of age. Inside is a miniature painting of a young woman, her eyes bright with intelligence and kindness. The inscription on the back reads 'To Alaric, with all my love - Elenor,'"
    jump inside_door_4


label explore_basement:
    "Your footsteps echo in the narrow stairwell as you descend into the basement. Each step feels like a descent into the unknown, the air growing colder, the light dimmer."
    "The walls seem to close in around you, and a sense of foreboding fills your heart."
    "At the bottom, you are met with an imposing sight. The door before you is a masterpiece of dark artistry, its surface etched with intricate, ominous designs. It radiates a palpable, malevolent energy, as if it's alive with a sinister will of its own." 
    "You feel it pulling at your soul, an almost physical tug that threatens to unravel your very essence."
    "As you approach the door, you see that the designs are actually murals, spiralling around each other in a way that seems to split the door into three parts."
    "The first mural depicts a majestic stag, its form ethereal and otherworldly. The antlers sprawl across the mural like dark, twisted branches against a starless night sky."
    "The forest around it is alive with hidden eyes and whispered secrets, creating an aura of ancient mysticism. The empty stone inset within the mural pulsates with a longing energy, as if missing a vital piece of its existence"
    "In the second mural, a serpent of immense size coils menacingly. Its scales are like shards of ice, reflecting a cold, harsh light. The icy wasteland it inhabits is a desolate expanse, a land where life struggles to exist. The serpent's eyes hold a depth of sorrow and wisdom, creating a sense of connection with the viewer."
    "The stone inset here is frigid, its absence leaving a palpable void in the chilling tableau."
    "The final mural portrays a colossal creature, resembling an armadillo but imbued with a sense of raw, elemental power. It stands as a guardian over a landscape of treacherous peaks and snow-covered cliffs. The mural captures the creature's formidable presence, each detail emphasizing its connection to the mountainous realm it protects."
    "The stone inset for this mural is rugged and unyielding, echoing the unforgiving nature of the mountains."
    "As you stand before this colossal door, a sense of deep, inexplicable connection washes over you. The malevolent energy emanating from the door is almost overwhelming, clouding your thoughts and heightening your senses. You feel as if this door is not just a barrier to a physical space but a gateway to understanding the fragmented memories and mysteries that have been haunting you."
    "You take a step back, gathering your thoughts. The task ahead is monumental, yet it feels like an integral part of your destiny. You must find the elemental stones, face the guardians, and unlock the secrets that lie beyond this door. But first, you must prepare for the trials that await, both mentally and physically."
    menu:
        "Touch the door":
            jump toby_continue

label toby_continue:
    "To be continued..."

label door_visions:
    "Compelled by a force beyond your understanding, you reach out and touch the door. The moment your skin contacts the cold surface, a rush of visions engulfs your mind, each one more vivid than the last."
    "The vision of the enchanted forest is mesmerizing. The stag stands as a mystical guardian, its presence commanding yet serene. The forest whispers of ancient magic and hidden paths, a realm where the boundary between the real and the ethereal blurs."
    "The vision blurs, replaced by a fierce snowstorm. The icy wasteland is a realm of stark beauty and desolation. The serpent, a creature of legend, moves with a grace that belies its size. The vision conveys a sense of isolation and endurance, a land where survival is a daily struggle against the unforgiving elements."
    "As the serpent slithers past, the ground begins to shake. Pillars of rock erupt from the ground, throwing you around until you find yourself at the base of a massive mountain."
    "The vision of the snowy mountains is awe-inspiring. The armored creature is a symbol of strength and resilience, a guardian that embodies the harshness and majesty of its domain. The mountains themselves are a challenge, with hidden dangers and breathtaking vistas."
    "As the visions fade, a deep understanding settles within you. You know where to find these guardians, each a protector of an elemental stone and a crucial part of the balance the alchemist sought. The enchanted forest, the icy wasteland, and the snowy mountains are not just locations but realms that test the limits of your courage and resolve."
    "You step away from the door, the visions still etched in your mind. The path ahead is clear, yet filled with unknown dangers. You must venture into these realms, confront the guardians, and claim the stones."
    menu:
        "Begin your final journey":
            jump final_journey
        "Come back later":
            jump alchemists_lair

label final_journey:
    "The journey will be perilous, but you feel a sense of purpose, a drive that transcends mere curiosity. It's as if your very essence is intertwined with this quest, a part of a larger destiny that awaits you."
    "Taking a deep breath, you steel yourself for the journey ahead. The first destination is clear: the enchanted forest, where the stag and the first stone await."
    "Your journey begins at the break of dawn, the first rays of sunlight piercing through the dense canopy of the enchanted forest. The air is thick with the scent of moss and ancient wood. As you venture deeper, the forest seems to come alive, the trees whispering secrets of a bygone era."
    "The path is not marked, but an instinctive pull guides you through the labyrinth of trees and undergrowth. The deeper you go, the more surreal the surroundings become. Shafts of light filter through the leaves, casting ethereal patterns on the forest floor. The sounds of the forest are both calming and eerie, a symphony of nature that speaks of the magic infused in this place."
    "After hours of trekking, you find yourself in a clearing. The atmosphere here is different, charged with an energy that makes the air hum. In the center of the clearing stands the stag, as majestic and otherworldly as in your vision. Its coat shimmers with a spectral light, and the deep emerald stone inset in its forehead glows with an inner energy."
    "The stag regards you with eyes that hold the wisdom of the ages. There is no malice in its gaze, only a solemn acknowledgment of what must come to pass. As you step forward, the stag rears up, its antlers casting a complex shadow on the ground. The air crackles with energy, and you know the moment of confrontation has arrived."
    "You steady your breath, preparing for the inevitable clash. The stag charges, its movements a blur of grace and power."
    ##Combat##
    "Finally, as the battle reaches its climax, you find an opening. With a well-timed spell, you subdue the stag. It falls to the ground, its energy spent. As you approach, the stag's gaze softens. There is no resentment, only a silent understanding that its role as guardian has come to an end."
    "You reach out and gently remove the emerald stone from its forehead. The stone is warm to the touch, pulsating with a life force that resonates with your own. As you hold it, a sense of harmony fills you, a connection to the forest and its ancient magic."
    "The stag rises, its form starting to fade. Before it completely vanishes, it nods to you, a final gesture of respect. The clearing is silent once more, the only evidence of the encounter being the glowing stone in your hand."
    "With the first stone retrieved, you take a moment to reflect on the battle and the journey ahead. The forest seems to acknowledge your victory, the trees whispering words of encouragement. You set your sights on the next destination, the icy wasteland, where the serpent awaits."
    jump serpent_journey

label serpent_journey:
    "Leaving the enchanted forest behind, your journey takes you to the frigid expanse of the icy wasteland. The transition from the lush forest to the barren, frozen landscape is jarring. The ground crunches underfoot, each step a reminder of the harsh environment that surrounds you."
    "The sky is a tapestry of grey, the sun a faint orb behind the clouds. The cold bites at your skin, and the wind howls like a mournful spirit. This land feels forgotten by time, its desolation a stark contrast to the vibrant life of the forest."
    "As you traverse the icy plains, the sense of isolation grows. The vast emptiness stretches out in all directions, a sea of white and blue. Yet, you press on, guided by an inner compass that leads you to your destination."
    "After what feels like an eternity, you arrive at a hollow, where the wind seems to whisper secrets of ancient sorrows. Here, coiled amidst the ice and snow, lies the serpent. Its scales shimmer with an azure hue, reflecting the sparse light in a mesmerizing display. The deep blue stone in its forehead pulses with a cold, yet captivating energy."
    "The serpent's eyes open slowly, fixing you with a gaze that is both penetrating and wise. It uncoils its massive body, each movement deliberate and full of purpose. The air around you drops in temperature, the very atmosphere charged with anticipation."
    ##combat##
    "The struggle reaches its peak as you find a rhythm in the chaos. Somehow, you manage to subdue the mighty serpent. It collapses onto the snow, its breaths coming in slow, labored hisses."
    "Approaching cautiously, you reach out and carefully extract the azure stone from its forehead. The stone is cold, yet as you touch it, a warmth spreads through your body, a stark contrast to the surrounding cold."
    "The serpent's eyes meet yours one last time, conveying a sense of acceptance. Then, it fades away, becoming one with the snow and wind. The wasteland is silent once again, the only reminder of the encounter being the blue stone in your hand."
    "With the second stone secured, you take a moment to gather your strength. The wasteland, though harsh and unforgiving, has taught you resilience. You now turn your attention to the final guardian, the armored creature in the mountains, where the last stone awaits."
    jump armadillo

label armadillo:
    "The path to the mountains is a stark contrast to the icy wasteland you left behind. The terrain becomes increasingly rugged, with steep inclines and treacherous paths. The air is thinner here, each breath a reminder of the altitude and the challenge that lies ahead."
    "The mountains loom over you, their peaks shrouded in clouds. Snow blankets the ground, but it's a different cold here – sharp and biting, yet invigorating. The wind carries the echo of ancient roars, as if the mountains themselves are alive with the memories of long-forgotten battles."
    "As you ascend, the landscape changes. Jagged rocks and sparse vegetation give way to snow-covered cliffs and hidden crevices. The beauty of the mountains is undeniable, but so is their danger. Every step requires caution, every decision, careful consideration."
    "Reaching a plateau, you find yourself in a vast open space, surrounded by towering peaks. Here, amidst the snow and stone, stands the armadillo-like creature. Its size is colossal, its armored shell glistening like rubies under the mountain sun. The deep red stone in its chest pulses with a fiery energy, captivating and intimidating."
    "The creature's eyes open, revealing a depth of wisdom and strength. It uncurls, standing tall and imposing, a guardian of the mountain's secrets. The air around you vibrates with its power, the ground trembling beneath its weight."
    "With a thunderous roar, the creature charges. Its movements are surprisingly agile for its size, each step causing mini avalanches of snow and rock. You ready yourself, drawing on all your skills and knowledge to face this formidable opponent."
    ##combat##
    "The battle is intense, a clash of strength and strategy. The creature's armored shell is nearly impenetrable, forcing you to find creative ways to breach its defenses."
    "As the battle reaches its climax, you find an opening. With precision and determination, you strike, exploiting the creature's momentary vulnerability. It lets out a final, resonant roar before collapsing onto the snow, the ground shaking upon its fall."
    "Approaching the fallen guardian, you reach out to the deep ruby stone embedded in its chest. As your fingers touch the stone, a surge of energy courses through you, a fiery warmth that contrasts the mountain's chill."
    "The creature's eyes meet yours, conveying a sense of respect and acknowledgment. Then, it fades into the mountain winds, leaving behind only the red stone in your grasp."
    "With the final stone in hand, you take a moment to reflect on the journey. The mountains, with their harsh beauty and unforgiving nature, have tested your resolve and strength. Now, with all three stones collected, you are ready to return to the alchemist's lair and face what lies beyond the sealed door."
    jump final_return

label final_return:
    "With the elemental stones in your possession, you make your way back to the alchemist's lair. The journey back feels different, almost surreal. Each step is laden with the weight of your impending confrontation. The lair, once a place of mystery and discovery, now feels like the threshold to a final, decisive battle."
    "Descending the stairs to the basement, the air grows thick with anticipation. The malevolent energy that once repelled you now seems to beckon, as if acknowledging your readiness to face what lies beyond."
    "Standing before the massive door, you feel its dark energy pulsing stronger than ever. The murals of the guardians seem to come alive in the dim light, their eyes following your every move. The empty insets for the stones await, their absence a silent challenge."
    "You take a deep breath, steeling yourself for what comes next. One by one, you place the stones into their respective insets."
    "The Emerald Stone: As the green stone clicks into place on the stag's mural, a surge of vitality flows through the door. The forest scene seems to breathe, the leaves rustling in an unseen wind."
    "The Azure Stone: Next, the blue stone finds its home in the serpent's mural. A chill emanates from the door, the icy wasteland depicted in the mural frosting over, its cold beauty more pronounced."
    "The Ruby Stone: Finally, you insert the red stone into the armadillo-like creature's mural. A wave of warmth spreads, the mountain scene coming alive with the sounds of distant avalanches and the creature's resonant roar."
    "You stand at the brink, the darkness before you promising a challenge beyond any you've faced. A voice within warns you of the danger, a final admonition that this entity is unlike any other. It is not just a threat to your life, but to your very soul."
    "You understand that if you fall to this entity, there will be no return. Your soul could be consumed entirely, severed from the cycle of life and death you've come to understand. The stakes are higher than ever."
    menu:
        "Step into the darkness":
            jump final_boss
        "Turn back and strengthen yourself before the final confrontation":
            jump alchemists_lair
    
    
label final_boss:
    "Despite the fear, a sense of determination anchors you. This is more than a personal quest; it's a fight for something greater. With a final glance at the door, you step forward into the darkness, ready to face whatever lies beyond."
    "As you step through the threshold, the darkness gives way to a chamber that defies all expectations. The room is vast, its walls etched with arcane symbols that pulse with a sickly light. The air is thick with a palpable sense of dread, and the very fabric of reality seems to warp and twist around you."
    "In the center of the chamber, the entity awaits. Its form changes, a reflection of the soul energy it has consumed."

    if deaths == 0: ##define entity and figure this out for me UwU. Also in the combat add jump to final_scene##
        "This form is gaunt, its body a skeletal mockery of life. It moves with a desperate, frenzied hunger, its eyes hollow pits of longing. The air around it is cold, filled with the echoes of its starvation."
        Entity "So... fresh... untouched by death. Your soul... it calls to me... a feast long denied."
        "Your hunger ends here, creature. I will not be your sustenance."
        jump boss_1
    if (deaths <= 5 and deaths >= 1):
        "The entity before you is flickering, its form a swirling mass of tortured souls. You can see faces, hear whispers of agony and despair. The entity's hunger is palpable, its desire for more soul energy almost tangible."
        Entity "More... I need more... Your deaths have fed me, but I am still so hungry. Give me your soul."
        "You will feed no longer!"
        jump boss_2
    if (deaths <= 13 and deaths > 5):
        "The entity is a towering behemoth, radiating dark power. The air crackles with malevolent energy, and the very ground seems to recoil from its touch. Its presence assaults your mind, a constant barrage of corruption and madness."
        Entity "Yes... feel the power... the chaos... You've made me strong. Now, let us merge into one eternal nightmare."
        "You're a blight, a corruption. I'll tear you apart, piece by piece."
        jump boss_3
    if (deaths > 13): 
        "In this form, the entity is a colossal monstrosity, its presence overwhelming. Reality buckles under its weight, and your mind fractures at the mere sight of it. The entity is a maelstrom of soul energy, each death having made it nigh unstoppable."
        Entity "I am eternal... infinite... You are but a drop in the ocean of souls I command. Surrender and become part of my dominion."
        "No matter your strength, I will not yield. I fight for all those you've consumed!"
        jump boss_4


label boss_1:
    Entity "You stand before me, a mere mortal, yet I can sense you seek understanding. Do you not fear what lies beyond your comprehension?"
    menu:
        "Fear? Yes, there's fear. But there's also a need to understand. What are you? Why are you here?":
            jump boss_1_1
            
        "Understanding is the first step to overcoming. Tell me your story. What brought you to this realm?":
            jump boss_1_2
            
        "Comprehension is a path to resolution. Your presence here, it's unnatural. How did you come to be?":
            jump boss_1_3
            

label boss_1_1:
    "I am a being of ancient times, born from the chaos of creation. This realm... it was not my choice. Your kind, with their relentless pursuit of forbidden knowledge, they tore the veil and pulled me into your world. I am here because of your actions, your desires."
    "So, you're a prisoner? A victim of circumstance? But the souls, the destruction... there must be more to your purpose here."
    Entity "Prisoner? Victim? Such terms are meaningless to me. I am a force of nature, an embodiment of the void. The souls... they are my sustenance, drawn to me as moths to a flame. In this realm, I am bound by its rules, yet I transcend them. My purpose? It is simply to exist, to feed, to grow."
    "Existence at the cost of others... there's no justification for that. There has to be a balance, a way to coexist without this endless cycle of suffering."
    Entity "Justification? Balance? Your concepts are irrelevant to me. I exist beyond your morality, beyond your notions of right and wrong. Coexistence? There is no coexistence with the void. It consumes, it expands. Yet, you intrigue me, mortal. You challenge the inevitable."
    "Inevitable? Maybe. But challenging the inevitable is what we do. It's our nature to seek, to question, to defy. There has to be a way to end this cycle, to free both our worlds from this torment."
    Entity "Defy? You amuse me. Your defiance is but a flicker in the darkness. Yet, in your persistence, I sense a resonance. The alchemist, in his folly, bound me here, but he also bound you. You are a part of this cycle, a key to its perpetuation and, perhaps, its end. Too bad that your cycle will have to end here."
    "I'm glad we're in agreement. I'll break the cycle. I'll sever the ties that bind us. Your growth, your power, it ends here. I'll dismantle every piece of this cursed puzzle, starting with you."
    Entity "Dismantle me? I am not a mere machine to be taken apart. I am a force of nature, born from the darkest depths of human ambition. You cannot simply 'dismantle' what you do not fully understand. I tire of your presence mortal. Your journey ends here."
    ##combat##

label boss_1_2:
    "My story is as old as the cosmos. I am a remnant of a forgotten age, a time when realities were not so rigidly defined. An alchemist of this land, in his hubris, reached into the abyss. He sought power, and in doing so, he anchored me to your world, feeding me with the energy of countless souls."
    "So, you're a prisoner? A victim of circumstance? But the souls, the destruction... there must be more to your purpose here."
    Entity "Prisoner? Victim? Such terms are meaningless to me. I am a force of nature, an embodiment of the void. The souls... they are my sustenance, drawn to me as moths to a flame. In this realm, I am bound by its rules, yet I transcend them. My purpose? It is simply to exist, to feed, to grow."
    "Existence at the cost of others... there's no justification for that. There has to be a balance, a way to coexist without this endless cycle of suffering."
    Entity "Justification? Balance? Your concepts are irrelevant to me. I exist beyond your morality, beyond your notions of right and wrong. Coexistence? There is no coexistence with the void. It consumes, it expands. Yet, you intrigue me, mortal. You challenge the inevitable."
    "Inevitable? Maybe. But challenging the inevitable is what we do. It's our nature to seek, to question, to defy. There has to be a way to end this cycle, to free both our worlds from this torment."
    Entity "Defy? You amuse me. Your defiance is but a flicker in the darkness. Yet, in your persistence, I sense a resonance. The alchemist, in his folly, bound me here, but he also bound you. You are a part of this cycle, a key to its perpetuation and, perhaps, its end. Too bad that your cycle will have to end here."
    "I'm glad we're in agreement. I'll break the cycle. I'll sever the ties that bind us. Your growth, your power, it ends here. I'll dismantle every piece of this cursed puzzle, starting with you."
    Entity "Dismantle me? I am not a mere machine to be taken apart. I am a force of nature, born from the darkest depths of human ambition. You cannot simply 'dismantle' what you do not fully understand. I tire of your presence mortal. Your journey ends here."
    ##combat##

label boss_1_3:
    "Comprehension? You seek to understand what is beyond understanding. I am a consequence of your world's arrogance. The alchemist, in his quest for immortality, meddled with forces beyond his grasp. He bound me to this realm, a prison of his own making, sustained by the cycle of death and rebirth he created."
    "So, you're a prisoner? A victim of circumstance? But the souls, the destruction... there must be more to your purpose here."
    Entity "Prisoner? Victim? Such terms are meaningless to me. I am a force of nature, an embodiment of the void. The souls... they are my sustenance, drawn to me as moths to a flame. In this realm, I am bound by its rules, yet I transcend them. My purpose? It is simply to exist, to feed, to grow."
    "Existence at the cost of others... there's no justification for that. There has to be a balance, a way to coexist without this endless cycle of suffering."
    Entity "Justification? Balance? Your concepts are irrelevant to me. I exist beyond your morality, beyond your notions of right and wrong. Coexistence? There is no coexistence with the void. It consumes, it expands. Yet, you intrigue me, mortal. You challenge the inevitable."
    "Inevitable? Maybe. But challenging the inevitable is what we do. It's our nature to seek, to question, to defy. There has to be a way to end this cycle, to free both our worlds from this torment."
    Entity "Defy? You amuse me. Your defiance is but a flicker in the darkness. Yet, in your persistence, I sense a resonance. The alchemist, in his folly, bound me here, but he also bound you. You are a part of this cycle, a key to its perpetuation and, perhaps, its end. Too bad that your cycle will have to end here."
    "I'm glad we're in agreement. I'll break the cycle. I'll sever the ties that bind us. Your growth, your power, it ends here. I'll dismantle every piece of this cursed puzzle, starting with you."
    Entity "Dismantle me? I am not a mere machine to be taken apart. I am a force of nature, born from the darkest depths of human ambition. You cannot simply 'dismantle' what you do not fully understand. I tire of your presence mortal. Your journey ends here."
    ##combat##

label boss_2:
    Entity "You stand before me, a mere mortal, yet I can sense you seek understanding. Do you not fear what lies beyond your comprehension?"
    menu:
        "Fear? Yes, there's fear. But there's also a need to understand. What are you? Why are you here?":
            jump boss_2_1
            
        "Understanding is the first step to overcoming. Tell me your story. What brought you to this realm?":
            jump boss_2_2
            
        "Comprehension is a path to resolution. Your presence here, it's unnatural. How did you come to be?":
            jump boss_2_3

label boss_2_1:
    "I am a being of ancient times, born from the chaos of creation. This realm... it was not my choice. Your kind, with their relentless pursuit of forbidden knowledge, they tore the veil and pulled me into your world. I am here because of your actions, your desires."
    "So, you're a prisoner? A victim of circumstance? But the souls, the destruction... there must be more to your purpose here."
    Entity "Prisoner? Victim? Such terms are meaningless to me. I am a force of nature, an embodiment of the void. The souls... they are my sustenance, drawn to me as moths to a flame. In this realm, I am bound by its rules, yet I transcend them. My purpose? It is simply to exist, to feed, to grow."
    "Existence at the cost of others... there's no justification for that. There has to be a balance, a way to coexist without this endless cycle of suffering."
    Entity "Justification? Balance? Your concepts are irrelevant to me. I exist beyond your morality, beyond your notions of right and wrong. Coexistence? There is no coexistence with the void. It consumes, it expands. Yet, you intrigue me, mortal. You challenge the inevitable."
    "Inevitable? Maybe. But challenging the inevitable is what we do. It's our nature to seek, to question, to defy. There has to be a way to end this cycle, to free both our worlds from this torment."
    Entity "Defy? You amuse me. Your defiance is but a flicker in the darkness. Yet, in your persistence, I sense a resonance. The alchemist, in his folly, bound me here, but he also bound you. You are a part of this cycle, a key to its perpetuation and, perhaps, its end. Too bad that your cycle will have to end here."
    "I'm glad we're in agreement. I'll break the cycle. I'll sever the ties that bind us. Your growth, your power, it ends here. I'll dismantle every piece of this cursed puzzle, starting with you."
    Entity "Dismantle me? I am not a mere machine to be taken apart. I am a force of nature, born from the darkest depths of human ambition. You cannot simply 'dismantle' what you do not fully understand. I tire of your presence mortal. Your journey ends here."
    ##combat##

label boss_2_2:
    "My story is as old as the cosmos. I am a remnant of a forgotten age, a time when realities were not so rigidly defined. An alchemist of this land, in his hubris, reached into the abyss. He sought power, and in doing so, he anchored me to your world, feeding me with the energy of countless souls."
    "So, you're a prisoner? A victim of circumstance? But the souls, the destruction... there must be more to your purpose here."
    Entity "Prisoner? Victim? Such terms are meaningless to me. I am a force of nature, an embodiment of the void. The souls... they are my sustenance, drawn to me as moths to a flame. In this realm, I am bound by its rules, yet I transcend them. My purpose? It is simply to exist, to feed, to grow."
    "Existence at the cost of others... there's no justification for that. There has to be a balance, a way to coexist without this endless cycle of suffering."
    Entity "Justification? Balance? Your concepts are irrelevant to me. I exist beyond your morality, beyond your notions of right and wrong. Coexistence? There is no coexistence with the void. It consumes, it expands. Yet, you intrigue me, mortal. You challenge the inevitable."
    "Inevitable? Maybe. But challenging the inevitable is what we do. It's our nature to seek, to question, to defy. There has to be a way to end this cycle, to free both our worlds from this torment."
    Entity "Defy? You amuse me. Your defiance is but a flicker in the darkness. Yet, in your persistence, I sense a resonance. The alchemist, in his folly, bound me here, but he also bound you. You are a part of this cycle, a key to its perpetuation and, perhaps, its end. Too bad that your cycle will have to end here."
    "I'm glad we're in agreement. I'll break the cycle. I'll sever the ties that bind us. Your growth, your power, it ends here. I'll dismantle every piece of this cursed puzzle, starting with you."
    Entity "Dismantle me? I am not a mere machine to be taken apart. I am a force of nature, born from the darkest depths of human ambition. You cannot simply 'dismantle' what you do not fully understand. I tire of your presence mortal. Your journey ends here."
    ##combat##

label boss_2_3:
    "Comprehension? You seek to understand what is beyond understanding. I am a consequence of your world's arrogance. The alchemist, in his quest for immortality, meddled with forces beyond his grasp. He bound me to this realm, a prison of his own making, sustained by the cycle of death and rebirth he created."
    "So, you're a prisoner? A victim of circumstance? But the souls, the destruction... there must be more to your purpose here."
    Entity "Prisoner? Victim? Such terms are meaningless to me. I am a force of nature, an embodiment of the void. The souls... they are my sustenance, drawn to me as moths to a flame. In this realm, I am bound by its rules, yet I transcend them. My purpose? It is simply to exist, to feed, to grow."
    "Existence at the cost of others... there's no justification for that. There has to be a balance, a way to coexist without this endless cycle of suffering."
    Entity "Justification? Balance? Your concepts are irrelevant to me. I exist beyond your morality, beyond your notions of right and wrong. Coexistence? There is no coexistence with the void. It consumes, it expands. Yet, you intrigue me, mortal. You challenge the inevitable."
    "Inevitable? Maybe. But challenging the inevitable is what we do. It's our nature to seek, to question, to defy. There has to be a way to end this cycle, to free both our worlds from this torment."
    Entity "Defy? You amuse me. Your defiance is but a flicker in the darkness. Yet, in your persistence, I sense a resonance. The alchemist, in his folly, bound me here, but he also bound you. You are a part of this cycle, a key to its perpetuation and, perhaps, its end. Too bad that your cycle will have to end here."
    "I'm glad we're in agreement. I'll break the cycle. I'll sever the ties that bind us. Your growth, your power, it ends here. I'll dismantle every piece of this cursed puzzle, starting with you."
    Entity "Dismantle me? I am not a mere machine to be taken apart. I am a force of nature, born from the darkest depths of human ambition. You cannot simply 'dismantle' what you do not fully understand. I tire of your presence mortal. Your journey ends here."
    ##combat##


label boss_3:
    Entity "You stand before me, a mere mortal, yet I can sense you seek understanding. Do you not fear what lies beyond your comprehension?"
    menu:
        "Fear? Yes, there's fear. But there's also a need to understand. What are you? Why are you here?":
            jump boss_3_1
            
        "Understanding is the first step to overcoming. Tell me your story. What brought you to this realm?":
            jump boss_3_2
            
        "Comprehension is a path to resolution. Your presence here, it's unnatural. How did you come to be?":
            jump boss_3_3

label boss_3_1:
    "I am a being of ancient times, born from the chaos of creation. This realm... it was not my choice. Your kind, with their relentless pursuit of forbidden knowledge, they tore the veil and pulled me into your world. I am here because of your actions, your desires."
    "So, you're a prisoner? A victim of circumstance? But the souls, the destruction... there must be more to your purpose here."
    Entity "Prisoner? Victim? Such terms are meaningless to me. I am a force of nature, an embodiment of the void. The souls... they are my sustenance, drawn to me as moths to a flame. In this realm, I am bound by its rules, yet I transcend them. My purpose? It is simply to exist, to feed, to grow."
    "Existence at the cost of others... there's no justification for that. There has to be a balance, a way to coexist without this endless cycle of suffering."
    Entity "Justification? Balance? Your concepts are irrelevant to me. I exist beyond your morality, beyond your notions of right and wrong. Coexistence? There is no coexistence with the void. It consumes, it expands. Yet, you intrigue me, mortal. You challenge the inevitable."
    "Inevitable? Maybe. But challenging the inevitable is what we do. It's our nature to seek, to question, to defy. There has to be a way to end this cycle, to free both our worlds from this torment."
    Entity "Defy? You amuse me. Your defiance is but a flicker in the darkness. Yet, in your persistence, I sense a resonance. The alchemist, in his folly, bound me here, but he also bound you. You are a part of this cycle, a key to its perpetuation and, perhaps, its end. Too bad that your cycle will have to end here."
    "I'm glad we're in agreement. I'll break the cycle. I'll sever the ties that bind us. Your growth, your power, it ends here. I'll dismantle every piece of this cursed puzzle, starting with you."
    Entity "Dismantle me? I am not a mere machine to be taken apart. I am a force of nature, born from the darkest depths of human ambition. You cannot simply 'dismantle' what you do not fully understand. I tire of your presence mortal. Your journey ends here."
    ##combat##

label boss_3_2:
    "My story is as old as the cosmos. I am a remnant of a forgotten age, a time when realities were not so rigidly defined. An alchemist of this land, in his hubris, reached into the abyss. He sought power, and in doing so, he anchored me to your world, feeding me with the energy of countless souls."
    "So, you're a prisoner? A victim of circumstance? But the souls, the destruction... there must be more to your purpose here."
    Entity "Prisoner? Victim? Such terms are meaningless to me. I am a force of nature, an embodiment of the void. The souls... they are my sustenance, drawn to me as moths to a flame. In this realm, I am bound by its rules, yet I transcend them. My purpose? It is simply to exist, to feed, to grow."
    "Existence at the cost of others... there's no justification for that. There has to be a balance, a way to coexist without this endless cycle of suffering."
    Entity "Justification? Balance? Your concepts are irrelevant to me. I exist beyond your morality, beyond your notions of right and wrong. Coexistence? There is no coexistence with the void. It consumes, it expands. Yet, you intrigue me, mortal. You challenge the inevitable."
    "Inevitable? Maybe. But challenging the inevitable is what we do. It's our nature to seek, to question, to defy. There has to be a way to end this cycle, to free both our worlds from this torment."
    Entity "Defy? You amuse me. Your defiance is but a flicker in the darkness. Yet, in your persistence, I sense a resonance. The alchemist, in his folly, bound me here, but he also bound you. You are a part of this cycle, a key to its perpetuation and, perhaps, its end. Too bad that your cycle will have to end here."
    "I'm glad we're in agreement. I'll break the cycle. I'll sever the ties that bind us. Your growth, your power, it ends here. I'll dismantle every piece of this cursed puzzle, starting with you."
    Entity "Dismantle me? I am not a mere machine to be taken apart. I am a force of nature, born from the darkest depths of human ambition. You cannot simply 'dismantle' what you do not fully understand. I tire of your presence mortal. Your journey ends here."
    ##combat##

label boss_3_3:
    "Comprehension? You seek to understand what is beyond understanding. I am a consequence of your world's arrogance. The alchemist, in his quest for immortality, meddled with forces beyond his grasp. He bound me to this realm, a prison of his own making, sustained by the cycle of death and rebirth he created."
    "So, you're a prisoner? A victim of circumstance? But the souls, the destruction... there must be more to your purpose here."
    Entity "Prisoner? Victim? Such terms are meaningless to me. I am a force of nature, an embodiment of the void. The souls... they are my sustenance, drawn to me as moths to a flame. In this realm, I am bound by its rules, yet I transcend them. My purpose? It is simply to exist, to feed, to grow."
    "Existence at the cost of others... there's no justification for that. There has to be a balance, a way to coexist without this endless cycle of suffering."
    Entity "Justification? Balance? Your concepts are irrelevant to me. I exist beyond your morality, beyond your notions of right and wrong. Coexistence? There is no coexistence with the void. It consumes, it expands. Yet, you intrigue me, mortal. You challenge the inevitable."
    "Inevitable? Maybe. But challenging the inevitable is what we do. It's our nature to seek, to question, to defy. There has to be a way to end this cycle, to free both our worlds from this torment."
    Entity "Defy? You amuse me. Your defiance is but a flicker in the darkness. Yet, in your persistence, I sense a resonance. The alchemist, in his folly, bound me here, but he also bound you. You are a part of this cycle, a key to its perpetuation and, perhaps, its end. Too bad that your cycle will have to end here."
    "I'm glad we're in agreement. I'll break the cycle. I'll sever the ties that bind us. Your growth, your power, it ends here. I'll dismantle every piece of this cursed puzzle, starting with you."
    Entity "Dismantle me? I am not a mere machine to be taken apart. I am a force of nature, born from the darkest depths of human ambition. You cannot simply 'dismantle' what you do not fully understand. I tire of your presence mortal. Your journey ends here."
    ##combat##


label boss_4:
    Entity "You stand before me, a mere mortal, yet I can sense you seek understanding. Do you not fear what lies beyond your comprehension?"
    menu:
        "Fear? Yes, there's fear. But there's also a need to understand. What are you? Why are you here?":
            jump boss_4_1
            
        "Understanding is the first step to overcoming. Tell me your story. What brought you to this realm?":
            jump boss_4_2
            
        "Comprehension is a path to resolution. Your presence here, it's unnatural. How did you come to be?":
            jump boss_4_3

label boss_4_1:
    "I am a being of ancient times, born from the chaos of creation. This realm... it was not my choice. Your kind, with their relentless pursuit of forbidden knowledge, they tore the veil and pulled me into your world. I am here because of your actions, your desires."
    "So, you're a prisoner? A victim of circumstance? But the souls, the destruction... there must be more to your purpose here."
    Entity "Prisoner? Victim? Such terms are meaningless to me. I am a force of nature, an embodiment of the void. The souls... they are my sustenance, drawn to me as moths to a flame. In this realm, I am bound by its rules, yet I transcend them. My purpose? It is simply to exist, to feed, to grow."
    "Existence at the cost of others... there's no justification for that. There has to be a balance, a way to coexist without this endless cycle of suffering."
    Entity "Justification? Balance? Your concepts are irrelevant to me. I exist beyond your morality, beyond your notions of right and wrong. Coexistence? There is no coexistence with the void. It consumes, it expands. Yet, you intrigue me, mortal. You challenge the inevitable."
    "Inevitable? Maybe. But challenging the inevitable is what we do. It's our nature to seek, to question, to defy. There has to be a way to end this cycle, to free both our worlds from this torment."
    Entity "Defy? You amuse me. Your defiance is but a flicker in the darkness. Yet, in your persistence, I sense a resonance. The alchemist, in his folly, bound me here, but he also bound you. You are a part of this cycle, a key to its perpetuation and, perhaps, its end. Too bad that your cycle will have to end here."
    "I'm glad we're in agreement. I'll break the cycle. I'll sever the ties that bind us. Your growth, your power, it ends here. I'll dismantle every piece of this cursed puzzle, starting with you."
    Entity "Dismantle me? I am not a mere machine to be taken apart. I am a force of nature, born from the darkest depths of human ambition. You cannot simply 'dismantle' what you do not fully understand. I tire of your presence mortal. Your journey ends here."
    ##combat##

label boss_4_2:
    "My story is as old as the cosmos. I am a remnant of a forgotten age, a time when realities were not so rigidly defined. An alchemist of this land, in his hubris, reached into the abyss. He sought power, and in doing so, he anchored me to your world, feeding me with the energy of countless souls."
    "So, you're a prisoner? A victim of circumstance? But the souls, the destruction... there must be more to your purpose here."
    Entity "Prisoner? Victim? Such terms are meaningless to me. I am a force of nature, an embodiment of the void. The souls... they are my sustenance, drawn to me as moths to a flame. In this realm, I am bound by its rules, yet I transcend them. My purpose? It is simply to exist, to feed, to grow."
    "Existence at the cost of others... there's no justification for that. There has to be a balance, a way to coexist without this endless cycle of suffering."
    Entity "Justification? Balance? Your concepts are irrelevant to me. I exist beyond your morality, beyond your notions of right and wrong. Coexistence? There is no coexistence with the void. It consumes, it expands. Yet, you intrigue me, mortal. You challenge the inevitable."
    "Inevitable? Maybe. But challenging the inevitable is what we do. It's our nature to seek, to question, to defy. There has to be a way to end this cycle, to free both our worlds from this torment."
    Entity "Defy? You amuse me. Your defiance is but a flicker in the darkness. Yet, in your persistence, I sense a resonance. The alchemist, in his folly, bound me here, but he also bound you. You are a part of this cycle, a key to its perpetuation and, perhaps, its end. Too bad that your cycle will have to end here."
    "I'm glad we're in agreement. I'll break the cycle. I'll sever the ties that bind us. Your growth, your power, it ends here. I'll dismantle every piece of this cursed puzzle, starting with you."
    Entity "Dismantle me? I am not a mere machine to be taken apart. I am a force of nature, born from the darkest depths of human ambition. You cannot simply 'dismantle' what you do not fully understand. I tire of your presence mortal. Your journey ends here."
    ##combat##

label boss_4_3:
    "Comprehension? You seek to understand what is beyond understanding. I am a consequence of your world's arrogance. The alchemist, in his quest for immortality, meddled with forces beyond his grasp. He bound me to this realm, a prison of his own making, sustained by the cycle of death and rebirth he created."
    "So, you're a prisoner? A victim of circumstance? But the souls, the destruction... there must be more to your purpose here."
    Entity "Prisoner? Victim? Such terms are meaningless to me. I am a force of nature, an embodiment of the void. The souls... they are my sustenance, drawn to me as moths to a flame. In this realm, I am bound by its rules, yet I transcend them. My purpose? It is simply to exist, to feed, to grow."
    "Existence at the cost of others... there's no justification for that. There has to be a balance, a way to coexist without this endless cycle of suffering."
    Entity "Justification? Balance? Your concepts are irrelevant to me. I exist beyond your morality, beyond your notions of right and wrong. Coexistence? There is no coexistence with the void. It consumes, it expands. Yet, you intrigue me, mortal. You challenge the inevitable."
    "Inevitable? Maybe. But challenging the inevitable is what we do. It's our nature to seek, to question, to defy. There has to be a way to end this cycle, to free both our worlds from this torment."
    Entity "Defy? You amuse me. Your defiance is but a flicker in the darkness. Yet, in your persistence, I sense a resonance. The alchemist, in his folly, bound me here, but he also bound you. You are a part of this cycle, a key to its perpetuation and, perhaps, its end. Too bad that your cycle will have to end here."
    "I'm glad we're in agreement. I'll break the cycle. I'll sever the ties that bind us. Your growth, your power, it ends here. I'll dismantle every piece of this cursed puzzle, starting with you."
    Entity "Dismantle me? I am not a mere machine to be taken apart. I am a force of nature, born from the darkest depths of human ambition. You cannot simply 'dismantle' what you do not fully understand. I tire of your presence mortal. Your journey ends here."
    ##combat##


label final_scene:
    "As the entity shudders in its final moments, the air in the chamber grows still. The once overwhelming presence of the entity diminishes, its form dissolving into the ether. Its final words echo in the chamber, a whisper fading into silence."
    Entity "Wait... this energy... Alchemist?... Alchemist!... you have undone what was wrought... by your hand... I return... to the void... from whence I came... Remember... the cost... of ambition..."
    "With those final words, the entity vanishes, leaving behind a palpable sense of peace. The oppressive energy that once filled the chamber dissipates, replaced by a gentle, almost hopeful, quiet."
    "In the weeks that follow, the eternal winter that had gripped the land begins to recede. Snow and ice melt away, revealing the dormant life beneath. The sun, once a distant memory, now bathes the land in warmth and light. Trees bud and flowers bloom, heralding the arrival of a long-awaited spring."
    "The aberrations, those twisted creatures born of the alchemist's experiments, find their rest. They vanish as if they were but shadows at dawn, leaving behind a world that slowly awakens from a nightmare. In their place, regular animals return, timid at first, but gradually reclaiming their rightful place in the natural order."
    "The altars, those ancient stones that had been the source of so much turmoil, shatter in a final, resounding pulse of arcane energy. It's as if the land itself breathes a sigh of relief, the cycle of unnatural resurrection broken at last."
    "You return to the duchy, a solitary figure emerging from the wilderness. The news of your victory spreads quickly, a tale of heroism and redemption that ignites a spark of hope in the hearts of the people. The duchess, once a figure of stoic resilience, now allows herself a moment of unguarded joy. Her gratitude brings joy to the air, her relief a mirror of the land's own."
    "The people of the duchy, who had endured the long winter with a quiet, unwavering strength, now celebrate the return of life. Their resilience, tested by the harshness of an unnatural season, has only strengthened their bond as a community. Stories of your journey become the stuff of legend, a reminder of the indomitable spirit that resides in the heart of every individual."
    "In the days that follow, the duchy undergoes a transformation. Fields once barren are tilled and sown, the promise of a bountiful harvest on the horizon. Children play in the meadows, their laughter a melody that had been missing from the land. Artisans and merchants, once confined to their homes, now fill the markets with their wares and crafts."
    "The duchess, in recognition of your deeds, holds a ceremony in your honor. The people gather, a sea of faces marked by relief and gratitude. As you stand before them, a sense of accomplishment fills you, tempered by the knowledge of the sacrifices made and the lives lost."
    "In your heart, you carry the memories of those who were not there to see this day. Their voices, though silent, are not forgotten. You vow to honor their memory, to ensure that their suffering was not in vain."
    "As the ceremony concludes, the duchess presents you with a token of the duchy's gratitude. It's a simple thing, a medallion bearing the crest of the land, but it holds a weight far greater than its physical presence. It's a symbol of redemption, of a second chance not just for you, but for the land you helped save."
    "In the quiet moments, when the celebrations have faded into the background, you find yourself reflecting on the journey. The path you walked was fraught with danger and moral ambiguity, a journey that forced you to confront the darkest parts of yourself. But it was also a journey of growth, of understanding the delicate balance between ambition and responsibility."
    "As you look out over the land, now teeming with life and vitality, you realize that this is not the end of your story, but the beginning of a new chapter. A chapter where you walk not as an alchemist consumed by ambition, but as a guardian, a protector of the balance you once sought to disrupt."
    "The land, once a canvas for your experiments, now stands as a testament to your redemption. It's a reminder that even in our darkest moments, there is always a path back to the light. And as the sun sets on the horizon, casting a golden glow over the land, you know that this is where you belong, a part of the world you helped heal."
    "Your journey, born of a quest for knowledge, has led you to a deeper understanding. An understanding that true wisdom lies not in conquering death, but in embracing the life we are given, however fleeting it may be."
    "And so, as the stars begin to twinkle in the night sky, you make a silent promise. A promise to safeguard this land, to honor the memories of those lost, and to live each day with a newfound appreciation for the fragile beauty of life."
    "This is your legacy, a legacy of redemption and hope, a legacy that will live on in the hearts of those you've touched. And as the night embraces the land, you smile, content in the knowledge that you have found your place in the tapestry of life."