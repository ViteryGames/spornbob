# myScreens.rpy - Exploration System for External Areas (English)
# External locations with entry options to places

# Images of areas during the day
image area_siricascudo_dia = "images/kk.jpg"
image area_sandy_dia = "images/casasandyy.png"
image area_aguasvivas_dia = "images/jellyfieldings.png"
image area_loja_dia = "images/bangnday.png"
image area_perola_dia = "images/casa_perola_exterior_dia.png"
image area_room3_dia = "images/room3_exterior_dia.png"  # NEW: Room 3 exterior

# Images of areas during the night
image area_siricascudo_noite = "images/kk_night.jpg"
image area_sandy_noite = "images/sandy_exterior_noite.png"
image area_aguasvivas_noite = "images/aguasvivas_exterior_noite.png"
image area_loja_noite = "images/bangnnight.png"
image area_perola_noite = "images/casa_perola_exterior_noite.png"
image area_room3_noite = "images/room3_exterior_noite.png"  # NEW: Room 3 at night

# Map images - NEW: Add different map versions
image mapibeta = "mapibeta.png"  # Original map with locked areas
image mapibeta_unlocked = "mapibeta_unlocked.png"  # Updated map with all areas unlocked

# Variables to track if player already visited a location
default visitou_siricascudo = False
default visitou_sandy_exterior = False
default visitou_aguasvivas = False
default visitou_loja_exterior = False
default visitou_praia_exterior = False
default visitou_perola_exterior = False
default visitou_room3_exterior = False  # NEW: Track Room 3 visits

# NEW: Map unlock system variables
default area_3_desbloqueada = False    # Track if area 3 has been unlocked

# Function to unlock area 3
init python:
    def desbloquear_area_3():
        global area_3_desbloqueada, inventario
        if not area_3_desbloqueada and 30 in inventario:  # Assuming item ID 30 is map piece 3
            # Remove map piece from inventory
            inventario.remove(30)
            # Mark area as unlocked
            area_3_desbloqueada = True
            # Play unlock sound
            renpy.music.play("unlockbucket.mp3", channel="sound", loop=False)
            return True
        return False

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
                # VERIFICAR SE DEVE ATIVAR A DESCOBERTA DA PÉROLA (DIA 12+)
                if dia >= 12 and not perola_descoberta_financeira:
                    jump descoberta_financeira_perola
                else:
                    # Call lobbykk screen normally
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

label explorar_praia:
    # Check if it's too late (after 8 PM)
    if hora_do_dia >= 20:
        scene praia noite
        "It's too late. Goon Lagoon Beach is closed at night."
        
        menu:
            "Go back home":
                jump room4
    else:
        # Show area during the day
        scene praca praia
        
        # Show description only on first visit
        if not visitou_praia_exterior:
            "You're at the entrance to Goon Lagoon Beach."

            "You can hear the sound of waves and see muscular sea creatures working out."
            $ visitou_praia_exterior = True
        
        menu:
            "Enter Goo Lagoon Beach":
                jump praia
                
            "Go back to map":
                call screen mapScreen

# Pearl's house exploration
label explorar_casa_perola:
    # Check if address is known
    if not endereco_perola_descoberto:
        "You don't know where Pearl lives. You need to find out her address first."
        
        menu:
            "Go back to map":
                call screen mapScreen
    
    # Check if it's too late (after 8 PM)
    if hora_do_dia >= 20:
        scene area_perola_noite
        "It's too late. Pearl is probably sleeping and Mr. Krotch might be home."
        
        menu:
            "Go back home":
                jump room4
            "Go back to map":
                call screen mapScreen
    else:
        # Show area during the day
        scene area_perola_dia
        
        # Show description only on first visit
        if not visitou_perola_exterior:
            "You arrive at Rua das Baleias, 69 - Pearl's house."
            "It's a luxurious mansion that clearly shows Mr. Krotch's wealth."
            "You can see expensive decorations and a well-maintained garden."
            $ visitou_perola_exterior = True
        else:
            "You're back at Pearl's house on Rua das Baleias, 69."
        
        menu:
            "Visit Pearl":
                jump visitar_casa_perola
                
            "Go back to map":
                call screen mapScreen

