# comcumbina_random.rpy - Complete random prostitute system
# Completely replaces the original comcumbina.rpy

# List of available prostitutes (Sally + Kate + one commented for future)
default prostitutas_disponiveis = ["sally", "kate"] # , "crystal"
default prostituta_atual = ""

# Variable to control if it's the first time (global for all prostitutes)
default primeira_vez_puta_random = True

# Function to choose random prostitute
init python:
    import random
    def escolher_prostituta_aleatoria():
        global prostituta_atual
        prostituta_atual = random.choice(prostitutas_disponiveis)
        return prostituta_atual

# Image definitions for Sally (keeps originals)
image puta sally:
    "images/puta sally.png"
    zoom 0.75
    xalign 0.8
    yalign 0.9

# Animation definitions for Sally (keeps originals)
image keket_sally_anim:
    "keket sfull 1"
    pause 0.4
    "keket sfull 2"
    pause 0.4
    "keket sfull 3"
    pause 0.4
    repeat

image keket_sally_anim_rapida:
    "keket sfull 1"
    pause 0.2
    "keket sfull 2"
    pause 0.2
    "keket sfull 3"
    pause 0.2
    repeat

image vagina_sally_anim:
    "vagina sally 1"
    pause 0.4
    "vagina sally 2"
    pause 0.4
    "vagina sally 3"
    pause 0.4
    repeat

image vagina_sally_anim_rapida:
    "vagina sally 1"
    pause 0.2
    "vagina sally 2"
    pause 0.2
    "vagina sally 3"
    pause 0.2
    repeat

image cuzin_sally_anim:
    "cuzin sally 1"
    pause 0.4
    "cuzin sally 2"
    pause 0.4
    "cuzin sally 3"
    pause 0.4
    repeat

image cuzin_sally_anim_rapida:
    "cuzin sally 1"
    pause 0.2
    "cuzin sally 2"
    pause 0.2
    "cuzin sally 3"
    pause 0.2
    repeat

# Cum animations for Sally
image gozada_boquete_sally_anim:
    "gozada boquete 1"
    pause 0.3
    "gozada boquete 2"
    pause 0.3
    repeat

image gozada_vagina_sally_anim:
    "gozada vagina 1"
    pause 0.3
    "gozada vagina 2"
    pause 0.3
    repeat

image gozada_anal_sally_anim:
    "gozada cu 1"
    pause 0.3
    "gozada cu 2"
    pause 0.3
    repeat

image sally_gozada_boquete = "images/sally_gozada_boquete.png"
image sally_gozada_vagina = "images/sally gozada vagina.png" 
image sally_gozada_anal = "images/sally_gozada_anal.png"

# Image definitions for Kate (new prostitute)
image puta kate:
    "images/kate.png"
    zoom 0.75
    xalign 0.8
    yalign 0.9

image keket_kate_anim:
    "keket kate 1"
    pause 0.4
    "keket kate 2"
    pause 0.4
    "keket kate 3"
    pause 0.4
    repeat

image keket_kate_anim_rapida:
    "keket kate 1"
    pause 0.2
    "keket kate 2"
    pause 0.2
    "keket kate 3"
    pause 0.2
    repeat

image vagina_kate_anim:
    "vagina kate 1"
    pause 0.4
    "vagina kate 2"
    pause 0.4
    "vagina kate 3"
    pause 0.4
    repeat

image vagina_kate_anim_rapida:
    "vagina kate 1"
    pause 0.2
    "vagina kate 2"
    pause 0.2
    "vagina kate 3"
    pause 0.2
    repeat

image cuzin_kate_anim:
    "cuzin kate 1"
    pause 0.4
    "cuzin kate 2"
    pause 0.4
    "cuzin kate 3"
    pause 0.4
    repeat

image cuzin_kate_anim_rapida:
    "cuzin kate 1"
    pause 0.2
    "cuzin kate 2"
    pause 0.2
    "cuzin kate 3"
    pause 0.2
    repeat

