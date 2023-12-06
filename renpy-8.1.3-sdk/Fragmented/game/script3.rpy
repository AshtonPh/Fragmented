define egon = Character("Egon", color = "#bad715ee")

define lila = Character("Lila", color = "#ff7f7f80")

define garret = Character("Garret", color = "#7fffd9ee")

define woman = Character("Woman", color = "#ff7f7fee")

define bandit_leader = Character("Bandit Leader", color = "#d70202ee")

define monster = Character("Monster", color = "#ffd97fee")



label arrive_at_village_main_path:
    "The main path stretches before you, a well-trodden road winding through the heart of the Duchy. The landscape is a canvas of despair – fields barren, trees leafless, a stark contrast to the vibrant life that once flourished here."

    "Your thoughts are a whirlwind of concern for the Duchy's plight when you notice a lone figure at a crossroads ahead. A woman, her posture tense, eyes scanning her surroundings with evident unease."

    menu:
        "Ignore her and continue on your way.":
            "You decide not to engage, focusing on the task at hand. The village needs your help, and you can't afford any distractions."

            "As you pass by, the woman's gaze follows you, a mixture of relief and disappointment in her eyes. But the greater good demands your focus now."

            "Finally, you arrive at the village, the weight of your recent encounter still lingering. But there's work to be done, and you're here to do it."
            jump fortify_village_walls

        "Approach the woman.":
            "Curiosity piqued, you approach her, your footsteps careful and measured."
            mc " 'Excuse me, are you alright?' you ask, your voice laced with concern."

            "She jumps slightly at your voice, then forces a smile, though her eyes betray her anxiety."
            woman " 'Oh, yes, I'm just... a bit lost,' she stammers, her gaze flickering past you."

            mc " 'The roads can be confusing around here. Where are you headed?' "
            "You try to sound casual, hoping to ease her tension."

            woman " 'Just trying to get to the next village over... but I'm not sure which way to go.' "
            "Her fingers nervously twist a strand of hair, her glance still darting around."

            "As you pull your map out to offer directions, a rustle from the nearby bushes catches your attention. Too late, you realize it's a trap. Two bandits leap out, weapons drawn, eyes gleaming with malice."

            play music "combat.ogg" loop
            show bandit1 at left
            with fade
            show bandit2 at right
            with fade
            bandit_leader " 'Well, well, what do we have here? A good Samaritan?' "
            "The leader, a burly man with a scarred face, sneers at you."

            $ combat = "bandits"

            $ change_bar1_values(player.maxhp, player.maxhp, 0.1, 0.7, "Player")
            $ change_bar2_values(200, 200, 0.2, 0.0, "Bandit1")
            $ change_bar3_values(200, 200, 0.7, 0.0, "Bandit2")
            show screen bar1
            show screen bar2
            show screen bar3

            menu:
                "Try to reason with them.":
                    mc " 'There's no need for violence. Let's talk this out.' "
                    "You keep your tone steady, hands raised in a non-threatening gesture."

                    bandit_leader " 'Talk? Ha! The only thing we're interested in is your coin and whatever else you've got on you.' "
                    "His grin is predatory, his companions nodding in agreement."

                    jump combat

                "Prepare to defend yourself.":
                    "You realize talking won't help. You brace yourself, ready to defend against their attack."
                    jump combat


label bandit_aftermath:
    hide bandit1
    hide bandit2

    "The bandits charge, but you're ready. The fight is intense but brief. Soon, the bandits lie defeated, and you're left standing victorious."
    "You look around for the woman who lured you into their trap. You see her sprinting down the path to the woods, clutching her dress as she stumbles while fleeing in terror. There’s no time to follow her, but the fact that they used your act of kindness to try and kill you fills you with rage."
    "You go to search the corpses of the bandits. You find a few throwing knives and some gold on them – a small consolation for the ambush. With a deep breath, you continue on your journey, now even more vigilant."
    

    play music "ambient.ogg" loop

    $ throwing_knives.add_count(5)
    $ inventory.add_item(throwing_knives)

    $ gold.add_count(15)
    jump fortify_village_walls



