# boatingschool.rpy - Mrs. Puff's file
# Lesson system with rough ex-convict pretending to be SpongeBob

# Define Mrs. Puff character
define puff = Character("Mrs. Puffy", who_color="#ff69b4")
define b = Character("You", who_color="#ffff00")  # The protagonist pretending to be Bob

# Image definitions for Mrs. Puff
image mrs_puff normal = "images/puffy_idle.png"
image mrs_puff seducao = "images/puffyflirt.png"
image bg_escola_puffy = "images/bg_escola_puffy.png"

# Animations for handjob (Lesson 2) - 3 frames
image puffy_punheta_anim:
    "puffy_punheta_1"
    pause 0.4
    "puffy_punheta_2"
    pause 0.4
    "puffy_punheta_3"
    pause 0.4
    repeat

image puffy_punheta_anim_rapida:
    "puffy_punheta_1"
    pause 0.2
    "puffy_punheta_2"
    pause 0.2
    "puffy_punheta_3"
    pause 0.2
    repeat

# Animations for blowjob (Lesson 3) - 3 frames
image puffy_boquete_anim:
    "puffy_boquete_1"
    pause 0.4
    "puffy_boquete_2"
    pause 0.4
    "puffy_boquete_3"
    pause 0.4
    repeat

image puffy_boquete_anim_rapida:
    "puffy_boquete_1"
    pause 0.2
    "puffy_boquete_2"
    pause 0.2
    "puffy_boquete_3"
    pause 0.2
    repeat

# Animations for vaginal (Lesson 4) - 3 frames
image puffy_vaginal_anim:
    "puffy_vaginal_1"
    pause 0.4
    "puffy_vaginal_2"
    pause 0.4
    "puffy_vaginal_3"
    pause 0.4
    repeat

image puffy_vaginal_anim_rapida:
    "puffy_vaginal_1"
    pause 0.2
    "puffy_vaginal_2"
    pause 0.2
    "puffy_vaginal_3"
    pause 0.2
    repeat

# Animations for anal (Lesson 5) - 3 frames
image puffy_anal_anim:
    "puffy_anal_1"
    pause 0.4
    "puffy_anal_2"
    pause 0.4
    "puffy_anal_3"
    pause 0.4
    repeat

image puffy_anal_anim_rapida:
    "puffy_anal_1"
    pause 0.2
    "puffy_anal_2"
    pause 0.2
    "puffy_anal_3"
    pause 0.2
    repeat

# Cum images for each lesson
image puffy_gozada_punheta = "images/puffy_gozada_punheta.png"
image puffy_gozada_boquete = "images/puffy_gozada_boquete.png"
image puffy_gozada_vaginal = "images/puffy_gozada_vaginal.png"
image puffy_gozada_anal = "images/puffy_gozada_anal.png"

# Variables to track Mrs. Puff's state
default ja_visitou_puffy = False  # Tracks if already visited Mrs. Puff before
default aulas_completadas = 0  # Completed lessons counter
default ultimo_dia_aula = -1  # Stores the 'dia' variable value when a lesson was done
default favores_desbloqueados = False  # If favors were unlocked
default proposta_pendente = False  # If there's a pending proposal from lesson 2
default valor_proposta = 20  # Current proposal value

# Variables to control favors once per day
default ultimo_dia_favor_punheta = -1
default ultimo_dia_favor_boquete = -1
default ultimo_dia_favor_vaginal = -1
default ultimo_dia_favor_anal = -1

# Functions to check if can do lesson/favors today
init python:
    def pode_fazer_aula_hoje():
        global ultimo_dia_aula, dia
        return ultimo_dia_aula != dia
    
    def pode_fazer_favor_punheta():
        global ultimo_dia_favor_punheta, dia
        return ultimo_dia_favor_punheta != dia
        
    def pode_fazer_favor_boquete():
        global ultimo_dia_favor_boquete, dia
        return ultimo_dia_favor_boquete != dia
        
    def pode_fazer_favor_vaginal():
        global ultimo_dia_favor_vaginal, dia
        return ultimo_dia_favor_vaginal != dia
        
    def pode_fazer_favor_anal():
        global ultimo_dia_favor_anal, dia
        return ultimo_dia_favor_anal != dia

