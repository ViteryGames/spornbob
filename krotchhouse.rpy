# krotchhouse_main.rpy - Purrl's House Visit System - TRULY FINAL VERSION

# Variables for Purrl's house system
default perola_nivel_intimidade = 0  # Purrl's intimacy level with player
default visitas_casa_perola = 0  # Number of visits to Purrl's house
default primeiro_twerk = False  # Track if first twerking scene happened
default perola_acordou_sexualmente = False  # Track if Purrl awakened sexually
default ultimo_dia_visita_perola = -1  # Last day player visited Purrl
default perola_chantagem_resolvida = False  # Track if blackmail situation is resolved
default perola_ultimas_conversas = []  # Track recent conversation topics
default perola_presentes_dados = []    # Track gifts given to Purrl
default perola_presentes_hoje = 0  # Track gifts given today
default dia_ultimo_presente = -1  # Last day a gift was given

# Purrl house images
image casa_perola_externa = "images/casa_perola_externa.png"
image quarto_perola = "images/quarto_perola.png"
image sala_perola = "images/sala_perola.png"
image perola_pijama = "images/perola_pijama.png"
image perola_provocante = "images/perola_provocante.png"
image perola_excitada = "images/perola_excitada.png"
image perola_satisfeita = "images/perola_satisfeita.png"
image perola_normal = "images/perola_normal.png"

# Basic twerk frames (8 frames)
image perola_twerk_frame1 = "images/perola_twerk_frame1.png"
image perola_twerk_frame2 = "images/perola_twerk_frame2.png"
image perola_twerk_frame3 = "images/perola_twerk_frame3.png"
image perola_twerk_frame4 = "images/perola_twerk_frame4.png"
image perola_twerk_frame5 = "images/perola_twerk_frame5.png"
image perola_twerk_frame6 = "images/perola_twerk_frame6.png"
image perola_twerk_frame7 = "images/perola_twerk_frame7.png"
image perola_twerk_frame8 = "images/perola_twerk_frame8.png"

# Professional twerk frames
image perola_twerk_pro_frame1 = "images/perola_twerk_pro_frame1.png"
image perola_twerk_pro_frame2 = "images/perola_twerk_pro_frame2.png"
image perola_twerk_pro_frame3 = "images/perola_twerk_pro_frame3.png"
image perola_twerk_pro_frame4 = "images/perola_twerk_pro_frame4.png"
image perola_twerk_pro_frame5 = "images/perola_twerk_pro_frame5.png"
image perola_twerk_pro_frame6 = "images/perola_twerk_pro_frame6.png"
image perola_twerk_pro_frame7 = "images/perola_twerk_pro_frame7.png"
image perola_twerk_pro_frame8 = "images/perola_twerk_pro_frame8.png"

# Basic twerk animations
image perola_twerk_anim_normal:
    "perola_twerk_frame1"
    pause 0.15
    "perola_twerk_frame2"
    pause 0.15
    "perola_twerk_frame3"
    pause 0.15
    "perola_twerk_frame4"
    pause 0.15
    "perola_twerk_frame5"
    pause 0.15
    "perola_twerk_frame6"
    pause 0.15
    "perola_twerk_frame7"
    pause 0.15
    "perola_twerk_frame8"
    pause 0.15
    repeat

image perola_twerk_anim_rapida:
    "perola_twerk_frame1"
    pause 0.08
    "perola_twerk_frame2"
    pause 0.08
    "perola_twerk_frame3"
    pause 0.08
    "perola_twerk_frame4"
    pause 0.08
    "perola_twerk_frame5"
    pause 0.08
    "perola_twerk_frame6"
    pause 0.08
    "perola_twerk_frame7"
    pause 0.08
    "perola_twerk_frame8"
    pause 0.08
    repeat

