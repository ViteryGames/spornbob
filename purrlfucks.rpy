# purrlfucks.rpy - Pearl Sexual Content (English) - COMPLETE VERSION

# Sexual animations for Pearl
image perola_peitos_anim:
    "images/perola_peitos_1.png"
    pause 0.5
    "images/perola_peitos_2.png"
    pause 0.5
    repeat

# Twerking sexual animations
image perola_twerk_sexual_anim:
    "images/perola_twerk_sexual_1.png"
    pause 0.3
    "images/perola_twerk_sexual_2.png"
    pause 0.3
    "images/perola_twerk_sexual_3.png"
    pause 0.3
    repeat

image perola_twerk_sexual_rapida:
    "images/perola_twerk_sexual_1.png"
    pause 0.15
    "images/perola_twerk_sexual_2.png"
    pause 0.15
    "images/perola_twerk_sexual_3.png"
    pause 0.15
    repeat

# Handjob animations
image perola_punheta_anim:
    "images/perola_punheta_1.png"
    pause 0.4
    "images/perola_punheta_2.png"
    pause 0.4
    "images/perola_punheta_3.png"
    pause 0.4
    repeat

image perola_punheta_rapida:
    "images/perola_punheta_1.png"
    pause 0.2
    "images/perola_punheta_2.png"
    pause 0.2
    "images/perola_punheta_3.png"
    pause 0.2
    repeat

# Blowjob animations
image perola_boquete_anim:
    "images/perola_boquete_1.png"
    pause 0.35
    "images/perola_boquete_2.png"
    pause 0.35
    "images/perola_boquete_3.png"
    pause 0.35
    repeat

image perola_boquete_rapida:
    "images/perola_boquete_1.png"
    pause 0.15
    "images/perola_boquete_2.png"
    pause 0.15
    "images/perola_boquete_3.png"
    pause 0.15
    repeat

# Vaginal animations
image perola_vaginal_anim:
    "images/perola_vaginal_1.png"
    pause 0.4
    "images/perola_vaginal_2.png"
    pause 0.4
    "images/perola_vaginal_3.png"
    pause 0.4
    repeat

image perola_vaginal_rapida:
    "images/perola_vaginal_1.png"
    pause 0.2
    "images/perola_vaginal_2.png"
    pause 0.2
    "images/perola_vaginal_3.png"
    pause 0.2
    repeat

# Anal animations
image perola_anal_anim:
    "images/perola_anal_1.png"
    pause 0.4
    "images/perola_anal_2.png"
    pause 0.4
    "images/perola_anal_3.png"
    pause 0.4
    repeat

image perola_anal_rapida:
    "images/perola_anal_1.png"
    pause 0.18
    "images/perola_anal_2.png"
    pause 0.18
    "images/perola_anal_3.png"
    pause 0.18
    repeat

# Cum images
image perola_gozada_peitos = "images/perola_gozada_peitos.png"
image perola_gozada_boca = "images/perola_gozada_boca.png"
image perola_gozada_vaginal = "images/perola_gozada_vaginal.png"
image perola_gozada_anal = "images/perola_gozada_anal.png"

# Sound for sexual scenes
define audio.perola_gemidos = "audio/perola_moans.mp3"
define audio.sexmusic_perola = "audio/sexmusic_teen.mp3"
define audio.gozada = "audio/cum_sound.mp3"

# Variables for Pearl's sexual progression
default perola_vezes_peitos = 0
default perola_vezes_twerk_sexual = 0
default perola_vezes_punheta = 0
default perola_vezes_boquete = 0
default perola_vezes_vaginal = 0
default perola_vezes_anal = 0
default perola_ultimo_ato_sexual = -1

# NOVO: Variables for intimate activities from krotchhouse
default perola_vezes_toque_intimo = 0
default perola_vezes_massagem = 0
default perola_vezes_beijos_avancados = 0
default perola_vezes_exploracao = 0
default perola_vezes_surpresa = 0

