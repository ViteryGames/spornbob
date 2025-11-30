# purrlfucks.rpy - Purrl Sexual Content - RENAMED CONTENT

# Sexual animations
image perola_peitos_anim:
    "images/perola_peitos_1.png"
    pause 0.5
    "images/perola_peitos_2.png"
    pause 0.5
    repeat

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

image perola_tease_anim:
    "images/perola_tease_1.png"
    pause 0.35
    "images/perola_tease_2.png"
    pause 0.35
    "images/perola_tease_3.png"
    pause 0.35
    repeat

image perola_tease_rapida:
    "images/perola_tease_1.png"
    pause 0.15
    "images/perola_tease_2.png"
    pause 0.15
    "images/perola_tease_3.png"
    pause 0.15
    repeat

image perola_vaginal_anim:
    zoom 0.9
    "images/perola_vagina_1.png"
    pause 0.12
    "images/perola_vagina_2.png"
    pause 0.12
    "images/perola_vagina_3.png"
    pause 0.12
    "images/perola_vagina_4.png"
    pause 0.12
    "images/perola_vagina_5.png"
    pause 0.12
    "images/perola_vagina_6.png"
    pause 0.12
    repeat

image perola_vaginal_rapida:
    zoom 0.9
    "images/perola_vagina_1.png"
    pause 0.06
    "images/perola_vagina_2.png"
    pause 0.06
    "images/perola_vagina_3.png"
    pause 0.06
    "images/perola_vagina_4.png"
    pause 0.06
    "images/perola_vagina_5.png"
    pause 0.06
    "images/perola_vagina_6.png"
    pause 0.06
    repeat

image perola_anal_anim:
    "images/perola_anal_1.png"
    pause 0.2
    "images/perola_anal_2.png"
    pause 0.2
    "images/perola_anal_3.png"
    pause 0.2
    "images/perola_anal_4.png"
    pause 0.2
    repeat

image perola_anal_rapida:
    "images/perola_anal_1.png"
    pause 0.08
    "images/perola_anal_2.png"
    pause 0.08
    "images/perola_anal_3.png"
    pause 0.08
    "images/perola_anal_4.png"
    pause 0.08
    repeat

# Cum images
image perola_gozada_peitos = "images/perola_gozada_peitos.png"
image perola_gozada_tease = "images/perola_gozada_tease.png"
image perola_gozada_vaginal = "images/perola_gozada_vaginal.png"
image perola_gozada_anal = "images/perola_gozada_anal.png"

# Sounds
define audio.perola_gemidos = "audio/perola_moans.mp3"
define audio.sexmusic_perola = "audio/sexmusic_teen.mp3"
define audio.gozada = "audio/cum_sound.mp3"
define audio.pai_chegando = "footsteps.mp3"

# Variables for sexual progression
default perola_vezes_peitos = 0
default perola_vezes_twerk_sexual = 0
default perola_vezes_punheta = 0
default perola_vezes_tease = 0
default perola_vezes_vaginal = 0
default perola_vezes_anal = 0
default perola_ultimo_ato_sexual = -1

# Function to check if can do sexual act today
init python:
    def pode_fazer_ato_sexual_perola():
        global perola_ultimo_ato_sexual, dia
        return perola_ultimo_ato_sexual != dia

