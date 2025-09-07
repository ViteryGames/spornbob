# krotchhouse_main.rpy - Pearl's House Visit System (Main) - COMPLETE VERSION

# Variables for Pearl's house system
default perola_nivel_intimidade = 0  # Pearl's intimacy level with player
default visitas_casa_perola = 0  # Number of visits to Pearl's house
default primeiro_twerk = False  # Track if first twerking scene happened
default perola_acordou_sexualmente = False  # Track if Pearl awakened sexually
default ultimo_dia_visita_perola = -1  # Last day player visited Pearl
default mr_krotch_em_casa = True  # Track if Mr. Krotch is home
default perola_chantagem_resolvida = False  # Track if blackmail situation is resolved
default perola_ultimas_conversas = []  # Track recent conversation topics
default perola_presentes_dados = []    # Track gifts given to Pearl
default perola_humor = "normal"        # Pearl's current mood (normal, happy, excited, angry)

# Pearl house images
image casa_perola_externa = "images/casa_perola_externa.png"
image quarto_perola = "images/quarto_perola.png"
image sala_perola = "images/sala_perola.png"
image perola_pijama = "images/perola_pijama.png"
image perola_provocante = "images/perola_provocante.png"
image perola_excitada = "images/perola_excitada.png"

# ORIGINAL: Definições de frames para twerk (8 frames - sem frame0)
image perola_twerk_frame1 = "images/perola_twerk_frame1.png"
image perola_twerk_frame2 = "images/perola_twerk_frame2.png"
image perola_twerk_frame3 = "images/perola_twerk_frame3.png"
image perola_twerk_frame4 = "images/perola_twerk_frame4.png"
image perola_twerk_frame5 = "images/perola_twerk_frame5.png"
image perola_twerk_frame6 = "images/perola_twerk_frame6.png"
image perola_twerk_frame7 = "images/perola_twerk_frame7.png"
image perola_twerk_frame8 = "images/perola_twerk_frame8.png"

# NOVO: Frames para twerk profissional (desbloqueado na 3ª visita)
image perola_twerk_pro_frame1 = "images/perola_twerk_pro_frame1.png"
image perola_twerk_pro_frame2 = "images/perola_twerk_pro_frame2.png"
image perola_twerk_pro_frame3 = "images/perola_twerk_pro_frame3.png"
image perola_twerk_pro_frame4 = "images/perola_twerk_pro_frame4.png"
image perola_twerk_pro_frame5 = "images/perola_twerk_pro_frame5.png"
image perola_twerk_pro_frame6 = "images/perola_twerk_pro_frame6.png"
image perola_twerk_pro_frame7 = "images/perola_twerk_pro_frame7.png"
image perola_twerk_pro_frame8 = "images/perola_twerk_pro_frame8.png"

# ORIGINAL: Animações de twerk básico (mantendo sua versão)
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
    "perola_twerk_frame5"
    pause 0.15
    "perola_twerk_frame6"
    pause 0.15
    "perola_twerk_frame7"
    pause 0.15
    "perola_twerk_frame8"
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
    "perola_twerk_frame5"
    pause 0.15
    "perola_twerk_frame6"
    pause 0.15
    "perola_twerk_frame7"
    pause 0.15
    "perola_twerk_frame8"
    pause 0.1
    repeat

image perola_twerk_anim_rapida:
    "perola_twerk_frame1"
    pause 0.1
    "perola_twerk_frame2"
    pause 0.1
    "perola_twerk_frame3"
    pause 0.1
    "perola_twerk_frame4"
    pause 0.05
    "perola_twerk_frame5"
    pause 0.05
    "perola_twerk_frame6"
    pause 0.05
    "perola_twerk_frame7"
    pause 0.05
    "perola_twerk_frame8"
    pause 0.05
    "perola_twerk_frame4"
    pause 0.07
    "perola_twerk_frame5"
    pause 0.07
    "perola_twerk_frame6"
    pause 0.07
    "perola_twerk_frame7"
    pause 0.05
    "perola_twerk_frame8"
    pause 0.05
    repeat

# NOVO: Animações de twerk profissional (3ª visita+)
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

# Function to check if can visit Pearl today
init python:
    def pode_visitar_perola_hoje():
        global ultimo_dia_visita_perola, dia
        return ultimo_dia_visita_perola != dia
    
    def mr_krotch_esta_em_casa():
        global hora_do_dia
        # Mr. Krotch is at restaurant during work hours (8-20)
        return hora_do_dia < 8 or hora_do_dia > 20
    
    def reset_conversas_perola():
        global perola_ultimas_conversas
        perola_ultimas_conversas = []
    
    # Call this function at the start of each new day
    def novo_dia_perola():
        reset_conversas_perola()

