# room4.rpy - Room 4 Game Logic

# Room 4 specific variables
default vezes_investigou = 0
default saida = 0
default tv_quebrada = False  # Variable to control if TV is already broken

# Images for TV sequence
image tv_reporter1 = "images/tv_reporter1.png"  # Frame 1 of anchor fish
image tv_reporter2 = "images/tv_reporter2.png"  # Frame 2 of anchor fish (mouth open)
image tv_reporter3 = "images/tv_reporter3.png"  # Frame 3 of anchor fish
image tv_batavo_soco = "images/tv_batavo_soco.png"  # Batavo punching the TV
image tv_quebrada = "images/tv_quebrada.png"  # Broken TV

# Anchor fish animation
image tv_reporter_anim:
    "tv_reporter1"
    pause 0.3
    "tv_reporter2"
    pause 0.3
    "tv_reporter3"
    pause 0.3
    repeat

# Main room 4 label
label room4:
    # Disable map when player is inside the house
    $ mapa_disponivel = False
    
    # Check if it's after 8 PM to redirect to night scene
    if hora_do_dia >= 20:
        jump quanaite
    
    # If not night, continue normally  
    scene quartobob

    show batavo1 at Transform(xzoom=-1):
        zoom 1.3 xpos 1000 ypos 200 
        
    play music "bobesponja.mp3" fadein 2.0

    "What should I do now?"
    jump chegada_em_casa

# Home arrival menu
label chegada_em_casa:
    # Check if it's after 8 PM to redirect to night scene
    if hora_do_dia >= 20:
        jump quanaite
        
    # If not night, continue normally
    # Start a loop of options that always returns to the initial menu
    while True:
        # Menu with credits option only after 15 days and nap option during day
        if dia >= 15:
            menu:
                "Go to the living room":
                    $ hora_do_dia += 1
                    play sound som_opcao
                    $ escolha = "cozinha"
                    jump salabob

                "Check Spoogebob":
                    $ escolha = "bob"
                    jump opcoes

                "Investigate":
                    $ escolha = "inv"
                    jump opcoes
                    
                "Take a nap" if hora_do_dia < 20:
                    jump take_nap
                    
                "View Credits": # Option available after 15 days
                    play sound som_opcao
                    "You turn on the television and see a special program about Bikini Bottom..."
                    jump creditos
        else:
            # Normal menu for days < 15 with nap option
            menu:
                "Go to the living room":
                    $ hora_do_dia += 1
                    play sound som_opcao
                    $ escolha = "cozinha"
                    jump salabob

                "Check Spoogebob":
                    $ escolha = "bob"
                    jump opcoes

                "Investigate":
                    $ escolha = "inv"
                    jump opcoes
                    
                "Take a nap" if hora_do_dia < 20:
                    jump take_nap

# Nap function
label take_nap:
    "I'm feeling tired... maybe I should get some rest."
    
    # Fade to black for sleep effect
    scene black with fade
    
    # Sleep sound effect (if you have one)
    # play sound "sleep.mp3"
    
    # Show sleeping text
    "You lie down on Spoogebob's bed and close your eyes..."
    "..."
    "....."
    "......."
    
    # Time skip to 8 PM
    $ hora_do_dia = 20
    
    # Fade back to night scene
    pause 2.0
    
    "You wake up feeling refreshed."
    "It's now evening..."
    
    # Go directly to night scene
    jump quanaite

# Action options handler
label opcoes:
    # Here you can customize what happens depending on the choice
    if escolha == "cozinha":
        "You go to the kitchen."
    elif escolha == "bob":
        show bobmorto
        "Spoogebob is unconscious"
        hide bobmorto
    elif escolha == "inv":
        if vezes_investigou == 0:
            "You discover 10 dollars under the mattress."
            "Inside an envelope written: 'Last 20 years salary'."
            $ money += 10
        elif vezes_investigou == 1:
            "You discovered that today is opposite day."
            $ dia_do_contra = True 
        else:
            "Nothing more to investigate."
        $ vezes_investigou += 1
    elif escolha == "gary":
        # Temporarily disable typing sound
        $ temp_callbacks = config.all_character_callbacks[:]
        $ config.all_character_callbacks = []
        
        play sound "gary1.wav"
        $ renpy.music.set_volume(0.2, channel="sound")
        "Gary" "Meow"
        
        # Restore typing sound system
        $ config.all_character_callbacks = temp_callbacks
        
        jump salabob     

    # Automatically return to options menu after a choice
    jump chegada_em_casa