# LEVEL 10 - Show tits
label ver_peitos_perola_full:
    if not pode_fazer_ato_sexual_perola():
        prl "We already did stuff today. Come back tomorrow."
        jump menu_principal_perola
    
    $ perola_ultimo_ato_sexual = dia
    $ perola_vezes_peitos += 1
    
    scene quarto_perola
    
    if perola_vezes_peitos == 1:
        prl "You wanna see my pearls? Finally someone asks!"
        prl "Been dying to show these to a real man."
    else:
        prl "You love looking at these, don't you?"
    
    hide perola_provocante
    show perola_peitos_1
    
    if perola_vezes_peitos == 1:
        prl "So? Good enough for you?"

        b "Fuck! Those are HUGE!!"
        prl "Damn right they are!"

        window hide
        $ renpy.pause(hard=False)

    else:
        prl "Stare all you want!"

        window hide
        $ renpy.pause(hard=False)

        
        prl "Enjoying the view?"
    
    pause 3.0
    
    hide perola_peitos_1
    show perola_peitos_2 :
      zoom 0.8 xpos 300 ypos -88
    
    prl "Being wanted like that feels good."
    
    $ hora_do_dia += 1
    
    # MR. KROTCH ARRIVES HOME!
    play sound audio.pai_chegando
    prl "SHIT! I hear footsteps!"
    prl "It's my dad! GET OUT!"
    
    b "Damn!"
    
    prl "Use the window! NOW!"
    
    "You jump out the window and run away!"
    
    $ mapa_disponivel = True
    call screen bobCasas

# LEVEL 15 - Sexual twerking
label twerk_sexual_perola_full:
    if not pode_fazer_ato_sexual_perola():
        prl "Already did my show today. Come back tomorrow."
        jump menu_principal_perola
    
    $ perola_ultimo_ato_sexual = dia
    $ perola_vezes_twerk_sexual += 1
    
    prl "You want me to shake my rear seductively? I'm so good at this now..."
    
    play music audio.twerk_music fadein 1.0
    
    scene quarto_perola
    show perola_twerk_sexual_anim at center
    
    if perola_vezes_twerk_sexual == 1:
        prl "This time I'm doing it to really get your attention!"
        prl "Look at you already!"
        b "Keep moving."
        prl "That's what I wanted to hear!"
    else:
        prl "Watch this work!"
        b "You're getting too good at this."
        prl "I know what gets your attention!"
    
    hide perola_twerk_sexual_anim
    show perola_twerk_sexual_rapida at center
    
    prl "I'm getting so excited!"
    prl "Your eyes on me make me feel amazing!"
    
    b "Keep going."
    
    prl "Yes! I'm your dancer!"
    
    stop music fadeout 1.0
    hide perola_twerk_sexual_rapida
    show perola_excitada at center
    
    prl "I'm so turned on right now..."
    
    $ hora_do_dia += 2
    
    # DAD ARRIVES!
    play sound audio.pai_chegando
    prl "Oh no! Dad's home!"
    prl "You need to leave NOW!"
    
    "You quickly escape through the window!"
    
    $ mapa_disponivel = True
    call screen bobCasas

# LEVEL 20 - Handjob
label punheta_perola_full:
    if not pode_fazer_ato_sexual_perola():
        prl "I already helped you today. Greedy."
        jump menu_principal_perola
    
    $ perola_ultimo_ato_sexual = dia
    $ perola_vezes_punheta += 1
    
    scene quarto_perola
    
    if perola_vezes_punheta == 1:
        prl "You want me to help you with my hands?"
        prl "Never done this before..."
    else:
        prl "I love doing this for you!"
    
    play music "sexmusic.wav"
    show perola_punheta_anim at center
    
    if perola_vezes_punheta == 1:
        prl "Wow, it's so firm!"
        prl "Am I doing this right?"
        window hide
        $ renpy.pause(hard=False)
        b "Oh yeah!Just like that baby girl"
        prl "I can feel it throbbing!"
    else:
        prl "I know exactly how you like it!"
        b "Stroke slow, then fast."
        prl "I control the pace!"
        window hide
        $ renpy.pause(hard=False)
    
    hide perola_punheta_anim
    show perola_punheta_rapida at center
    
    prl "You're close!"
    b "Almost there!"

    window hide
    $ renpy.pause(hard=False)

    prl "Let go!"

    menu:
        "Bust a nut":
            pass
    hide perola_punheta_rapida
    show perola_gozada_pupunha at center
    
    play audio "porra.mp3"
    with hpunch
    
    b "Yeah!" with hpunch
    
    play audio "porra.mp3"
    with hpunch

    window hide
    $ renpy.pause(hard=False)

    prl "So much!"

    hide perola_gozada_pupunha
    show perola_gozada at center
    
    stop music fadeout 1.0
    
    $ hora_do_dia += 2
    
    # DAD ARRIVES!
    prl "I need to clean up and you need to go!"
    prl "Dad will be home any minute!"
    
    "You quickly get dressed and leave!"
    
    $ mapa_disponivel = True
    call screen bobCasas