# Cum animations for Kate
image gozada_boquete_kate_anim:
    "gozada boquete kate 1"
    pause 0.3
    "gozada boquete kate 2"
    pause 0.3
    repeat

image gozada_vagina_kate_anim:
    "gozada vagina kate 1"
    pause 0.3
    "gozada vagina kate 2"
    pause 0.3
    repeat

image gozada_anal_kate_anim:
    "gozada cu kate"
    pause 0.3
    "gozada cu kate"
    pause 0.3
    repeat

image kate_gozada_boquete = "images/kate_gozada_boquete.png"
image kate_gozada_vagina = "images/kate gozada vagina.png" 
image kate_gozada_anal = "images/kate_gozada_anal.png"

# Commented definitions for Crystal (future prostitute)
# image puta crystal:
#     "images/puta crystal.png"
#     zoom 0.75
#     xalign 0.8
#     yalign 0.9

# image keket_crystal_anim:
#     "keket crystal 1"
#     pause 0.4
#     "keket crystal 2"
#     pause 0.4
#     "keket crystal 3"
#     pause 0.4
#     repeat

# image keket_crystal_anim_rapida:
#     "keket crystal 1"
#     pause 0.2
#     "keket crystal 2"
#     pause 0.2
#     "keket crystal 3"
#     pause 0.2
#     repeat

# image vagina_crystal_anim:
#     "vagina crystal 1"
#     pause 0.4
#     "vagina crystal 2"
#     pause 0.4
#     "vagina crystal 3"
#     pause 0.4
#     repeat

# image vagina_crystal_anim_rapida:
#     "vagina crystal 1"
#     pause 0.2
#     "vagina crystal 2"
#     pause 0.2
#     "vagina crystal 3"
#     pause 0.2
#     repeat

# image cuzin_crystal_anim:
#     "cuzin crystal 1"
#     pause 0.4
#     "cuzin crystal 2"
#     pause 0.4
#     "cuzin crystal 3"
#     pause 0.4
#     repeat

# image cuzin_crystal_anim_rapida:
#     "cuzin crystal 1"
#     pause 0.2
#     "cuzin crystal 2"
#     pause 0.2
#     "cuzin crystal 3"
#     pause 0.2
#     repeat

# # Cum animations for Crystal
# image gozada_boquete_crystal_anim:
#     "gozada boquete crystal 1"
#     pause 0.3
#     "gozada boquete crystal 2"
#     pause 0.3
#     repeat

# image gozada_vagina_crystal_anim:
#     "gozada vagina crystal 1"
#     pause 0.3
#     "gozada vagina crystal 2"
#     pause 0.3
#     repeat

# image gozada_anal_crystal_anim:
#     "gozada cu crystal 1"
#     pause 0.3
#     "gozada cu crystal 2"
#     pause 0.3
#     repeat

# image crystal_gozada_boquete = "images/crystal_gozada_boquete.png"
# image crystal_gozada_vagina = "images/crystal gozada vagina.png" 
# image crystal_gozada_anal = "images/crystal_gozada_anal.png"

# Function to get prostitute name based on current one
init python:
    def get_prostituta_nome():
        if prostituta_atual == "sally":
            return "Whore"
        elif prostituta_atual == "kate":
            return "Kate"
        # elif prostituta_atual == "crystal":
        #     return "Crystal"
        else:
            return "Whore"