# Professional twerk animations
image perola_twerk_pro_anim_normal:
    "perola_twerk_pro_frame1"
    pause 0.2
    "perola_twerk_pro_frame2"
    pause 0.2
    "perola_twerk_pro_frame3"
    pause 0.2
    "perola_twerk_pro_frame4"
    pause 0.2
    "perola_twerk_pro_frame5"
    pause 0.2
    "perola_twerk_pro_frame6"
    pause 0.2
    "perola_twerk_pro_frame7"
    pause 0.2
    "perola_twerk_pro_frame8"
    pause 0.2
    repeat

image perola_twerk_pro_anim_rapida:
    "perola_twerk_pro_frame1"
    pause 0.08
    "perola_twerk_pro_frame2"
    pause 0.08
    "perola_twerk_pro_frame3"
    pause 0.08
    "perola_twerk_pro_frame4"
    pause 0.08
    "perola_twerk_pro_frame5"
    pause 0.08
    "perola_twerk_pro_frame6"
    pause 0.08
    "perola_twerk_pro_frame7"
    pause 0.08
    "perola_twerk_pro_frame8"
    pause 0.08
    repeat

# Sound effects
define audio.twerk_music = "twerksong.mp3"
define audio.porta_casa = "house_door.mp3"
define audio.pai_chegando = "footsteps.mp3"

# Functions - USING 'dia' CORRECTLY
init python:
    def pode_visitar_perola_hoje():
        global ultimo_dia_visita_perola, dia
        return ultimo_dia_visita_perola != dia
    
    def reset_conversas_perola():
        global perola_ultimas_conversas
        perola_ultimas_conversas = []
    
    def novo_dia_perola():
        global perola_presentes_hoje, dia_ultimo_presente, dia
        # Reset daily gift counter if it's a new day
        if dia_ultimo_presente != dia:
            perola_presentes_hoje = 0
            dia_ultimo_presente = dia
        reset_conversas_perola()
    
    def pode_dar_presente():
        global perola_presentes_hoje, dia_ultimo_presente, dia
        # Check if it's a new day and reset counter if needed
        if dia_ultimo_presente != dia:
            perola_presentes_hoje = 0
            dia_ultimo_presente = dia
        return perola_presentes_hoje < 2

# Main label to visit Purrl's house
label visitar_casa_perola:
    # Reset gift counter if it's a new day
    $ novo_dia_perola()
    
    # Check if address is known
    if not endereco_perola_descoberto:
        "You don't know where Purrl lives yet."
        return
    
    scene casa_perola_externa
    "You arrive at Purrl's house on Whale Street, 69."
    "It's a large, luxurious house... Mr. Krotch's money shows."
    
    # Check if already visited today
    if not pode_visitar_perola_hoje():
        "You already visited Purrl today. Better come back tomorrow."
        jump room4
    
    # Mark visit
    $ ultimo_dia_visita_perola = dia
    $ visitas_casa_perola += 1
    
    # First visit - special scene
    if visitas_casa_perola == 1:
        jump primeira_visita_perola
    # Second visit - continuation
    elif visitas_casa_perola == 2:
        jump segunda_visita_perola
    # Third visit onwards - direct to main menu
    else:
        scene quarto_perola
        show perola_provocante at center
        prl "You're back... good."
        prl "What you wanna do today?"
        jump menu_principal_perola

# First visit - Awakening
label primeira_visita_perola:
    play sound audio.porta_casa
    
    scene quarto_perola
    show perola_pijama at center
    
    prl "So... you actually came, you bastard."
    prl "Wasn't sure you'd have the balls to show up."
    
    jump perola_sozinha_primeira_vez

# Second visit - Building tension
label segunda_visita_perola:
    scene quarto_perola
    show perola_provocante at center
    
    prl "You came back... I've been thinking about yesterday all fucking day."
    prl "That twerking... it awakened something in me."
    prl "I wanna learn more shit."
    
    jump segunda_visita_desenvolvimento