# LEVEL 25 - Rub and tease (renamed from the previous content)
label boquete_perola_full:
    if not pode_fazer_ato_sexual_perola():
        prl "I already teased you enough today. Tomorrow."
        jump menu_principal_perola
    
    $ perola_ultimo_ato_sexual = dia
    $ perola_vezes_tease += 1
    
    scene quarto_perola
    
    if perola_vezes_tease == 1:
        prl "I'm so fucking wet, and it's not only because we are underwater"
        prl "It's because I can't stop thinking about your fat smelly cock!"
    else:
        prl "I love teasing you!"
    
    play music audio.sexmusic_perola fadein 1.0
    show perola_tease_anim at center
    
    if perola_vezes_tease == 1:
        prl "Mmm... different than expected..."
        prl "Go deeper!"
        b "Yeah, just like that."
    else:
        prl "Fuck it went deep"
        b "You're really something."
        prl "Let me suck those fingers"
    
    hide perola_tease_anim
    show perola_tease_rapida at center
    
    prl "You close?"
    b "Almost there!"
    prl "Let it happen!"
    
    hide perola_tease_rapida
    show perola_gozada_tease at center
    
    play sound audio.gozada
    with hpunch
    
    b "Yes!"
    prl "So intense!"
    
    pause 2.0
    hide perola_gozada_tease
    show perola_satisfeita at center
    
    stop music fadeout 1.0
    
    $ hora_do_dia += 2
    
    # DAD ARRIVES!
    play sound audio.pai_chegando
    prl "*cough* Oh no! Dad's car!"
    prl "You gotta go! NOW!"
    
    "You grab your clothes and jump out the window!"
    
    $ mapa_disponivel = True
    call screen bobCasas

# LEVEL 30 - Anal
label foder_perola_anal_full:
    if not pode_fazer_ato_sexual_perola():
        prl "I'm still sore. Give me a day."
        jump menu_principal_perola
    
    $ perola_ultimo_ato_sexual = dia
    $ perola_vezes_anal += 1
    
    scene quarto_perola
    
    if perola_vezes_anal == 1:
        prl "You want to try that? Never done it before!"
        prl "Be gentle... at first."
    else:
        prl "I love this feeling!"
    
    play music "sexmusic.wav"
    play musica2 "nocuzin.wav"

    show perola_anal_anim at center
    
    if perola_vezes_anal == 1:
        prl "WOW! It's intense!"
        prl "It hurts but... don't stop!"
        b "Fuck! It's too tight"
        b "Tell your ass that this dick is getting in with or without permission!!!"
        prl "Ah! I can feel it stretching all the way down"
        
        window hide
        $ renpy.pause(hard=False)

        b "Shake it faster bitch!"

    else:
        prl "YES! Just like that!"
        b "Your ass is a lot easier to fuck now huh"


        prl "Thanks to your fat cock I am now a loose whore!"

        window hide
        $ renpy.pause(hard=False)

        prl "Deeper! Harder!"
        
        b "Full speed now whore"
    
    stop musica2
    play musica2 "nocuzinf.mp3"
    hide perola_anal_anim
    show perola_anal_rapida at center
    window hide
    $ renpy.pause(hard=False)

    prl "I'M GONNA LOSE IT!"
    b "Ah your fucking my brains out I can't even spahshdjkahdjakshkjhdajshjkda!"
    prl "YES! YOUR GIRL!"

    menu:
        "Cum inside her tight asshole":
            pass
    hide perola_anal_rapida
    show perola_gozada_anal at center
    stop music
    stop musica2

    stop sound
    play audio "porra.mp3"
    with hpunch

        
    b "Take it all inside bitch!"

    play audio "porra.mp3"
    with hpunch

    window hide
    $ renpy.pause(hard=False)

    prl "FILL MY FUCKING ASS!!!!"
    play audio "porra.mp3"
    with hpunch
    
    pause 2.0
    hide perola_gozada_anal

    show perola_peitos_2 :
      zoom 0.8 xpos 300 ypos -88
    
    stop music fadeout 1.0
    
    $ hora_do_dia += 3
    
    # DAD ARRIVES!
    play sound audio.pai_chegando
    prl "Holy hell! Dad's home!"
    prl "I'm still leaking! GET OUT!"
    
    b "I'm going!"
    
    "You barely manage to get dressed before jumping out the window!"
    
    $ mapa_disponivel = True
    call screen bobCasas

