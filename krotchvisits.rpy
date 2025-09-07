# krotchhouse_visits.rpy - Pearl's House Visits and Conversations System

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
    show perola_excitada at center with vpunch:
        yalign 0.6
        zoom 0.5
    
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
        "Show me bitch":
            jump primeira_cena_twerk
            
        "Nah I don't give a fuck":
            prl "Well too bad!!"
            prl "I want to experience everything!"
            jump primeira_cena_twerk
            
        "Your dad could come back":
            prl "That makes it even more exciting!"
            jump primeira_cena_twerk

# First twerking scene
label primeira_cena_twerk:
    $ primeiro_twerk = True
    $ perola_acordou_sexualmente = True
    
    hide perola_excitada
    
    prl "I learned this thing called... twerking."
    prl "It's supposed to be... provocative."
    
    # Music starts
    play music audio.twerk_music fadein 1.0
    
    prl "Don't laugh, okay? This is my first time doing this for someone..."
    
    # Pearl starts twerking - VELOCIDADE NORMAL
    scene quarto_perola
    show perola_twerk_anim_normal at center
    
    "She's clearly inexperienced but enthusiastic."
    
    prl "Am I... am I doing it right?"
    prl "The videos made it look so easy..."
    
    b "Holy shit, Purrl..."
    
    # She gets more confident
    prl "You like it? I can feel something... awakening inside me..."
    prl "This feeling is incredible!"
    
    # The music and movement continue
    "Purrl gets more and more into it, discovering her sexuality."
    
    prl "I feel so... powerful! So sexy!"
    prl "Is this what being a woman feels like?"
    
    menu:
        "You're a natural":
            prl "Really? I feel like I was born for this!"
            $ perola_nivel_intimidade += 2
            
        "Fuck yeah! Don't stop now":
            prl "I don't want to stop! This feels amazing!"
            $ perola_nivel_intimidade += 1
            jump twerk_keep_going
            
        "Your father would have a heart attack":
            prl "Good! I'm tired of being his innocent little girl!"
            $ perola_nivel_intimidade += 2
    
    jump twerk_climax

# Quando jogador escolhe "Keep going"
label twerk_keep_going:
    prl "Yes! I want to keep going!"
    prl "I can feel the rhythm getting stronger!"
    
    # MUDAR PARA ANIMAÇÃO RÁPIDA
    hide perola_twerk_anim_normal
    show perola_twerk_anim_rapida at center
    
    "Purrl's movements become faster and more intense!"
    
    prl "Oh my God! This is so much better!"
    prl "I can't stop! My body is moving on its own!"
    
    b "That's it, Purrl! Let yourself go!"
    
    prl "I'm getting so excited! I never knew I could feel like this!"
    prl "My whole body is tingling!"
    
    "The faster rhythm makes Purrl lose all inhibitions."
    
    prl "I feel like... like I'm going to explode with pleasure!"
    prl "This is better than anything I've ever experienced!"
    
    jump twerk_climax

# Clímax da cena
label twerk_climax:
    # Climax of the scene
    hide perola_twerk_anim_normal
    hide perola_twerk_anim_rapida
    play audio "soco.mp3"
    show perola_excitada at center with vpunch:
        yalign 0.6
        zoom 0.5

    stop music fadeout 2.0
    pause (1.0)

    prl "Oh my God... I'm so... excited!"
    prl "I never felt anything like this before!"
    prl "My body is tingling all over!"
    
    hide perola_excitada
    show perola_excitada2 at center:
        yalign 0.6
        zoom 0.5
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

# Alternative paths
label perola_se_provoca:
    hide perola_provocante
    show perola_determinada at center
    
    prl "Spoiled kid? I'll show you what this 'kid' can do!"
    prl "I've been learning things online... things that would blow your mind!"
    prl "Want to see how 'spoiled' I really am?"
    
    jump primeira_cena_twerk

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
    
    "Visit completed! Purrl's intimacy level: [perola_nivel_intimidade]"
    
    jump room4

# Confrontation visit (if intimacy is still 0)
label visita_confronto_perola:
    scene quarto_perola
    show perola_irritada at center
    
    prl "You came back... I wasn't sure you would."
    prl "We still need to resolve this situation between us."
    
    menu:
        "What situation?":
            prl "The situation where you're pretending to be someone you're not!"
            $ perola_nivel_intimidade += 1
            
        "There's nothing to resolve":
            prl "Nothing?! You've completely changed!"
            
        "Maybe we can work something out":
            prl "Work something out? I'm listening..."
            $ perola_nivel_intimidade += 2
    
    jump despertar_sexual_perola

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