# Main label to visit Pearl's house
label visitar_casa_perola:
    # Check if address is known
    if not endereco_perola_descoberto:
        "You don't know where Purrl lives yet."
        return
    
    scene casa_perola_externa
    "You arrive at Purrl's house on Whale Street, 69."
    "It's a large, luxurious house... Mr. Krotch's money shows."
    
    # Check if already visited today
    if not pode_visitar_perola_hoje():
        scene casa_perola_externa
        "You already visited Pearl today. Better come back tomorrow."
        "You can hear loud music and voices from inside..."
        jump room4
    
    # Mark visit
    $ ultimo_dia_visita_perola = dia
    $ visitas_casa_perola += 1
    
    # Check if Mr. Krotch is home
    $ mr_krotch_em_casa = mr_krotch_esta_em_casa()
    
    # Sistema de progressão baseado em visitas
    if visitas_casa_perola == 1:
        jump primeira_visita_perola
    elif perola_nivel_intimidade == 0:
        jump visita_confronto_perola  
    elif visitas_casa_perola >= 6:
        jump visita_intima_avancada_perola  # CONECTA COM PURRLFUCKS
    elif visitas_casa_perola >= 3:
        jump visita_pro_perola  # Twerk profissional
    elif perola_nivel_intimidade < 3:
        jump visita_curiosidade_perola
    else:
        jump visita_intima_perola

# Sistema de twerk com progressão
label twerk_avancado:
    if visitas_casa_perola >= 3:
        jump twerk_profissional_avancado
    else:
        jump twerk_basico_avancado

label twerk_basico_avancado:
    prl "Yes! I want to get better at it!"
    prl "Teach me your techniques!"
    
    play music audio.twerk_music fadein 1.0
    scene quarto_perola
    show perola_twerk_anim_normal at center
    
    prl "Like this? Am I moving it right?"
    
    b "Lower... slower... feel the rhythm."
    
    prl "Oh! Like this?"
    prl "I can feel it... this power over you..."
    
    "Pearl practices for several minutes, getting more confident."
    
    prl "I'm getting good at this, aren't I?"
    prl "I love how you look at me when I move like this..."
    
    menu:
        "Keep going faster":
            hide perola_twerk_anim_normal
            show perola_twerk_anim_rapida at center
            
            prl "Faster? Oh my God, yes!"
            prl "I can feel the energy building up!"
            
            "Pearl's movements become wild and uninhibited."
            
            prl "This is incredible! I feel so alive!"
            prl "I never want this feeling to end!"
            
            $ perola_nivel_intimidade += 2
            
        "That's perfect":
            prl "Perfect? Really? I feel like I could do even better!"
            $ perola_nivel_intimidade += 1
    
    stop music fadeout 1.0
    
    hide perola_twerk_anim_normal
    hide perola_twerk_anim_rapida
    show perola_satisfeita at center
    
    prl "That was amazing! Next time, I want to try... other things."
    
    $ hora_do_dia += 2
    jump final_visita_perola

label twerk_profissional_avancado:
    prl "Now I can show you my REAL skills!"
    prl "I've been perfecting my professional techniques!"
    
    play music audio.twerk_music fadein 1.0
    scene quarto_perola
    show perola_twerk_pro_anim_normal at center
    
    prl "This is what months of practice gets you!"
    prl "Every movement is calculated, every rhythm perfected."
    
    b "Holy shit, Pearl... you're incredible now."
    
    prl "Incredible? This is just my warm-up routine!"
    prl "Watch what I can do at full speed..."
    
    "Her professional technique is mesmerizing."
    
    prl "I can maintain this pace for so much longer now."
    prl "All that stamina training was worth it!"
    
    menu:
        "Show me your full speed":
            hide perola_twerk_pro_anim_normal
            show perola_twerk_pro_anim_rapida at center
            
            prl "Like this?! I can go even faster if you want!"
            prl "I've built up incredible stamina just for you!"
            
            "Pearl's professional moves at maximum speed are hypnotic."
            
            prl "This is what dedication to my craft looks like!"
            prl "Every second of practice was thinking about this moment!"
            
            $ perola_nivel_intimidade += 3
            
        "Your technique is flawless":
            prl "Flawless? I'm always finding ways to improve!"
            prl "Next time I'll show you some moves you've never seen before!"
            $ perola_nivel_intimidade += 2
    
    stop music fadeout 1.0
    
    hide perola_twerk_pro_anim_normal
    hide perola_twerk_pro_anim_rapida
    show perola_satisfeita at center
    
    prl "That's what happens when you combine natural talent with dedication!"
    prl "And I did it all for you..."
    
    $ hora_do_dia += 2
    jump final_visita_perola

