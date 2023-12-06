
# upper level initial narration + variable initialization
label explore_upper_levels:
    

    "As the staircase ends, you step into a surprisingly serene and well-lit space, a stark contrast to the lair's lower levels. The upper floor unfolds before you, divided into distinct areas, each revealing a different aspect of the alchemist's life."

    "To your left, a warm, inviting glow draws your attention. A large bed, its covers neatly arranged, sits against the wall."

    "Nearby, a desk is cluttered with an array of papers, ink pots, and quills, suggesting a space of deep thought. Bookshelves line the walls, filled with an eclectic mix of books. Among the titles, you notice both alchemical treatises and classic poetry. Personal artifacts, like framed sketches and small trinkets, are scattered throughout, giving the room a lived-in feel."

    "Ahead, the grandeur of a library unfolds. Towering shelves, filled with ancient tomes and rare manuscripts, reach up to the high ceiling. The air carries the distinct scent of old parchment and leather."

    "Some books, bound in unusual materials, catch your eye with their strange titles. Amidst the shelves, a large globe and several intricate orreries stand, hinting at a fascination with the celestial."

    "To your right, an astral observatory commands your attention. A brass telescope, its lens pointing towards a skylight, allows a clear view of the night sky."

    "The walls are adorned with charts and maps of constellations, and various astrological instruments are meticulously arranged on tables. The setup suggests a deep connection with the cosmos, possibly influencing the alchemist's work."

    "In a corner, a sanctuary of restorative magic offers a tranquil retreat. Lush green plants thrive, nourished by the soft glow of crystals embedded in the walls."

    "The gentle sound of a fountain creates a soothing atmosphere, and the air feels fresh and invigorating. This nook, with its peaceful ambiance, seems designed for healing and reflection."

    "A sense of déjà vu washes over you. The room, a harmonious blend of scholarly pursuit and personal comfort, seems both alien and intimately familiar."

    jump upper_level_choice

###
# main upper level menu
###
label upper_level_choice:
    menu:
        "Examine the Desk":
            jump examine_desk
        "Look at the Bookshelves":
            jump look_bookshelves
        "Inspect the Bed":
            jump inspect_bed
        "Inspect the Bedside Table" if small_table:
            jump personal_artifacts
        "Go to Library":
            jump library
        "Go to Observatory":
            jump observatory
        "Go to Sanctuary":
            jump sanctuary
        "Return to the main chamber":
            jump alchemists_lair
        ##### LOOK AT ME EHEHHEHEHHE plz
        # todo "return to lower level"
        

###
# upper level section
###
label examine_desk:
    "The desk is a landscape of organized chaos. Amidst the clutter, a letter, mid-sentence, draws your attention."

    "\"Dearest Elenor, "

    "As I delve deeper into the unknown, I find myself at a crossroads between moral obligation and the pursuit of knowledge. The weight of my actions grows heavier with each passing day...\""

    "The letter trails off, leaving an unfinished thought hanging in the air. Beside it, a framed portrait of a woman with kind eyes and a gentle smile evokes an unexplained warmth in your heart."

    jump upper_level_choice

label look_bookshelves:
    "The bookshelves are a diverse collection. A well-worn book titled \"The Ethereal Connection\" stands out. Flipping through, a passage is heavily annotated:"

    "\"Memory is the anchor of the soul. But what becomes of a man when those memories are unmoored? Is he still the same, or does he become a ship lost at sea?\""

    jump upper_level_choice

label inspect_bed:
    "The bed, with its inviting covers, holds a sense of solitude. A journal on the bedside table, open to the latest entry."

    "\"Tonight, the silence is deafening. I long for the days of laughter and love, now just echoes in the corridors of my mind. What have I sacrificed in my quest for eternity?\""

    "Besides the Journal, it looks like there are a few other personal artifacts on the bedside table."

    jump upper_level_choice

label personal_artifacts:
    "Among the personal artifacts on the bedside table, a locket with a faded photograph of a woman with kind eyes and a gentle smile catches your eye."
    
    "The back of the locket is engraved with \"To my Alaric, forever yours, Elenor.\" A collection of rare coins from distant lands lies nearby, alongside a small wooden box. Inside the box, a lock of golden hair tied with a blue ribbon and a perfectly preserved violet rest, symbols of a cherished memory."

    jump upper_level_choice

###
# libary section
###
label library:
    if library_intro:
        "In the library, a sense of intellectual curiosity permeates the air. The room is a testament to a lifetime of study, with shelves lined with books on various subjects, from alchemy to ancient history. The atmosphere is one of quiet reflection, a sanctuary for a mind that thirsts for knowledge."
        $ libary_intro = False

    if library_time == 2:
        "As you continue to explore the library, a particular book catches your eye, almost as if calling out to you. It's an ancient grimoire, its cover worn and pages yellowed with age. The book exudes a subtle aura of power, suggesting that it contains knowledge beyond ordinary understanding."

    menu:
        "Examine Alchemical Texts":
            $ libary_time += 1
            jump alchemical_texts
        "Look at the Historical Volumes":
            $ libary_time += 1
            jump historical_volumes
        "Inspect the Personal Notes":
            $ libary_time += 1
            jump personal_notes
        "Examine Grimoire" if libary_time >= 2:
            jump grimoire
        "Return to Upper Level":
            jump upper_level_choice

