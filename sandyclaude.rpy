# sandyclaude.rpy - Sandy Main Character File (English)
# Imports dialogues and sequences from sandy_talks.rpy file
# Sexual functions have been moved to sandyfucks.rpy

# Define Sandy character
define sd = Character("Sandy Cunts", who_color="#ff69b4")
define you = Character("You", who_color="#ffff00")
define b =  Character("Frank", who_color="#ff69b4")
# Variables to track Sandy's state
default sandy_tesao = False  # Initially not horny
default ja_visitou_sandy = False  # Tracks if already visited Sandy before
default pontos_interesse_sandy = 0  # Sandy's interest points
default nivel_interesse_sandy = 0  # Sandy's interest level (based on points)
default vezes_mostrou_peitos = 0  # Counter for times Sandy showed her tits
default vezes_punheta = 0  # Counter for times Sandy gave a handjob
default vezes_mostrou_buceta = 0  # Counter for times Sandy showed her pussy
default vezes_cuzinho = 0  # Counter for times player fucked her ass
default vezes_boquete = 0  # Counter for times Sandy gave a blowjob
default vezes_foder_buceta = 0  # Counter for times player fucked her pussy
default vezes_nozes_cuzinho = 0  # Counter for times player stuck nuts in her ass
default ultimo_dia_acao_sexual = -1  # Stores the 'dia' variable value when sexual action was performed

# NEW: Sexual enhancement system variables
default acoes_extras_dia = 0  # Extra actions available today
default reef_powder_usado_hoje = False  # Track if reef powder was used today
default jaguar_power_usado_hoje = False  # Track if jaguar power was used today

# Function to update interest level based on points
init python:
    def atualizar_nivel_interesse():
        global pontos_interesse_sandy, nivel_interesse_sandy
        nivel_interesse_sandy = pontos_interesse_sandy // 5
        # Limit to maximum level 20
        if nivel_interesse_sandy > 20:
            nivel_interesse_sandy = 20
    
    # NEW: Functions for sexual enhancement system
    def usar_reef_powder():
        global acoes_extras_dia, reef_powder_usado_hoje, inventario
        if 26 in inventario and not reef_powder_usado_hoje:
            inventario.remove(26)
            acoes_extras_dia += 1
            reef_powder_usado_hoje = True
            return True
        return False
    
    def usar_jaguar_power():
        global acoes_extras_dia, jaguar_power_usado_hoje, inventario
        if 27 in inventario and not jaguar_power_usado_hoje:
            inventario.remove(27)
            acoes_extras_dia += 2
            jaguar_power_usado_hoje = True
            return True
        return False
    
    def pode_fazer_acao_sexual():
        global ultimo_dia_acao_sexual, dia, acoes_extras_dia
        # Can do action if it's a different day OR if has extra actions available
        return ultimo_dia_acao_sexual != dia or acoes_extras_dia > 0
    
    def consumir_acao_sexual():
        global ultimo_dia_acao_sexual, dia, acoes_extras_dia
        if ultimo_dia_acao_sexual != dia:
            # First action of the day - mark as used
            ultimo_dia_acao_sexual = dia
        else:
            # Using extra action
            acoes_extras_dia -= 1
    
    def resetar_enhancers_diarios():
        global reef_powder_usado_hoje, jaguar_power_usado_hoje, acoes_extras_dia
        # Reset daily enhancer usage (call this when day changes)
        reef_powder_usado_hoje = False
        jaguar_power_usado_hoje = False
        acoes_extras_dia = 0

# Label to interact with Sandy
label sandy:
    # Check if day changed and reset enhancers
    if ultimo_dia_acao_sexual < dia - 1:
        $ resetar_enhancers_diarios()
    
    if not ja_visitou_sandy:
        scene bg casa_sandy with dissolve
        "You arrive at Sandy's house for the first time."
        $ ja_visitou_sandy = True
    else:
        scene bg casa_sandy with dissolve
        "You arrive at Sandy's house."

    show sandy normal at center
    
    play audio "hisandy.mp3"

    sd "Howdy, Spoogebob Squirtpants! What brings you here partner?"
    "Current interest level: [nivel_interesse_sandy]"
    if acoes_extras_dia > 0:
        "🔥 Extra spicy actions available: [acoes_extras_dia] 🔥"
    
    jump mostrar_menu_sandy