# Repeat twerking com sistema de progressão
label repetir_twerk:
    if visitas_casa_perola >= 3:
        jump repetir_twerk_profissional
    else:
        jump repetir_twerk_basico

label repetir_twerk_basico:
    prl "I've been practicing!"
    
    play music audio.twerk_music fadein 1.0
    scene quarto_perola
    show perola_twerk_anim_rapida at center
    
    "Pearl's twerking is much more confident now."
    
    prl "I'm getting better, right?"
    prl "I love the way you watch me..."
    prl "Look how fast I can go now!"
    
    "Her movements are fluid and hypnotic."
    
    prl "I've been thinking about this all day!"
    prl "The way it makes me feel... it's addictive!"
    
    $ perola_nivel_intimidade += 1
    $ hora_do_dia += 1
    
    stop music fadeout 1.0
    
    hide perola_twerk_anim_rapida
    show perola_satisfeita at center
    
    jump final_visita_perola

label repetir_twerk_profissional:
    prl "I've been perfecting my professional routine!"
    prl "Wait until you see how much I've improved!"
    
    play music audio.twerk_music fadein 1.0
    scene quarto_perola
    show perola_twerk_pro_anim_rapida at center
    
    "Pearl's professional twerking is now at an expert level."
    
    prl "This is what dedication looks like!"
    prl "I can maintain this intensity for so much longer now!"
    prl "Every move is perfected... just for you!"
    
    "Her technique is flawless, mesmerizing, completely professional."
    
    prl "I've been practicing new variations too..."
    prl "This routine is constantly evolving!"
    
    b "You're incredible, Pearl."
    
    prl "Incredible? This is what happens when passion meets practice!"
    prl "And you're my inspiration for every single move!"
    
    $ perola_nivel_intimidade += 2
    $ hora_do_dia += 1
    
    stop music fadeout 1.0
    
    hide perola_twerk_pro_anim_rapida
    show perola_satisfeita at center
    
    prl "That's my professional level... and it keeps getting better!"
    
    jump final_visita_perola

# Gift menu for Pearl
label menu_presentes_perola:
    "What gift do you want to give Pearl?"
    
    # Check what items player has
    $ presentes_disponiveis = []
    $ nomes_presentes = []
    
    # Check specific items that Pearl would like
    if 2 in inventario:  # Chocolate
        $ presentes_disponiveis.append(2)
        $ nomes_presentes.append("Chocolate")
        
    if 10 in inventario:  # Books
        $ presentes_disponiveis.append(10)
        $ nomes_presentes.append("Books")
        
    if 16 in inventario:  # Soap Bubble
        $ presentes_disponiveis.append(16)
        $ nomes_presentes.append("Soap Bubble")
        
    if 19 in inventario:  # Pineapple
        $ presentes_disponiveis.append(19)
        $ nomes_presentes.append("Pineapple")
        
    if 1 in inventario:  # Cowboy Hat
        $ presentes_disponiveis.append(1)
        $ nomes_presentes.append("Cowboy Hat")
        
    if 6 in inventario:  # Nut Pie
        $ presentes_disponiveis.append(6)
        $ nomes_presentes.append("Nut Pie (Straight from Texas)")
        
    if 5 in inventario:  # Seaweed Pie
        $ presentes_disponiveis.append(5)
        $ nomes_presentes.append("Seaweed Pie")
    
    # Check if player has any gifts
    if len(presentes_disponiveis) == 0:
        "You don't have any gifts that Pearl might like."
        jump menu_perola_casa_completo
    
    # Create dynamic menu with available gifts
    $ result = renpy.display_menu([(nome, id_item) for nome, id_item in zip(nomes_presentes, presentes_disponiveis)] + [("Go back", -1)])
    
    # Process choice
    if result == -1:
        jump menu_perola_casa_completo
    elif result == 2:  # Chocolate
        jump presente_chocolate_perola
    elif result == 10:  # Books
        jump presente_livros_perola
    elif result == 16:  # Soap Bubble
        jump presente_bolhas_perola
    elif result == 19:  # Pineapple
        jump presente_abacaxi_perola
    elif result == 1:  # Cowboy Hat
        jump presente_chapeu_perola
    elif result == 6:  # Nut Pie
        jump presente_torta_noz_perola
    elif result == 5:  # Seaweed Pie
        jump presente_torta_alga_perola

