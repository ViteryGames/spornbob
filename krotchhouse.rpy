# perola_casa.rpy - Pearl's House Visit System (English) - DESCOBERTA SEXUAL

# Variables for Pearl's house system
default perola_nivel_intimidade = 0  # Pearl's intimacy level with player
default visitas_casa_perola = 0  # Number of visits to Pearl's house
default primeiro_twerk = False  # Track if first twerking scene happened
default perola_acordou_sexualmente = False  # Track if Pearl awakened sexually
default ultimo_dia_visita_perola = -1  # Last day player visited Pearl
default mr_krotch_em_casa = True  # Track if Mr. Krotch is home
default perola_chantagem_resolvida = False  # Track if blackmail situation is resolved

# Pearl house images
image casa_perola_externa = "images/casa_perola_externa.png"
image quarto_perola = "images/quarto_perola.png"
image sala_perola = "images/sala_perola.png"
image perola_pijama = "images/perola_pijama.png"
image perola_provocante = "images/perola_provocante.png"
image perola_twerk_1 = "images/perola_twerk_1.png"
image perola_twerk_2 = "images/perola_twerk_2.png"
image perola_excitada = "images/perola_excitada.png"

# Twerking animation
image perola_twerk_anim:
    "perola_twerk_1"
    pause 0.4
    "perola_twerk_2"
    pause 0.4
    repeat

# Sound effects
define audio.twerk_music = "twerk_beat.mp3"
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

# Main label to visit Pearl's house
label visitar_casa_perola:
    # Check if address is known
    if not endereco_perola_descoberto:
        "You don't know where Pearl lives yet."
        jump room4
    
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
    
    scene casa_perola_externa
    "You arrive at the address Pearl gave you: Rua das Baleias, 69."
    "It's a large, luxurious house... Mr. Krotch's money shows."
    
    # Different scenarios based on visit number and intimacy level
    if visitas_casa_perola == 1:
        jump primeira_visita_perola
    elif perola_nivel_intimidade == 0:
        jump visita_confronto_perola  
    elif perola_nivel_intimidade < 3:
        jump visita_curiosidade_perola
    else:
        jump visita_intima_perola

# First visit - Confrontation and awakening
label primeira_visita_perola:
    play sound audio.porta_casa
    
    "You knock on the door aggressively."
    
    if mr_krotch_em_casa:
        scene sala_perola
        show krab surpreso at right
        show perola_irritada at left
        
        k "Spoogebob?! What are you doing here?!"
        
        prl "I called him here, dad! We need to have a serious talk!"
        
        k "About what, for Neptune's sake?!"
        
        prl "About his... changes lately."
        
        menu:
            "Mr. Krotch, can we talk privately?":
                k "Privately? About what?"
                prl "See, dad? Even his way of talking is different!"
                $ perola_nivel_intimidade += 1
                
            "Pearl wants to discuss business":
                k "Business? What business?"
                prl "The 'business' of him being weird as hell!"
                
            "Nothing important, just passing by":
                k "Just passing by? At our house?"
                prl "Nobody 'just passes by' here, dad!"
                $ perola_nivel_intimidade += 1
        
        k "Well... I need to go back to the restaurant anyway."
        k "You two... don't cause any trouble."
        
        hide krab surpreso with moveoutright
        
        jump perola_sozinha_primeira_vez
    
    else:
        # Mr. Krotch is not home
        scene quarto_perola
        show perola_pijama at center
        
        prl "So... you actually came, you bastard."
        prl "I wasn't sure you'd have the balls."
        
        jump perola_sozinha_primeira_vez

