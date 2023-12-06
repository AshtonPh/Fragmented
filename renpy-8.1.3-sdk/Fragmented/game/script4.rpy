
define shopkeeper = Character("Shopkeeper", color = "#c8c8c8ff")
define bartender = Character("Bartender", color = "#7f9bffee")
define assistant = Character("Assistant", color = "#7fffffee")


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
                    if gold.count >= 10:
                        $ gold.use(10)
                        $ standard_health_potion.add_count(1)
                        $ inventory.add_item(standard_health_potion)
                        "You hand over the coins and take the potion, feeling reassured by its presence."
                    else:
                        "You don't have enough gold for that."
                "Greater Elixir (20 gold)":
                    if gold.count >= 20:
                        $ gold.use(20)
                        $ greater_elixir.add_count(1)
                        $ inventory.add_item(greater_elixir)
                        "You hand over the coins and take the elixir, feeling its power thrum through your fingers."
                    else:
                        "You don't have enough gold for that."
                "Nevermind.":
                    pass
            jump village_shop
        "Do you have any arrows":
            "He shows you a variety of arrows."
            shopkeeper "All arrows come as a sheath of twelve. We sell standard arrows for five gold."
            menu:
                "Standard Arrows (5 gold)":
                    if gold.count >= 5:
                        $ gold.use(5)
                        $ arrows.add_count(12)
                        "You hand over the coins and take the arrows, feeling their weight in your hands."
                    else:
                        "You don't have enough gold for that."
                "Nevermind.":
                    pass
            jump village_shop
                    


        "Any potions for enhancing abilities?":
            "His eyes gleam as he presents two potions."
            shopkeeper "For the discerning adventurer, I have a Strength Potion and an Agility Potion, each for 25 gold."
            menu:
                "Strength Potion (25 gold)":
                    if gold.count >= 25:
                        $ gold.use(25)
                        $ strength_potion.add_count(1)
                        $ inventory.add_item(strength_potion)
                        "You purchase the Strength Potion, though you hope you won’t need it anytime soon."
                    else:
                        "You don't have enough gold for that."
                "Agility Potion (25 gold)":
                    if gold.count >= 25:
                        $ gold.use(25)
                        $ agility_potion.add_count(1)
                        $ inventory.add_item(agility_potion)
                        "You purchase the Agility Potion, though you hope you won’t need it anytime soon."
                    else:
                        "You don't have enough gold for that."
            jump village_shop
        "That’ll be all, thanks.":
            jump thats_all

label thats_all:
"With your purchases complete, you thank the shopkeeper and step back into the village, better equipped for your journey."
    jump main_village



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
            $ gold.use(1)
            "He pours you a frothy ale. You take a sip, savoring the rich flavor. Before you know it, you’ve downed the whole flagon."
            bartender "Ha! I haven’t seen someone with vigor like that in a long time. Stay as long as you’d like!"

        "Leave the tavern":
            jump main_village
        
        "Seek out the alchemist's former assistant.":
            "You scan the tavern and spot a nervous-looking individual in a corner, surrounded by a dozen or so empty ales."
            "Approaching cautiously, you notice he’s wearing dirty and tattered laboratory garb. He looks up at you, dark circles beneath his eyes."
            jump assistant_encounter

label assistant_encounter:
        "You sit across from the assistant, a man with a weathered face marked by years of toil and worry. His eyes, deep-set and shadowed, narrow slightly as he studies your features. There's a certain intelligence in his gaze, reminiscent of a scholar who has seen much yet understands little of the world's whims."
        "His hair, unkempt and streaked with grey, falls haphazardly over his forehead. His hands, rough and stained with ink, fidget nervously on the table as he leans in, an air of curiosity mingling with caution in his demeanor."

        assistant "Have we met before? You seem... familiar."

        if seal == True:
        # So this is supposed to be two separate options– he talks to you willingly if you have the seal. If you don’t you have to buy an ale from the barkeep to bring him, but I’m not quite sure how to accomplish that in code## 
            "Perhaps… I don’t remember much, I recently woke up with amnesia. I’m here on the duchess’s order, trying to fix whatever the hell is going on here."
            "You present the seal of the duchess, a symbol of authority and trust. The assistant's eyes widen slightly, his demeanor changing instantly. He seems to snap out of his drunken stupor, straightening his back and adjusting his clothes."
            jump seal_assistant
        else: 
            "I don't think so. I'm here to learn about the alchemist's experiments."
            assistant "Fuck off! I've got no time for strangers poking around in my business. Unless you're bringing me ale, I've got nothing to say to you."
            #then either you leave or bring him an ale##
            jump tavern_ale