# Function to check if can do sexual act today
init python:
    def pode_fazer_ato_sexual_perola():
        global perola_ultimo_ato_sexual, dia
        return perola_ultimo_ato_sexual != dia

# MAIN SEXUAL MENU - Connected from krotchhouse.rpy - WITH PROGRESSIVE UNLOCKING
label menu_atos_sexuais_perola_completo:
    if not pode_fazer_ato_sexual_perola():
        prl "We already had our fun today, tiger..."
        prl "Come back tomorrow and we'll explore more."
        jump final_visita_perola
    
    scene quarto_perola
    show perola_provocante at center
    
    prl "What do you want to do to me today?"
    
    # Show available options based on progression
    if perola_vezes_peitos == 0:
        prl "I'm ready to try... new things with you."
    elif perola_vezes_twerk_sexual == 0:
        prl "I want to show you more of my body..."
    elif perola_vezes_punheta == 0:
        prl "I'm ready to touch you... intimately."
    elif perola_vezes_anal == 0:
        prl "I want to try something... really naughty."
    elif perola_vezes_vaginal == 0:
        prl "I think I'm ready for... everything."
    else:
        prl "I'm ready for anything you want!"
    
    menu:
        "Intimate touching" if visitas_casa_perola >= 6:
            jump toque_intimo_perola_completo
            
        "Sensual massage" if visitas_casa_perola >= 6:
            jump massagem_sensual_perola_completo
            
        "Advanced kissing" if visitas_casa_perola >= 6:
            jump beijos_avancados_perola_completo
            
        "Body exploration" if visitas_casa_perola >= 6:
            jump exploracao_corpo_perola_completo
            
        "Pearl's special surprise" if visitas_casa_perola >= 6:
            jump surpresa_especial_perola_completo
            
        "Show me your tits":
            jump ver_peitos_perola
            
        "Sexual twerking performance" if perola_vezes_peitos >= 3:
            jump twerk_sexual_perola
            
        "I want a handjob" if perola_vezes_twerk_sexual >= 3:
            jump punheta_perola
            
        "Anal sex" if perola_vezes_punheta >= 3:
            jump foder_perola_anal
            
        "Fuck your pussy" if perola_vezes_anal >= 3:
            jump foder_perola_vaginal
            
        "Maybe later":
            jump final_visita_perola

# NOVO: Intimate Activities (from krotchhouse integration)
# Note: toque_intimo_perola_completo is defined in krotchhouse_visits.rpy

# NOVO: Massagem Sensual Completa
label massagem_sensual_perola_completo:
    $ perola_ultimo_ato_sexual = dia
    $ perola_vezes_massagem += 1
    
    if perola_vezes_massagem == 1:
        prl "I learned about massages online... want to try?"
        prl "I want to make you feel as good as you make me feel."
    else:
        prl "I've gotten so much better at massaging..."
        prl "Let me show you my improved technique."
    
    show perola_provocante at center
    
    "Pearl dims the lights and creates a more intimate atmosphere."
    
    prl "Lie down... let me take care of you."
    prl "I want to learn every inch of your body."
    
    "Her hands are surprisingly skilled, working out tension you didn't even know you had."
    
    if perola_vezes_massagem >= 2:
        prl "I know exactly where you like to be touched now..."
        prl "Let me massage... everywhere..."
        
        "Pearl's massage becomes increasingly erotic."
        
        prl "I love how hard you get when I touch you like this..."
        prl "Should I massage here too?"
        
        "She starts massaging more intimate areas."
        
        prl "I can feel how much you want me..."
        prl "This is making me so wet..."
    
    prl "I love how you relax under my touch..."
    prl "This makes me feel so powerful... so feminine."
    
    b "Where did you learn this?"
    
    prl "Videos... but mostly instinct. I want to please you."
    prl "Tell me what feels good... I want to learn everything."
    
    "The massage becomes increasingly sensual and intimate."
    
    prl "I could do this all day... taking care of you like this."
    prl "Next time, maybe you can return the favor?"
    
    if perola_vezes_massagem == 1:
        $ perola_nivel_intimidade += 3
    else:
        $ perola_nivel_intimidade += 2
    
    $ hora_do_dia += 2
    jump final_visita_perola