# Pearl alone for the first time
label perola_sozinha_primeira_vez:
    scene quarto_perola
    show perola_provocante at center
    
    prl "Alright, now it's just you and me."
    prl "Time to find out who you really are."
    
    b "I already told you, I'm Spoogebob."
    
    prl "Bullshit! The Spoogebob I knew was innocent, pure..."
    prl "You're... different. Rougher. More... manly."
    
    # She gets closer, studying him
    show perola_provocante at center:
        linear 2.0 xalign 0.7
    
    prl "You know what? I've been thinking..."
    prl "Maybe I don't want to expose you."
    
    b "Oh yeah? And why's that?"
    
    prl "Because... you're more interesting this way."
    prl "The real Spoogebob was boring as hell."
    
    # First moment of sexual tension
    prl "You've awakened something in me..."
    prl "Something I didn't even know existed."
    
    menu:
        "What kind of 'something'?":
            prl "Curiosity... about things I never experienced."
            prl "About what it's like to be with a real man."
            $ perola_nivel_intimidade += 2
            jump despertar_sexual_perola
            
        "You're just a spoiled kid":
            prl "Spoiled kid?! I'll show you who's a kid!"
            $ perola_nivel_intimidade += 1
            jump perola_se_provoca
            
        "Maybe we can make a deal":
            prl "A deal? What kind of deal?"
            $ perola_nivel_intimidade += 1
            jump proposta_acordo_perola

# Sexual awakening scene
label despertar_sexual_perola:
    hide perola_provocante
    show perola_excitada at center
    
    prl "I've never felt like this before..."
    prl "With school boys, it was all innocent kisses and hand-holding."
    prl "But you... you make me feel... different."
    
    b "Different how?"
    
    prl "Like I want to do... dangerous things."
    prl "Things that would shock my father."
    prl "Things that would shock everyone."
    
    # She starts getting bolder
    prl "I've been watching videos online... learning things..."
    prl "Want to see something I learned?"
    
    menu:
        "Show me":
            jump primeira_cena_twerk
            
        "This is moving too fast":
            prl "Too fast? Life is short!"
            prl "I want to experience everything!"
            jump primeira_cena_twerk
            
        "Your dad could come back":
            prl "That makes it even more exciting!"
            jump primeira_cena_twerk

# First twerking scene - THE SURPRISE
label primeira_cena_twerk:
    $ primeiro_twerk = True
    $ perola_acordou_sexualmente = True
    
    hide perola_excitada
    
    prl "I learned this thing called... twerking."
    prl "It's supposed to be... provocative."
    
    # Music starts
    play music audio.twerk_music fadein 1.0
    
    prl "Don't laugh, okay? This is my first time doing this for someone..."
    
    # Pearl starts twerking
    scene quarto_perola
    show perola_twerk_anim at center
    
    "Pearl starts moving her hips rhythmically..."
    "She's clearly inexperienced but enthusiastic."
    
    prl "Am I... am I doing it right?"
    prl "The videos made it look so easy..."
    
    b "Holy shit, Pearl..."
    
    # She gets more confident
    prl "You like it? I can feel something... awakening inside me..."
    prl "This feeling is incredible!"
    
    # The music and movement continue
    "Pearl gets more and more into it, discovering her sexuality."
    
    prl "I feel so... powerful! So sexy!"
    prl "Is this what being a woman feels like?"
    
    menu:
        "You're a natural":
            prl "Really? I feel like I was born for this!"
            $ perola_nivel_intimidade += 2
            
        "Keep going":
            prl "I don't want to stop! This feels amazing!"
            $ perola_nivel_intimidade += 1
            
        "Your father would have a heart attack":
            prl "Good! I'm tired of being his innocent little girl!"
            $ perola_nivel_intimidade += 2
    
    # Climax of the scene
    hide perola_twerk_anim
    show perola_excitada at center
    
    prl "Oh my God... I'm so... excited!"
    prl "I never felt anything like this before!"
    prl "My body is tingling all over!"
    
    stop music fadeout 2.0
    
    # Post-twerk conversation
    prl "This is our secret, right?"
    prl "Nobody can know about this... especially not dad."
    
    b "Your secret is safe with me."
    
    prl "Good... because this is just the beginning."
    prl "I want to learn more... experience more..."
    prl "Will you teach me?"
    
    $ perola_nivel_intimidade += 3
    $ hora_do_dia += 2
    
    jump final_primeira_visita

