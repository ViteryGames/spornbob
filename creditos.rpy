# creditos.rpy - Credits Scene

# Define sound for credits
define audio.oceanman = "oceanman.mp3"

# Main credits label
label creditos:
    # Hide dialogue interface and xerequinha screen
    $ renpy.hide_screen("xerequinha")
    window hide
    $ _game_menu_screen = None
    
    # Stop any music that is playing
    stop music fadeout 2.0
    
    # Play credits music - creditson.mp3 (maintaining your music choice)
    play music "creditson.mp3" fadein 2.0
    
    # First image of Patchy saying "Ha, you're there!"
    scene black
    show patchy1
    with dissolve
    
    # Variable to store menu response
    $ menu_resposta = ""
    
    # Patchy Pirate dialogue talking to player - without dialogue boxes
    $ narrator_mode = True
    
    call screen tv_centered_text("HAR! There you are, matey! Good to see you!")
    
    call screen tv_centered_text("I'm Patchy Sins, the biggest fan of adult games on the whole planet!")
    
    call screen tv_centered_text("I see you've reached the end of the game... or at least this version of it!")
    
    # Custom menu to avoid traditional dialogue box - CORRECTED
    $ menu_resposta = renpy.call_screen("credits_menu")
    
    # Show response based on choice
    if menu_resposta == "gostei":
        call screen tv_centered_text("ARRR! I'm so happy to hear that, matey! The game creators will love to know you had fun!")
    elif menu_resposta == "interessante":
        call screen tv_centered_text("HAHAHA! I know what you mean, buddy! It's an adult game with quite a peculiar sense of humor!")
    elif menu_resposta == "mais":
        call screen tv_centered_text("THAT'S the right question, smart sailor!")
    
    # Second image of Patchy looking at the viewer
    hide patchy1
    show patchy2
    with dissolve
    
    call screen tv_centered_text("Let me tell you an important secret, just between us...")
    
    call screen tv_centered_text("This is only version 0.0.9 BETA of the Spornbob game!")
    
    call screen tv_centered_text("There's MUCH more content in development, with new scenes, characters and minigames!")
    
    call screen tv_centered_text("The game creator is working tirelessly on new content...")
    
    call screen tv_centered_text("And you can get early access to all this extra content by visiting his Patreon!")
    
    # Custom menu for Patreon questions - CORRECTED
    $ menu_resposta = renpy.call_screen("credits_menu_patreon")
    
    # Show response based on choice
    if menu_resposta == "como":
        call screen tv_centered_text("It's simple, matey! Just click the button that will appear on the credits screen! Or copy and paste https://www.patreon.com/FRANKTOPIAGAMESTUDIO!")
    elif menu_resposta == "exclusivo":
        call screen tv_centered_text("There's early access, game sprites, exclusive art, polls, direct interaction with the team, playtests and much more!")
    elif menu_resposta == "olhada":
        call screen tv_centered_text("Wise decision, buddy! You won't regret it!")
    
    call screen tv_centered_text("Now, without further ado, let's go to the credits of this wonderful game!")
    
    call screen tv_centered_text("And remember: SPORNBOB WILL RETURN SOON WITH MUCH MORE CONTENT!")
    
    # Show the 5 credits images in sequence
    hide patchy2
    
    # Switch to oceanman music here (kept from your code)
    play music audio.oceanman fadein 2.0
    
    # Credits image 1
    show creditos1
    with dissolve
    pause 3.0
    
    # Credits image 2
    hide creditos1
    show creditos2
    with dissolve
    pause 3.0
    
    # Credits image 3
    hide creditos2
    show creditos3
    with dissolve
    pause 3.0
    
    # Credits image 4
    hide creditos3
    show creditos4
    with dissolve
    pause 3.0
    
    # Credits image 5
    hide creditos4
    show patreons1
    with dissolve
    pause 3.0

    hide patreons1
    show patreons2
    with dissolve
    pause 3.0

    hide patreons2
    show patreons3
    with dissolve
    pause 3.0

    hide patreons3
    show patreons4
    with dissolve
    pause 3.0

    hide patreons4
    show patreons5
    with dissolve
    pause 3.0

    hide patreons5
    show patreons6
    with dissolve
    pause 3.0

    hide patreons6
    show patreons7
    with dissolve
    pause 3.0

    hide patreons7
    show patreons8
    with dissolve
    pause 3.0

    hide patreons8
    show creditos5
    with dissolve
    pause 3.0
    
    # Final screen with clickable Patreon link
    hide creditos5
    
    # Show Patchy again before final screen
    show patchy1
    
    call screen tv_centered_text("It was an honor to share this adventure with you, matey!")
    
    call screen tv_centered_text("I hope to see you again soon in the ocean of updates!")
    
    call screen tv_centered_text("Don't forget to check out the Patreon, there are many hidden treasures there!")
    
    call screen tv_centered_text("ARRR! Until next time, comrade!")
    
    hide patchy1
    
    # Show black screen with Patreon button
    call screen creditos_patreon
    
    # Restore interface when returning to game
    window show
    $ _game_menu_screen = "save"
    $ renpy.show_screen("xerequinha")  # CORRECTED: changed show_screen to renpy.show_screen
    
    # End credits music with fade
    stop music fadeout 2.0
    
    # Return to Bob's room
    jump room4
    
    return