# NOVO: Beijos Avançados Completos
label beijos_avancados_perola_completo:
    $ perola_ultimo_ato_sexual = dia
    $ perola_vezes_beijos_avancados += 1
    
    if perola_vezes_beijos_avancados == 1:
        prl "I want to learn how to kiss properly..."
        prl "Not those innocent pecks from school boys."
    else:
        prl "I've been practicing my kissing technique..."
        prl "I want to show you how much I've improved."
    
    show perola_excitada at center
    
    "Pearl moves very close, her lips slightly parted."
    
    if perola_vezes_beijos_avancados == 1:
        prl "Teach me... show me what a real kiss feels like."
        prl "I've been watching movies and imagining this moment."
        
        "The first kiss is tentative, sweet, but quickly becomes more passionate."
        
        prl "Oh my God... I had no idea kissing could feel like this!"
        prl "My whole body is tingling... is this normal?"
        
        b "Completely normal."
        
        prl "I want to practice more... a lot more."
        prl "Kiss me again... I want to get better for you."
    else:
        prl "Kiss me like you did last time... but more intense."
        prl "I want to feel that electricity again."
        
        "Your kisses are immediately passionate and deep."
        
        prl "Mmm... yes! Just like that!"
        prl "I love how you take control..."
    
    "Each kiss becomes more confident, more passionate."
    
    if perola_vezes_beijos_avancados >= 3:
        prl "I want you to kiss me... everywhere..."
        prl "My neck... my shoulders... lower..."
        
        "You start kissing her neck and shoulders."
        
        prl "Oh God... that's driving me wild!"
        prl "Don't stop... kiss me everywhere!"
        
        "The kissing session becomes incredibly heated."
        
        prl "I'm getting so turned on from your kisses..."
        prl "I want more... so much more..."
    
    prl "I think I'm getting addicted to your lips..."
    prl "This is so much better than I ever imagined."
    
    if perola_vezes_beijos_avancados == 1:
        $ perola_nivel_intimidade += 3
    else:
        $ perola_nivel_intimidade += 2
    
    $ hora_do_dia += 2
    jump final_visita_perola

# NOVO: Exploração do Corpo Completa
label exploracao_corpo_perola_completo:
    $ perola_ultimo_ato_sexual = dia
    $ perola_vezes_exploracao += 1
    
    if perola_vezes_exploracao == 1:
        prl "I want us to explore each other..."
        prl "I'm so curious about everything."
    else:
        prl "I want to explore even more today..."
        prl "I've been thinking about this all week."
    
    show perola_provocante at center
    
    "Pearl's boldness has reached new levels."
    
    if perola_vezes_exploracao == 1:
        prl "I want to learn about your body... and I want you to learn about mine."
        prl "We can take it slow... but I want to feel everything."
        
        "The exploration is gentle but thorough, educational but deeply sensual."
        
        prl "This is incredible... I never knew touching could feel so good."
        prl "Every sensation is new and exciting."
    else:
        prl "I know what I like now... and I want more of it."
        prl "Touch me like you did last time... but don't hold back."
        
        "The exploration is immediately more intense and focused."
        
        prl "Yes! Right there... I love when you touch me there!"
        prl "I've been craving this feeling..."
    
    b "You're amazing, Pearl."
    
    prl "Amazing? I'm just discovering what I'm capable of..."
    prl "And I want to discover so much more with you."
    
    "The intimate exploration continues, building trust and passion."
    
    if perola_vezes_exploracao >= 2:
        prl "I want to explore you too..."
        prl "Can I touch you... everywhere?"
        
        "Pearl becomes more adventurous in her exploration."
        
        prl "You feel so good... so hard..."
        prl "I love learning about your body..."
    
    prl "I feel so safe with you... so free to be myself."
    prl "This is what I've been missing all my life."
    
    if perola_vezes_exploracao == 1:
        $ perola_nivel_intimidade += 5
    else:
        $ perola_nivel_intimidade += 3
    
    $ hora_do_dia += 3
    jump final_visita_perola