# Individual gift reactions
label presente_chocolate_perola:
    $ inventario.remove(2)
    $ perola_presentes_dados.append(2)
    
    show perola_feliz at center
    prl "Chocolate! I love chocolate!"
    prl "You remembered that I have a sweet tooth."
    prl "This is so thoughtful of you!"
    $ perola_nivel_intimidade += 2
    
    $ money += 3
    "Pearl gives you $3 as thanks!"
    $ hora_do_dia += 1
    jump menu_perola_casa_completo

label presente_livros_perola:
    $ inventario.remove(10)
    $ perola_presentes_dados.append(10)
    
    show perola_interessada at center
    prl "Books? How... intellectual."
    prl "Are these the kind of books that will teach me... things?"
    prl "I love learning new things, especially from you."
    $ perola_nivel_intimidade += 3
    
    $ money += 5
    "Pearl gives you $5 for the educational gift!"
    $ hora_do_dia += 1
    jump menu_perola_casa_completo

label presente_bolhas_perola:
    $ inventario.remove(16)
    $ perola_presentes_dados.append(16)
    
    show perola_brincalhona at center
    prl "Soap bubbles! How cute and... innocent."
    prl "We could have fun with these..."
    prl "Maybe blow bubbles while we... do other things?"
    $ perola_nivel_intimidade += 1
    
    $ money += 2
    "Pearl gives you $2 for the playful gift!"
    $ hora_do_dia += 1
    jump menu_perola_casa_completo

label presente_abacaxi_perola:
    $ inventario.remove(19)
    $ perola_presentes_dados.append(19)
    
    show perola_provocante at center
    prl "A pineapple? This is... interesting."
    prl "It's so... phallic shaped..."
    prl "Are you trying to tell me something?"
    
    if perola_nivel_intimidade >= 6:
        prl "I know exactly what we could do with this..."
        $ perola_nivel_intimidade += 3
    else:
        prl "It's sweet and... hard. Like someone I know."
        $ perola_nivel_intimidade += 2
    
    $ money += 4
    "Pearl gives you $4 for the 'interesting' gift!"
    $ hora_do_dia += 1
    jump menu_perola_casa_completo

label presente_chapeu_perola:
    $ inventario.remove(1)
    $ perola_presentes_dados.append(1)
    
    show perola_excitada at center
    prl "A cowboy hat! How... dominant!"
    prl "I love men who take charge..."
    prl "Maybe you could wear this while we... play?"
    $ perola_nivel_intimidade += 2
    
    $ money += 6
    "Pearl gives you $6 for the dominant accessory!"
    $ hora_do_dia += 1
    jump menu_perola_casa_completo

label presente_torta_noz_perola:
    $ inventario.remove(6)
    $ perola_presentes_dados.append(6)
    
    show perola_impressionada at center
    prl "Nut pie from Texas! This is expensive!"
    prl "You really spent money on me..."
    prl "I'm so touched! This must mean I'm special to you."
    $ perola_nivel_intimidade += 4
    
    $ money += 10
    "Pearl gives you $10 for the expensive, thoughtful gift!"
    $ hora_do_dia += 1
    jump menu_perola_casa_completo

label presente_torta_alga_perola:
    $ inventario.remove(5)
    $ perola_presentes_dados.append(5)
    
    show perola_duvidosa at center
    prl "Seaweed pie? This is... different."
    prl "I guess it's the thought that counts..."
    prl "Thanks... I think?"
    $ perola_nivel_intimidade += 1
    
    $ money += 1
    "Pearl gives you $1, trying to be polite about the weird gift."
    $ hora_do_dia += 1
    jump menu_perola_casa_completo

# Final visit conclusion
label final_visita_perola:
    scene quarto_perola
    show perola_satisfeita at center
    
    prl "Thank you for today..."
    prl "I can't wait until next time."
    
    if perola_nivel_intimidade >= 10:
        prl "You've awakened the woman in me."
        prl "I'm completely yours now."
    elif perola_nivel_intimidade >= 5:
        prl "I'm learning so much about myself."
        prl "About what I really want."
    else:
        prl "This is just the beginning."
        prl "I want to discover everything."
    
    "Pearl's intimacy level: [perola_nivel_intimidade]"
    "Visits completed: [visitas_casa_perola]"
    
    if visitas_casa_perola == 2:
        "Next visit: Professional twerking unlocked!"
    elif visitas_casa_perola == 5:
        "Next visit: Intimate activities unlocked!"
    elif visitas_casa_perola >= 6:
        "All activities unlocked! Pearl is completely yours!"
    else:
        "Keep visiting to unlock new content!"
    
    jump room4

# Integration functions
label resetar_conversas_perola_diario:
    $ novo_dia_perola()
    return
    
label unlock_perola_house:
    $ mapa_disponivel = True
    "Pearl's house location added to map!"
    return