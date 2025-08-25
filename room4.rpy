# room4.rpy - Room 4 Game Logic - REORGANIZED

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

# Home arrival menu - REORGANIZED
label chegada_em_casa:
    # Check if it's after 8 PM to redirect to night scene
    if hora_do_dia >= 20:
        jump quanaite
        
    # If not night, continue normally
    # Start a loop of options that always returns to the initial menu
    while True:
        # Menu with credits option only after 15 days and actions submenu
        if dia >= 15:
            menu:
                "Go to the living room":
                    $ hora_do_dia += 1
                    play sound som_opcao
                    $ escolha = "cozinha"
                    jump salabob

                "Actions":
                    jump menu_acoes_quarto
                    
                "View Credits": # Option available after 15 days
                    play sound som_opcao
                    "You turn on the television and see a special program about Bikini Bottom..."
                    jump creditos
        else:
            # Normal menu for days < 15 with actions submenu
            menu:
                "Go to the living room":
                    $ hora_do_dia += 1
                    play sound som_opcao
                    $ escolha = "cozinha"
                    jump salabob

                "Actions":
                    jump menu_acoes_quarto

# NEW: Actions submenu for bedroom - UPDATED WITH MYSTERIOUS ITEM
label menu_acoes_quarto:
    menu:
        "What action do you want to take?"
        
        # Only show "Check Spoogebob" before day 3
        "Check Spoogebob" if dia < 3:
            $ escolha = "bob"
            jump opcoes_quarto

        "Investigate":
            $ escolha = "inv"
            jump opcoes_quarto
            
        "Take a nap" if hora_do_dia < 20:
            jump take_nap
            
        "Scratch your balls":
            $ escolha = "cocar_saco"
            jump opcoes_quarto
            
        # NEW: Mysterious Item option - only appears if player has item ID 20
        "Look at mysterious item" if 20 in inventario:
            jump ver_item_misterioso
            
        "Go back":
            jump chegada_em_casa

# NEW: Label for mysterious item
label ver_item_misterioso:
    play music "tensada.mp3"

    "You decide to take a look at that mysterious item you bought..."
    "You carefully unwrap it, curious about what could be so expensive..."
    "It HAS to be something really awesome and worth your time"
    "Right?"
    "What could it be?"
    "So much mystery!"
    "You waited so long for this, it's going to be worth it!!"
    "You finally open it"
    # Show the mysterious image
    stop music
    play audio "quackbob.mp3"
    scene mr_krotch_calcinha
    
    pause (4.0)
    y"What?"

    y"What the fuck is this?"
    
    "You quickly hide the photo again, your hands shaking."
    "Some things cannot be unseen..."
    
    $ hora_do_dia += 1
    
    # Return to bedroom
    scene quartobob
    show batavo1 at Transform(xzoom=-1):
        zoom 1.3 xpos 1000 ypos 200
    
    jump menu_acoes_quarto

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

# Action options handler - RENAMED for bedroom
label opcoes_quarto:
    # Here you can customize what happens depending on the choice
    if escolha == "bob":
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
    elif escolha == "cocar_saco":
        $ dialogo_random = renpy.random.randint(1, 5)
        
        if dialogo_random == 1:
            "You scratch your balls with satisfaction."
            "Ah, that feels good. Nothing like a good ball scratch."
        elif dialogo_random == 2:
            "You scratch your balls vigorously."
            "Prison habits die hard. At least here you have privacy."
        elif dialogo_random == 3:
            "You give your balls a proper scratch."
            "Being underwater doesn't stop the itch. Some things never change."
        elif dialogo_random == 4:
            "You scratch your balls and sigh with relief."
            "Life's simple pleasures. Even criminals need comfort."
        else:
            "You scratch your balls like a true man."
            "Spoogebob probably never did this with such style."

    # Automatically return to actions menu after a choice
    jump menu_acoes_quarto

# Living room - REORGANIZED
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

        # Menu with Mrs. Puffy option after day 8 and actions submenu
        if dia >= 8:
            menu:
                "Go back to bedroom":
                    $ hora_do_dia += 1
                    scene quartobob

                    show batavo1 at Transform(xzoom=-1) with fade:
                        zoom 1.0 xpos 1000 ypos 400

                    jump chegada_em_casa

                "Actions":
                    jump menu_acoes_sala
                    
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
            # Normal menu for days < 8 with actions submenu
            menu:
                "Go back to bedroom":
                    $ hora_do_dia += 1
                    scene quartobob

                    show batavo1 at Transform(xzoom=-1) with fade:
                        zoom 1.0 xpos 1000 ypos 400

                    jump chegada_em_casa

                "Actions":
                    jump menu_acoes_sala

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

# NEW: Actions submenu for living room
label menu_acoes_sala:
    menu:
        "What action do you want to take?"
        
        "Watch TV":
            $ hora_do_dia += 1
            jump assistir_tv
            
        "Talk to Gary":
            $ escolha = "gary"
            jump opcoes_sala
            
        "Go back":
            jump salabob

# TV watching function - SEPARATED
label assistir_tv:
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
    
    jump menu_acoes_sala

# Action options handler for living room
label opcoes_sala:
    # Here you can customize what happens depending on the choice
    if escolha == "gary":
        # Temporarily disable typing sound
        $ temp_callbacks = config.all_character_callbacks[:]
        $ config.all_character_callbacks = []
        
        play sound "gary1.wav"
        $ renpy.music.set_volume(0.2, channel="sound")
        "Gary" "Meow"
        
        # Restore typing sound system
        $ config.all_character_callbacks = temp_callbacks
        
        jump menu_acoes_sala     

    # Automatically return to actions menu after a choice
    jump menu_acoes_sala

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