# NOVO: Surpresa Especial Completa
label surpresa_especial_perola_completo:
    $ perola_ultimo_ato_sexual = dia
    $ perola_vezes_surpresa += 1
    
    if perola_vezes_surpresa == 1:
        prl "I have a very special surprise for you today..."
        prl "Something I've been planning for weeks."
    else:
        prl "I have another surprise for you..."
        prl "Each time I try to outdo myself."
    
    show perola_excitada at center
    
    prl "Close your eyes... and don't open them until I say so."
    
    "You close your eyes and hear rustling sounds, music starting softly."
    
    prl "Okay... open them now."
    
    if perola_vezes_surpresa == 1:
        # Combinação de twerk profissional com elementos sensuais
        play music audio.twerk_music fadein 1.0
        scene quarto_perola
        show perola_twerk_pro_anim_normal at center
        
        prl "This is my ultimate performance... just for you."
        prl "Every move, every rhythm... it's all designed to show you how much I want you."
        
        "Pearl combines her professional twerking skills with incredibly sensual movements."
        
        prl "I practiced this routine thinking about you every single time."
        prl "This is me... completely yours."
        
        menu:
            "This is incredible":
                hide perola_twerk_pro_anim_normal
                show perola_twerk_pro_anim_rapida at center
                
                prl "Incredible? This is just the warm-up!"
                prl "Now comes the real surprise..."
                
                "Pearl's routine becomes even more intimate and personal."
                
                prl "I want you to remember this moment forever..."
                prl "Because this is when I became completely yours."
                $ perola_nivel_intimidade += 5
                
            "You're perfect":
                prl "Perfect for you... only for you."
                prl "Everything I do is to make you happy."
                $ perola_nivel_intimidade += 4
        
        stop music fadeout 2.0
        
        hide perola_twerk_pro_anim_normal
        hide perola_twerk_pro_anim_rapida
        show perola_satisfeita at center
        
        prl "That was my heart and soul... all for you."
        prl "I hope you liked your surprise..."
    
    else:
        # Surpresas subsequentes são mais íntimas
        prl "This time my surprise is more... hands-on."
        prl "I want to give you pleasure like never before."
        
        "Pearl's surprise involves increasingly intimate activities."
        
        prl "I've been learning new techniques just for you..."
        prl "Let me show you what I can do now..."
        
        "The surprise becomes incredibly sensual and personal."
        
        prl "Do you like my surprise?"
        prl "I have so many more ideas for next time..."
        
        $ perola_nivel_intimidade += 3
    
    $ hora_do_dia += 3
    jump final_visita_perola

# ORIGINAL SEXUAL ACTIVITIES

# Pearl shows her tits
label ver_peitos_perola:
    $ perola_ultimo_ato_sexual = dia
    $ perola_vezes_peitos += 1
    
    if perola_vezes_peitos == 1:
        prl "You want to see my tits? I've been waiting for someone to ask..."
        prl "I've been so curious about my body lately..."
    else:
        prl "You love my tits, don't you? I love showing them to you..."
    
    # Hide clothed Pearl
    hide perola_provocante
    
    # Show tits animation
    show perola_peitos_anim at center
    
    if perola_vezes_peitos == 1:
        prl "How do they look? Are they... normal?"
        prl "I've never shown them to anyone before..."
        
        b "They're fucking perfect, Pearl."
        
        prl "Really? They make me feel so... womanly."
        prl "I love how you look at them..."
    else:
        prl "I love the way you stare at them..."
        prl "It makes me feel so sexy and powerful!"
        
        b "They're amazing, Pearl."
        
        prl "Touch them... I want to feel your hands on me..."
    
    # Show for a few seconds
    pause 3.0
    
    hide perola_peitos_anim
    show perola_satisfeita at center
    
    prl "That felt so good... being desired like that."
    if perola_vezes_peitos == 1:
        prl "I'm discovering so much about myself..."
        $ perola_nivel_intimidade += 1
    
    $ hora_do_dia += 1
    jump final_visita_perola