# Living room
label salabob:
    # Check if it's after 8 PM to redirect to night scene
    if hora_do_dia >= 20:
        jump quanaite
        
    # Still inside house, map continues disabled
    scene bg room4
    
    show batavo1 at Transform(xzoom=-1):
        zoom 1.0 xpos 1000 ypos 400

    show gary at left:
        zoom 0.3 xpos 500 ypos 1000
    
    while True:
        if not sala_mensagem_exibida:
            "You are in the living room"  
            $ sala_mensagem_exibida = True 

        # Menu with Mrs. Puffy option after day 12
        if dia >= 8:
            menu:
                "Go back to bedroom":
                    $ hora_do_dia += 1
                    scene quartobob

                    show batavo1 at Transform(xzoom=-1) with fade:
                        zoom 1.0 xpos 1000 ypos 400

                    jump chegada_em_casa

                "Watch TV":
                    $ hora_do_dia += 1
                    if not tv_quebrada:
                        # First time watching TV
                        # Show anchor fish animation
                        scene bg room4
                        show tv_reporter_anim
                        
                        # Anchor fish dialogue
                        "News Anchor" "Breaking news! A dangerous human criminal escaped from prison in a boat!"
                        
                        "News Anchor" "The boat crashed near Bikini Bottom! Any information should be reported to the author-"
                        
                        # Batavo punches the TV
                        hide tv_reporter_anim
                        show tv_batavo_soco
                        
                        play sound "soco.mp3" volume 0.8
                        with hpunch
                        
                        b "SHUT THE FUCK UP!"
                        
                        # Broken TV
                        hide tv_batavo_soco
                        show tv_quebrada
                        
                        "You broke the TV with a punch."
                        
                        # Mark TV as permanently broken
                        $ tv_quebrada = True
                    else:
                        # TV already broken
                        scene bg room4
                        show tv_quebrada
                        
                        "The TV is broken."
                    
                    # Return to living room menu
                    scene bg room4
                    show batavo1 at Transform(xzoom=-1):
                        zoom 1.0 xpos 1000 ypos 400
                    
                    show gary at left:
                        zoom 0.3 xpos 500 ypos 1000
                    
                    jump salabob

                "Gary":
                    $ escolha = "gary"
                    jump opcoes
                    
                "Go to the boating school":
                    "You go there "
                    jump puffy

                "Exit":
                    $ hora_do_dia += 1
                    play sound som_opcao
                    # Enable map when player exits home
                    $ saida += 1  # Increment variable each click
                    if saida == 1:
                        jump storymode  # First time, go to storymode
                    elif saida == 2:
                        jump day2  # Second time, go to day2
                    elif saida == 3:
                        jump day3  # Third time, go to day3    
                    elif saida == 4:
                        jump landal  # Fourth time, go to landal   
                    elif saida == 10:
                        jump mrs_puffy_visit  # Tenth time, go to mrs_puffy_visit           
                    else:
                        $ mapa_disponivel = True
                        call screen bobCasas # From second time onwards, show screen
        else:
            # Normal menu for days < 12
            menu:
                "Go back to bedroom":
                    $ hora_do_dia += 1
                    scene quartobob

                    show batavo1 at Transform(xzoom=-1) with fade:
                        zoom 1.0 xpos 1000 ypos 400

                    jump chegada_em_casa

                "Watch TV":
                    $ hora_do_dia += 1
                    if not tv_quebrada:
                        # First time watching TV
                        # Show anchor fish animation
                        scene bg room4
                        show tv_reporter_anim
                        
                        # Anchor fish dialogue
                        "News Anchor" "Breaking news! A dangerous human criminal escaped from prison in a boat!"
                        
                        "News Anchor" "The boat crashed near Bikini Bottom! Any information should be reported to the author-"
                        
                        # Batavo punches the TV
                        hide tv_reporter_anim
                        show tv_batavo_soco
                        
                        play sound "soco.mp3" volume 0.8
                        with hpunch
                        
                        b "SHUT THE FUCK UP!"
                        
                        # Broken TV
                        hide tv_batavo_soco
                        show tv_quebrada
                        
                        "You broke the TV with a punch."
                        
                        # Mark TV as permanently broken
                        $ tv_quebrada = True
                    else:
                        # TV already broken
                        scene bg room4
                        show tv_quebrada
                        
                        "The TV is broken."
                    
                    # Return to living room menu
                    scene bg room4
                    show batavo1 at Transform(xzoom=-1):
                        zoom 1.0 xpos 1000 ypos 400
                    
                    show gary at left:
                        zoom 0.3 xpos 500 ypos 1000
                    
                    jump salabob

                "Gary":
                    $ escolha = "gary"
                    jump opcoes

                "Exit":
                    $ hora_do_dia += 1
                    play sound som_opcao
                    # Enable map when player exits home
                    $ saida += 1  # Increment variable each click
                    if saida == 1:
                        jump storymode  # First time, go to storymode
                    elif saida == 2:
                        jump day2  # Second time, go to day2
                    elif saida == 3:
                        jump day3  # Third time, go to day3    
                    elif saida == 4:
                        jump landal  # Fourth time, go to landal   
                    elif saida == 10:
                        jump mrs_puffy_visit  # Tenth time, go to mrs_puffy_visit           
                    else:
                        $ mapa_disponivel = True
                        call screen bobCasas # From second time onwards, show screen

# Night scene at home
label casanoite:
    # When returning home at night, disable map again
    $ mapa_disponivel = False
    
    scene quartobob noite

    show batavo1 at left with fade:
        zoom 1.2

    "What should I do now?"

    # Redirect to quanaite, which is Bob's room at night
    jump quanaite

# End scene 1
label end1:
    # Enable map when exiting and show houses
    $ mapa_disponivel = True
    
    call screen bobCasas