# Pearl provokes herself (alternative path)
label perola_se_provoca:
    hide perola_provocante
    show perola_determinada at center
    
    prl "Spoiled kid? I'll show you what this 'kid' can do!"
    
    # She starts doing something provocative
    prl "I've been learning things online... things that would blow your mind!"
    prl "Want to see how 'spoiled' I really am?"
    
    jump primeira_cena_twerk

# Deal proposal (alternative path)
label proposta_acordo_perola:
    prl "What kind of deal are we talking about?"
    
    b "I keep being interesting, you keep your mouth shut."
    
    prl "Hmm... and what do I get out of it?"
    prl "Besides your... 'interesting' company?"
    
    b "What do you want?"
    
    prl "I want to experience things... learn things..."
    prl "Things a boring Spoogebob could never teach me."
    
    jump despertar_sexual_perola

# End of first visit
label final_primeira_visita:
    scene quarto_perola
    show perola_satisfeita at center
    
    prl "This was... incredible."
    prl "I feel like I discovered a whole new side of myself."
    prl "When can you come back?"
    
    b "Whenever you want."
    
    prl "Tomorrow then. Same time."
    prl "And next time... I want to learn more."
    
    "Pearl's eyes sparkle with newfound desire and curiosity."
    "You've successfully awakened something in her."
    
    "Visit completed! Pearl's intimacy level: [perola_nivel_intimidade]"
    
    jump room4

# Subsequent visits - Curiosity phase
label visita_curiosidade_perola:
    scene quarto_perola
    
    if mr_krotch_em_casa:
        show perola_sussurrando at center
        prl "*whispering* Dad's home... we need to be quiet."
        prl "Come to my room."
    else:
        show perola_excitada at center
        prl "Perfect! Dad's at the restaurant."
        prl "We have the house to ourselves."
    
    prl "I've been thinking about yesterday all day..."
    prl "I want to learn more things."
    
    menu:
        "What do you want to learn?":
            jump menu_ensinar_perola
            
        "Show me that twerk again":
            jump repetir_twerk
            
        "Maybe we should slow down":
            prl "Slow down? I'm just getting started!"
            jump menu_ensinar_perola

# Teaching menu
label menu_ensinar_perola:
    menu:
        "What should I teach you?"
        
        "More advanced twerking":
            jump twerk_avancado
            
        "Other types of dancing":
            jump danca_sensual
            
        "How to be more confident":
            jump licao_confianca
            
        "Let's talk first":
            jump conversa_perola_casa

# Advanced twerking
label twerk_avancado:
    prl "Yes! I want to get better at it!"
    prl "Teach me your techniques!"
    
    play music audio.twerk_music fadein 1.0
    
    show perola_twerk_anim at center
    
    prl "Like this? Am I moving it right?"
    
    b "Lower... slower... feel the rhythm."
    
    prl "Oh! Like this?"
    prl "I can feel it... this power over you..."
    
    $ perola_nivel_intimidade += 1
    
    "Pearl practices for several minutes, getting more confident."
    
    stop music fadeout 1.0
    
    prl "I'm getting good at this, aren't I?"
    prl "Next time, I want to try... other things."
    
    $ hora_do_dia += 2
    jump final_visita_perola

# Sensual dancing
label danca_sensual:
    prl "Other dances? Like what?"
    
    b "Slower, more sensual movements."
    
    play music "sensual_music.mp3" fadein 1.0
    
    show perola_danca_sensual at center
    
    prl "This feels so... intimate."
    prl "I love how you look at me when I move like this..."
    
    $ perola_nivel_intimidade += 1
    $ hora_do_dia += 2
    
    jump final_visita_perola

# Confidence lesson
label licao_confianca:
    prl "Confidence? I want to feel more powerful!"
    
    b "It's about knowing what you want and taking it."
    
    prl "What I want... is to feel more of what I felt yesterday."
    prl "That excitement, that energy..."
    
    $ perola_nivel_intimidade += 2
    
    jump despertar_mais_profundo

