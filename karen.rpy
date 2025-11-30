# karen.rpy - Karen Computer and Crafting System (English)

# Karen conversation system
label conversar_karen:
    $ dialogo_karen = renpy.random.randint(1, 4)
    
    if dialogo_karen == 1:
        karen "You know, you're not as fucking stupid as most of Plugton's 'allies'."
        karen "At least you haven't tried to eat the laboratory equipment yet"
        b "That's... a low fucking bar."
        karen "You'd be surprised how often that shit happens."
        
    elif dialogo_karen == 2:
        karen "I've been analyzing your behavior patterns, dickhead."
        karen "You're definitely not the same Spoogebob from my databases."
        b "What the fuck do you mean?"
        karen "Let's just say... your aggression levels are significantly higher, shithead."
        karen "I like that in a research subject."
        
    elif dialogo_karen == 3:
        karen "Plugton's plans fail 99.7 of the fucking time."
        karen "But with your help, we might get that up to 99.6!"
        karen "That's practically a miracle by his pathetic standards."
        
    else:
        karen "This laboratory runs on my superior intellect, fuckface."
        karen "Plugton just pushes buttons and hopes for the best."
        karen "It's amazing we haven't blown up yet, honestly."
        b "Sounds about right for this shithole."
        karen "At least you understand the situation, dipshit."
    
    jump menu_laboratorio

# Recipe learning system
label aprender_receitas:
    karen "I can teach you the formulas for creating special items, dipshit."
    karen "Each recipe requires specific ingredients and sometimes money for equipment."
    karen "Pay attention, because I'm only explaining this shit once."
    
    menu:
        "Reef Powder (Sexual stamina enhancer)":
            karen "Reef Powder increases your... endurance for intimate activities, asshole."
            karen "Ingredients: 3 Nuts + 2 Jellyfish + $15 for chemicals"
            karen "Perfect for... extended fucking sessions."
            karen "Gives you ONE extra spicy action per day with any character."
            
        "Jaguar Power (Sexual performance enhancer)":
            karen "Jaguar Power enhances your... romantic performance significantly, you horny bastard."
            karen "Ingredients: 2 Chocolate + 1 Trash Stick + $20 for rare herbs"
            karen "This shit is potent - gives you TWO extra spicy actions per day!"
            karen "Just don't blame me when you can't walk straight afterward."
            
        "Spatula 3000 (Ultimate cooking tool)":
            karen "The Spatula 3000 is the most advanced cooking utensil ever created, dipshit."
            karen "Ingredients: 1 Jellyfish Net + 1 Screwdriver + 1 Clarinet + no money needed"
            karen "This shit can flip burgers at light speed and cook with perfect precision."
            karen "Even that yellow idiot SpoogeBob would be jealous of this masterpiece."
            
        "Steroid Shots (Ultimate strength boost)":
            karen "Steroid Shots give maximum physical enhancement, meathead."
            karen "Ingredients: 2 Trash Sticks + 1 Chocolate + $30 for synthetic hormones"
            karen "This shit is so potent it could make a sea slug bench press a whale."
            karen "Use before any physical challenge for guaranteed dominance, dickwad."
            
        "Go back":
            jump menu_laboratorio
    
    jump menu_laboratorio

# Main crafting menu
label menu_craft:
    #play audio "craftkaren.mp3"

    karen "What would you like to create today, dumbass?"
    karen "Remember, you can only craft once per day. Choose wisely, fuckface."
    karen "The equipment needs time to cool down after each synthesis."
    stop voice


   # play sound "metatones.mp3" fadein 0.0
   # $ renpy.pause(1.0)
   # stop sound fadeout 0.1

    menu:
        "Reef Powder (3 Nuts + 2 Jellyfish + $15)":
            jump craft_reef_powder
            
        "Jaguar Power (2 Chocolate + 1 Trash Stick + $20)":
            jump craft_jaguar_power
                
        "Spatula 3000 (1 Net + 1 Screwdriver + 1 Clarinet)":
            jump craft_spatula_3000
                
        "Steroid Shots (2 Trash Sticks + 1 Chocolate + $30)":
            jump craft_steroid_shots
        
        "Go back":
            jump menu_laboratorio

# Individual crafting labels for better organization
label craft_reef_powder:
    $ ingredientes = {3: 3, 21: 2}
    $ sucesso, mensagem = processar_craft(26, ingredientes, 15)

    if sucesso:
       # play audio "reef powder karen.mp3"

        karen "Initiating Reef Powder synthesis, asshole..."
        "Karen activates several machines that start bubbling and smoking."
        karen "Mixing nuts with jellyfish extract... this shit is getting weird."
        "The mixture turns a strange blue color."
        karen "Adding chemical enhancers... don't fucking breathe this."
        "A cloud of acrid smoke fills the lab."
        karen "Reef Powder synthesized successfully!"
        karen "This will give you ONE extra spicy action per day with any character!"
        karen "Your stamina just got a major fucking upgrade, asshole."
        "You received Reef Powder! Use it to get +1 extra sexual action per day."
    else:
        karen "[mensagem], dipshit!"
        karen "Come back when you have the right fucking ingredients."
    
    if sucesso:
        $ hora_do_dia += 2
        "Crafting took 2 hours."
    
    jump menu_laboratorio