# Main label to interact with Mrs. Puff
label puffy:

    stop music
    play music "school.mp3"

    # First visit - special dialogue
    if not ja_visitou_puffy:
        scene bg_escola_puffy with dissolve
        "You arrive at Mrs. Puffy's Boating School."
        
        show puffyhappy at center
        
        puff "Well, well! If it isn't SpongeBob!"
        
        b "Yeah, that's me..."
        
        puff "Bob, dear, you've been failing so much in regular classes that I decided to offer you something special."
        
        puff "How about some private lessons? More... personalized methods?"
        
        b "What kind of methods?"
        
        hide puffyhappy
        show puffyflirt at center
        
        puff "Well, let's say they're more practical techniques. Hands-on, you know?"
        
        puff "I'm sure you'll perform much better with my individual attention..."
        
        b "Whatever. If it doesn't cost anything..."
        
        puff "Perfect! You can come here every day for a new lesson. I have a very... special curriculum prepared."
        
        $ ja_visitou_puffy = True
        
        jump menu_puffy
    else:
        # Subsequent visits
        scene bg_escola_puffy with dissolve
        "You arrive at Mrs. Puffy's Boating School."
        
        show mrs_puff normal at center
        
        puff "Welcome back, my special student!"
        
        jump menu_puffy

# Mrs. Puff's main menu
label menu_puffy:
    scene bg_escola_puffy
    stop music
    play music "school.mp3"
    show mrs_puff normal at center
    
    # Check if there's a pending proposal from lesson 2
    if proposta_pendente:
        jump aula_2_proposta
    
    menu:
        "What do you want to do?"
        
        # Start lesson - only if haven't done today
        "Start today's lesson ([aulas_completadas]/5 completed)" if pode_fazer_aula_hoje():
            jump aula_especial
            
        # Disabled version if already did lesson today
        "Lesson already done today (come back tomorrow)" if not pode_fazer_aula_hoje():
            puff "You already had your dose of learning for today, dear. Come back tomorrow for more!"
            jump menu_puffy
        
        # Special favors - only after 5 lessons
        "Special favors" if favores_desbloqueados:
            jump menu_favores_puffy
        
        "Talk to Mrs. Puffy":
            jump conversar_puffy
            
        "Leave":
            jump sair_puffy

# Progressive lesson system
label aula_especial:
    # Mark that did lesson today
    $ ultimo_dia_aula = dia
    
    # Different lessons based on progress
    if aulas_completadas == 0:
        jump aula_1
    elif aulas_completadas == 1:
        jump aula_2
    elif aulas_completadas == 2:
        jump aula_3
    elif aulas_completadas == 3:
        jump aula_4
    elif aulas_completadas == 4:
        jump aula_5
    else:
        # Repeated lessons after completing the 5
        jump aula_repetida

# LESSON 1 - Double entendre
label aula_1:
    show mrs_puff normal at center
    
    puff "Very good, Bob! Your first private lesson!"
    
    puff "Today we're going to work on your... driving technique. You need to learn how to hold the wheel properly."
    
    b "Hold the wheel? What the fuck is this shit?"
    
    show puffyflirt at center
    
    puff "Bob! Language! But I see you have... energy. That's good."
    
    puff "First, show me how you hold things. Take this bar here..."
    
    "Mrs. Puffy hands you a cylindrical bar and approaches."
    
    puff "That's it... now move it up and down... slowly... feel the movement..."
    
    b "What the fuck is this? Feels like I'm jerking off."
    
    puff "*blushing* Bob! It's... it's a coordination exercise! Continue... just like that..."
    
    puff "Now faster... feel the rhythm... that's it... perfect..."
    
    b "Yeah, this is weird as fuck. What kind of class is this?"
    
    puff "It's... advanced driving! Now show me how you... insert the key in the ignition."
    
    "She hands you a big key and points to a hole in the table."
    
    puff "Stick it in deep... carefully... that's it... turn it... harder..."
    
    b "You horny old bitch, are you turned on or what?"
    
    puff "*panting* I... I'm just being a dedicated teacher! Class dismissed for today!"
    
    $ aulas_completadas += 1
    $ hora_do_dia += 2
    jump menu_puffy

# LESSON 2 - Money proposal
label aula_2:

    hide mrs_puff normal
    show puffyflirt at center
    
    puff "Lesson two! Today we need to evaluate your... equipment."
    
    b "What equipment?"
    
    puff "Well, Bob... to be a good driver, I need to see if you have the... adequate size."
    
    puff "Can you pull down your pants so I can take a look?"
    
    b "WHAT THE FUCK?! Are you crazy, old lady?"
    
    puff "It's... it's just for educational purposes! Please?"
    
    b "Hell no! What kind of perverted school is this?"
    
    puff "Wait! What if I... pay you for it? Just a quick peek?"
    
    jump aula_2_proposta