label tavern_ale:
    menu: 
        "Leave the tavern":
            jump main_village

        "Go get the man an ale":
            jump assistant_questions

        ##Sorry nam you’ll have to figure out some way to make you able to buy the ale for the assistant and not yourself##

label seal_assistant:

    assistant "Ah, I see. Working for the duchess, are you? Then I suppose I should help. What do you need to know?"

    jump assistant_questions

label assistant_questions:
    menu:
        "What kind of experiments were conducted there?":
            assistant "Experiments that defied nature. We were merging flesh and machine, bending the will of the elements, transmuting the lives of the flora and fauna."
            "His voice drops to a whisper."
            assistant "But at the heart of it all was the pursuit of deathlessness, a quest that consumed the alchemist."

        "Where did all of this happen?":
            assistant "Ah, the lair. It's a place of twisted magic and dark science. Hidden deep within the cursed lands, it's a labyrinth of his madness."
            "He shivers slightly."
            assistant "The lair is protected by his creations, each more grotesque than the last."
    

        "Was there any success in these experiments?":
            assistant "Success and failure are intertwined. Yes, there were breakthroughs, but at a terrible cost. The alchemist lost his humanity in the process. His failed experiments couldn’t be contained– they started prowling the night, terrorizing the people and changing the landscape."
            "He looks at you intently."
            assistant "He became something else, something... inhuman."

        "How can I find the alchemist now?":
            assistant "After I found out the true nature of the experiments, he cast me out when I protested his methods. He attempted one final experiment, to become a being who rules over death itself. He hasn’t been seen nor have more aberrations come from his lair, so god willing the experiment killed him."
            assistant "Still, it would be worth it to visit his lair. We might be able to glean some information of what happened to him, or how to stop his nightmares from terrorizing the populace."

            menu: 
                "Will you come with me to the alchemist’s lair?":
                    jump path_to_hell_with_assistant
                "Thanks for the information. I’ll be heading out now":
                    jump main_village

            return


label armory:

    "The armory is a testament to the Duchy's once-great power. Rows of weapons line the walls, each piece gleaming under the torchlight. Shields and armor stand in silent vigil, waiting for their next call to battle."

    "Sir Hendrick gestures towards a rack of particularly impressive items."

    sir_hendrick "Choose wisely. These are not ordinary weapons. They've been enchanted to aid in our fight against the darkness."

    menu:
        "A magic sword, glowing with an inner light.":
            "You pick up the sword, feeling its power thrum through your fingers. It's light, yet deadly, a perfect balance of grace and strength."
            $ inventory.add_item(magic_sword)
            "Sir Hendrick nods approvingly."
            sir_hendrick "A fine choice. That sword has felled many a foul creature."

        "A new magic staff, pulsing with arcane energy.":
            "The staff calls to you, its energy resonating with your own. As you grasp it, a surge of power flows through you, awakening latent abilities."
            $ inventory.add_item(arcane_staff)
            "Sir Hendrick smiles."
            sir_hendrick "Ah, a wise choice for those who understand the mysteries of magic."


    menu:

        "I'll take on this challenge. Where was it last seen?": 
            sir_hendrick "Brave decision. The last sighting was near the old mill in the woods. Be cautious, it's a dangerous foe."

            jump monster_preparation_2
 
        "I think I’ll check out the village first":
            sir_hendrick "No worries– please, if you have time come back and give us any assistance you can spare but I understand that you have an important mission that comes first. Stay safe."

            jump main_village

        "I’m going to head to the Alchemist’s lair before I do anything first, see if I can glean any important information.":
            sir_hendrick "Of course. It’s a dangerous path, I wish you the safest of travels and godspeed to you. Feel free to come back when you’re done– we could always use more help."
            jump path_to_hell

label monster_preparation_2:
    duchess "Ah, I'm glad you've come. I've decided to join the hunt for this beast. It's time I took a more active role in protecting my people."

    mc "Your Grace, are you sure? It's dangerous out there."

    duchess "I must. Since my husband's disappearance, the burden of leadership has been heavy. I’ve had to show my people that I'm a ruler, not just in title but in action."

    menu:
        "I admire your courage.":
            duchess "Courage is born from necessity. I've learned that leading a Duchy in these troubled times requires more than just words."
       
        "It's risky, but I'll ensure your safety.":
            duchess "Thank you, but remember, we're in this together. I'm not just a figurehead; I've trained for combat too. My late husband wanted to make sure that I could always protect myself, even when he wasn’t around. It seems he had good intuition, the bastard."
    "The duchess lets loose a morbid chuckle."
    "You both prepare to leave for the old mill, the location of the last sighting of the beast."

    jump duchess_monster_hunt_journey