# Main label - REPLACES the original comcumbinas
label comcumbinas:
    # Choose random prostitute automatically
    $ escolher_prostituta_aleatoria()
    
    if not hasattr(store, "visitou_puta_dia_{}".format(saida)):
        $ setattr(store, "visitou_puta_dia_{}".format(saida), False)
    
    $ visitou_hoje = getattr(store, "visitou_puta_dia_{}".format(saida))
    
    if visitou_hoje:
        "There's nobody outside."
        jump quanaite
    else:
        scene quartobob noite

        if primeira_vez_puta_random:
            # Show the chosen prostitute
            if prostituta_atual == "sally":
                show puta sally:
                    xalign 1.2
                    yalign 0.5
                show puta sally:
                    linear 1.5 xalign 0.9
            elif prostituta_atual == "kate":
                show puta kate:
                    xalign 1.2
                    yalign 0.5
                show puta kate:
                    linear 1.5 xalign 0.9
            # elif prostituta_atual == "crystal":
            #     show puta crystal:
            #         xalign 1.2
            #         yalign 0.5
            #     show puta crystal:
            #         linear 1.5 xalign 0.9
            
            $ primeira_vez_puta_random = False
        else:
            # Show directly in center
            if prostituta_atual == "sally":
                show puta sally at center
            elif prostituta_atual == "kate":
                show puta kate at center
            # elif prostituta_atual == "crystal":
            #     show puta crystal at center

        $ nome_prostituta = get_prostituta_nome()
        "[nome_prostituta]" "I'm a whore"
        jump sou_puta

label sou_puta:
    $ nome_prostituta = get_prostituta_nome()
    
    menu:
        "Blowjob $15":
            if money >= 15:
                $ money -= 15
                jump boquete_scene
            else:
                "You don't have enough cash sugar. You need $15."
                jump sou_puta
                
        "Pussy $30":
            if money >= 30 and 14 in inventario:
                $ money -= 30
                $ inventario.remove(14)
                jump vagina_scene
            elif money < 30:
                "You don't have enough money to eat my pussy. You need $30 you broke ass loser."
                jump sou_puta
            else:
                "You need to have a condom for this option. Buy one at the store first."
                jump sou_puta
                
        "Ass $60":
            if money >= 60 and 14 in inventario:
                $ money -= 60
                $ inventario.remove(14)
                jump cuzin_scene
            elif money < 60:
                "You don't have enough to eat my ass."
                jump sou_puta
            else:
                "You need to have a condom for this option. Buy one at the store first."
                jump sou_puta
        
        "Talk (Free)":
            jump conversar_scene

# BLOWJOB SCENE
label boquete_scene:
    scene cama bob noite
    # Hide all prostitutes
    hide puta sally
    hide puta kate
    # hide puta crystal
    
    stop music
    stop sound
    
    play music "sexmusic.wav" fadein 1.0
    
    # Show animation based on current prostitute
    if prostituta_atual == "sally":
        show keket_sally_anim
    elif prostituta_atual == "kate":
        show keket_kate_anim
    # elif prostituta_atual == "crystal":
    #     show keket_crystal_anim
    
    $ nome_prostituta = get_prostituta_nome()
    
    "[nome_prostituta]" "I'm gonna suck you real good now, you bastard"
    "[nome_prostituta]" "Hmm, never sucked a sponge before... you have a unique taste!"
    b "Shut up and suck already, damn! I didn't pay to listen to bullshit."
    "[nome_prostituta]" "Fuck, such aggression!"
    b "Don't compare me to that TV shit. Suck it before I lose my patience!"
    
    # Hide slow animation and show fast one
    if prostituta_atual == "sally":
        hide keket_sally_anim
        show keket_sally_anim_rapida
    elif prostituta_atual == "kate":
        hide keket_kate_anim
        show keket_kate_anim_rapida
    # elif prostituta_atual == "crystal":
    #     hide keket_crystal_anim
    #     show keket_crystal_anim_rapida
    
    "[nome_prostituta]" "Alright, alright... I'll use my tongue in a special way..."
    b "That's it, bitch! That's how I like it... Holy shit, what a tasty little mouth!"
    "[nome_prostituta]" "Are you enjoying it? I never imagined SpongeBob would be so... intense."
    
    b "I'm gonna cum, damn! Get ready!"
    
    stop sound
    
    # Hide animation and show SPECIFIC cum for each prostitute
    if prostituta_atual == "sally":
        hide keket_sally_anim_rapida
        show gozada_boquete_sally_anim
    elif prostituta_atual == "kate":
        hide keket_kate_anim_rapida
        show gozada_boquete_kate_anim
    # elif prostituta_atual == "crystal":
    #     hide keket_crystal_anim_rapida
    #     show gozada_boquete_crystal_anim
    
    with hpunch
    b "Take it all, you slut!"
    
    with hpunch
    b "Keep sucking! I'm not done yet, damn!"
    
    with hpunch
    "[nome_prostituta]" "Wow! Never seen so much... how can you produce so much?"
    
    # Hide cum animation
    if prostituta_atual == "sally":
        hide gozada_boquete_sally_anim
    elif prostituta_atual == "kate":
        hide gozada_boquete_kate_anim
    # elif prostituta_atual == "crystal":
    #     hide gozada_boquete_crystal_anim
    
    # Show SPECIFIC final image based on prostitute
    if prostituta_atual == "sally":
        show sally gozo b at center  # Keep Sally's original
    elif prostituta_atual == "kate":
        show kate_gozada_boquete at center   # Kate's specific image
    # elif prostituta_atual == "crystal":
    #     show crystal_gozada_boquete at center
    
    pause 2.0
    
    "[nome_prostituta]" "What a different taste... never tasted anything like it!"
    
    stop music fadeout 1.0
    
    menu:
        "Go back to the room":
            stop music
            stop sound
            if prostituta_atual == "sally":
                hide sally gozo b
            elif prostituta_atual == "kate":
                hide kate_gozada_boquete
            # elif prostituta_atual == "crystal":
            #     hide crystal_gozada_boquete
            $ hora_do_dia += 2 
            $ setattr(store, "visitou_puta_dia_{}".format(saida), True)
            jump quanaite