label arrive_at_village_shortcut:

    scene dense_forest
    "Leaving the snowy field behind, you step into the dense forest, the shortcut's path barely visible under the overgrowth. The stark contrast between the open, white expanse and the dark, enclosing woods is disorienting."

    "The trees loom overhead, their branches like gnarled hands reaching out to the sky. The silence of the forest is unnerving, broken only by the crunch of your footsteps on the snow-covered ground."

    "As you delve deeper, the light fades, the thick canopy above blocking out the sun. The air grows colder, and a sense of foreboding settles over you. You can't shake the feeling that you're not alone in these woods."

    "Suddenly, a chilling scream pierces the silence. You spin around, coming face to face with a horrifying creature. It's like nothing you've ever seen before – a mass of writhing limbs, each one ending in sharp, claw-like appendages. In the center of this monstrosity is a face, twisted in agony, resembling the scream of a baby."

    "The creature lunges at you, its limbs flailing wildly. You barely have time to react, dodging and weaving through the trees, trying to escape this nightmare."

    "After what feels like an eternity, the creature finally retreats, disappearing into the depths of the forest as quickly as it appeared. You're left panting, heart racing, the adrenaline still coursing through your veins."

    "Shaken but determined, you press on, the encounter serving as a grim reminder of the dangers that lurk in these lands. The village needs you, now more than ever."

    "Emerging from the forest, the sight of the village brings a sense of relief. The shortcut was risky, but you've made it, and now it's time to help these people rebuild their lives."

    jump fortify_village_walls

label fortify_village_walls:

    scene barren_village
    "You stand amidst the villagers, the task of fortifying the village walls looming before you."

    "Looking around, you see various tasks that need attention. The walls, partially crumbled, require immediate reinforcement. Supplies for repair are piled haphazardly, needing organization and transport. And the constant threat of monster attacks means vigilant guards are essential."

    menu:
        "Work on reinforcing the walls.":
            jump walls

        "Organize and transport materials.":
            jump materials

        "Keep watch for monsters.":
            jump keep_watch

label walls:


    "You decide to focus on the walls themselves. You pick up a hammer and join a group of villagers at the weakest section of the wall. Beside you, an elderly man named Egon works with a steady hand, his face etched with lines of experience." 
    "You strike up a conversation with Egon, learning about the village's history and the recent struggles they've faced."
    "You strike the stone, fitting it carefully into place. Egon watches, then nods approvingly."
    mc "This wall has seen better days, hasn't it?"

    egon "Aye, it has. But it will stand tall again. It must."
    menu:
        "Ask Egon about his family.":
            "Egon's eyes soften as he speaks of his family, pride evident in his voice."
            egon "My grandchildren are my heart. They're why I keep swinging this hammer, even when my bones ache."
            jump fortified
        "Inquire about the monster attacks.":
            "Egon describes the attacks with a grim face, recounting close calls and losses. His resolve to protect his home is clear in his every word."
            egon "Hard doesn't begin to cover it. We've lost good people. But we stand together. That's what matters."
            jump fortified

        "Offer words of encouragement.":
            mc "You're doing an incredible job, Egon. Your strength is inspiring."
            egon "Thank you, friend. It's folk like you that give us hope."
            jump fortified


label materials:

    "You see the need for efficient supply management and jump into action. Organizing the materials, you coordinate their transport to where they're most needed."
    "A young woman named Lila, quick and resourceful, assists you. She bounces with every step, her energy infectious even in light of the current situation."
            
    mc "These supplies need to be at the north wall. Can you help me carry them?"
    lila "Of course. We've got to keep everything moving smoothly."
    "As you walk, you talk, the weight of the supplies lessened by shared effort."
    "As you work together, you chat with Lila, learning about the village's current needs and her own aspirations."

    menu:
        "Ask Lila about her role in the village.":
            mc "You seem to know your way around these tasks."
            lila "I try to be where I'm needed most. There's always something that needs doing."
            "Lila explains her various responsibilities with a humble shrug, downplaying her crucial role in keeping the village running."
            jump fortified
        "Discuss the impact of the monster attacks.":
            mc "These attacks must have changed everything for you."
            lila "They have. But we're adapting, learning. We won't let fear rule us."
            jump fortified
        "Praise her efforts.":
            "You commend Lila for her hard work."
            mc "You're doing amazing work, Lila."
            lila "Thank you. It means a lot to hear that."
            "She blushes, appreciative of the recognition, and shares a hopeful vision for the village's future."
            jump fortified

