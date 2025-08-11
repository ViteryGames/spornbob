# flashback.rpy - Flying Dutchman Scene (English)

# Define images for the Flying Dutchman
image fumaca_verde:
    "fumaca_verde.png"  # Add this image to your resources
    zoom 1.5
    alpha 0.0
    linear 1.0 alpha 1.0
    easein 0.5 zoom 1.0 alpha 0.8
    
image holandes_normal:
    "holandes garrafa.png"  # Add this image to your resources
    zoom 0.8
    xalign 0.5
    yalign 0.5

image holandes_risada:
    "holandes metedor risada.png"  # Add this image to your resources
    zoom 0.8
    xalign 0.5
    yalign 0.5
    
image garrafa:
    "garrafa.png"  # Add this image to your resources
    zoom 0.5
    xalign 0.5
    yalign 0.8

image mapa:
    "mapa.png"  # Add this image to your resources
    zoom 0.7

# Define Flying Dutchman character
define h = Character("Flying Fuckman", color="#34A65F")

# Define variable to track if player already met the Dutchman
default encontrou_holandes = False
default tem_mapa_holandes = False

# Add this new label in storymode.rpy

label landal:
    scene bg room4
    stop music fadeout 1.0
    play audio "holandes.mp3" fadeout 2.0
    # Check if it's night
    if hora_do_dia >= 18 or hora_do_dia < 6:
        scene quartobob noite
    
    show batavo1 at Transform(xzoom=-1) with hpunch:
        zoom 1.0 xpos 1000 ypos 400
    
    "The living room door is locked."
    
    b "Huh, did it get stuck with cum?"
    
    # Shake effect for Dutchman's entrance
    show fumaca_verde at truecenter with dissolve
    
    play sound "risada_holandes.mp3" volume 0.8  # Add this sound
    
    "Strange green smoke appears in the room!"
    
    b "What the fuck is this now?!"
    
    # Intense shake when Dutchman appears
    with hpunch
    with vpunch
    
    hide fumaca_verde
    show holandes_risada with dissolve
    play audio "laugh2.mp3" fadeout 2.0
    
    h "HAHAHAHA! Look what we have here!"
    
    # Additional shake effect when he screams
    with hpunch
    
    h "SOMEONE NEW IN BIKINI BOTTOM, HUH?!"
    hide holandes_risada
    show holandes_normal
    
    h "Every new resident receives... a GIFT!"
    
    b "And who are you? A floating green faggot?"

    hide holandes_normal
    show holandes direita
    
    h "FAGGOT?! I am THE FLYING FUCKMAN you fat piece of shit!!"
    
    # Floating bottle movement
    hide holandes direita
    show garrafa at center with moveinbottom
    
    h "This map shows everything you need to explore this shitty city!"
    
    h "I'm tired of jerking off watching the crab's daughter in the shower, I want to see spicier things..."
    
    # Here the Dutchman narrows his eyes, suspecting
    h "Spoogebob Squirtpants was never much of a player. But you're not exactly Spoogebob, are you?"
    
    # Light shake effect to create tension
    with hpunch
    
    b "Fuck you talking about? Of course I'm Spoogebob you braided faggot! You gay sissy!"
    hide holandes_normal
    hide holandes direita
    show holandes_risada
    
    h "HAHAHA! I like your... style. One more reason to give you this map."
    
    h "There are... INTERESTING places marked on it! Use it wisely you fat impotent!"
    
    hide holandes_risada
    "The Flying Fuckman leaves the bottle floating in the air."
    
    show holandes_normal:
        alpha 1.0
        ease 1.5 alpha 0.0
        
    hide holandes_normal
    
    play sound "risada_holandes.mp3" volume 0.5
    
    "The Flying Fuckman's laughter echoes as he disappears..."
    
    b "What the fuck was that?"

    "You acquired the MAP, it will be available whenever you leave home in the upper right corner."
    
    # Define variable to activate new locations on map
    $ tem_mapa_holandes = True
    $ mapa_disponivel = True
    
    # Return to normal flow
    jump salabob