# NOVO: Visita PRO (3ª visita em diante) - Twerk Profissional
label visita_pro_perola:
    scene quarto_perola
    show perola_excitada at center
    
    prl "I've been practicing something special for you..."
    prl "I learned some... professional moves."
    
    if mr_krotch_em_casa:
        prl "*whispering* Dad's home, but I can't wait to show you this!"
        prl "I'll be extra quiet... but extra naughty."
    else:
        prl "Perfect! Dad's not here... I can really let loose!"
        prl "You're going to see a whole new side of me!"
    
    prl "I've been watching more... advanced videos online."
    prl "The things I learned... they're so much more exciting!"
    
    menu:
        "Show me these new moves":
            jump twerk_profissional_perola
            
        "How professional are we talking?":
            prl "Professional enough to drive you crazy!"
            prl "I've been practicing every day thinking about you..."
            jump twerk_profissional_perola
            
        "Talk to Pearl":
            jump menu_conversa_perola_casa
            
        "Give a gift to Pearl":
            jump menu_presentes_perola

# NOVO: Twerk Profissional (3ª visita)
label twerk_profissional_perola:
    prl "Get ready... this is going to blow your mind!"
    prl "I call this my 'professional performance'..."
    
    play music audio.twerk_music fadein 1.0
    
    # Nova animação PRO
    scene quarto_perola
    show perola_twerk_pro_anim_normal at center
    
    "Pearl's movements are completely different now..."
    "More confident, more sensual, more... professional."
    
    prl "Do you see the difference? I'm not that innocent girl anymore..."
    prl "I've learned how to move like a real woman!"
    
    b "Holy shit, Pearl... where did you learn this?"
    
    prl "Online... but I perfected it thinking about you watching me."
    prl "Every move is designed to drive you wild!"
    
    "Her technique is incredible - fluid, hypnotic, seductive."
    
    prl "I can go even faster now... want to see?"
    
    menu:
        "Show me how fast you can go":
            # Mudar para velocidade PRO rápida
            hide perola_twerk_pro_anim_normal
            show perola_twerk_pro_anim_rapida at center
            
            prl "Like this?! I can keep this pace for so long now!"
            prl "I've been building up my stamina... just for you!"
            
            "Pearl's professional moves at high speed are mesmerizing."
            
            prl "I love how you can't take your eyes off me!"
            prl "This is what months of practice gets you!"
            
            $ perola_nivel_intimidade += 3
            
        "That's already perfect":
            prl "Perfect? I'm just getting started!"
            prl "Wait until you see what I can do in our next visits..."
            $ perola_nivel_intimidade += 2
            
        "You're incredible":
            prl "Incredible? This is nothing compared to what I'm planning!"
            prl "I have so many more surprises for you..."
            $ perola_nivel_intimidade += 2
    
    stop music fadeout 1.0
    
    hide perola_twerk_pro_anim_normal
    hide perola_twerk_pro_anim_rapida
    show perola_satisfeita at center
    
    prl "That was just a taste of my new skills..."
    prl "Each visit, I get better and better for you."
    prl "Next time... I might show you even more advanced moves."
    
    $ hora_do_dia += 2
    jump final_visita_perola

# NOVA: Visita Íntima Avançada (6+ visitas) - CONECTA COM PURRLFUCKS
label visita_intima_avancada_perola:
    scene quarto_perola
    show perola_provocante at center
    
    prl "Finally... I've been waiting for this moment."
    prl "I think we're ready for... everything."
    
    if mr_krotch_em_casa:
        prl "*whispering seductively* Dad's home... that makes this even more exciting."
        prl "We'll have to be very... very quiet."
    else:
        prl "Perfect! We have the house to ourselves..."
        prl "I can be as loud as I want... and trust me, I want to be loud."
    
    prl "I've learned so much about my body... and what I want."
    prl "I want to explore everything with you."
    prl "Are you ready for the real Pearl?"
    
    menu:
        "I've been waiting for this":
            prl "Good... because I have so many ideas!"
            jump menu_perola_intima_avancada
            
        "Show me what you've learned":
            prl "Oh, I'll show you everything I've learned..."
            jump menu_perola_intima_avancada
            
        "What exactly do you have in mind?":
            prl "Everything... starting with soft touches and ending with..."
            prl "Well, you'll find out if you're brave enough."
            jump menu_perola_intima_avancada

