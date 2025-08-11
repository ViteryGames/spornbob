# myScreens.rpy - Exploration System for External Areas (English)
# External locations with entry options to places

# Images of areas during the day
image area_siricascudo_dia = "images/kk.jpg"
image area_sandy_dia = "images/casasandyy.png"
image area_aguasvivas_dia = "images/jellyfieldings.png"
image area_loja_dia = "images/bangnday.png"

# Images of areas during the night
image area_siricascudo_noite = "images/kk_night.jpg"
image area_sandy_noite = "images/sandy_exterior_noite.png"
image area_aguasvivas_noite = "images/aguasvivas_exterior_noite.png"
image area_loja_noite = "images/bangnnight.png"

# Variables to track if player already visited a location
default visitou_siricascudo = False
default visitou_sandy_exterior = False
default visitou_aguasvivas = False
default visitou_loja_exterior = False

# Main label for exploration
label explorar_siricascudo:
    # Check if it's too late (after 8 PM)
    if hora_do_dia >= 20:
        scene area_siricascudo_noite
        "It's too late. The Krusty Krotch is already closed."
        
        menu:
            "Go back home":
                jump room4
    else:
        # Show area during the day
        scene area_siricascudo_dia
        
        # Show description only on first visit
        if not visitou_siricascudo:
            "You're in front of the Krusty Krotch. It's a popular restaurant in Bikini Bottom."
            $ visitou_siricascudo = True
        
        menu:
            "Enter the Krusty Krotch":
                # Call lobbykk screen instead of room2
                call screen lobbykk with fade
                
            "Go back to map":
                call screen mapScreen

label explorar_sandy:
    # Check if it's too late (after 8 PM)
    if hora_do_dia >= 20:
        scene area_sandy_noite
        "It's too late. Sandy is probably sleeping."
        
        menu:
            "Go back home":
                jump room4
    else:
        # Show area during the day
        scene area_sandy_dia
        
        # Show description only on first visit
        if not visitou_sandy_exterior:
            "You're in front of Sandy's house. It's an air dome where she lives."
            $ visitou_sandy_exterior = True
        
        menu:
            "Visit Sandy":
                jump sandy
                
            "Go back to map":
                call screen mapScreen

label explorar_aguasvivas:
    # Check if it's too late (after 8 PM)
    if hora_do_dia >= 20:
        scene area_aguasvivas_noite
        "It's too late. It's dangerous to hunt jellyfish at night."
        
        menu:
            "Go back home":
                jump room4
    else:
        # Show area during the day
        scene area_aguasvivas_dia
        
        # Show description only on first visit
        if not visitou_aguasvivas:
            "You're in the jellyfish fields. It's a perfect place to hunt them."
            $ visitou_aguasvivas = True
        
        menu:
            "Hunt jellyfish":
                # Check if has a net (item ID 7)
                if 7 in inventario:
                    jump minigame_aguasvivas
                else:
                    "You need a net to hunt jellyfish. Buy one at the store."
                    jump explorar_aguasvivas
                
            "Go back to map":
                call screen mapScreen

label explorar_loja:
    # Check if it's too late (after 8 PM)
    if hora_do_dia >= 20:
        scene area_loja_noite
        "It's too late. The store is already closed."
        
        menu:
            "Go back home":
                jump room4
    else:
        # Show area during the day
        scene area_loja_dia
        
        # Show description only on first visit
        if not visitou_loja_exterior:
            "You're in front of the store. Here you can buy useful items."
            $ visitou_loja_exterior = True
        
        menu:
            "Enter the store":
                jump barg
                
            "Go back to map":
                call screen mapScreen

# Add this code to screens.rpy or myScreens.rpy file to modify the map screen
# so it uses the new exploration labels

screen mapScreen():
    modal True  # Blocks interactions with screens below
    
    # Map background image
    add "mapibeta.png"
    
    # Navigation buttons with links to new exploration labels
    #Room 1
    imagebutton:
        xpos 545
        ypos 250
        idle "R1 idle.png"
        hover "R1 hover.png"
        action [Hide("mapScreen"), Jump("room1")]
        
    #Room 2 - Krusty Krotch
    imagebutton:
        xpos 22
        ypos 100
        idle "R2 idle.png"
        hover "R2 hover.png"
        action [Hide("mapScreen"), Jump("explorar_siricascudo")]
        
    #Room 3
   # imagebutton:
       # xpos 130
       # ypos 385
       # idle "R3 idle.png"
       # hover "R3 hover.png"
       # action [Hide("mapScreen"), Jump("room3")]
        
    #Room 4 - Sandy
    imagebutton:
        xpos 530
        ypos 600
        idle "R4 idle.png"
        hover "R4 hover.png"
        action [Hide("mapScreen"), Jump("explorar_sandy")]
    
    #Room 5
    #imagebutton:
        #xpos 1430
        #ypos 25
        #idle "R5 idle.png"
       # hover "R5 hover.png"
       # action [Hide("mapScreen"), Jump("praia")]
        
    #Jellyfish Fields
    imagebutton:
        xpos 1500
        ypos 590
        idle "jellyfields idle.png"
        hover "jellyfields hover.png"
        action [Hide("mapScreen"), Jump("explorar_aguasvivas")]
    
    #Store
    imagebutton:
        xpos 1395
        ypos 310
        idle "loja idle.png"
        hover "loja hover.png"
        action [Hide("mapScreen"), Jump("explorar_loja")]

         
    
    # Button to close map
    textbutton "Close Map":
        action Hide("mapScreen")
        xalign 0.5
        yalign 0.95
        text_size 40
        text_color "#FFFFFF"
        text_hover_color "#FFFF99"
        text_outlines [(2, "#003399", 0, 0)]
        background "#225599"
        hover_background "#3366BB"