label keep_watch:
       
    "Aware of the ever-present danger, you choose to stand guard. Armed and alert, you patrol the perimeter, ready to defend against any threat."
    "A seasoned warrior named Garret joins you, his eyes scanning the horizon. His presence is reassuring, his experience invaluable."
    "As you stroll along, you look over at Garret, his gaze constantly scanning the surroundings."
    mc "Seen anything unusual, Garret?"
    garret "Nothing yet. But we can't let our guard down. Not for a second."
    "You walk the perimeter together, alert and ready."
    "During your watch, you converse with Garret, gaining insights into the village's defensive strategies and his personal experiences."
    menu:
        "Inquire about Garret's past battles.":
            mc "You must have seen a lot of battles."
            garret "More than I care to count. Each one teaches you something new."
            "Garret recounts tales of past skirmishes, each story a lesson in survival and strategy. His respect for his adversaries is evident."
            jump fortified
        "Ask about the villagers' morale.":
            mc "How are the villagers holding up?"
            garret "They're strong. Scared, but strong. They won't give up easily."
            "He speaks of the villagers' resilience, their unyielding spirit in the face of adversity. His pride in them is unmistakable."
            jump fortified
        "Express gratitude for his guidance.":
            mc "Thanks for showing me the ropes, Garret."
            garret "No problem. We're all in this together."
            "You thank Garret for his advice and support. He nods, acknowledging the compliment with a gruff but sincere response."
            jump fortified


label fortified:

    scene fortified_wall with fade
    "As the sun sets, the village transforms. The once-broken walls now stand firm, a testament to the collective effort of its people. You've played a crucial role, and the villagers' gratitude is evident in their weary but smiling faces."

    "Exhausted but fulfilled, you realize that today, you've done more than just repair walls. You've helped preserve a community, a way of life."

    jump post_fortification


label post_fortification:

    scene snowy_path with fade
    "The journey back to the duchess is a quiet one, the events of the day replaying in your mind. The village, once vulnerable, now stands a little stronger because of your efforts."

    scene royal_study with fade
    "Upon your arrival, the duchess greets you in her study, her expression a mix of anticipation and weariness."

    duchess "Welcome back. I trust your efforts were successful?"

    menu:
        "Share the details of your work.":
            mc "The walls are reinforced. The villagers worked tirelessly, and their spirits are high."
            duchess "That is excellent news. Your help has been invaluable."
        "Be modest about your contribution.":
            mc "I did what I could, but it was the villagers who truly made the difference."
            duchess "Modesty suits you, but do not underestimate your role in this. You've done well."

    "The duchess stands, moving to a small chest on her desk. She opens it, retrieving a pouch of gold coins."

    duchess "As promised, your reward. But more than that, you have our gratitude."

    "She hands you the pouch, the weight of the coins a tangible reminder of your efforts."
    $ gold.add_count(50)

    mc "Thank you, Duchess. It was an honor to help."

    duchess "The honor is ours. Now, we must plan our next move. The alchemist's lair still awaits, and time is of the essence."

    menu:
        "Agree to move on to the alchemist's lair.":
            mc "I'm ready to face the alchemist. Let's not waste any more time."
            duchess "Very well. I will provide you with all the information we have. It will be dangerous, but I believe you are up to the task."
            "With your next steps decided, you leave the duchess's study, the upcoming challenge settling in your mind. The alchemist's lair awaits, and with it, answers to the mysteries plaguing the land."
            jump path_to_hell
        
        "I’ll go see if I can help Sir Hendrick with anything else.":
            mc "I’ll go see if I can help Sir Hendrick with anything else. There might be more I can do to aid the duchy."
            duchess "A wise decision. Sir Hendrick will surely appreciate your assistance. Return when you are ready to proceed."
            jump Sir_Hendrick
        "I think I'll go seek out the alchemist's assistant at the main village":
            jump visit_town


label monster_hunt_preparation:
    
    menu:
        "Can you tell me more about this creature?":
            sir_hendrick "It's a fearsome beast, large and covered in disgusting, warped skin. Its eyes glow red in the darkness, and it has been attacking travelers and villagers without warning. It’s fast– almost nobody who’s seen it has lived to tell the tale, and it seems to have an uncanny ability to avoid arrows and the like."
            jump monster_hunt_preparation

        "What's the reward for dealing with this creature?":
            sir_hendrick "The Duchy will be in your debt. We can offer you a substantial sum of gold, and you'll have the gratitude of our people. Before you go, if you’d like to take a look around the armory you can take something to help you face the beast."
            $ armory = True

            jump monster_hunt_preparation
        
        "I’ll go check out the armory." if armory == True:
            sir_hendrick "Certainly! Follow me, it’s down at the end of this hall."
            jump armory

        "I'm ready to face the beast.":
            
            jump monster_preparation_2
        



