# Sandy's menu separated into its own label
label mostrar_menu_sandy:
    scene bg casa_sandy
    show sandy normal at center

    menu:
        "What do you want to do?"
        
        "Just talk":
            jump conversar_sandy
            
        "Offer a gift":
            jump presentear_sandy
        
        # NEW: Enhancement options
        "Use Reef Powder (+1 extra spicy action)" if 26 in inventario and not reef_powder_usado_hoje:
            $ sucesso = usar_reef_powder()
            if sucesso:
                show sandy seducao at center
                sd "Mmm... what's that strange powder you're taking? You seem more... energetic!"
                sd "I can feel the energy radiating from you, cowboy..."
                "You used Reef Powder! You now have +1 extra spicy action today!"
            jump mostrar_menu_sandy
            
        "Use Jaguar Power (+2 extra spicy actions)" if 27 in inventario and not jaguar_power_usado_hoje:
            $ sucesso = usar_jaguar_power()
            if sucesso:
                show sandy seducao at center
                sd "Holy cow! What did you just take? Your whole aura changed!"
                sd "You look like a wild animal ready to pounce... I like it!"
                "You used Jaguar Power! You now have +2 extra spicy actions today!"
            jump mostrar_menu_sandy
        
        # See tits - UPDATED with new system
        "See her tits ([min(vezes_mostrou_peitos, 3)]/3)" if nivel_interesse_sandy >= 1:
            if not pode_fazer_acao_sexual():
                show sandy seducao at center
                $ dialogo = obter_dialogo_recusa()
                sd "[dialogo]"
                jump mostrar_menu_sandy
            else:
                jump ver_peitos_sandy
        
        # See pussy - UPDATED with new system
        "See her pussy ([min(vezes_mostrou_buceta, 3)]/3)" if nivel_interesse_sandy >= 5 and vezes_punheta >= 3:
            if not pode_fazer_acao_sexual():
                show sandy seducao at center
                $ dialogo = obter_dialogo_recusa()
                sd "[dialogo]"
                jump mostrar_menu_sandy
            else:
                jump ver_buceta_sandy
        
        # Submenu for sexual favors (ONLY sex actions)
        "Sexual favors" if nivel_interesse_sandy >= 3:
            jump menu_favores_sexuais
            
        "Leave":
            jump sair_da_sandy

# Submenu for sexual favors (UPDATED with new system)
label menu_favores_sexuais:
    menu:
        "What sexual favor do you want?"
                
        # Handjob - UPDATED with new system
        "Ask for a handjob ([min(vezes_punheta, 3)]/3)" if nivel_interesse_sandy >= 3:
            if not pode_fazer_acao_sexual():
                show sandy seducao at center
                $ dialogo = obter_dialogo_recusa()
                sd "[dialogo]"
                jump menu_favores_sexuais
            else:
                jump punheta_sandy
                
        # Blowjob - UPDATED with new system
        "Get a blowjob ([min(vezes_boquete, 3)]/3)" if nivel_interesse_sandy >= 7:
            if not pode_fazer_acao_sexual():
                show sandy seducao at center
                $ dialogo = obter_dialogo_recusa()
                sd "[dialogo]"
                jump menu_favores_sexuais
            else:
                jump boquete_sandy
                
        # Fuck her pussy - UPDATED with new system
        "Fuck her pussy ([min(vezes_foder_buceta, 3)]/3)" if nivel_interesse_sandy >= 10:
            if not pode_fazer_acao_sexual():
                show sandy seducao at center
                $ dialogo = obter_dialogo_recusa()
                sd "[dialogo]"
                jump menu_favores_sexuais
            else:
                jump foder_buceta_sandy
        
        # Fuck her ass - UPDATED with new system
        "Fuck her ass ([min(vezes_cuzinho, 3)]/3)" if nivel_interesse_sandy >= 20:
             if not pode_fazer_acao_sexual():
                show sandy seducao at center
                $ dialogo = obter_dialogo_recusa()
                sd "[dialogo]"
                jump menu_favores_sexuais
             else:
                 jump comer_cuzinho
        
        # Option to return to main menu
        "Go back":
            jump mostrar_menu_sandy


# Leaving Sandy's house
label sair_da_sandy:
    sd "Leaving already cowboy? That's okay, come back whenever you want!"
    
    scene black with dissolve
    "You leave Sandy's house..."
    
    # Check if it's the first time player is leaving Sandy's house
    if ja_visitou_sandy and ultimo_dia_acao_sexual == -1:
        $ ultimo_dia_acao_sexual = 0  # Mark that already had first visit
        jump room4  # Go to room4 the first time
    else:
        jump explorar_sandy  # Return to explore option as it was in the code

# Simple conversation with Sandy
label conversar_sandy:
    sd "So, what have you been up to lately?"
    
    menu:
        "Talk about work at the Krusty Krab":
            sd "That old crab still pays you badly, right? You should demand a raise!"
            sd "Plus Mr.Krotch is a total CREEP! He stole my panties."
            sd "4 TIMES!!"
            
        "Talk about adventures with Fatrick":
            sd "You two always get into trouble! But I must admit it's fun."
            sd "He does have a big package tho, if you know what I mean..."
            
        "Talk about science":
            $ sandy_tesao = True  # Sandy gets excited with science talk
            sd "Wow! I'm impressed with your interest in science! I just developed a new experiment..."
            "Sandy talks animatedly about her experiments for almost an hour."
    
    jump finalizar_sandy  # Go to interaction end