label aula_2_proposta:
    $ proposta_pendente = True
    
    puff "How about $[valor_proposta] just to take a peek? It's easy money!"
    
    menu:
        "Accept the $[valor_proposta]":
            $ proposta_pendente = False
            $ money += valor_proposta
            $ valor_proposta = 20  # Reset for next time
            jump aula_2_aceita
            
        "Refuse":
            if valor_proposta < 60:
                $ valor_proposta += 20
                puff "Alright! How about $[valor_proposta]? It's a very good offer!"
                jump aula_2_proposta
            else:
                # Third refusal - leave
                jump aula_2_vai_embora

# Accepts showing the dick
label aula_2_aceita:
    b "Shit, for that money... alright."
    
    "You reluctantly pull down your pants."
    hide puffyflirt
    show puffywt

    puff "Wow! Bob! That's... much bigger than I imagined!"
    
    b "Yeah, prison makes a man grow. Now stop looking, I got my money."
    
    puff "Wait! Let me... touch it just a little? For... scientific purposes?"
    
    b "What the hell... whatever."
    
    # Change to sex scene and show animation
    scene bg_escola_puffy
    show puffy_punheta_anim
    
    "Mrs. Puffy approaches and starts touching timidly."
    
    puff "It's so... hard... and hot... is this normal?"
    
    b "Of course it's normal, you virgin. Never seen a dick before?"
    
    puff "I... well... can I move my hand like this?"
    
    "She starts moving her hand up and down."
    
    b "Hey old lady, now you're jerking me off."
    
    # Switch to fast animation
    hide puffy_punheta_anim
    show puffy_punheta_anim_rapida
    
    puff "*panting* It's... it's research! Anatomical research!"
    
    b "Keep going... I'm about to cum..."
    
    puff "Cumming? What does that mean?"
    
    b "You're about to find out!"
    
    # Show cum image
    hide puffy_punheta_anim_rapida
    show puffy_gozada_punheta
    
    with hpunch
    b "Take that, you curious bitch!"
    
    "She continues until you cum."
    
    puff "Wow! What was that white stuff?"
    
    b "Cum, you dummy. You made me cum."
    
    hide puffy_gozada_punheta
    show puffyflirt at center
    
    puff "Fascinating! Very... educational lesson!"
    
    puff "Here's $25 for your... educational patience!"
    
    $ money += 25
    $ aulas_completadas += 1
    $ hora_do_dia += 2
    jump menu_puffy

# Leaves in lesson 2
label aula_2_vai_embora:
    b "Not worth even $60. I'm leaving."
    
    puff "Wait! Bob! We can negotiate!"
    
    b "Fuck off, you perverted old lady."
    
    "You leave slamming the door."
    
    $ hora_do_dia += 1
    # Proposal remains pending for next visit
    jump sair_puffy

# LESSON 3 - Blowjob
label aula_3:
    scene bg_escola_puffy
    show puffyflirt at center
    
    puff "Lesson three! Today we're going to work on... oral skills."
    
    b "Oral skills? What the fuck is this now?"
    
    puff "Communication is important in driving! And I want to... practice with your equipment."
    
    b "You want to suck my dick, is that it?"
    
    puff "*blushing* I... well... it's for educational purposes!"
    
    b "Whatever. Go ahead and suck it."
    
    # Change to sex scene and show animation
    scene bg boat sex
    show puffy_boquete_anim
    
    "Mrs. Puffy is sucking your dick in the middle of the classroom."
    
    puff "Hmmmmmhmhmhm hmah mmhsmdms mm"
    
    b "WHAT?! Can't understand shit with my dick in your mouth, just suck and shut up!"
    
    "She obeys and stays quiet, continuing to try to suck it all."
    
    b "Damn, your mouth is small. Open wider."
    
    puff "*trying to talk with mouth full* Like this?"
    
    b "Better. Now move your tongue. That's it, continue."
    
    # Switch to fast animation
    hide puffy_boquete_anim
    show puffy_boquete_anim_rapida
    
    "Mrs. Puffy gains confidence and rhythm."
    
    b "Don't stop... I'm gonna cum..."
    
    puff "*trying to respond* Mmph!"
    
    # Show cum image
    hide puffy_boquete_anim_rapida
    show puffy_gozada_boquete
    
    with hpunch
    b "Swallow it all!"
    
    "You cum in her mouth."
    
    puff "*choking* It's... it's a lot! And it has a strange taste!"
    
    b "First time is always like that. You learn."
    
    hide puffy_gozada_boquete
    show puffyflirt at center
    
    puff "It was... interesting. Very educational!"
    
    puff "Here's $35 for the... practical lesson!"
    
    $ money += 35
    $ aulas_completadas += 1
    $ hora_do_dia += 2
    jump menu_puffy

