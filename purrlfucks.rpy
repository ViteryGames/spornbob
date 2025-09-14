# purrlfucks.rpy - Purrl Sexual Content - FINAL WITH MAP RETURN

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

# Sounds
define audio.perola_gemidos = "audio/perola_moans.mp3"
define audio.sexmusic_perola = "audio/sexmusic_teen.mp3"
define audio.gozada = "audio/cum_sound.mp3"
define audio.pai_chegando = "footsteps.mp3"

# Variables for sexual progression
default perola_vezes_peitos = 0
default perola_vezes_twerk_sexual = 0
default perola_vezes_punheta = 0
default perola_vezes_boquete = 0
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
        prl "We already did shit today. Come back tomorrow."
        jump menu_principal_perola
    
    $ perola_ultimo_ato_sexual = dia
    $ perola_vezes_peitos += 1
    
    scene quarto_perola
    
    if perola_vezes_peitos == 1:
        prl "You wanna see my tits? Finally someone asks!"
        prl "Been dying to show these to a real man."
    else:
        prl "You love these tits, don't you?"
    
    hide perola_provocante
    show perola_peitos_anim at center
    
    if perola_vezes_peitos == 1:
        prl "So? Good enough for you?"
        b "They're fucking perfect."
        prl "Damn right they are!"
    else:
        prl "Stare all you want, pervert!"
        b "They're mine to look at."
        prl "Touch them... grab them hard!"
    
    pause 3.0
    
    hide perola_peitos_anim
    show perola_satisfeita at center
    
    prl "Fuck... being wanted like that feels good."
    
    $ hora_do_dia += 1
    
    # MR. KROTCH ARRIVES HOME!
    play sound audio.pai_chegando
    prl "SHIT! I hear footsteps!"
    prl "It's my dad! GET THE FUCK OUT!"
    
    b "Fuck!"
    
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
    
    prl "You want me to shake my ass sexually? I'm so fucking good at this now..."
    
    play music audio.twerk_music fadein 1.0
    
    scene quarto_perola
    show perola_twerk_sexual_anim at center
    
    if perola_vezes_twerk_sexual == 1:
        prl "This time I'm doing it to make you hard as fuck!"
        prl "Look at that bulge already!"
        b "Keep moving that ass."
        prl "That's what I wanted to hear!"
    else:
        prl "Watch this ass work!"
        b "You're getting too good at this."
        prl "I know what makes your dick twitch!"
    
    hide perola_twerk_sexual_anim
    show perola_twerk_sexual_rapida at center
    
    prl "My pussy's getting so wet!"
    prl "Your eyes on my ass make me so horny!"
    
    b "Keep going, slut."
    
    prl "Yes! I'm your twerk slut!"
    
    stop music fadeout 1.0
    hide perola_twerk_sexual_rapida
    show perola_excitada at center
    
    prl "I'm so fucking turned on right now..."
    
    $ hora_do_dia += 2
    
    # DAD ARRIVES!
    play sound audio.pai_chegando
    prl "FUCK! Dad's home!"
    prl "You need to leave NOW!"
    
    "You quickly escape through the window!"
    
    $ mapa_disponivel = True
    call screen bobCasas

# LEVEL 20 - Handjob
label punheta_perola_full:
    if not pode_fazer_ato_sexual_perola():
        prl "I already jacked you off today. Greedy bastard."
        jump menu_principal_perola
    
    $ perola_ultimo_ato_sexual = dia
    $ perola_vezes_punheta += 1
    
    scene quarto_perola
    
    if perola_vezes_punheta == 1:
        prl "You want me to jack you off?"
        prl "Never touched a dick before..."
    else:
        prl "I love stroking your cock!"
    
    play music audio.sexmusic_perola fadein 1.0
    show perola_punheta_anim at center
    
    if perola_vezes_punheta == 1:
        prl "Fuck, it's so hard!"
        prl "Am I doing this right?"
        b "Just like that."
        prl "I can feel it throbbing!"
    else:
        prl "I know exactly how you like it!"
        b "Start slow, then fast."
        prl "I control when you cum!"
    
    hide perola_punheta_anim
    show perola_punheta_rapida at center
    
    prl "You're gonna cum!"
    b "Gonna blow!"
    prl "Cum all over me!"
    
    hide perola_punheta_rapida
    show perola_gozada_peitos at center
    
    play sound audio.gozada
    with hpunch
    
    b "Fuck yeah!"
    prl "So much cum!"
    
    pause 2.0
    hide perola_gozada_peitos
    show perola_satisfeita at center
    
    stop music fadeout 1.0
    
    $ hora_do_dia += 2
    
    # DAD ARRIVES!
    prl "Shit, I need to clean up and you need to go!"
    prl "Dad will be home any minute!"
    
    "You quickly get dressed and leave!"
    
    $ mapa_disponivel = True
    call screen bobCasas