# VAGINAL SCENE
label vagina_scene:
    scene cama bob
    
    stop music
    stop sound
    
    play music "sexmusic.wav" fadein 1.0
    play sound "gemidos.mp3" loop
    
    # Show animation based on current prostitute
    if prostituta_atual == "sally":
        show vagina_sally_anim
    elif prostituta_atual == "kate":
        show vagina_kate_anim
    # elif prostituta_atual == "crystal":
    #     show vagina_crystal_anim
    
    $ nome_prostituta = get_prostituta_nome()
    
    "[nome_prostituta]" "Eat my pussy you fat pervert!"
    "[nome_prostituta]" "Good thing you brought a condom! Safety first!"
    "[nome_prostituta]" "That's it, stick it all in! Who would've thought a sponge would have all that equipment!"
    b "Shut up and bounce on this dick, you slut! I'm gonna wreck you!"
    "[nome_prostituta]" "Wow, Bob! You're so... different than I imagined!"
    
    # Switch to fast animation
    if prostituta_atual == "sally":
        hide vagina_sally_anim
        show vagina_sally_anim_rapida
    elif prostituta_atual == "kate":
        hide vagina_kate_anim
        show vagina_kate_anim_rapida
    # elif prostituta_atual == "crystal":
    #     hide vagina_crystal_anim
    #     show vagina_crystal_anim_rapida
    
    stop sound
    play sound "botadarapida.mp3" loop
    
    b "Don't call me Bob, damn! I'm more man than anyone in this shitty sea!"
    "[nome_prostituta]" "What should I call you then?"
    b "You don't need to call me anything. Just moan real good and do your job, damn!"
    "[nome_prostituta]" "Wow, I can feel you throbbing inside me... you're different than I imagined!"
    
    b "I'm gonna cum, you bitch! Get ready!"
    
    stop sound
    
    # Hide animation and show SPECIFIC cum
    if prostituta_atual == "sally":
        hide vagina_sally_anim_rapida
        show gozada_vagina_sally_anim
    elif prostituta_atual == "kate":
        hide vagina_kate_anim_rapida
        show gozada_vagina_kate_anim
    # elif prostituta_atual == "crystal":
    #     hide vagina_crystal_anim_rapida
    #     show gozada_vagina_crystal_anim
    
    with hpunch
    b "Damn! Take it all, you slut!"
    
    with hpunch
    "[nome_prostituta]" "Yes! I feel it dripping down my legs!"
    
    with hpunch
    b "Never seen so much cum, huh bitch?"
    
    # Hide cum animation
    if prostituta_atual == "sally":
        hide gozada_vagina_sally_anim
    elif prostituta_atual == "kate":
        hide gozada_vagina_kate_anim
    # elif prostituta_atual == "crystal":
    #     hide gozada_vagina_crystal_anim
    
    # Show SPECIFIC final image based on prostitute
    if prostituta_atual == "sally":
        show sally_gozada_vagina at center  # Sally's specific
    elif prostituta_atual == "kate":
        show kate_gozada_vagina at center   # Kate's specific
    # elif prostituta_atual == "crystal":
    #     show crystal_gozada_vagina at center
    
    pause 2.0
    
    "[nome_prostituta]" "Wow! You're a machine for producing... never seen anything like it!"
    
    stop music fadeout 1.0
    
    menu:
        "Go back to the room":
            stop music
            stop sound
            if prostituta_atual == "sally":
                hide sally_gozada_vagina
            elif prostituta_atual == "kate":
                hide kate_gozada_vagina
            # elif prostituta_atual == "crystal":
            #     hide crystal_gozada_vagina
            $ hora_do_dia += 2 
            $ setattr(store, "visitou_puta_dia_{}".format(saida), True)
            jump quanaite