# LESSON 4 - Vaginal
label aula_4:
    scene bg_escola_puffy
    show puffyflirt at center
    
    puff "Fourth lesson! Today is about... internal driving."
    
    b "Internal driving?"
    
    puff "Yes! You're going to... drive inside me!"
    
    b "You mean you want me to crack you?"
    
    puff "In... educational terms, yes!"
    
    "Mrs. Puffy takes off her clothes, revealing her body."
    
    b "Hmm, not bad for an old lady."
    
    puff "Thank you... I think. Now, be gentle, it's my first time."
    
    b "First time? How old are you anyway?"
    
    puff "That doesn't matter! Just... go slow."
    
    # Change to sex scene and show animation
    scene bg boat sex
    show puffy_vaginal_anim
    
    "You penetrate her without much delicacy."
    
    puff "Ow! It's... it's bigger than it looked!"
    
    b "Stop complaining and move."
    
    "You find a rhythm, with Mrs. Puff moaning loudly."
    
    puff "This is... incredible! Why didn't anyone teach me this before?"
    
    # Switch to fast animation
    hide puffy_vaginal_anim
    show puffy_vaginal_anim_rapida
    
    b "Because you're an old spinster. Now shut up, I'm gonna cum."
    
    puff "Harder! I want to feel everything!"
    
    # Show cum image
    hide puffy_vaginal_anim_rapida
    show puffy_gozada_vaginal
    
    with hpunch
    b "Take it all!"
    
    "You cum inside her."
    
    puff "I feel everything hot inside me! Is that normal?"
    
    b "Completely normal. Congratulations, you're not a virgin anymore."
    
    hide puffy_gozada_vaginal
    show puffyflirt at center
    
    puff "What a wonderful lesson!"
    
    puff "Here's $50 for the... complete educational experience!"
    
    $ money += 50
    $ aulas_completadas += 1
    $ hora_do_dia += 2
    jump menu_puffy

# LESSON 5 - Anal
label aula_5:
    show puffyflirt at center
    
    puff "Last lesson! Today is about... rear driving!"
    
    b "You want me to fuck your asshole?"
    
    puff "In educational terms... yes! I want to experience all forms of... direction."
    
    b "It's gonna hurt like hell."
    
    puff "I can take it! I'm stronger than I look!"
    
    "Mrs. Puffy lubes up her shithole"
    
    puff "Be gentle... it's virgin back there too."
    
    b "Virgin everywhere, how pathetic."
    
    # Change to sex scene and show animation
    scene bg boat sex
    show puffy_anal_anim
    
    "You penetrate her anally with little patience."
    
    puff "AAAHHH! It's... it's too much! Stop!"
    
    b "Relax, you asked for this."
    
    "Gradually she gets used to it and starts moaning."
    
    puff "It's... it's getting good! What a strange sensation!"
    
    b "Yeah, the ass is tight. Much better than pussy."
    
    # Switch to fast animation
    hide puffy_anal_anim
    show puffy_anal_anim_rapida
    
    puff "Harder! I want to feel everything!"
    
    b "Now you're getting the hang of it!"
    
    # Show cum image
    hide puffy_anal_anim_rapida
    show puffy_gozada_anal
    
    with hpunch
    b "I'm gonna fill your ass with cum!"
    
    "You increase the pace until you cum."
    
    puff "I feel it dripping! What a... complete experience!"
    
    b "There, now you've been fucked in all holes."
    
    hide puffy_gozada_anal
    show puffyflirt at center
    
    puff "Thank you so much for the... education. You can come here whenever you want more... lessons."
    
    puff "Here's $75 for the complete education!"
    
    $ money += 75
    $ aulas_completadas += 1
    $ favores_desbloqueados = True
    $ hora_do_dia += 2
    
    "SPECIAL FAVORS UNLOCKED!"
    
    jump menu_puffy