# LEVEL 25 - Blowjob
label boquete_perola_full:
    if not pode_fazer_ato_sexual_perola():
        prl "My jaw's still sore from earlier. Tomorrow."
        jump menu_principal_perola
    
    $ perola_ultimo_ato_sexual = dia
    $ perola_vezes_boquete += 1
    
    scene quarto_perola
    
    if perola_vezes_boquete == 1:
        prl "You want me to suck your dick?"
        prl "First time for everything..."
    else:
        prl "I love the taste of your cock!"
    
    play music audio.sexmusic_perola fadein 1.0
    show perola_boquete_anim at center
    
    if perola_vezes_boquete == 1:
        prl "Mmm... different than expected..."
        prl "*slurp* Am I doing good?"
        b "Yeah, just like that."
    else:
        prl "*slurp* I'm so good at this now!"
        b "You're a real cocksucker."
        prl "*muffled* Your cocksucker!"
    
    hide perola_boquete_anim
    show perola_boquete_rapida at center
    
    prl "*slurp* *glup* You close?"
    b "Gonna fill your mouth!"
    prl "*muffled* Give it to me!"
    
    hide perola_boquete_rapida
    show perola_gozada_boca at center
    
    play sound audio.gozada
    with hpunch
    
    b "Swallow it all!"
    prl "*gulp* So thick!"
    
    pause 2.0
    hide perola_gozada_boca
    show perola_satisfeita at center
    
    stop music fadeout 1.0
    
    $ hora_do_dia += 2
    
    # DAD ARRIVES!
    play sound audio.pai_chegando
    prl "*cough* FUCK! Dad's car!"
    prl "You gotta go! NOW!"
    
    "You grab your clothes and jump out the window!"
    
    $ mapa_disponivel = True
    call screen bobCasas

# LEVEL 30 - Anal
label foder_perola_anal_full:
    if not pode_fazer_ato_sexual_perola():
        prl "My ass is still sore. Give me a day."
        jump menu_principal_perola
    
    $ perola_ultimo_ato_sexual = dia
    $ perola_vezes_anal += 1
    
    scene quarto_perola
    
    if perola_vezes_anal == 1:
        prl "In my ass? Fuck... never done that!"
        prl "Be gentle... at first."
    else:
        prl "I love when you fuck my ass!"
    
    play music audio.sexmusic_perola fadein 1.0
    play sound audio.perola_gemidos loop
    show perola_anal_anim at center
    
    if perola_vezes_anal == 1:
        prl "FUCK! It's huge!"
        prl "Hurts but... don't stop!"
        b "Take it all."
        prl "So fucking full!"
    else:
        prl "YES! Wreck my ass!"
        b "That's right, take it."
        prl "Deeper! Harder!"
    
    hide perola_anal_anim
    show perola_anal_rapida at center
    
    prl "I'M GONNA CUM FROM MY ASS!"
    b "Because you're an anal slut!"
    prl "YES! YOUR ANAL SLUT!"
    
    hide perola_anal_rapida
    show perola_gozada_anal at center
    
    stop sound
    play sound audio.gozada
    with hpunch
    
    b "Take my cum!"
    prl "FILL MY ASS!"
    
    pause 2.0
    hide perola_gozada_anal
    show perola_satisfeita at center
    
    stop music fadeout 1.0
    
    $ hora_do_dia += 3
    
    # DAD ARRIVES!
    play sound audio.pai_chegando
    prl "Holy shit! Dad's home!"
    prl "My ass is still leaking cum! GET OUT!"
    
    b "Fuck, I'm going!"
    
    "You barely manage to get dressed before jumping out the window!"
    
    $ mapa_disponivel = True
    call screen bobCasas

# LEVEL 35 - Vaginal
label foder_perola_vaginal_full:
    if not pode_fazer_ato_sexual_perola():
        prl "My pussy needs rest. Tomorrow."
        jump menu_principal_perola
    
    $ perola_ultimo_ato_sexual = dia
    $ perola_vezes_vaginal += 1
    
    scene quarto_perola
    
    if perola_vezes_vaginal == 1:
        prl "You wanna fuck my pussy?"
        prl "Pop my fucking cherry!"
    else:
        prl "I need your dick inside me!"
    
    play music audio.sexmusic_perola fadein 1.0
    play sound audio.perola_gemidos loop
    show perola_vaginal_anim at center
    
    if perola_vezes_vaginal == 1:
        prl "SHIT! So big!"
        prl "This is what fucking feels like?"
        b "You're tight as fuck."
        prl "Not a virgin anymore!"
    else:
        prl "Fill my pussy!"
        b "Take it, slut."
        prl "Your slut! Fuck me harder!"
    
    hide perola_vaginal_anim
    show perola_vaginal_rapida at center
    
    prl "HARDER! DESTROY THIS PUSSY!"
    b "Take it all, whore!"
    prl "YES! I'M YOUR WHORE!"
    
    hide perola_vaginal_rapida
    show perola_gozada_vaginal at center
    
    stop sound
    play sound audio.gozada
    with hpunch
    
    b "Gonna fill you up!"
    prl "CUM IN ME!"
    
    pause 2.0
    hide perola_gozada_vaginal
    show perola_satisfeita at center
    
    stop music fadeout 1.0
    
    $ hora_do_dia += 3
    
    # DAD ARRIVES - DRAMATIC!
    play sound audio.pai_chegando
    
    prl "OH FUCK! DAD'S HOME!"
    prl "I'M FULL OF YOUR CUM!"
    prl "GET THE FUCK OUT BEFORE HE FINDS YOU!"
    
    b "Shit shit shit!"
    
    "You grab your clothes and dive out the window naked!"
    "You get dressed outside while running away!"
    
    $ mapa_disponivel = True
    call screen bobCasas