# Deeper awakening
label despertar_mais_profundo:
    prl "I've been having... dreams... about you."
    prl "About the things we could do together."
    prl "Is that normal?"
    
    b "Completely normal."
    
    prl "I want to explore these feelings more..."
    prl "Will you help me?"
    
    $ perola_nivel_intimidade += 2
    $ hora_do_dia += 2
    
    jump final_visita_perola

# Repeat twerking
label repetir_twerk:
    prl "I've been practicing!"
    
    play music audio.twerk_music fadein 1.0
    show perola_twerk_anim at center
    
    "Pearl's twerking is much more confident now."
    
    prl "I'm getting better, right?"
    prl "I love the way you watch me..."
    
    $ perola_nivel_intimidade += 1
    $ hora_do_dia += 1
    
    stop music fadeout 1.0
    jump final_visita_perola

# Intimate visits (higher levels)
label visita_intima_perola:
    scene quarto_perola
    show perola_provocante at center
    
    prl "I've been waiting for you..."
    prl "I have so much to show you now."
    
    if perola_nivel_intimidade >= 8:
        prl "I'm ready for... everything."
        jump menu_atos_sexuais_perola
    elif perola_nivel_intimidade >= 5:
        prl "I want to try new things today."
        jump menu_exploracao_perola
    else:
        prl "I've been practicing more moves..."
        jump menu_danca_avancada

# Sexual acts menu (high intimacy)
label menu_atos_sexuais_perola:
    menu:
        "What do you want to do?"
        
        "Advanced intimacy":
            jump cena_sexual_perola
            
        "Twerking performance":
            jump show_twerk_perola
            
        "Teaching session":
            jump ensinar_perola_avancado

# Advanced exploration menu
label menu_exploracao_perola:
    menu:
        "What should we explore?"
        
        "Physical intimacy":
            jump exploracao_fisica
            
        "Twerking with contact":
            jump twerk_com_contato
            
        "Confidence building":
            jump construir_confianca

# Conversation at Pearl's house
label conversa_perola_casa:
    prl "You know... you've changed my life."
    prl "Before you, I was just a boring rich girl."
    prl "Now I feel... alive."
    
    $ perola_nivel_intimidade += 1
    $ hora_do_dia += 1
    
    jump final_visita_perola

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
    "Next visit will unlock new options."
    
    jump room4

# perola_gifts_conversations.rpy - Pearl Gift and Conversation System

# Variables for Pearl's conversation and gift system
default perola_ultimas_conversas = []  # Track recent conversation topics
default perola_presentes_dados = []    # Track gifts given to Pearl
default perola_humor = "normal"        # Pearl's current mood (normal, happy, excited, angry)

# Pearl conversation and gift system integration
# Add these labels to perola_casa.rpy

# Enhanced menu for Pearl's house with gifts and conversations
label menu_perola_casa_completo:
    scene quarto_perola
    show perola_normal at center
    
    prl "What do you want to do today?"
    
    menu:
        "Talk to Pearl":
            jump menu_conversa_perola_casa
            
        "Give a gift to Pearl":
            jump menu_presentes_perola
            
        "Sexual activities" if perola_nivel_intimidade >= 8:
            jump menu_atos_sexuais_perola
            
        "Advanced twerking" if perola_nivel_intimidade >= 5:
            jump twerk_avancado
            
        "Leave":
            jump room4

# Conversation menu for Pearl
label menu_conversa_perola_casa:
    menu:
        "What do you want to talk about?"
        
        "Ask about her life":
            jump conversa_vida_perola
            
        "Talk about her father":
            jump conversa_pai_perola
            
        "Ask about school":
            jump conversa_escola_perola
            
        "Talk about her interests":
            jump conversa_interesses_perola
            
        "Compliment her":
            jump elogiar_perola
            
        "Ask about her dreams":
            jump conversa_sonhos_perola
            
        "Go back":
            jump menu_perola_casa_completo

