# praia.rpy - Main Beach System (English) - FIXED VERSION

# Variables to track beach state
default ja_visitou_praia = False  # Track if already visited beach before

# Beach images
image bg_praia_dia = "images/praia_dia.png"
image bg_praia_noite = "images/praia_noite.jpg"

# Function to clean all beach-related screens
init python:
    def limpar_telas_praia():
        # Hide all possible mini-game screens that might be open
        renpy.hide_screen("arm_wrestling_game")
        renpy.hide_screen("sorvete_ingredientes_screen")
        renpy.hide_screen("ag_game_screen")
        renpy.hide_screen("ag_game_info")
        # Hide any other potential overlay screens
        renpy.hide_screen("quick_menu")
        # Force hide any modal screens
        try:
            renpy.hide_screen("say")
        except:
            pass

# Main beach label
label praia:
    # Clean any leftover screens when entering
    $ limpar_telas_praia()
    
    # Check if it's too late (after 8 PM)
    if hora_do_dia >= 20:
        scene bg_praia_noite
        "The beach is closed at night. Better come back during the day."
        
        menu:
            "Go back home":
                # Clean screens before leaving
                $ limpar_telas_praia()
                jump room4
    else:
        # Show beach during the day
        scene praia crowd
        play music "dabeach.mp3"

        # Show description only on first visit
        if not ja_visitou_praia:
            "You arrive at Goon Lagoon Beach for the first time."
            "The sun is shining and it's really fucking hot."
            "There are two main areas: Larry's workout zone and an ice cream stand."
            $ ja_visitou_praia = True
        else:
            "You're back at Goon Lagoon Beach."
        
        jump menu_praia_principal

# Main beach menu - Choose area
label menu_praia_principal:
    scene praia crowd

    menu:
        "Which area do you want to visit?"
        
        "Larry's Workout Zone":
            jump area_larry
            
        "Ice Cream Stand":
            jump area_sorvete
            
        "Leave the beach":
            jump sair_praia

# Exit beach - FIXED VERSION
label sair_praia:
    # IMPORTANT: Clean all screens before leaving
    $ limpar_telas_praia()
    
    # Stop any playing sounds/music from mini-games
    stop sound
    stop music fadeout 1.0
    
    # Clear any ongoing timers
    $ arm_wrestling_active = False
    $ ice_cream_active = False
    
    # Force screen refresh
    scene black
    pause 0.1
    
    scene black with dissolve
    "You leave Goon Lagoon Beach..."
    
    # Ensure quick_menu is back
    $ quick_menu = True
    
    # Return to map instead of room4 to avoid conflicts
    $ mapa_disponivel = True
    call screen mapScreen

# Additional cleanup function for emergencies
label limpar_praia_completo:
    # Nuclear option - clean everything
    $ limpar_telas_praia()
    $ arm_wrestling_active = False
    $ ice_cream_active = False
    $ quick_menu = True
    scene black
    pause 0.1
    jump sair_praia