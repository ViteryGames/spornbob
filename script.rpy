# script.rpy - Main Script File (English Version)

# Define sounds for typing effects
define audio.typing = "bubbles.mp3"  # Sound for character dialogues
define audio.narration = "generic.mp3"  # Sound for narration/text without character

# Code to control typing sound
init python:
    # Global variable to control if sound is playing
    typing_sound_playing = False
    
    # Function to start and stop sound during typing
    def typing_sound_callback(event, **kwargs):
        global typing_sound_playing
        
        if event == "show":
            # Start sound when text begins to show
            renpy.music.play(audio.typing, channel="sound", loop=True)
            typing_sound_playing = True
        
        elif event == "slow_done" or event == "end":
            # Stop sound when all typing is done
            if typing_sound_playing:
                renpy.music.stop(channel="sound")
                typing_sound_playing = False
    
    # Function for narration callback (texts without character)
    def narration_sound_callback(event, **kwargs):
        global typing_sound_playing
        
        if event == "show":
            # Start sound when text begins to show
            renpy.music.play(audio.narration, channel="sound", loop=True)
            typing_sound_playing = True
        
        elif event == "slow_done" or event == "end":
            # Stop sound when all typing is done
            if typing_sound_playing:
                renpy.music.stop(channel="sound")
                typing_sound_playing = False

# Defining the narrator with narration callback
define narrator = Character(None, callback=narration_sound_callback)

# Configure callback to be called on character text events
init python:
    config.all_character_callbacks.append(typing_sound_callback)

# Background images
image fundo_dia = "fundo_dia.jpg"
image fundo_noite = "fundo_noite.jpg"

# Background display function
label mostrar_fundo():
    if hora_do_dia >= 6 and hora_do_dia < 18:
        show fundo_dia
    else:
        show fundo_noite
    return 

# Test label for day/night system
label inicio:
    call mostrar_fundo from _call_mostrar_fundo
    "It's dawn."  # Will use generic.mp3
    
    "Do you want to wait or continue?"  # Will use generic.mp3
    
    menu:
        "Wait":
            $ hora_do_dia += 6  # Pass 6 hours
            call mostrar_fundo from _call_mostrar_fundo_1
            "Now it's [hora_do_dia] o'clock."  # Will use generic.mp3
        "Continue":
            "You moved forward."  # Will use generic.mp3

    return

# Time advancement function
label avancar_tempo():
    $ hora_do_dia += 6
    if hora_do_dia >= 24:
        $ hora_do_dia = 0  # Return to midnight
    return

# Main game start
label start:
    # Play background music
    play music "bobesponja.mp3" fadein 2.0
    
    # Game variables - Default values
    default contrap1 = False
    default nugget = False 
    default mainmap = False
    default money = 0
    default macaca = False
    default sala_mensagem_exibida = False
    default hora_do_dia = 8  # Starts at 8 AM
    default mapa_disponivel = False
    
    # Character definitions with English names
    define p = Character("Fatrick Star", callback=typing_sound_callback)
    define bs = Character("Spoogebob Squirtpants", callback=typing_sound_callback)
    
    # Sound definitions
    define som_opcao = "open.wav"
    
    $ money = 0 

    # Override default menu behavior to play sound
    init python:
        # Store reference to original menu
        original_menu = renpy.display_menu

        # Custom function to play sound when choosing
        def custom_menu(choices, *args, **kwargs):
            # Play sound when player makes a choice
            renpy.play(som_opcao, channel="sound")
            # Call original menu
            return original_menu(choices, *args, **kwargs)

        # Replace default menu with custom one
        renpy.display_menu = custom_menu

    # Start the main cutscene
    jump cutscene

# Main cutscene sequence
label cutscene:
    # Start with suspense music
    scene disclaimer

    pause 2.0
    
    play music "susmusic.mp3" fadein 2.0
    play audio "bubaus.mp3" fadein 1.0

    show ingameburuba with fade

    "Uh... what?"
    show cutscene2 with fade
    
    "What is that? A pineapple?!"
    
    show cuts1

    "Spoogebob Squirtpants" "La lala lala"  # Will use bubbles.mp3 because it has character name

    # When franky appears, play the scream
    play audio "classicdrama.mp3"
    play audio "gritobob.mp3" volume 0.18
    show frankys with hpunch

    "Spoogebob Squirtpants" "AHHHHHHHHHHH"  # Will use bubbles.mp3 because it has character name
    
    # Fade to black screen after last image
    scene black with fade
    
    # Play ripping sound on black screen
    play audio "rasgazzo.mp3"
    # Wait a bit for sound to play
    pause 5.0

    play audio "gritobob.mp3" volume 0.18
    "Spoogebob Squirtpants" "NO! STOP! MY CLOTHES! MY FACE! WHAT ARE YOU DOING!"
    play audio "franklaugh.mp3"
    "You" "SHUT THE FUCK UP!"

    scene black with fade
    play audio "fewmom.mp3"

    show fewmom

    pause 3.0
    
    show screen xerequinha 
    stop audio
    stop sound
    stop music
    stop audio

    jump room4
# Configure o callback para ser chamado nos eventos de texto de personagens

if mainmap = True:
  call screen mapScreen
   
 

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
   #scene areia
    #Código para exibir texto na tela
    #text "{size=40}{color=#008000}[money]/[oppois_hit]{/color}{/size} Money" xpos 1100 ypos 50

    #image areia:
    # "areia.png"
    # zoom 1.5 
     
    #show areia
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #image batavo:
    # "batavo.png"
    # zoom 1.35 

    #image hard:
     #"hard.png"
    # zoom 1.35 
     
   # show batavo at left
    

    # These display lines of dialogue.

  #  "Bob Estrupo" "Oi bem?" 
   # "Bob Estrupro" "Caguei nas calças"
  #  with fade

    # This ends the game.
    
  #  "Dou you like niggers"
  #  menu: 

   #  "Yes": 

   #       jump choices1_a

   #  "Fuck you SpornBob":

   #       jump choices1_b

   # label choices1_a:
   #           "Good"

   # label choices1_b:
   #          "Uuuh"  with fade

   # "Dou you like raping for fun?"
   # menu: 

   #  "Yes": 

   #       jump choices2_a

    # "Fuck you SpornBob":

   #       jump choices2_b

  #  label choices2_a:
  #            "Good"
              
  #            show hard at left
              
   # label choices2_b:
   #          "Uuuh"

# (Continuação do código anterior)

# Dia 4 (Continuação)

    
return