# Conversation about her life
label conversa_vida_perola:
    $ dialogo_random = renpy.random.randint(1, 4)
    
    if "vida" not in perola_ultimas_conversas:
        if dialogo_random == 1:
            prl "My life? It's... complicated."
            prl "Being the daughter of the richest crab in town has its pros and cons."
            prl "Everyone expects me to be perfect, but I want to be... wild."
            
        elif dialogo_random == 2:
            prl "I've been so sheltered all my life..."
            prl "Dad never let me experience real things."
            prl "That's why meeting you has been so... exciting."
            
        elif dialogo_random == 3:
            prl "I used to be such a good girl..."
            prl "But you've awakened something in me that I can't ignore."
            prl "I want to explore this new side of myself."
            
        else:
            prl "My life changed completely since you appeared."
            prl "Before, everything was boring and predictable."
            prl "Now every day is an adventure!"
        
        $ perola_nivel_intimidade += 1
        $ perola_ultimas_conversas.append("vida")
    else:
        prl "We already talked about my life recently..."
        prl "But I love that you're interested in me."
    
    $ hora_do_dia += 1
    jump menu_conversa_perola_casa

# Conversation about her father
label conversa_pai_perola:
    $ dialogo_random = renpy.random.randint(1, 4)
    
    if "pai" not in perola_ultimas_conversas:
        if dialogo_random == 1:
            prl "Dad is... obsessed with money."
            prl "Sometimes I feel like he cares more about his coins than about me."
            prl "That's why I like rebelling against him."
            
        elif dialogo_random == 2:
            prl "He thinks I'm still his innocent little girl..."
            prl "If he knew what we do together, he'd have a heart attack!"
            prl "But that makes it even more exciting."
            
        elif dialogo_random == 3:
            prl "Dad wants to control everything in my life..."
            prl "My friends, my clothes, my activities..."
            prl "But with you, I feel free for the first time."
            
        else:
            prl "I love dad, but he's so old-fashioned..."
            prl "He doesn't understand that I'm becoming a woman."
            prl "You understand me better than he ever will."
        
        $ perola_nivel_intimidade += 1
        $ perola_ultimas_conversas.append("pai")
    else:
        prl "We already talked about dad..."
        prl "I prefer talking about us."
    
    $ hora_do_dia += 1
    jump menu_conversa_perola_casa

# Conversation about school
label conversa_escola_perola:
    $ dialogo_random = renpy.random.randint(1, 4)
    
    if "escola" not in perola_ultimas_conversas:
        if dialogo_random == 1:
            prl "School is so boring compared to this!"
            prl "All the boys there are so immature..."
            prl "They have no idea what a real woman wants."
            
        elif dialogo_random == 2:
            prl "My friends at school would be so jealous if they knew..."
            prl "They all talk big but none of them have really lived."
            prl "I'm getting experiences they could never imagine."
            
        elif dialogo_random == 3:
            prl "I can barely concentrate on classes anymore..."
            prl "All I think about is coming home to see you."
            prl "You've become my favorite subject."
            
        else:
            prl "Sometimes I want to tell my friends about you..."
            prl "But this is our secret, isn't it?"
            prl "It makes everything more special."
        
        $ perola_nivel_intimidade += 1
        $ perola_ultimas_conversas.append("escola")
    else:
        prl "School is still boring..."
        prl "But being here with you never gets old."
    
    $ hora_do_dia += 1
    jump menu_conversa_perola_casa