# Centered text screen for dialogues without box - CORRECTED TO FIT TV SIZE
screen tv_centered_text(text_to_show):
    modal True
    
    # Clickable area to advance
    button:
        xfill True
        yfill True
        action Return()
    
    # Frame with limited size to fit TV
    frame:
        xalign 0.5
        yalign 0.8  # Updated position as per your code
        xsize 600  # Width limited to fit TV
        background None
        padding (20, 20)
        
        text text_to_show:
            xalign 0.5
            text_align 0.5
            size 30  # Reduced size
            color "#FFFFFF"
            outlines [(2, "#000000", 0, 0)]
            layout "subtitle"  # Better line breaking for long texts

# Custom menu for choices during credits
screen credits_menu():
    modal True
    
    frame:
        xalign 0.5
        yalign 0.8
        xsize 600  # Width limited to fit TV
        background None
        
        vbox:
            spacing 20
            xalign 0.5
            
            textbutton "I really liked the game!":
                action Return("gostei")
                xalign 0.5
                text_size 25  # Reduced size
                text_color "#FFFFFF"
                text_hover_color "#FFFF00"
                text_outlines [(2, "#000000", 0, 0)]
                background "#00000080"
                hover_background "#33333380"
                
            textbutton "The game was... interesting...":
                action Return("interessante")
                xalign 0.5
                text_size 25  # Reduced size
                text_color "#FFFFFF"
                text_hover_color "#FFFF00"
                text_outlines [(2, "#000000", 0, 0)]
                background "#00000080"
                hover_background "#33333380"
                
            textbutton "When is more content coming?":
                action Return("mais")
                xalign 0.5
                text_size 25  # Reduced size
                text_color "#FFFFFF"
                text_hover_color "#FFFF00"
                text_outlines [(2, "#000000", 0, 0)]
                background "#00000080"
                hover_background "#33333380"

# Custom menu for Patreon questions
screen credits_menu_patreon():
    modal True
    
    frame:
        xalign 0.5
        yalign 0.8
        xsize 600  # Width limited to fit TV
        background None
        
        vbox:
            spacing 20
            xalign 0.5
            
            textbutton "How do I access Patreon?":
                action Return("como")
                xalign 0.5
                text_size 25  # Reduced size
                text_color "#FFFFFF"
                text_hover_color "#FFFF00"
                text_outlines [(2, "#000000", 0, 0)]
                background "#00000080"
                hover_background "#33333380"
                
            textbutton "What's exclusive on Patreon?":
                action Return("exclusivo")
                xalign 0.5
                text_size 25  # Reduced size
                text_color "#FFFFFF"
                text_hover_color "#FFFF00"
                text_outlines [(2, "#000000", 0, 0)]
                background "#00000080"
                hover_background "#33333380"
                
            textbutton "I'll take a look!":
                action Return("olhada")
                xalign 0.5
                text_size 25  # Reduced size
                text_color "#FFFFFF"
                text_hover_color "#FFFF00"
                text_outlines [(2, "#000000", 0, 0)]
                background "#00000080"
                hover_background "#33333380"

# Screen with Patreon button
screen creditos_patreon():
    modal True
    tag creditos
    
    # Dark background
    add "black"
    
    # Thanks
    vbox:
        xalign 0.5
        yalign 0.3
        spacing 20
        
        text "Thank you for playing Spornbob!" size 50 color "#FFDD00" xalign 0.5 outlines [(3, "#DD6600", 0, 0)]
        text "Version 0.0.9 BETA" size 30 color "#FFFFFF" xalign 0.5 outlines [(2, "#555555", 0, 0)]
        
        null height 80
        
        text "For more content, updates and full versions:" size 30 color "#FFFFFF" xalign 0.5
    
    # Big Patreon button
    vbox:
        xalign 0.5
        yalign 0.7
        
        # Stylized Patreon button
        textbutton "VISIT OUR PATREON":
            action OpenURL("https://www.patreon.com/FRANKTOPIAGAMESTUDIO")
            xalign 0.5
            text_size 40
            text_color "#FFFFFF"
            text_hover_color "#FF424D"  # Patreon red color
            text_outlines [(2, "#052D49", 0, 0)]
            background "#FF424D"  # Button color is Patreon color
            hover_background "#FF6B70"
            padding (50, 20)
        
        null height 20
        
        # Patreon URL
        text "patreon.com/FRANKTOPIAGAMESTUDIO" size 30 color "#FF424D" xalign 0.5 outlines [(1, "#052D49", 0, 0)]
    
    # Button to return to room
    vbox:
        xalign 0.5
        yalign 0.95
        
        textbutton "Back to room":
            action Return()
            xalign 0.5
            text_size 30
            text_color "#FFFFFF"
            text_hover_color "#FFDD00"
            text_outlines [(2, "#333333", 0, 0)]
            background "#444444"
            hover_background "#666666"
            padding (30, 10)