# NOVO: Menu Íntimo Avançado (redirecionamentos para PURRLFUCKS)
label menu_perola_intima_avancada:
    scene quarto_perola
    show perola_provocante at center
    
    prl "What would you like to do with me today?"
    
    menu:
        "Professional twerking show":
            jump show_twerk_pro_performance
            
        "Sexual activities" if perola_nivel_intimidade >= 8:
            jump menu_atos_sexuais_perola_completo  # CONEXÃO COM PURRLFUCKS
            
        "Talk and gifts":
            jump menu_perola_casa_completo
            
        "Leave":
            jump room4

# Atividades românticas leves (ficam no krotchhouse)


# Other activities
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

label licao_confianca:
    prl "Confidence? I want to feel more powerful!"
    
    b "It's about knowing what you want and taking it."
    
    prl "What I want... is to feel more of what I felt yesterday."
    prl "That excitement, that energy..."
    
    $ perola_nivel_intimidade += 2
    
    jump despertar_mais_profundo

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

# Intimate visits (higher levels)
label visita_intima_perola:
    scene quarto_perola
    show perola_provocante at center
    
    prl "I've been waiting for you..."
    prl "I have so much to show you now."
    
    if perola_nivel_intimidade >= 8:
        prl "I'm ready for... everything."
        jump menu_atos_sexuais_perola_completo  # CONEXÃO COM PURRLFUCKS
    elif perola_nivel_intimidade >= 5:
        prl "I want to try new things today."
        jump menu_exploracao_perola
    else:
        prl "I've been practicing more moves..."
        jump menu_danca_avancada

label menu_exploracao_perola:
    menu:
        "What should we explore?"
            
        "Twerking with contact":
            jump twerk_com_contato
            

label show_twerk_pro_performance:
    prl "You want a show? Now I can give you a REAL performance!"
    prl "This is my professional routine!"
    
    play music audio.twerk_music fadein 1.0
    scene quarto_perola
    show perola_twerk_pro_anim_rapida at center
    
    "Pearl performs with incredible skill and confidence."
    "Her professional training shows in every movement."
    
    prl "This is what months of practice gets you!"
    prl "Every move calculated for maximum impact!"
    
    "Her technique is flawless and mesmerizing."
    
    prl "I can see the desire in your eyes... that's what I was aiming for."
    prl "This performance was designed specifically for you!"
    
    $ perola_nivel_intimidade += 2
    $ hora_do_dia += 1
    
    stop music fadeout 1.0
    
    hide perola_twerk_pro_anim_rapida
    show perola_satisfeita at center
    
    prl "That's my professional level performance!"
    prl "But if you want something even more special... you know what to choose."
    
    jump final_visita_perola

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
            
        "Professional twerking" if visitas_casa_perola >= 3:
            jump twerk_profissional_avancado
            
        "Basic twerking" if visitas_casa_perola < 3:
            jump twerk_basico_avancado
            
        "Sexual activities" if perola_nivel_intimidade >= 8:
            jump menu_atos_sexuais_perola_completo  # CONEXÃO COM PURRLFUCKS
            
        "Leave":
            jump room4

# CONVERSATION SYSTEM

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

# Conversation implementations
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

label conversa_perola_casa:
    prl "You know... you've changed my life."
    prl "Before you, I was just a boring rich girl."
    prl "Now I feel... alive."
    
    $ perola_nivel_intimidade += 1
    $ hora_do_dia += 1
    
    jump final_visita_perola

# Labels que estavam faltando



label twerk_com_contato:
    prl "I want to try something... more intimate."
    
    play music audio.twerk_music fadein 1.0
    
    scene quarto_perola
    
    # Verificar qual animação usar
    if visitas_casa_perola >= 3:
        show perola_twerk_pro_anim_normal at center
    else:
        show perola_twerk_anim_normal at center
    
    "Pearl starts twerking closer to you..."
    "The intimacy is electric."
    
    prl "This feels so much more intense..."
    prl "I can feel your energy..."
    
    $ perola_nivel_intimidade += 3
    $ hora_do_dia += 2
    
    stop music fadeout 1.0
    jump final_visita_perola

label menu_danca_avancada:
    prl "I want to show you my advanced moves!"
    jump twerk_avancado