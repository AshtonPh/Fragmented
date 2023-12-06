label old_mill_monster_encounter:

    "You and the Duchess cautiously step through the creaking doorway, your senses alert to any movement."

    duchess "Be on your guard. We don't know what lies within."

    "As you move deeper into the mill, the floorboards suddenly give way above you with a deafening crack."



    "You're thrown to the ground as the ceiling collapses, sending up a cloud of dust and splinters as the wood crashes down. The Duchess is knocked back, struggling to regain her footing."

    "From the gaping hole in the floor, a monstrous form emerges. It's a grotesque amalgamation of flesh and darkness, its body twisted and malformed. Its skin is a sickly green, covered in pulsating boils and oozing sores."

    "The creature's eyes are like voids, black and endless, fixated on you with a malevolent hunger. Its mouth, a jagged maw of razor-sharp teeth, opens to emit a guttural, chilling hiss."

    monster "YOUUUUuuu..."

    "The air grows cold, the very atmosphere tainted by the creature's malevolent presence. You feel a primal fear clawing at your heart, but you steel yourself, gripping your weapon tightly."

    "The Duchess, recovering from the initial shock, stands beside you, her expression one of grim determination."

    duchess "We must end this abomination."

    "The creature lunges forward, its movements a blur of malice and fury."

    $ combat = "millMonster"

    $ change_bar1_values(player.maxhp, player.maxhp, 0.1, 0.7, "Player")
    $ change_bar2_values(1000, 1000, 0.5, 0.0, "Hideous Monster")

    show screen bar1
    show screen bar2
    jump combat


label post_monster_fight:

    "The creature lies defeated at your feet, its twisted form slowly dissolving into shadow and mist. The air feels lighter as if a great weight has been lifted."

    "You and the Duchess stand in the aftermath, catching your breath, the adrenaline of the fight still coursing through your veins."

    duchess "You fought bravely. This creature... it was a blight upon our land."

    mc "It's over now. The mill... and your people... are safe."

    "The Duchess looks around the old mill, her gaze lingering on the remnants of the creature."

    duchess "Safe? Ha. This victory... it's a step towards reclaiming our home. But there's still much to be done."

    mc "We'll face whatever comes. Together."

    "The Duchess nods. Together, you exit the mill, leaving the shadows of the ruined mill behind."
        jump back_with_duchess

label back_with_duchess:
    "The battle at the old mill has left its mark, both physically and emotionally. As you walk back through the forest with the Duchess, there's a sense of shared accomplishment and relief."
    duchess "That was a fearsome creature. Your courage in the face of such evil... it gives me hope."
    "The forest around you seems to have taken on a new life, the sunlight filtering through the trees a little brighter, the air a bit fresher."
    "The Duchess stops, turning to face you. She reaches into her cloak and pulls out a small, intricately crafted ring."
    duchess "I want you to have this. It belonged to my husband, the duke. He was a brave man, much like you. I believe he would have wanted you to have it."
    "The ring is elegant, yet sturdy, crafted from silver with a small, but vibrant, gemstone set in the center."
    duchess "There's still much to do. The land is healing, but the scars run deep. We'll need strong hearts and willing hands to rebuild."
    mc "I'll be here, every step of the way. Whatever you need, you can count on me."
    "The Duchess smiles, a genuine expression of gratitude and respect."
    duchess "Thank you. With your help, I believe we can restore our duchy to its former glory, and perhaps... find even greater peace."
    "The walk back is filled with plans and promises, a shared vision of a brighter future. As you part ways at the edge of the forest, you feel a renewed sense of purpose and a deep connection to the land and its people."
        jump main_village
        