# ANAL SCENE
label cuzin_scene:
    scene cama bob
    
    stop music
    stop sound
    
    play music "sexmusic.wav" fadein 1.0
    play sound "gemidos.mp3" loop
    
    show filtro noite
    
    # Show animation based on current prostitute
    if prostituta_atual == "sally":
        show cuzin_sally_anim
    elif prostituta_atual == "kate":
        show cuzin_kate_anim
    # elif prostituta_atual == "crystal":
    #     show cuzin_crystal_anim
    
    $ nome_prostituta = get_prostituta_nome()
    
    "[nome_prostituta]" "Good thing you brought a condom! In the ass it's even more important!"
    "[nome_prostituta]" "That's it, stick it all in my ass! A sponge like you must know how to clean all the corners!"
    b "I'm gonna destroy that ass, bitch! You'll never sit right after me!"
    "[nome_prostituta]" "Wow, you're bigger than you look! Take it easy!"
    
    hide kradeath
    
    # Switch to fast animation
    if prostituta_atual == "sally":
        hide cuzin_sally_anim
        show cuzin_sally_anim_rapida
    elif prostituta_atual == "kate":
        hide cuzin_kate_anim
        show cuzin_kate_anim_rapida
    # elif prostituta_atual == "crystal":
    #     hide cuzin_crystal_anim
    #     show cuzin_crystal_anim_rapida
    
    stop sound
    play sound "botadarapida.mp3" loop
    
    b "Easy my ass! I paid good money for this ass, I'll use it however I want!"
    "[nome_prostituta]" "Ow! It hurts! You're nothing like on TV!"
    b "TV is a lie, you dumbass! Real life is very different, damn!"
    "[nome_prostituta]" "O-okay! Oh, that's it! You found the right spot! Keep going!"
    
    b "I'm gonna cum in this tight ass! Hold on tight, bitch!"
    
    stop sound
    
    # Hide animation and show SPECIFIC cum
    if prostituta_atual == "sally":
        hide cuzin_sally_anim_rapida
        show gozada_anal_sally_anim
    elif prostituta_atual == "kate":
        hide cuzin_kate_anim_rapida
        show gozada_anal_kate_anim
    # elif prostituta_atual == "crystal":
    #     hide cuzin_crystal_anim_rapida
    #     show gozada_anal_crystal_anim
    
    with hpunch
    b "Take it up the ass, you slut!"
    
    with hpunch
    "[nome_prostituta]" "Holy King! I can feel it shooting inside me!"
    
    with hpunch
    b "It's not over yet! Take more!"
    
    # Hide cum animation
    if prostituta_atual == "sally":
        hide gozada_anal_sally_anim
    elif prostituta_atual == "kate":
        hide gozada_anal_kate_anim
    # elif prostituta_atual == "crystal":
    #     hide gozada_anal_crystal_anim
    
    # Show SPECIFIC final image based on prostitute
    if prostituta_atual == "sally":
        show gozada cu 2 at center          # Sally's specific (keep as is)
    elif prostituta_atual == "kate":
        show kate_gozada_anal at center     # Kate's specific
    # elif prostituta_atual == "crystal":
    #     show crystal_gozada_anal at center
    
    pause 2.0
    
    "[nome_prostituta]" "Wow! How can you produce so much? It's like a hose!"
    
    stop music fadeout 1.0
    
    menu:
        "Go back to the room":
            stop music
            stop sound
            if prostituta_atual == "sally":
                hide gozada cu 2
            elif prostituta_atual == "kate":
                hide kate_gozada_anal
            # elif prostituta_atual == "crystal":
            #     hide crystal_gozada_anal
            $ hora_do_dia += 2 
            $ setattr(store, "visitou_puta_dia_{}".format(saida), True)
            jump quanaite

