# preda.rpy - Fatrick's House Interactions (English)

label vaginapodi:
    scene bg preda

    show pautrick joia with moveoutright:
        zoom 1.75
        align (0.5, 0.5)  # Center the image (x=0.5 is center, y=0.5 is center)
        yoffset 100       # Move image down (positive values = downward)
        # OR use xalign and yalign separately:
        # xalign 0.5      # 0.5 = center, 0.0 = left, 1.0 = right
        # yalign 0.7      # 0.5 = center, 0.0 = top, 1.0 = bottom

    p "Hi Spoogebob Squirtpants{w}"  
    window hide
    $ renpy.pause(1)

    show pautrick joia
    $ renpy.pause(1)
    
    "Fatrick" "Want to see my dick?"
    menu: 
        "Yes":
            jump opa

        "No":
            jump opb

    label opa:
        # Hide current character
        hide pautrick joia
        
        # Camera effect with initial zoom at bottom, slowly rising then zoom out
        show sandybb:
            zoom 2.5       # Closer initial zoom
            align (0.5, 0.5)  # Center the image
            yoffset -300   # Start focusing on the TOP part 
            linear 4.0 yoffset 300   # Move slowly DOWNWARD (focusing on bottom part)
            ease 1.0 zoom 1.75 yoffset 0  # Return to normal zoom and center
        
        jump end
        
    label opb: 
        show patrick poxa1 with moveoutright:
            zoom 1.75
            align (0.5, 0.5)  # Center the image
        hide pautrick joia
        p "Damn..."
        jump end
        
label end:
    menu: 
        "Leave":
            call screen bobCasas

# preda.rpy - Interactions with Fatrick at his house
# This file should be placed in the "game" folder of your Ren'Py project

# Add jelly item to items dictionary (if it doesn't exist)
init 1 python:
    if 23 not in itens_loja:
        itens_loja[23] = {"nome": "Jar with Jelly", "preco": 50}
    
    # Function to create jelly from jellyfish and jars
    def criar_pote_jeleia():
        global inventario
        
        # Check if we have enough jellyfish and jars
        qnt_aguas_vivas = inventario.count(21)  # Captured jellyfish ID
        qnt_potes = inventario.count(8)         # Jellyfish jar ID
        qnt_jeleias = inventario.count(23)      # Jar with jelly ID
        
        # Check if already at limit
        if qnt_jeleias >= 5:
            return "max"
            
        # Check if we have enough ingredients
        if qnt_aguas_vivas < 5:
            return "falta_aguas"
            
        if qnt_potes < 1:
            return "falta_pote"
            
        # Remove ingredients from inventory
        for i in range(5):
            inventario.remove(21)  # Remove 5 jellyfish
        inventario.remove(8)       # Remove 1 jar
            
        # Add jelly to inventory
        inventario.append(23)      # Add 1 jar with jelly
        
        return "sucesso"

# Fatrick's house image
image casa_patrick = "images/casa_patrick.jpg"

# Main label to interact with Fatrick
label preda:
    scene bg preda
    
    "You arrive at Fatrick's house."
    
    # Check if Fatrick is home
    $ hora_atual = hora_do_dia % 24
    if 2 <= hora_atual <= 5:
        "Fatrick is not awake right now. Better come back later."
        jump room4
    
    # Fatrick appears
    show pautrick
    
    p "Hey, Spoogebob Squirtpants! What a surprise to see you here!"
    
    # Main interaction menu
    menu patrick_opcoes:
        "What do you want to talk to Fatrick about?"
        
        "Chat a little":
            jump conversar_patrick
            
        "See Fatrick shirtless" if money >= 10:
            $ money -= 10
            p "You want to see me shirtless? Well... for 10 coins, that's fine."
            
            # Show Fatrick shirtless
            hide pautrick
            show pautrick mole
             
            window hide
            $ renpy.pause(hard=False) 
            
            p "Are you satisfied now?"
            
            "Fatrick seems a little uncomfortable."
            
            hide pautrick mole
            show pautrick
            
            jump patrick_opcoes
            
        "See Fatrick shirtless" if money < 10:
            p "To see me shirtless, you need at least 10 coins."
            
            jump patrick_opcoes
            
        "Make Jar with Jelly":
            # Check if already at limit
            $ qnt_jeleias = inventario.count(23)
            
            if qnt_jeleias >= 5:
                p "You already have the maximum number of jelly jars you can carry (5)."
                jump patrick_opcoes
                
            # Check ingredients and create jelly
            $ resultado = criar_pote_jeleia()
            
            if resultado == "sucesso":
                p "Great! Let's turn these jellyfish into delicious jelly!"
                
                "Fatrick mixes the jellyfish in the jar with some secret ingredients."
                
                p "Here's your Jar with Jelly! It'll be even better after a few days."
                "You received a Jar with Jelly."
                
            elif resultado == "falta_aguas":
                p "We need at least 5 jellyfish to make good jelly. Want to hunt some more?"
                
                menu:
                    "Let's hunt jellyfish":
                        p "Let's go!"
                        jump minigame_aguasvivas
                        
                    "Maybe later":
                        p "Whenever you want, just let me know."
                
            elif resultado == "falta_pote":
                p "We need a jar to store the jelly. Go buy one at Mr. Krack's store."
            
            jump patrick_opcoes
            
        "Leave":
            p "Bye! Come back whenever you want!"
            call screen bobCasas

# Simple conversations with Fatrick
label conversar_patrick:
    menu:
        "What do you want to talk about?"
        
        "How's your day going?":
            p "My day is going great! I spent the morning looking at clouds, then ate some sand, and now I'm here with you!"
            
        "Any news in Bikini Bottom?":
            p "Hmm, Squirtward is annoyed as always. Mr. Krack is still obsessed with money."
            p "And there's a new modern art exhibition at the museum! It's rocks... just rocks really."
            
        "What do you like to do?":
            p "I like to sleep, eat, hunt jellyfish with you, and look at the stars!"
            p "Sometimes I also like to do absolutely nothing. I'm very good at that."
            
        "Go back":
            jump patrick_opcoes
            
    jump conversar_patrick