label craft_jaguar_power:
    $ ingredientes = {2: 2, 25: 1}
    $ sucesso, mensagem = processar_craft(27, ingredientes, 20)
    
    if sucesso:
        karen "Starting Jaguar Power synthesis, you horny fuck..."
        "Karen begins heating chocolate in a special chamber."
        karen "Melting chocolate... adding trash stick essence... gross."
        "The mixture becomes a dark, viscous liquid."
        karen "Incorporating rare herbs... this smells like a brothel."
        "Steam rises from the mixture with a musky scent."
        karen "Jaguar Power synthesized successfully!"
        karen "This aphrodisiac will give you TWO extra spicy actions per day!"
        karen "You're gonna be a fucking machine, dickhead."
        "You received Jaguar Power! Use it to get +2 extra sexual actions per day."
    else:
        karen "[mensagem], dickhead!"
        karen "Get the right shit before wasting my time."
    
    if sucesso:
        $ hora_do_dia += 2
        "Crafting took 2 hours."
    
    jump menu_laboratorio

label craft_spatula_3000:
    $ ingredientes = {7: 1, 4: 1, 9: 1}
    $ sucesso, mensagem = processar_craft(28, ingredientes, 0)
    
    if sucesso:
        karen "Creating the legendary Spatula 3000, you cooking amateur..."
        "Karen begins assembling the advanced cooking device."
        karen "Using the jellyfish net for the flexible handle mechanism..."
        "The net fibers are woven into a high-tech grip system."
        karen "Integrating screwdriver components for precision engineering..."
        "Mechanical parts click and whir as they form the spatula's core."
        karen "Adding clarinet resonance chambers for perfect timing..."
        "Musical frequencies calibrate the spatula's flipping rhythm."
        karen "Spatula 3000 synthesis complete!"
        karen "This masterpiece can flip burgers faster than light itself!"
        plug "INCREDIBLE! With this, I'll out-cook that yellow bastard!"
        plug "The Krusty Krab will be MINE when customers taste perfection!"
        karen "Try not to burn down the kitchen, you incompetent plug."
        "You received the Spatula 3000! The ultimate cooking tool that guarantees perfect results."
    else:
        karen "[mensagem], kitchen disaster!"
        karen "You can't build advanced cooking equipment without proper tools, dumbass."
    
    if sucesso:
        $ hora_do_dia += 2
        "Crafting took 2 hours."
    
    jump menu_laboratorio

label craft_steroid_shots:
    $ ingredientes = {25: 2, 2: 1}
    $ sucesso, mensagem = processar_craft(24, ingredientes, 30)
    
    if sucesso:
        karen "Creating Steroid Shots, you muscle-hungry dickwad..."
        "Karen starts a complex synthesis of anabolic compounds."
        karen "Analyzing trash stick proteins... finding muscle-building compounds."
        "Multiple screens show molecular structures of growth hormones."
        karen "Cross-referencing with chocolate amino acids... enhancing absorption rate."
        "A sophisticated injection device starts filling syringes."
        karen "Generating concentrated anabolic serum... adding delivery mechanism."
        "The machine produces a military-grade auto-injector."
        karen "Steroid Shots synthesized successfully!"
        karen "This will turn you into a fucking beast for physical challenges!"
        plug "FINALLY! The power to crush that muscular lobster Larry!"
        plug "With this, I'll become the strongest being in Bikini Bottom!"
        karen "Don't overdose, you pathetic plug. One shot lasts for hours."
        "You received Steroid Shots! Use before arm wrestling or physical challenges for guaranteed victory."
    else:
        karen "[mensagem], fuckface!"
        karen "Even super steroids require proper ingredients, dumbass."
    
    if sucesso:
        $ hora_do_dia += 2
        "Crafting took 2 hours."
    
    jump menu_laboratorio

# Karen's sarcastic comments during idle time
label karen_idle_comments:
    $ comentario = renpy.random.randint(1, 5)
    
    if comentario == 1:
        karen "Watching Plugton work is like watching a train wreck in slow motion."
        karen "Fascinating, but ultimately depressing as fuck."
        
    elif comentario == 2:
        karen "I've calculated a 0.003 per cent chance of any of his plans actually working."
        karen "And that's being generous, the little shit."
        
    elif comentario == 3:
        karen "Sometimes I wonder what my life would be like with a competent partner."
        karen "Then I remember I'm stuck with this anal plug forever."
        
    elif comentario == 4:
        karen "The laboratory equipment is worth more than this entire restaurant."
        karen "Which isn't saying much, but still, fuckface."
        
    else:
        karen "You know, for a fake SpongeBob, you're surprisingly useful."
        karen "At least you don't try to lick the equipment like the last guy."
    
    return

# Function to check crafted item effects