# CONVERSATION SCENE
label conversar_scene:
    $ nome_prostituta = get_prostituta_nome()
    $ dialogo_random = renpy.random.randint(1, 4)
    
    if dialogo_random == 1:
        "[nome_prostituta]" "So, are you really SpongeBob? You seem a bit... different"
        b "Of course I am, you stupid whore! Don't you see the sponge on my head?"
        "[nome_prostituta]" "And that scar on your neck? It looks like your head was... sewn on?"
        b "None of your business! It was an... accident. Now shut up about it before I get pissed!"
        "[nome_prostituta]" "And what happened to your voice? I remember it being more... high-pitched."
        b "I smoke three packs a day, damn! Got a problem with that? Now enough with the stupid questions!"
        
    elif dialogo_random == 2:
        "[nome_prostituta]" "Is this house really a pineapple? How does that work?"
        b "It's just a fucking house, damn! What's there to understand? Fell from a ship and that's it!"
        "[nome_prostituta]" "And it doesn't rot? We've been underwater for years..."
        b "Do I look like a marine biologist, you idiot? It's just a house, don't be a pain!"
        "[nome_prostituta]" "Fascinating. And all this furniture? Did it also fall from ships?"
        b "Some I stole, others I 'found'. Got a problem with that, princess?"
        "[nome_prostituta]" "You have peculiar taste in decoration. These flower curtains are... unique."
        b "I didn't choose this shit! It was already here when I arr... I mean, it was always like this. Now shut up!"
        
    elif dialogo_random == 4:
        "[nome_prostituta]" "What was that noise? It sounded like it came from that closet."
        b "Nothing at all! It's just the wind, damn! There's nothing in that closet!"
        "[nome_prostituta]" "It didn't sound like wind... It sounded more like someone moaning."
        b "Are you calling me a liar, you bitch? I already said it's nothing! It's Gary, my damn snail!"
        "[nome_prostituta]" "If you say so... Can I take a look at him? I love pets!"
        b "DON'T TOUCH THAT CLOSET, DAMN! I mean... he bites strangers. It's dangerous."
        "[nome_prostituta]" "Alright, alright! You don't need to yell, honey."
        b "I'm not your 'honey', got it? Now forget about that closet or we're gonna have problems!"
        
    "[nome_prostituta]" "Well, we've talked enough. Want to do something else now?"
    
    menu:
        "Go back to previous menu":
            jump sou_puta
            
        "Go back to the room":
            $ hora_do_dia += 2 
            $ setattr(store, "visitou_puta_dia_{}".format(saida), True)
            jump quanaite