# Lessons after completing the 5
label aula_repetida:
    show puffyflirt at center
    
    $ aula_tipo = renpy.random.randint(2, 5)  # Lessons 2-5 available
    
    if aula_tipo == 2:
        puff "How about we review that... anatomical observation lesson?"
        jump favor_punheta
    elif aula_tipo == 3:
        puff "Let's practice more oral skills..."
        jump favor_boquete
    elif aula_tipo == 4:
        puff "How about more internal driving?"
        jump favor_vaginal
    else:
        puff "Time for rear driving!"
        jump favor_anal

# Favors menu (unlocked after 5 lessons)
label menu_favores_puffy:
    menu:
        "What special favor can Mrs. Puffy pay you to do?"
        
        "Handjob ($3)" if pode_fazer_favor_punheta():
            jump favor_punheta
            
        "Handjob (already done today)" if not pode_fazer_favor_punheta():
            puff "We already did that today, dear! Come back tomorrow!"
            jump menu_puffy
            
        "Blowjob ($5)" if pode_fazer_favor_boquete():
            jump favor_boquete
            
        "Blowjob (already done today)" if not pode_fazer_favor_boquete():
            puff "We already did that today, dear! Come back tomorrow!"
            jump menu_puffy
            
        "Vaginal Sex ($7)" if pode_fazer_favor_vaginal():
            jump favor_vaginal
            
        "Vaginal Sex (already done today)" if not pode_fazer_favor_vaginal():
            puff "We already did that today, dear! Come back tomorrow!"
            jump menu_puffy
            
        "Anal sex (Patreon only)":
             $ renpy.run(OpenURL("https://www.patreon.com/FRANKTOPIAGAMESTUDIO"))
             "Be a member and find out sweetheart"
             jump sou_puta
            
        "Anal Sex (already done today)" if not pode_fazer_favor_anal():
            puff "We already did that today, dear! Come back tomorrow!"
            jump menu_puffy
            
        "See tits ($2)":
            puff "Want to see my tits? I'll pay you $2 just to look!"
            $ money += 2
            hide mrs_puff normal
            show puffytits

            "Mrs. Puffy shows her breasts shyly while you observe."

            pause 2.0

            "My nipples get hard just by looking at that THING..."

            hide puffytits
            $ hora_do_dia += 1
            jump menu_puffy
            
        "Back":
            jump menu_puffy

# HANDJOB FAVOR - Repeats lesson 2
label favor_punheta:
    $ ultimo_dia_favor_punheta = dia
    $ money += 3
    
    puff "With pleasure! I'll pay you $3 to let me relieve you..."
    
    # Change to sex scene and show animation
    scene bg boat sex
    play music "sexmusic.wav"
    show puffy_punheta_anim
    
    puff "Let me touch your equipment again..."
    
    b "Go for it, old lady."
    
    "Mrs. Puffy approaches and starts touching with more confidence now."
    
    puff "I already know how you like it..."
    
    b "Yeah, you got a lot better."
    
    "She starts moving her hand up and down."
    
    # Switch to fast animation
    hide puffy_punheta_anim
    show puffy_punheta_anim_rapida
    
    puff "I'm gonna make you cum good!"
    
    b "Keep going... I'm almost there..."
    
    # Show cum image
    hide puffy_punheta_anim_rapida
    show puffy_gozada_punheta
    
    with hpunch
    b "That's it! Take that!"
    
    "You cum in her hands."
    
    puff "I love it when you cum for me!"
    
    hide puffy_gozada_punheta
    show puffyflirt at center
    
    $ hora_do_dia += 1
    jump menu_puffy

# BLOWJOB FAVOR - Repeats lesson 3
label favor_boquete:
    $ ultimo_dia_favor_boquete = dia
    $ money += 5
    
    puff "I'll use all the techniques I learned! I'll pay you $5!"
    
    # Change to sex scene and show animation
    scene bg boat sex
    play music "sexmusic.wav"
    show puffy_boquete_anim
    
    "Mrs. Puffy kneels with experience now."
    
    puff "Now I know exactly how to do it..."
    
    b "Show me what you learned."
    
    "She starts sucking with much more skill."
    
    puff "*with mouth full* Mmm... I like your taste..."
    
    b "Damn, you got a lot better at this."
    
    # Switch to fast animation
    hide puffy_boquete_anim
    show puffy_boquete_anim_rapida
    
    "Mrs. Puffyy speeds up the rhythm with confidence."
    
    b "Don't stop... I'm gonna cum..."
    
    # Show cum image
    hide puffy_boquete_anim_rapida
    show puffy_gozada_boquete
    
    with hpunch
    b "Swallow it all!"
    
    "You cum in her mouth."
    
    puff "Mmm... now I love that taste!"
    
    hide puffy_gozada_boquete
    show puffyflirt at center
    
    $ hora_do_dia += 1
    jump menu_puffy

