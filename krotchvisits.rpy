# krotchvisits.rpy - Purrl's House Visits System - CLEAN VERSION (NO DUPLICATES)

# First visit scene
label perola_sozinha_primeira_vez:
    scene quarto_perola
    show pesuses:
      zoom 0.4 xpos 300 ypos 200
    
    prl "Alright, now it's just you and me, asshole."
    prl "Time to find out what the fuck is up with you."
    
    b "I told you already, I'm the same fucking Spoogebob."

    b "Bahahahaha! I'm readyyyy! I love moaning in the closet at cold nights la la la"
    
    prl "Bullshit! The Spoogebob I knew was a pussy!"
    prl "You're different. Rougher. Almost like a real man."
    
    hide pesuses
    show pehorny:
      zoom 0.4 xpos 300 ypos 200
    
    prl "You know what? Maybe I don't wanna rat you out."
    prl "You're not square like before."
    
    prl "You've got me feeling some type of way..."
    prl "Shit I never felt before."
    
    menu:
        "What kinda shit you talking about?":
            prl "Curious... about shit I never tried."
            prl "About what it's like with a real man."
            $ perola_nivel_intimidade += 1
            jump despertar_sexual_perola
            
        "You're just a spoiled little bitch":
            hide pehorny
            show pearl mad:
             zoom 0.4 xpos 300 ypos 200
       
            prl "How dare you call me a bitch at my own house!"
            prl "You work for my dad you fat loser"
            jump despertar_sexual_perola

# Sexual awakening
label despertar_sexual_perola:
    hide perola_provocante
    hide pesuses
    hide pehorny
    hide pearl mad
    show pesuses:
      zoom 0.4 xpos 300 ypos 200
    
    prl "You are lucky I'm really horny and dreaming about doing bad things!"
    
    b "How bad are we talking here hoe?"
    
    prl "Like... dirty stuff. Nasty shit."
    prl "Shit that would make my old man lose his fucking mind."
    
    prl "I've been watching videos online... learning..."

    b "Yeah we all watch porn, get to the point already my cock is getting hard"

    prl "Fine! You are really anti climatic you know that right?!"
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
    
    prl "I learned this thing called twerking."
    prl "It's supposed to make dicks hard."

    b "Oh boy here we go"
    
    play music audio.twerk_music fadein 1.0
    
    scene quarto_perola
    show perola_twerk_anim_normal at center
    
    prl "Am I doing this shit right?"
    prl "The videos made it look easy..."
    
    window hide
    $ renpy.pause(hard=False)

    b "Holy shit, Purrl..."
    b "(She sucks but that ass is HUGE)"
    
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

            b "Fuck yes!"

            window hide
            $ renpy.pause(hard=False)

            prl "You like staring at my butt huh?"
            $ perola_nivel_intimidade += 1
    
    stop music fadeout 2.0
    hide perola_twerk_anim_normal
    hide perola_twerk_anim_rapida
    
    play audio "soco.mp3"

    show perola_excitada with vpunch:
      zoom 0.5 xpos 400 ypos 250
    
    prl "Oh fuck... I'm so turned on!"
    prl "My legs are shaking so much!"

    prl "I can't even stand anymore..."
    
    window hide
    $ renpy.pause(hard=False)
    
    b "(Damn she is SOAKED down there)"

    prl "This is our secret, got it?"
    prl "Nobody can know about this."
    
    b "Who would I even talk about this? Fatrick?"
    b "Don't worry princess, your dirty secret is safe with me"
    
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

    window hide
    $ renpy.pause(hard=False)

    hide perola_twerk_anim_normal
    show perola_twerk_anim_rapida at center
    
    prl "See? I'm getting better!"
    prl "Your dick must be rock hard!"
    
    window hide
    $ renpy.pause(hard=False)

    $ perola_nivel_intimidade += 2
    
    stop music fadeout 1.0
    hide perola_twerk_anim_rapida

    play audio "soco.mp3"

    show perola_excitada with vpunch:
      zoom 0.48 xpos 500 ypos 250
    
    prl "Aaaah that's enough for my body today!"

    b "But my cock is super turned on now!"

    prl "T-tomorrow, come back again."
    prl "PLEASE!"
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

    prl "Now I'll show you my professional ass moves!"
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