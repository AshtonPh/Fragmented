define mc = Character("????")
label start:
    # Scene starts with the snow-covered wasteland.
    scene bg_wasteland
    with fade

    "The screen fades in from black, revealing a snow-covered wasteland. The wind howls eerily, its mournful wails echoing across the vast expanse of white. The relentless snowstorm rages on, each flake dancing whimsically before merging into the blanket beneath. The air is thick with the scent of frost and desolation."

    show altar with dissolve
    "A massive stone altar stands defiantly amidst the sea of snow. Chains dangle from its sides, their ends embedded in the frozen ground. At the center of the altar, a lone figure stirs, surrounded by intricate, glowing runes carved into the stone."

    "Your vision is blurred, and a sharp, pulsating pain thunders behind your eyes. Your body feels heavy, and an overwhelming cold numbs your senses. As your eyes adjust, the world around you starts to take form."

    mc "Wh... where am I?"

    "Your voice sounds foreign to your own ears, echoing back to you from the surrounding wasteland. You try to move, but your limbs feel sluggish, as though they've been weighed down."

    show bg_wasteland_pan with dissolve
    "The camera pans upwards, revealing an endless stretch of snow-covered plains, with the ruins of ancient buildings jutting out like skeletal fingers trying to grasp at the heavens. The sky overhead is a bleak shade of grey, with no sun in sight."

    "From the distance, you hear a faint growl, followed by the sound of shuffling feet. Shadows move beyond the curtain of the snowstorm."

    "The wind carries whispers of lament, stories of a land once vibrant, now reduced to a frozen hellscape. The Alchemist's experiments, they murmur, turned paradise into purgatory."

    show statue with dissolve
    "On your left, half buried in snow, lies a broken statue of a child, its face twisted in a silent scream. On your right, a tattered flag flutters weakly – an emblem of a kingdom or clan, perhaps, but its insignia has been weathered away."

    "As you attempt to stand, memories rush back, fragmented and disjointed. Flashes of a lavish chamber, shimmering vials filled with glowing liquids, and the echoing laughter of a man consumed by his obsession."

    mc "Who am I? What has happened here?"

    show bg_castle with dissolve
    "To the North, the snow begins to disperse, revealing a path leading to a dilapidated castle, its spires and towers gnawed away by time and neglect. But there's a magnetic pull, an instinctive need to move towards it."

    "The growls grow louder, more insistent."

    show monsters with dissolve
    "The remnants of the Alchemist's creations lurk in the shadows, souls trapped in monstrous forms, forever damned by their creator's insatiable thirst for power."

    "Emerging from the snowstorm, you see the grotesque figures of the failed experiments. Some resemble beasts with twisted human features, while others are more humanoid but with limbs and features grotesquely out of proportion. Their eyes, however, tell a story of pain, confusion, and anger."

    "Without thinking, your hand moves to your side, fingers wrapping around the hilt of a weapon you didn't know you possessed. It feels right, familiar."

    mc "I need to defend myself. But... I need answers. First, this castle. It beckons."

    menu:
        "Choose your weapon:"
        "A short sword":
            $ weapon = "short sword"
            mc "I feel the weight of a short sword by my side. It's sharp and ready for combat."
        "A Long Bow":
            $ weapon = "long bow"
            mc "A long bow is strapped to my back, with a quiver full of arrows. It's perfect for long-range attacks."
        "A mage's staff":
            $ weapon = "mage's staff"
            mc "A mage's staff is in my hand. It pulses with arcane energy, ready to unleash its power."
    
    jump combat