# Main menu for Purrl's house (3rd visit onwards)
label menu_principal_perola:
    scene quarto_perola
    show perola_normal at center
    
    "Purrl's Intimacy Level: [perola_nivel_intimidade]"
    "Day: [dia]"
    
    menu:
        "Talk to Purrl":
            jump menu_conversa_perola
            
        "Give a gift ([perola_presentes_hoje]/2 today)" if pode_dar_presente():
            jump menu_presentes_perola
            
        "Give a gift (Limit reached: 2 per day)" if not pode_dar_presente():
            prl "You already gave me enough shit today."
            prl "Come back tomorrow if you wanna spoil me more."
            jump menu_principal_perola
            
        "Sexual favors":
            jump menu_favores_sexuais_perola
            
        "Leave":
            prl "Leaving already? Pussy."
            $ mapa_disponivel = True
            call screen bobCasas

# Sexual favors menu with level requirements
label menu_favores_sexuais_perola:
    scene quarto_perola
    show perola_provocante at center
    
    prl "What dirty shit you want today?"
    
    menu:
        "Basic twerking" if perola_nivel_intimidade >= 0:
            jump twerk_basico
            
        "Professional twerking" if perola_nivel_intimidade >= 5:
            jump twerk_profissional
            
        "Show me your tits (Requires Level 10)" if perola_nivel_intimidade >= 10:
            jump ver_peitos_perola
            
        "Sexual twerking (Requires Level 15)" if perola_nivel_intimidade >= 15:
            jump twerk_sexual_perola
            
        "Handjob (Requires Level 20)" if perola_nivel_intimidade >= 20:
            jump punheta_perola
            
        "Blowjob (Requires Level 25)" if perola_nivel_intimidade >= 25:
            jump boquete_perola
            
        "Fuck your ass (Requires Level 30)" if perola_nivel_intimidade >= 30:
            jump foder_perola_anal
            
        "Fuck your pussy (Requires Level 35)" if perola_nivel_intimidade >= 35:
            jump foder_perola_vaginal
            
        "Not high enough level" if perola_nivel_intimidade < 10:
            prl "You need to increase our intimacy level first."
            prl "Current level: [perola_nivel_intimidade]"
            prl "Talk to me more, give me gifts... make me want you."
            jump menu_principal_perola
            
        "Go back":
            jump menu_principal_perola

# Basic twerking (always available)
label twerk_basico:
    prl "You wanna see me twerk? Alright..."
    
    play music audio.twerk_music fadein 1.0
    scene quarto_perola
    show perola_twerk_anim_normal at center
    
    prl "Like this? Am I doing it right?"
    prl "I've been practicing..."
    
    menu:
        "Go faster":
            hide perola_twerk_anim_normal
            show perola_twerk_anim_rapida at center
            prl "Faster? Like this?"
            prl "Fuck, this is making me hot..."
            $ perola_nivel_intimidade += 1
            
        "That's enough":
            prl "Already? Fine..."
    
    stop music fadeout 1.0
    hide perola_twerk_anim_normal
    hide perola_twerk_anim_rapida
    show perola_satisfeita at center
    
    $ hora_do_dia += 1
    jump menu_principal_perola

# Professional twerking (level 5+)
label twerk_profissional:
    prl "Now I'll show you my professional moves!"
    
    play music audio.twerk_music fadein 1.0
    scene quarto_perola
    show perola_twerk_pro_anim_normal at center
    
    prl "See the difference? I'm a fucking pro now!"
    prl "Every move calculated to make your dick hard!"
    
    menu:
        "Maximum speed":
            hide perola_twerk_pro_anim_normal
            show perola_twerk_pro_anim_rapida at center
            prl "Like this?! I can go even faster!"
            prl "Your dick must be rock hard now!"
            $ perola_nivel_intimidade += 1
            
        "Perfect":
            prl "Damn right it's perfect!"
    
    stop music fadeout 1.0
    hide perola_twerk_pro_anim_normal
    hide perola_twerk_pro_anim_rapida
    show perola_satisfeita at center
    
    $ hora_do_dia += 1
    jump menu_principal_perola

# Conversation menu
label menu_conversa_perola:
    menu:
        "Ask about her life":
            jump conversa_vida_perola
            
        "Talk about her father":
            jump conversa_pai_perola
            
        "Ask about school":
            jump conversa_escola_perola
            
        "Compliment her":
            jump elogiar_perola
            
        "Go back":
            jump menu_principal_perola