# Sexual twerking performance
label twerk_sexual_perola:
    $ perola_ultimo_ato_sexual = dia
    $ perola_vezes_twerk_sexual += 1
    
    prl "You want me to twerk for you? I've gotten so much better..."
    prl "And now I know exactly what it does to you..."
    
    # Start sexual twerk music
    play music audio.twerk_music fadein 1.0
    
    # Show sexual twerking animation
    scene quarto_perola
    show perola_twerk_sexual_anim at center
    
    if perola_vezes_twerk_sexual == 1:
        prl "This time I'm doing it to turn you on..."
        prl "I can see how hard you're getting!"
        
        b "Fuck, Pearl... you're driving me crazy."
        
        prl "That's exactly what I want!"
        prl "I love having this power over you!"
    else:
        prl "I've been practicing just for you..."
        prl "Watch how I move my ass for you!"
        
        b "You're getting too good at this."
        
        prl "I know exactly what you like now!"
        prl "Does this make you want to fuck me?"
    
    # Switch to faster rhythm
    hide perola_twerk_sexual_anim
    show perola_twerk_sexual_rapida at center
    
    prl "I'm getting so wet doing this for you..."
    prl "Your eyes on my ass make me so horny!"
    
    b "Keep going, you little slut."
    
    prl "Yes! Call me names! I love it!"
    prl "I'm your little twerking slut!"
    
    # Climax of performance
    hide perola_twerk_sexual_rapida
    show perola_excitada at center
    
    stop music fadeout 1.0
    
    prl "Did you like my show?"
    prl "I'm so turned on right now..."
    
    if perola_vezes_twerk_sexual == 1:
        $ perola_nivel_intimidade += 2
    else:
        $ perola_nivel_intimidade += 1
    
    $ hora_do_dia += 2
    jump final_visita_perola

# Pearl gives handjob
label punheta_perola:
    $ perola_ultimo_ato_sexual = dia
    $ perola_vezes_punheta += 1
    
    if perola_vezes_punheta == 1:
        prl "You want me to... touch you there?"
        prl "I've never done this before... will you teach me?"
    else:
        prl "I love making you feel good with my hands..."
        prl "I'm getting so good at this!"
    
    # Start sex scene
    scene quarto_perola
    play music audio.sexmusic_perola fadein 1.0
    show perola_punheta_anim at center
    
    if perola_vezes_punheta == 1:
        prl "It's so hard! And warm!"
        prl "Am I doing this right?"
        
        b "Just like that, Pearl. You're a natural."
        
        prl "This is so exciting! I love feeling your reaction!"
        prl "Your breathing changed... does it feel good?"
    else:
        prl "I remember exactly how you like it..."
        prl "Fast or slow today?"
        
        b "Start slow, then faster."
        
        prl "I love being in control of your pleasure..."
        prl "You're completely at my mercy!"
    
    # Switch to faster rhythm
    hide perola_punheta_anim
    show perola_punheta_rapida at center
    
    prl "You're getting close, aren't you?"
    prl "I can feel you throbbing in my hand!"
    
    b "I'm gonna cum, Pearl!"
    
    if perola_vezes_punheta == 1:
        prl "Cum for me! I want to see it!"
    else:
        prl "Yes! Cum all over me!"
    
    # Cum scene
    hide perola_punheta_rapida
    show perola_gozada_peitos at center
    
    play sound audio.gozada
    with hpunch
    
    b "Fuck yes!"
    
    with hpunch
    prl "So much! It's everywhere!"
    
    if perola_vezes_punheta == 1:
        prl "That was incredible! I made you feel that good?"
        $ perola_nivel_intimidade += 2
    else:
        prl "I love making you cum like that!"
        $ perola_nivel_intimidade += 1
    
    pause 2.0
    hide perola_gozada_peitos
    show perola_satisfeita at center
    
    stop music fadeout 1.0
    
    $ hora_do_dia += 2
    jump final_visita_perola