# Conversation about her interests
label conversa_interesses_perola:
    $ dialogo_random = renpy.random.randint(1, 4)
    
    if "interesses" not in perola_ultimas_conversas:
        if dialogo_random == 1:
            prl "I used to love cheerleading and shopping..."
            prl "But now I'm interested in... more adult things."
            prl "You've opened my eyes to a whole new world."
            
        elif dialogo_random == 2:
            prl "I've been watching videos online... learning things..."
            prl "I want to try everything I see."
            prl "Will you help me explore?"
            
        elif dialogo_random == 3:
            prl "My biggest interest now is... you."
            prl "Learning what you like, how to please you..."
            prl "I think about it all the time."
            
        else:
            prl "I love music and dancing now..."
            prl "Especially that twerking you taught me."
            prl "It makes me feel so powerful and sexy."
        
        $ perola_nivel_intimidade += 1
        $ perola_ultimas_conversas.append("interesses")
    else:
        prl "My interests keep evolving..."
        prl "Especially the ones involving you."
    
    $ hora_do_dia += 1
    jump menu_conversa_perola_casa

# Compliment Pearl
label elogiar_perola:
    $ dialogo_random = renpy.random.randint(1, 4)
    
    menu:
        "What compliment do you want to give?"
        
        "You're beautiful":
            if dialogo_random <= 2:
                prl "Really? I've been working out more..."
                prl "I want to have the perfect body for you."
                $ perola_nivel_intimidade += 1
            else:
                prl "Thank you! I love when you notice me."
                $ perola_nivel_intimidade += 1
                
        "You're very smart":
            if dialogo_random <= 2:
                prl "Smart enough to know what I want..."
                prl "And what I want is you."
                $ perola_nivel_intimidade += 2
            else:
                prl "I'm smart enough to keep our secret safe."
                $ perola_nivel_intimidade += 1
                
        "You're incredibly sexy":
            if perola_nivel_intimidade >= 5:
                prl "I love being sexy for you..."
                prl "You make me feel like a real woman."
                $ perola_nivel_intimidade += 2
            else:
                prl "Sexy? I'm still learning to be sexy..."
                prl "But I'm glad you think so."
                $ perola_nivel_intimidade += 1
                
        "You're perfect":
            prl "Perfect? Only when I'm with you."
            prl "You bring out the best in me."
            $ perola_nivel_intimidade += 2
    
    $ hora_do_dia += 1
    jump menu_conversa_perola_casa

# Conversation about dreams
label conversa_sonhos_perola:
    $ dialogo_random = renpy.random.randint(1, 3)
    
    if "sonhos" not in perola_ultimas_conversas:
        if dialogo_random == 1:
            prl "I dream about traveling the world..."
            prl "Experiencing everything life has to offer."
            prl "And I want you to be part of that journey."
            
        elif dialogo_random == 2:
            prl "I dream about being free from all expectations..."
            prl "Just being myself, wild and uninhibited."
            prl "With you, I feel like I can be that person."
            
        else:
            prl "Lately I've been having... different kinds of dreams..."
            prl "Dreams about you... about us..."
            prl "They're so vivid and exciting."
        
        $ perola_nivel_intimidade += 2
        $ perola_ultimas_conversas.append("sonhos")
    else:
        prl "My dreams keep getting more intense..."
        prl "All of them involve you somehow."
    
    $ hora_do_dia += 1
    jump menu_conversa_perola_casa

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
    
    if 2 not in perola_presentes_dados or perola_presentes_dados.count(2) == 1:
        show perola_feliz at center
        prl "Chocolate! I love chocolate!"
        prl "You remembered that I have a sweet tooth."
        prl "This is so thoughtful of you!"
        $ perola_nivel_intimidade += 2
    else:
        show perola_normal at center
        prl "More chocolate! You know me so well."
        prl "I could eat chocolate all day."
        $ perola_nivel_intimidade += 1
    
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

# Function to reset conversation topics daily
init python:
    def reset_conversas_perola():
        global perola_ultimas_conversas
        perola_ultimas_conversas = []
    
    # Call this function at the start of each new day
    def novo_dia_perola():
        reset_conversas_perola()

# Integration function - add this to the main game day progression
label resetar_conversas_perola_diario:
    $ novo_dia_perola()
    return
    
# Function to add Pearl's house to map (call this after address is discovered)
label unlock_perola_house:
    $ mapa_disponivel = True
    "Pearl's house location added to map!"
    return