# VAGINAL FAVOR - Repeats lesson 4
label favor_vaginal:
    $ ultimo_dia_favor_vaginal = dia
    $ money += 7
    
    puff "Let's drive together again! I'll pay you $7!"
    
    "Mrs. Puffy takes off her clothes eagerly."
    
    puff "I already miss you inside me..."
    
    b "Then come over here."
    
    # Change to sex scene and show animation
    scene bg boat sex
    play music "sexmusic.wav"
    show puffy_vaginal_anim
    
    "You penetrate her, and she receives with pleasure."
    
    puff "Ahh! How I wanted this!"
    
    b "You really became a whore, huh old lady?"
    
    "You find the rhythm quickly."
    
    puff "Your favorite whore! Continue!"
    
    # Switch to fast animation
    hide puffy_vaginal_anim
    show puffy_vaginal_anim_rapida
    
    b "Now you're asking for more, huh?"
    
    puff "I always want more of you!"
    
    # Show cum image
    hide puffy_vaginal_anim_rapida
    show puffy_gozada_vaginal
    
    with hpunch
    b "Take it all!"
    
    "You cum inside her intensely."
    
    puff "Delicious! I love feeling you cumming in me!"
    
    hide puffy_gozada_vaginal
    show puffyflirt at center
    
    $ hora_do_dia += 2
    jump menu_puffy

# ANAL FAVOR - Repeats lesson 5
label favor_anal:
    $ ultimo_dia_favor_anal = dia
    $ money += 9
    
    puff "Rear driving is my favorite now! I'll pay you $9!"
    
    "Mrs. Puffy positions herself to get it immediately."
    
    puff "Come on, stick it in my ass!"
    
    b "Look how you've changed..."
    
    # Change to sex scene and show animation
    scene bg boat sex
    play music "sexmusic.wav"
    show puffy_anal_anim
    
    "You penetrate her anally without resistance."
    
    puff "Ahhh! Delicious! Go deep!"
    
    b "Now you love taking it up the ass, don't you?"
    
    "She moves by herself, begging for more."
    
    puff "I love it! Destroy my ass!"
    
    # Switch to fast animation
    hide puffy_anal_anim
    show puffy_anal_anim_rapida
    
    b "You insatiable ass slut!"
    
    puff "I'm your bitch! Use me!"
    
    # Show cum image
    hide puffy_anal_anim_rapida
    show puffy_gozada_anal
    
    with hpunch
    b "Take cum in your ass!"
    
    "You fill her ass with cum."
    
    puff "Yes! Fill my ass with milk!"
    
    hide puffy_gozada_anal
    show puffyflirt at center
    
    $ hora_do_dia += 2
    jump menu_puffy

# Casual conversation
label conversar_puffy:
    $ dialogo_random = renpy.random.randint(1, 3)
    
    if dialogo_random == 1:
        puff "You know, Bob, you taught me a lot about... life."
        puff "Before you, I was so repressed. Now I feel free!"
        b "Yeah, prison teaches a lot about life."
        puff "Prison? Did you say prison?"
        b "I said driving. You're hearing wrong."
        
    elif dialogo_random == 2:
        puff "You're so different from other students, Bob."
        puff "So... experienced. Where did you learn all these things?"
        b "At the university of life, old lady."
        puff "What an interesting university! Must have a very practical curriculum."
        
    else:
        puff "Sometimes I feel guilty about our... educational methods."
        puff "But the results speak for themselves!"
        b "Yeah, I'm learning a lot here."
        puff "And me too! Especially about male anatomy!"
    
    jump menu_puffy

# Exit
label sair_puffy:

    puff "See you later, my favorite student! Come back whenever you want more... education."
    
    scene black with dissolve
    "You leave Mrs. Puffy's school..."
    stop music

    # Activate map to return
    $ mapa_disponivel = True
    call screen mapScreen