# Offer gifts to Sandy
label presentear_sandy:
    "What gift do you want to offer Sandy?"
    
    # Show only items the player has
    $ itens_para_sandy = []
    $ nomes_itens = []
    
    # Check specific items
    if 5 in inventario:  # Seaweed Pie
        $ itens_para_sandy.append(5)
        $ nomes_itens.append("Seaweed Pie")
        
    if 6 in inventario:  # Nut Pie
        $ itens_para_sandy.append(6)
        $ nomes_itens.append("Nut Pie (Straight from Texas)")
        
    if 15 in inventario:  # Blow-up Doll
        $ itens_para_sandy.append(15)
        $ nomes_itens.append("Blow-up Doll")
    
    # New items added
    if 4 in inventario:  # Screwdriver
        $ itens_para_sandy.append(4)
        $ nomes_itens.append("Screwdriver")
        
    if 3 in inventario:  # Nuts
        $ itens_para_sandy.append(3)
        $ nomes_itens.append("Nuts")
        
    if 2 in inventario:  # Chocolate
        $ itens_para_sandy.append(2)
        $ nomes_itens.append("Chocolate")
        
    if 10 in inventario:  # Books
        $ itens_para_sandy.append(10)
        $ nomes_itens.append("Books")
    
    # Check if player has any specific gifts
    if len(itens_para_sandy) == 0:
        "You don't have any gift that might interest Sandy."
        jump finalizar_sandy  # Go to interaction end
    
    # Create dynamic menu with available gifts
    $ result = renpy.display_menu([(nome, id_item) for nome, id_item in zip(nomes_itens, itens_para_sandy)] + [("Go back", -1)])
    
    # Process choice
    if result == -1:
        jump finalizar_sandy  # Go to interaction end
    elif result == 5:  # Seaweed Pie
        show sandy irritada at center
        sd "Eh, thanks Spoogebob you shit dickhead."
        "Sandy doesn't seem to have liked the gift much..."
        $ pontos_interesse_sandy += 3  # Even not liking it, increases 3 points
    elif result == 6:  # Nut Pie
        show sandy feliz at center
        sd "WOW SPOOGEBOB I loved this shit!"
        "Sandy gets super excited with the Texas gift!"
        $ pontos_interesse_sandy += 8  # Increases 8 points for being from Texas
    elif result == 15:  # Blow-up Doll
        if sandy_tesao:
            show sandy seducao at center
            sd "Let's play cowboy..."
            "Sandy pulls you inside the house and closes the door."
            scene black
            "..."
            $ pontos_interesse_sandy += 8  # Increases 8 points if she's horny
            scene bg casa_sandy
            show sandy satisfeita at center
        else:
            show sandy irritada at center
            sd "Stick it up your ass you gay piece of shit!"
            "Sandy kicks you out of her house."
            
    # New items added - Reactions and points
    elif result == 4:  # Screwdriver
        show sandy feliz at center
        sd "A screwdriver! Exactly what I needed for my experiments!"
        "Sandy seems very happy with the gift."
        $ pontos_interesse_sandy += 7  # Increases 7 points
        
    elif result == 3:  # Nuts
        show sandy normal at center
        sd "Hmm, nuts... Thanks, Spoogebob, I'll save them for later."
        "Sandy seems to like the gift, but isn't very excited."
        $ pontos_interesse_sandy += 2  # Increases 2 points
        
    elif result == 2:  # Chocolate
        show sandy normal at center
        sd "Chocolate? Well, it's not so healthy, but I like a little sweet from time to time."
        "Sandy accepts the gift with a slight smile."
        $ pontos_interesse_sandy += 1  # Increases 1 point
        
    elif result == 10:  # Books
        show sandy feliz at center
        sd "Books! I love expanding my knowledge, thank you!"
        "Sandy seems quite interested in the books."
        $ pontos_interesse_sandy += 3  # Increases 3 points
        $ sandy_tesao = True  # Books can also make her excited about science
    
    # Remove item from inventory after giving gift
    if result != -1:
        $ inventario.remove(result)
        $ money += 5  # Small bonus for giving a gift
        $ atualizar_nivel_interesse()  # Update interest level based on points
    
    jump finalizar_sandy  # Go to interaction end

# Finalize interaction with Sandy
label finalizar_sandy:
    if not ja_visitou_sandy:
        scene room2
        menu:
            "Go to the Krusty Krab you gay bastard":
                $ ja_visitou_sandy = True
                jump start
    
    jump mostrar_menu_sandy  # Return to Sandy's main menu