# Gift menu with daily limit - PROPERLY RESETTING
label menu_presentes_perola:
    # Double-check if it's a new day
    if dia_ultimo_presente != dia:
        $ perola_presentes_hoje = 0
        $ dia_ultimo_presente = dia
    
    if not pode_dar_presente():
        prl "You already gave me 2 gifts today. That's enough."
        jump menu_principal_perola
    
    "What gift you wanna give Purrl? (Daily limit: [perola_presentes_hoje]/2)"
    "Current Day: [dia]"
    
    $ presentes_disponiveis = []
    $ nomes_presentes = []
    
    if 2 in inventario:  # Chocolate
        $ presentes_disponiveis.append(2)
        $ nomes_presentes.append("Chocolate (+2 intimacy)")
        
    if 10 in inventario:  # Books
        $ presentes_disponiveis.append(10)
        $ nomes_presentes.append("Books (+3 intimacy)")
        
    if 19 in inventario:  # Pineapple
        $ presentes_disponiveis.append(19)
        $ nomes_presentes.append("Pineapple (+2 intimacy)")
        
    if 1 in inventario:  # Cowboy Hat
        $ presentes_disponiveis.append(1)
        $ nomes_presentes.append("Cowboy Hat (+2 intimacy)")
        
    if 6 in inventario:  # Nut Pie
        $ presentes_disponiveis.append(6)
        $ nomes_presentes.append("Nut Pie - Texas (+4 intimacy)")
    
    if len(presentes_disponiveis) == 0:
        "You don't have shit that Purrl might like."
        jump menu_principal_perola
    
    $ result = renpy.display_menu([(nome, id_item) for nome, id_item in zip(nomes_presentes, presentes_disponiveis)] + [("Go back", -1)])
    
    if result == -1:
        jump menu_principal_perola
    else:
        $ perola_presentes_hoje += 1
        $ dia_ultimo_presente = dia
        
    if result == 2:  # Chocolate
        $ inventario.remove(2)
        prl "Chocolate! Fuck yeah!"
        $ perola_nivel_intimidade += 2
        $ money += 3
        "Purrl gives you $3!"
        
    elif result == 10:  # Books
        $ inventario.remove(10)
        prl "Books? Interesting..."
        $ perola_nivel_intimidade += 3
        $ money += 5
        "Purrl gives you $5!"
        
    elif result == 19:  # Pineapple
        $ inventario.remove(19)
        prl "A pineapple? It's so... dick shaped..."
        $ perola_nivel_intimidade += 2
        $ money += 4
        "Purrl gives you $4!"
        
    elif result == 1:  # Cowboy Hat
        $ inventario.remove(1)
        prl "A cowboy hat! Fucking dominant!"
        $ perola_nivel_intimidade += 2
        $ money += 6
        "Purrl gives you $6!"
        
    elif result == 6:  # Nut Pie
        $ inventario.remove(6)
        prl "Expensive pie! You really spent money on me!"
        $ perola_nivel_intimidade += 4
        $ money += 10
        "Purrl gives you $10!"
    
    $ hora_do_dia += 1
    
    if pode_dar_presente():
        "You can give one more gift today."
    else:
        "Daily gift limit reached (2/2)."
    
    jump menu_principal_perola

# Labels for sexual actions that connect to purrlfucks
label ver_peitos_perola:
    jump ver_peitos_perola_full

label twerk_sexual_perola:
    jump twerk_sexual_perola_full

label punheta_perola:
    jump punheta_perola_full

label boquete_perola:
    jump boquete_perola_full

label foder_perola_anal:
    jump foder_perola_anal_full

label foder_perola_vaginal:
    jump foder_perola_vaginal_full

# Integration functions
label resetar_conversas_perola_diario:
    $ novo_dia_perola()
    return
    
label unlock_perola_house:
    $ mapa_disponivel = True
    "Purrl's house location added to map!"
    return