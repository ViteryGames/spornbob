# krotchvisits.rpy - Purrl's House Visits System - CLEAN VERSION (NO DUPLICATES)

# First visit scene
label perola_sozinha_primeira_vez:
    scene quarto_perola
    show perola_provocante at center
    
    prl "Alright, now it's just you and me, asshole."
    prl "Time to find out what the fuck is up with you."
    
    b "I told you already, I'm fucking Spoogebob."
    
    prl "Bullshit! The Spoogebob I knew was a pussy."
    prl "You're different. Rougher. More of a real fucking man."
    
    show perola_provocante at center:
        linear 2.0 xalign 0.7
    
    prl "You know what? Maybe I don't wanna rat you out."
    prl "You're not boring as shit like before."
    
    prl "You've got me feeling some type of way..."
    prl "Shit I never felt before."
    
    menu:
        "What kinda shit you talking about?":
            prl "Curious... about shit I never tried."
            prl "About what it's like with a real man."
            $ perola_nivel_intimidade += 1
            jump despertar_sexual_perola
            
        "You're just a spoiled little bitch":
            prl "Spoiled bitch?! I'll show you who's a bitch!"
            jump despertar_sexual_perola

# Sexual awakening
label despertar_sexual_perola:
    hide perola_provocante
    show perola_excitada at center
    
    prl "Fuck... I never felt like this before..."
    prl "You make me wanna do bad shit."
    
    b "Bad how?"
    
    prl "Like... dirty shit. Nasty shit."
    prl "Shit that would make my old man lose his fucking mind."
    
    prl "I've been watching videos online... learning shit..."
    prl "Wanna see what I learned?"
    
    menu:
        "Show me":
            jump primeira_cena_twerk
            
        "I don't give a shit":
            prl "Too fucking bad! I'm gonna show you anyway!"
            jump primeira_cena_twerk

# First twerking scene
label primeira_cena_twerk:
    $ primeiro_twerk = True
    $ perola_acordou_sexualmente = True
    
    prl "I learned this shit called twerking."
    prl "It's supposed to make dicks hard."
    
    play music audio.twerk_music fadein 1.0
    
    scene quarto_perola
    show perola_twerk_anim_normal at center
    
    prl "Am I doing this shit right?"
    prl "The videos made it look easy..."
    
    b "Holy shit, Purrl..."
    
    prl "You like it? I feel something wild inside me..."
    prl "This feeling is fucking incredible!"
    
    menu:
        "You're a natural":
            prl "For real? I was born for this shit!"
            $ perola_nivel_intimidade += 2
            
        "Keep that ass moving":
            prl "I don't wanna stop!"
            hide perola_twerk_anim_normal
            show perola_twerk_anim_rapida at center
            prl "Faster! Like this?"
            $ perola_nivel_intimidade += 1
    
    stop music fadeout 2.0
    hide perola_twerk_anim_normal
    hide perola_twerk_anim_rapida
    show perola_excitada at center
    
    prl "Oh fuck... I'm so turned on!"
    prl "Never felt shit like this before!"
    
    prl "This is our secret, got it?"
    prl "Nobody can know about this."
    
    b "Yeah whatever."
    
    prl "Good... come back tomorrow."
    prl "I wanna learn more..."
    
    $ hora_do_dia += 2
    
    "Visit completed! Purrl's intimacy level: [perola_nivel_intimidade]"
    
    jump room4

# Second visit development
label segunda_visita_desenvolvimento:
    prl "Yesterday was fucking insane."
    prl "I couldn't stop thinking about it."
    
    menu:
        "Show me that twerk again":
            prl "You liked it that much?"
            jump twerk_segunda_visita
            
        "Let's talk first":
            prl "Talk? About what?"
            jump conversa_segunda_visita

label twerk_segunda_visita:
    play music audio.twerk_music fadein 1.0
    scene quarto_perola
    show perola_twerk_anim_normal at center
    
    prl "I've been practicing!"
    prl "Watch this shit!"
    
    hide perola_twerk_anim_normal
    show perola_twerk_anim_rapida at center
    
    prl "See? I'm getting better!"
    prl "Your dick must be rock hard!"
    
    $ perola_nivel_intimidade += 2
    
    stop music fadeout 1.0
    hide perola_twerk_anim_rapida
    show perola_satisfeita at center
    
    prl "Tomorrow, come back again."
    prl "From now on, we can do whatever we want."
    
    $ hora_do_dia += 2
    jump room4

label conversa_segunda_visita:
    prl "You actually wanna talk? Fine."
    
    menu:
        "About your life":
            prl "My life is fucked up but getting better."
            prl "Since you showed up, everything changed."
            $ perola_nivel_intimidade += 1
            
        "About us":
            prl "Us? There's an us now?"
            prl "I guess... I do think about you a lot."
            $ perola_nivel_intimidade += 1
    
    $ hora_do_dia += 1
    jump twerk_segunda_visita

# Conversations (simplified and direct)
label conversa_vida_perola:
    if "vida" not in perola_ultimas_conversas:
        prl "My life? It's fucked up."
        prl "Being that greedy bastard's daughter ain't easy."
        prl "But meeting you changed everything."
        $ perola_nivel_intimidade += 1
        $ perola_ultimas_conversas.append("vida")
    else:
        prl "We already talked about that shit."
    
    $ hora_do_dia += 1
    jump menu_principal_perola

label conversa_pai_perola:
    if "pai" not in perola_ultimas_conversas:
        prl "Dad's obsessed with fucking money."
        prl "If he knew what we do, he'd have a heart attack."
        prl "But fuck him, I do what I want."
        $ perola_nivel_intimidade += 1
        $ perola_ultimas_conversas.append("pai")
    else:
        prl "Already told you about that old bastard."
    
    $ hora_do_dia += 1
    jump menu_principal_perola

label conversa_escola_perola:
    if "escola" not in perola_ultimas_conversas:
        prl "School is boring as fuck."
        prl "All the boys there are pussies."
        prl "You're the only real man I know."
        $ perola_nivel_intimidade += 1
        $ perola_ultimas_conversas.append("escola")
    else:
        prl "School's still boring."
    
    $ hora_do_dia += 1
    jump menu_principal_perola

label elogiar_perola:
    menu:
        "You're hot as fuck":
            prl "Damn right I am!"
            $ perola_nivel_intimidade += 1
            
        "That ass is incredible":
            prl "You love staring at it, don't you?"
            $ perola_nivel_intimidade += 1
            
        "You're alright":
            prl "Just alright? Fuck you!"
            $ perola_nivel_intimidade += 0
    
    $ hora_do_dia += 1
    jump menu_principal_perola

# Placeholder images (keep these for compatibility)
image perola_feliz = "images/perola_feliz.png"
image perola_interessada = "images/perola_interessada.png"
image perola_brincalhona = "images/perola_brincalhona.png"
image perola_impressionada = "images/perola_impressionada.png"
image perola_duvidosa = "images/perola_duvidosa.png"
image perola_determinada = "images/perola_determinada.png"
image perola_excitada2 = "images/perola_excitada2.png"
image perola_sussurrando = "images/perola_sussurrando.png"
image perola_irritada = "images/perola_irritada.png"