# NEW: Area 3 blocked message
label area_3_bloqueada:
    "🚫 ACCESS BLOCKED 🚫"
    "This area of the map is covered in mysterious fog..."
    "You need something to reveal what's hidden here."
    "Maybe you should look for a map piece or guide that shows this location?"
    
    # Check if player has map piece 3 in inventory
    if 30 in inventario:
        menu:
            "Use Map Piece 3":
                jump usar_mapa_piece_3
                
            "Go back to map":
                call screen mapScreen
    else:
        menu:
            "Go back to map":
                call screen mapScreen

# NEW: Use map piece 3 to unlock area
label usar_mapa_piece_3:

    play music "biurifou.mp3"

    "You pull out the mysterious map piece you found..."
    "As you hold it up to the foggy area, it begins to glow!"
    

    
    "The fog starts to clear, revealing a hidden path!"
    "You can now see a strange building in the distance..."
    "It looks like some kind of bucket-shaped restaurant!"
    
    $ desbloquear_area_3()
    
    "🗺️ AREA UNLOCKED! 🗺️" 
    play audio "unlockcumbuket.mp3" volume 0.8
    "You have unlocked:"
    "The Cum Bucket"
    "Map Piece 3 has been consumed and integrated into your map!"
    
    # Show the map screen with updated version
    call screen mapScreen

# Add this code to screens.rpy or myScreens.rpy file to modify the map screen
# so it uses the new exploration labels

screen mapScreen():
    modal True  # Blocks interactions with screens below
    
    # Show different map background based on unlock status
    if area_3_desbloqueada:
        add "mapibeta_unlocked.png"  # Updated map with all areas visible
    else:
        add "mapibeta.png"  # Original map with locked areas
    
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
        
    #Room 3 - UPDATED: Different behavior based on unlock status
    if area_3_desbloqueada:
        # Show normal Room 3 button if area is unlocked
        imagebutton:
            xpos 130
            ypos 385
            idle "R3 idle.png"
            hover "R3 hover.png"
            action [Hide("mapScreen"), Jump("explorar_balde_lixo")]
    else:
        # Show locked/mysterious version if area not unlocked
        imagebutton:
            xpos 130
            ypos 385
            idle "R3 locked.png"  # Different image for locked state
            hover "R3 locked_hover.png"  # Hover state for locked
            action [Hide("mapScreen"), Jump("area_3_bloqueada")]  # Go to blocked message
        
    #Room 4 - Sandy
    imagebutton:
        xpos 530
        ypos 600
        idle "R4 idle.png"
        hover "R4 hover.png"
        action [Hide("mapScreen"), Jump("explorar_sandy")]
    
    #Room 5
    imagebutton:
        xpos 1430
        ypos 25
        idle "R5 idle.png"
        hover "R5 hover.png"
        action [Hide("mapScreen"), Jump("explorar_praia")]
        
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

    # Pearl's House - only appears if address is known
    if endereco_perola_descoberto:
        imagebutton:
            xpos 450
            ypos 8
            idle "casa_perola_idle.png"
            hover "casa_perola_hover.png"
            action [Hide("mapScreen"), Jump("explorar_casa_perola")]
    
    # NEW: Map status indicator
    if area_3_desbloqueada:
        text "🗺️ Map Complete - All Areas Unlocked" xpos 50 ypos 930 size 25 color "#00FF00" outlines [(2, "#006600", 0, 0)]
    else:
        text "🗺️ Map Incomplete - Mysterious Area Detected" xpos 50 ypos 930 size 25 color "#FF6B6B" outlines [(2, "#8B0000", 0, 0)]
        # Show hint if player has map piece
        if 30 in inventario:
            text "💡 Map Piece 3 in inventory - Click locked area to use!" xpos 50 ypos 960 size 20 color "#FFD700" outlines [(2, "#8B4513", 0, 0)]
         
    
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