label duchess_monster_hunt_journey:

    "The forest is dense, the canopy above a patchwork of green and gold. Sunlight filters through, casting dappled shadows on the path ahead. The leaves ahead are so dense that they bow under the weight of the snow, trembling as they suspend the heavy blanket above the ground, keeping it miraculously dry and clear."

    duchess "This land... it was once so full of life and laughter. Now, it's a shadow of its former self."

    mc "It must be hard, seeing it change like this."

    duchess "It is. Every wilted flower, every withered tree... they're like echoes of the past."

    menu:
        "What was it like before all this?":
            duchess "It was vibrant. The markets were bustling, children played in the streets, and the nights were filled with music and dance."
            mc "It sounds wonderful."
            duchess "It was. But now, those memories are bittersweet."
            "You both continue walking, the Duchess lost in her thoughts."

        "How do you cope with such loss?":
            duchess "One day at a time. I focus on what I can do, not what I've lost."
            mc "That's a strong way to live."
            duchess "Strength is all I have left."
            "The Duchess's gaze is distant, reflecting memories of a time long passed."

        "We'll bring back some of that life.":
            duchess "I hope so. The people need something to believe in again."
            mc "They believe in you."
            duchess "I'm just one person. But together, maybe we can make a difference."
            "Her words carry a weight, a sense of determination and hope."

    "The path winds through the forest, the silence broken only by the occasional rustle of leaves and distant bird calls."

    duchess "Tell me, what drives you in this quest? It's rare to see such dedication."

    mc "I’m not sure. I can’t remember much, but hearing tales of the alchemist’s cruelty and insanity makes me feel responsible for bringing peace to this land. I am driven by something that stirs deep within me. Your guess is as good as mine as to what it is or where it’s from."

    menu:
        "Tell me more of your story":
            duchess "My story is one of duty and sacrifice. Since my husband vanished, I've had to be both a fighter  and ruler."
            mc "That's a heavy burden."
            duchess "It is. But I do it for my people. Sometimes I feel blessed that we were never able to have children. I hate to think of what they would’ve gone through, losing their father and their land to unseen horrors."
            "Her voice is steady, but there's a hint of sorrow in her eyes."

        "How do you stay so strong?":
            duchess "I draw strength from those around me. From the resilience of my people."
            mc "They're lucky to have you."
            duchess "And I'm lucky to have them. We give each other hope."
            "There's a mutual respect in her tone, a leader who sees herself as among her people, not above them."

        "We all have our roles to play.":
            duchess "Indeed. And sometimes, those roles choose us."
            mc "It seems like you were meant for this."
            duchess "Perhaps. But I often wonder what life would have been like on a different path."
    ##the three previous ones are all individual options, this next one should happen to end the scene regardless of what they pick#

    mc "You've done remarkably under the circumstances."

    duchess "One does what one must. But it's the people who suffer the most. That's why I'm here, with you, now."

    "She flashes a shy smile, and between her sparkling eyes and her soft features her intense gaze makes you blush."

    "The conversation continues, a mix of personal revelations and strategic planning, as you both approach the old mill."
   
    jump duchess_old_mill_arrival


label duchess_old_mill_arrival:

    "The old mill stands before you, its once sturdy structure now crumbling to neglect. The wooden beams are weathered and rotting, and the water wheel is motionless, entangled in overgrown vines."

    "The air is thick with an ominous stillness as if the very atmosphere is holding its breath in anticipation."

    duchess "This is it. Keep your senses sharp. We don't know what lies within."

    "You both step cautiously, the sound of your footsteps muffled by the thick layer of moss and fallen leaves covering the ground."

    "As you enter the mill, the musty smell of decay fills your nostrils. Shafts of light pierce through the broken roof, casting eerie shadows across the dusty floor."

    "The Duchess signals for silence, her hand resting on the hilt of her sword. You nod, slinking into a crouched position, creeping along, hand on your weapon."

    "Every step is deliberate, every breath measured, as you both navigate through the decrepit interior, searching for any sign of the beast."

    "The tension in the air catches in your lungs, a tangible force that seems to press against your very soul."

    "Suddenly, a noise from the upper floor breaks the silence, a reminder that you are not alone in this forsaken place."

    
    jump old_mill_monster_encounter