# Pearl gives blowjob (intimacy 9+)
label boquete_perola:
    $ perola_ultimo_ato_sexual = dia
    $ perola_vezes_boquete += 1
    
    if perola_vezes_boquete == 1:
        prl "You want me to... put it in my mouth?"
        prl "I've seen it in videos but... this is my first time."
    else:
        prl "I love the taste of your cock now..."
        prl "I crave it!"
    
    # Start blowjob scene
    scene quarto_perola
    play music audio.sexmusic_perola fadein 1.0
    show perola_boquete_anim at center
    
    if perola_vezes_boquete == 1:
        prl "Mmm... it tastes different than I expected..."
        prl "But I like it! Should I use my tongue?"
        
        b "Yes, just like that Pearl."
        
        prl "*muffled* This is so dirty... I love it!"
        prl "*slurp* Am I being a good girl?"
    else:
        prl "I've been dreaming about sucking your cock..."
        prl "*slurp* I'm getting so good at this!"
        
        b "You're becoming a real cock-sucker."
        
        prl "*muffled* Yes! I'm your little cocksucker!"
        prl "*glup* I love being dirty for you!"
    
    # Switch to faster rhythm
    hide perola_boquete_anim
    show perola_boquete_rapida at center
    
    prl "*slurp* *glup* Are you close?"
    prl "I want you to cum in my mouth!"
    
    b "I'm gonna fill your mouth!"
    
    prl "*muffled* Yes! Give it to me!"
    
    # Cum scene
    hide perola_boquete_rapida
    show perola_gozada_boca at center
    
    play sound audio.gozada
    with hpunch
    
    b "Swallow it all!"
    
    with hpunch
    prl "*gulp* So much! It's so thick!"
    
    if perola_vezes_boquete == 1:
        prl "*cough* That was... intense! I love the taste!"
        $ perola_nivel_intimidade += 3
    else:
        prl "Mmm... I swallowed every drop!"
        $ perola_nivel_intimidade += 1
    
    pause 2.0
    hide perola_gozada_boca
    show perola_satisfeita at center
    
    stop music fadeout 1.0
    
    $ hora_do_dia += 2
    jump final_visita_perola

# Fuck Pearl's pussy (intimacy 10+)
label foder_perola_vaginal:
    $ perola_ultimo_ato_sexual = dia
    $ perola_vezes_vaginal += 1
    
    if perola_vezes_vaginal == 1:
        prl "You want to... be inside me?"
        prl "I'm ready... I want to lose my virginity to you."
    else:
        prl "I need you inside me again..."
        prl "I'm addicted to your cock!"
    
    # Start vaginal scene
    scene quarto_perola
    play music audio.sexmusic_perola fadein 1.0
    play sound audio.perola_gemidos loop
    show perola_vaginal_anim at center
    
    if perola_vezes_vaginal == 1:
        prl "OH! It's so big! Go slow!"
        prl "I feel so full... is this what sex feels like?"
        
        b "You're so tight, Pearl."
        
        prl "It hurts a little but... it feels amazing!"
        prl "I'm not a virgin anymore!"
    else:
        prl "Yes! Fill me up with your cock!"
        prl "I love how you stretch me!"
        
        b "You're such a good little slut."
        
        prl "I'm your slut! Only yours!"
        prl "Fuck me harder!"
    
    # Switch to faster rhythm
    hide perola_vaginal_anim
    show perola_vaginal_rapida at center
    
    prl "HARDER! I want to feel everything!"
    prl "Make me scream!"
    
    b "Take it all, you little whore!"
    
    prl "YES! I'M YOUR WHORE! FUCK ME!"
    
    # Climax
    hide perola_vaginal_rapida
    show perola_gozada_vaginal at center
    
    stop sound
    play sound audio.gozada
    with hpunch
    
    b "I'm cumming inside you!"
    
    with hpunch
    prl "FILL ME UP! I WANT ALL YOUR CUM!"
    
    if perola_vezes_vaginal == 1:
        prl "I can feel it inside me! I'm a real woman now!"
        $ perola_nivel_intimidade += 4
    else:
        prl "So much cum! I love it!"
        $ perola_nivel_intimidade += 2
    
    pause 2.0
    hide perola_gozada_vaginal
    show perola_satisfeita at center
    
    stop music fadeout 1.0
    
    $ hora_do_dia += 3
    jump final_visita_perola