# LEVEL 35 - Vaginal
label foder_perola_vaginal_full:
    if not pode_fazer_ato_sexual_perola():
        prl "I need rest. Tomorrow."
        jump menu_principal_perola
    
    $ perola_ultimo_ato_sexual = dia
    $ perola_vezes_vaginal += 1
    

    scene quarto_perola
    
    if perola_vezes_vaginal == 1:
        prl "You wanna do it the normal way?"
        prl "This is my first time! Go easy on my premium whale pussy"
        prl "SO fucking hyped right now!I'm almost squirting already"
    else:
        prl "I need you inside me big boy!"
      
    play music "sexmusic.wav"
    play musica2 "nocuzin.wav"

    show perola_vaginal_anim at center
    
    if perola_vezes_vaginal == 1:
        prl "AH! FUCK IT'S EVERYWHERE"
        prl "This is what it feels like?"
        b "Damn, it's tighter than your ass!"
        b "But your fishy pussy is so delicious I never wanna pull out, holy shit!"
        
        window hide
        $ renpy.pause(hard=False)

        prl"Fuck me Daddy!"
    else:
        prl "Ah! Fuck me all day long"
        b "I love taking your innocence away, you little slut."
        prl "YES I AM YOUR SLUT!"
         
        window hide
        $ renpy.pause(hard=False) 

        prl "Harder Daddy! Wreck my holes!"
    
    stop musica2
    play musica2 "botada.mp3"
    hide perola_vaginal_anim
    show perola_vaginal_rapida at center
    
    prl "HARDER! DESTROY ME!"

    window hide
    $ renpy.pause(hard=False) 

    b "Uhhhh Fuuuuuuuuck!"
    prl "YES! I'M YOURS!"
    
    menu:
        "Cum deep inside her pussy":
            pass
    
    stop music
    stop musica2

    hide perola_vaginal_rapida

    show perola_gozada_vaginal at center:
     zoom 0.9

    play audio "porra.mp3"
    with hpunch
    window hide
    $ renpy.pause(hard=False) 

    stop sound
    play audio "porra.mp3"
    with hpunch
    
    b "I can feel my balls going away!"
    prl "INSIDE ME!"
    
    play audio "porra.mp3"
    with hpunch

    hide perola_gozada_vaginal
    show perola_peitos_2 :
      zoom 0.8 xpos 300 ypos -88
    
    stop music fadeout 1.0
    
    $ hora_do_dia += 3
    
    # DAD ARRIVES - DRAMATIC!
    play sound audio.pai_chegando
    
    prl "OH NO! DAD'S HOME!"
    prl "I'M FULL OF YOUR STUFF!"
    prl "GET OUT BEFORE HE FINDS YOU!"
    
    b "Going going going!"
    
    "You grab your clothes and dive out the window!"
    "You get dressed outside while running away!"
    
    $ mapa_disponivel = True
    call screen bobCasas