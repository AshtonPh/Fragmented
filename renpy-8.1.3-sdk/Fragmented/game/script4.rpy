
define shopkeeper = Character("Shopkeeper", color = "#c8c8c8ff")
define bartender = Character("Bartender", color = "#7f9bffee")


label main_village:

    scene main_village with fade
    "The village, once a bustling hub of trade and laughter, now holds a somber atmosphere. The streets are nearly empty, save for a few haggard souls."

    "You can visit the local shop, or head into the local tavern. You also know that you should head to the alchemist’s lair as soon as possible."

    menu:
        "Visit the local shop for supplies.":
            jump village_shop
        "Go to the tavern to gather information.":
            "The tavern is dimly lit, the air thick with the smell of stale ale and whispered secrets."
            jump tavern_gossip

        "It’s time to visit the lair":
            jump path_to_hell

label village_shop:

    scene village_shop with fade
    "The shop is a cozy, eclectic space, filled with an array of items from practical tools to curious trinkets. The air smells of dried herbs and old wood."

    "The shopkeeper, a stout man with a warm smile, greets you from behind the counter."

    shopkeeper "Ah, a traveler! What can I get for you today?"

    menu:
        "I'm looking for healing potions.":
            "He presents a selection of vials."
            shopkeeper "We have standard healing potions for 10 gold, and the stronger elixirs for 20 gold. Which would you prefer?"
            menu:
                "Standard Healing Potion (10 gold)":
                    $ player_gold -= 10
                    $ player_healing_potions += 1
                    "You hand over the coins and take the potion, feeling reassured by its presence."
                "Stronger Elixir (20 gold)":
                    $ player_gold -= 20
                    $ player_stronger_elixirs += 1
                    "You exchange more coins for the potent elixir, hoping it'll come in handy."

        "Do you have any special arrows?":
            "He shows you a variety of arrows."
            shopkeeper "All arrows come as a sheath of twelve. We sell standard arrows for five gold, have fire-tipped arrows for 15 gold a set, and ice arrows for 20 gold a set. Your choice."
            menu:
                "Standard Arrows (5 gold)":
                    $ gold -= 5
                    $ arrow_count += 5
                    "You can never go wrong with good old regular arrows. They’re cheap and always serve you well."
                "Fire-Tipped Arrows (15 gold)":
                    $ gold -= 15
                    $ player_fire_arrows += 5
                    "You purchase the fire-tipped arrows, feeling their warmth even through the quiver."
                "Ice Arrows (20 gold)":
                    $ gold -= 20
                    $ player_ice_arrows += 5
                    "You opt for the ice arrows, their tips glistening coldly."

        "Any potions for enhancing abilities?":
            "His eyes gleam as he presents two potions."
            shopkeeper "For the discerning adventurer, I have a Strength Potion and an Agility Potion, each for 25 gold."
            menu:
                "Strength Potion (25 gold)":
                    $ gold -= 25
                    $ player_strength_potion = True
                    "You purchase the Strength Potion, though you hope you won’t need it anytime soon."
                "Agility Potion (25 gold)":
                    $ gold -= 25
                    $ player_agility_potion = True
                    "You choose the Agility Potion, anticipating the swiftness it will grant."

        "That’ll be all, thanks."

        "With your purchases complete, you thank the shopkeeper and step back into the village, better equipped for your journey."

    return


label tavern_gossip:

    scene village_tavern with fade
    "The tavern is a bustling hub of activity, with patrons of all sorts sharing tales and drinks. The walls are adorned with old banners and the light from the hearth casts a warm glow over the wooden tables."

    "You find a seat near the back, a perfect spot for eavesdropping."

    menu:
        "Eavesdrop on the patrons.":
            "You lean back and tune into the conversations around you."
            "One table discusses a recent monster sighting near the old bridge, while another group argues about the best way to avoid the alchemist's cursed creatures."
            "A lone traveler at the bar mutters about barely escaping a horde of creatures near Greenfield."
            return
        "Ask the bartender for an ale and information.":
            "You approach the bartender, a burly man with a friendly demeanor."
            bartender "What'll it be? Ale?"
            "Just an ale, please."
            $ gold -= 2
            "He pours you a frothy ale. You take a sip, savoring the rich flavor. Before you know it, you’ve downed the whole flagon."
            bartender "Ha! I haven’t seen someone with vigor like that in a long time. Stay as long as you’d like!"

        "Leave the tavern":
            jump main_village







label path_to_hell:
    "The path to the alchemist's lair is fraught with danger. The very air seems to thicken with malice as you step onto the trail."

    "The trees are gnarled, and the ground beneath your feet crunches with a mixture of frost and ash. The silence is oppressive, broken only by the occasional distant scream."

    "You steel yourself for the journey ahead, knowing that each step takes you closer to the heart of darkness."

    "The path is not straightforward; it twists and turns, leading you through a landscape that seems designed to confuse and disorient."

    "But you press on, determined to confront the alchemist and end his reign of terror."

    return