# Fuck Pearl's ass (intimacy 12+)
label foder_perola_anal:
    $ perola_ultimo_ato_sexual = dia
    $ perola_vezes_anal += 1
    
    if perola_vezes_anal == 1:
        prl "In my... ass? I've never tried that!"
        prl "Will it hurt? I want to try everything with you..."
    else:
        prl "I love when you fuck my ass..."
        prl "It makes me feel so dirty!"
    
    # Start anal scene
    scene quarto_perola
    play music audio.sexmusic_perola fadein 1.0
    play sound audio.perola_gemidos loop
    show perola_anal_anim at center
    
    if perola_vezes_anal == 1:
        prl "OH GOD! It's so intense!"
        prl "It hurts but... I don't want you to stop!"
        
        b "Relax, you're doing great."
        
        prl "I feel so full! So stretched!"
        prl "This is so dirty... I love it!"
    else:
        prl "YES! Destroy my ass!"
        prl "I'm your anal slut!"
        
        b "That's right, take it all."
        
        prl "Deeper! Harder! I can take it!"
        prl "Use my ass however you want!"
    
    # Switch to faster rhythm
    hide perola_anal_anim
    show perola_anal_rapida at center
    
    prl "I'M GONNA CUM FROM MY ASS!"
    prl "HOW IS THAT POSSIBLE?!"
    
    b "Because you're a natural anal slut!"
    
    prl "YES! I'M YOUR ANAL SLUT!"
    
    # Climax
    hide perola_anal_rapida
    show perola_gozada_anal at center
    
    stop sound
    play sound audio.gozada
    with hpunch
    
    b "Take my cum in your ass!"
    
    with hpunch
    prl "FILL MY ASS! I LOVE IT!"
    
    if perola_vezes_anal == 1:
        prl "That was incredible! I came from anal!"
        $ perola_nivel_intimidade += 5
    else:
        prl "I love being your anal whore!"
        $ perola_nivel_intimidade += 2
    
    pause 2.0
    hide perola_gozada_anal
    show perola_satisfeita at center
    
    stop music fadeout 1.0
    
    $ hora_do_dia += 3
    jump final_visita_perola# purrlfucks.rpy - Pearl Sexual Content (English) - COMPLETE VERSION

# Sexual animations for Pearl
image perola_peitos_anim:
    "images/perola_peitos_1.png"
    pause 0.5
    "images/perola_peitos_2.png"
    pause 0.5
    repeat

# Twerking sexual animations
image perola_twerk_sexual_anim:
    "images/perola_twerk_sexual_1.png"
    pause 0.3
    "images/perola_twerk_sexual_2.png"
    pause 0.3
    "images/perola_twerk_sexual_3.png"
    pause 0.3
    repeat

image perola_twerk_sexual_rapida:
    "images/perola_twerk_sexual_1.png"
    pause 0.15
    "images/perola_twerk_sexual_2.png"
    pause 0.15
    "images/perola_twerk_sexual_3.png"
    pause 0.15
    repeat

image perola_punheta_anim:
    "images/perola_punheta_1.png"
    pause 0.4
    "images/perola_punheta_2.png"
    pause 0.4
    "images/perola_punheta_3.png"
    pause 0.4
    repeat

image perola_punheta_rapida:
    "images/perola_punheta_1.png"
    pause 0.2
    "images/perola_punheta_2.png"
    pause 0.2
    "images/perola_punheta_3.png"
    pause 0.2
    repeat