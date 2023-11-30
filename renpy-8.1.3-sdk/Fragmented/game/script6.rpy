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
        ##Only if with the assistant##
        "Talk to the Alchemist’s assitant." if assistant = True:
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

   

label battle_ice_incubus:
    "As you step forward, the ice incubus emits a chilling howl, a sound that seems to freeze the very air. Its movements are swift and graceful, each step leaving a trail of frost in its wake."

    "You ready your weapon, your breath visible in the cold air. The incubus lunges, its claws extended, aiming to ensnare you in its icy grasp."

##Insert Combat##

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
        "Vial 1":
            jump vial_1

        "Vial 2":
            jump vial_2

        "Vial 3":
            jump vial_3

        "Vial 4":
            jump vial_4

        "Vial 5":
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
            jump examine_vials:

label vial_2:
    "A deep, crimson fluid that bubbles slowly. You notice that where it bubbles, tiny sparks of light appear and disappear."
        menu:
            "Take the vial":
                "You grab the vial and slip it into your bag, hoping it will serve you well."
                $ vial_2 = True
                    jump explore_experimental_area

            "Look at the other vials":
                jump examine_vials:

label vial_3:
    "A clear liquid with a suspended, glowing orb in the center. The orb pulsates gently, emitting a soft, warm light."
        menu:
            "Take the vial":
                "You grab the vial and slip it into your bag, hoping it will serve you well."
                $ vial_3 = True
                    jump explore_experimental_area

            "Look at the other vials":
                jump examine_vials:

label vial_4:
    "A dark, viscous substance that clings to the sides of the vial. It has an almost gravitational pull, drawing your gaze inward."
        menu:
            "Take the vial":
                "You grab the vial and slip it into your bag, hoping it will serve you well."
                $ vial_4 = True
                    jump explore_experimental_area

            "Look at the other vials":
                jump examine_vials:

label vial_5:
    "A vial filled with a gas rather than a liquid. The gas shifts colors continuously, creating a mesmerizing kaleidoscope effect."
        menu:
            "Take the vial":
                "You grab the vial and slip it into your bag, hoping it will serve you well."
                $ vial_4 = True
                    jump explore_experimental_area

            "Look at the other vials":
                jump examine_vials:

label read_writings:
    "You turn your attention to the parchments and scrolls, each one a window into the alchemist's mind."

    menu:
        "Scroll 1":
            jump Scroll_1
        "Scroll 2":
            jump Scroll_2
        "Scroll 3":
            jump Scroll_3
        "Scroll 4":
            jump Scroll_4

        "Look at other things in the area":
            jump explore_experimental_area:

   
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
            "Turn to the alchemist's assistant" if assistant = True:
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

label inside_door_2:

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
    