label alchemical_texts:
    "A section dedicated to alchemy catches your eye. One particular tome, \"The Boundaries of Life and Death,\" lies open." 
    
    "A passage highlighted in the margins reads: \"In our quest to conquer death, we must be wary of losing ourselves. For in bending the laws of nature, do we not risk unraveling the very fabric of our being?\""

    jump library

label historical_volumes:
    "The historical volumes are a mix of common knowledge and obscure lore. A book titled \"Forgotten Civilizations\" is bookmarked."
    
    "Flipping to the marked page, you read: \"The lost city of Kethra, renowned for its advancements in arcane sciences, vanished without a trace. Rumors persist of a cataclysmic experiment that tore the city from reality itself.\""

    jump library

label personal_notes:
    "Scattered among the books are personal notes and journals. One journal, filled with meticulous handwriting, contains an entry that stands out."
    
    "\"Week 34: The experiment has been moving at a lightning fast pace, but at what cost? My dreams are haunted by the faces of those I've used in my research. Can the ends truly justify the means?\""

    jump library

# todo, create spells for the grimoire
label grimoire:
    "You carefully open the grimoire. The pages are filled with arcane symbols and complex incantations. It's clear that this book is a repository of powerful spells. As you leaf through it, three spells stand out, each marked with a distinct symbol."

    # second reminder, todo, create spells for the grimoire
    "These spells will be added in a later update for the game."

    jump library

###
# observatory section
###
label observatory:
    if observatory_intro:
        "The observatory is a sanctum of celestial wonder, a place where the alchemist sought to bridge the gap between the earthly and the ethereal."
        
        "As you step into the room, the air feels charged with a sense of discovery and ancient wisdom. The dome above is a masterful representation of the night sky, each star and constellation painted with meticulous care, glowing faintly in the dim light."
        
        "The room is circular, with the walls lined with bookshelves, cabinets, and various astronomical instruments. The centerpiece is a grand brass telescope, its lens aimed skyward, as if in eternal contemplation of the cosmos."

        $ observatory_intro = False

    menu:
        "Examine Star Charts":
            $ more_frantic_annotations = True
            jump star_charts
        "Examine Frantic Annotations" if more_frantic_annotations:
            jump frantic_annotation_lore
        "Examine Telescope":
            jump telescope
        "Return to the Upper Level":
            jump upper_level_choice

label star_charts:
    "The walls are adorned with detailed star charts and celestial maps, each one a testament to countless hours of observation and study. The charts are annotated with notes and symbols, indicating special interest in certain celestial events and alignments."

    "Some of the annotations seem to be written frantically, almost scarred into the wall."

    "\"The dance of the celestial bodies is a symphony of cosmic proportions. Each planet, each star, plays its part in a grander scheme, a pattern that holds the key to transcending the mundane.\""
    
    "\"Tonight, as Mars aligns with Jupiter, I sense a convergence of energies, a moment ripe for harnessing the essence of the cosmos. My experiments must align with this celestial event; the potential is too great to ignore...\""

    jump observatory

label telescope:
    "As you approach the telescope, you notice the finer details: the delicate gears that allow for precise adjustments, the smoothness of the rotating base, and the faint scent of oil used for maintenance." 
    
    "Looking through the eyepiece, you are greeted with a breathtaking view of the night sky, a canvas of infinite depth and beauty. The experience is almost spiritual, connecting you to the vastness of the universe and the mysteries it holds."

    jump observatory

label frantic_annotation_lore:
    "As you examine closer you see more scribblings written across the charts."

    "YES I'VE DONE IT...I FOUND THE KEY...THE ALTARS"

    jump observatory

###
# sanctuary section
###
label sanctuary:

    if sanctuary_intro:
        "The sanctuary unfolds before you like a forgotten chapter from a dream." 
        
        "Its high vaulted ceilings are adorned with frescoes depicting celestial bodies and arcane symbols, each brushstroke a breath of a bygone era of mysticism." 
        
        "The air is tinged with the scent of ancient incense, mingling with the faint aroma of old parchment and wax. The stained glass windows cast a kaleidoscope of colors across the room, illuminating the dust motes that dance in the sunbeams."

        "The shelves lining the walls are a trove of esoteric knowledge, filled with tomes bound in leather and strange artifacts whose purposes are as mysterious as their origins."

        $ sanctuary_intro = False

    menu:
        "Inspect Tomes":
            jump leather_tomes
        "Inspect Artifacts":
            jump sanctuary_artifacts
        "Return to Upper Level":
            jump upper_level_choice

label leather_tomes:
    "You read a tome."

    "\"Beneath the veil of reality lies a truth so profound that it threatens to unravel the mind. I have danced with the shadows at the edge of understanding, each step a delicate balance between enlightenment and madness."

    "The secrets I have uncovered are a burden no mortal was meant to bear, yet I cannot turn away. The path of the alchemist is lonely, for we walk where others dare not tread...\""

    jump sanctuary



label sanctuary_artifacts:

    "Among the artifacts, a set of crystal vials catches your eye. Each vial contains a swirling, luminescent substance, their colors shifting like the northern lights. As you touch one, a surge of emotions washes over you - joy, sorrow, fear, and wonder, all blending into a symphony of human experience."
    
    "Another artifact, a small, intricately carved box, seems to hum with a hidden energy, its surface adorned with symbols that speak of protection and containment."

    jump sanctuary