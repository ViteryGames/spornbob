# xerequinha.rpy - UI Interface System (English) - Modified with Skip Day button

screen xerequinha:
    # Basic information with underwater theme - left side
    text "Money = [money]" xpos 50 ypos 50 size 50 color "#8CEFFD" outlines [(2, "#0066CC", 0, 0), (4, "#003366", 1, 1)]
    text "Time = [hora_do_dia]h" xpos 50 ypos 100 size 50 color "#8CEFFD" outlines [(2, "#0066CC", 0, 0), (4, "#003366", 1, 1)]
    #text "Exit = [saida]" xpos 50 ypos 150 size 50 color "#8CEFFD" outlines [(2, "#0066CC", 0, 0), (4, "#003366", 1, 1)]
    text "Day = [dia]" xpos 50 ypos 150 size 50 color "#8CEFFD" outlines [(2, "#0066CC", 0, 0), (4, "#003366", 1, 1)]
    
    # Shows condom quantity with outline effect - left side
    #$ qnt_camisinhas = inventario.count(14)
    #if qnt_camisinhas > 0:
        #text "Condoms = [qnt_camisinhas]/5" xpos 50 ypos 200 size 50 color "#FF99CC" outlines [(2, "#CC0066", 0, 0), (4, "#990033", 1, 1)]
    
    # Shows nut quantity with outline effect - left side
    #$ qnt_nozes = inventario.count(3)
    #if qnt_nozes > 0:
        #text "Nuts = [qnt_nozes]/10" xpos 50 ypos 250 size 50 color "#DDBB77" outlines [(2, "#996633", 0, 0), (4, "#663300", 1, 1)]
    
    # Shows captured jellyfish quantity - left side
    #$ qnt_aguas_vivas = inventario.count(21)
    #if qnt_aguas_vivas > 0:
        #text "Jellyfish = [qnt_aguas_vivas]" xpos 50 ypos 300 size 50 color "#FF80BF" outlines [(2, "#CC0066", 0, 0), (4, "#990033", 1, 1)]
    
    # Buttons for Map, Inventory and Skip Day - right side
    vbox:
        xpos 1500  # Positioned on the right side of screen
        ypos 50    # Aligned with top
        spacing 20
        
        # Map button only appears if mapa_disponivel is True
        if mapa_disponivel:
            textbutton "Map":
                action Show("mapScreen")
                text_size 40
                text_color "#FFFFFF"
                text_hover_color "#FFCC00"
                text_outlines [(2, "#003399", 0, 0)]
                background "#225599"
                hover_background "#3366BB"
        else:
            # Disabled version of button when map is not available
            textbutton "Map":
                action NullAction()
                text_size 40
                text_color "#888888"  # Gray color to indicate disabled
                text_outlines [(2, "#003366", 0, 0)]
                background "#113344"  # Dark color to indicate disabled
                sensitive False
            
        textbutton "Inventory":
            action Show("inventarioScreen")
            text_size 40
            text_color "#FFFFFF"
            text_hover_color "#FFCC00"
            text_outlines [(2, "#006633", 0, 0)]
            background "#228866"
            hover_background "#33AA88"
            
        # NEW: Skip Day button
        textbutton "Skip Day":
            action Jump("skip_day_action")
            text_size 40
            text_color "#FFFFFF"
            text_hover_color "#FFCC00"
            text_outlines [(2, "#663300", 0, 0)]
            background "#CC6600"
            hover_background "#FF8800"

# NEW: Label to handle Skip Day action
label skip_day_action:
    # Save current location before skipping
    $ current_location = renpy.get_return_stack()
    
    # Show transition effect
    scene black with fade
    "Time passes quickly..."
    
    # Increment day
    $ dia += 1
    
    # Reset time to morning (8 AM)
    $ hora_do_dia = 8
    
    # Increment saida (exit counter)
    $ saida += 1
    
    # Reset daily variables if needed
    # You can add any other daily reset variables here
    
    # Show wake up message
    "You wake up. It's 8 AM on day [dia]."
    
    # Return to bedroom (starting location for new day)
    jump room4

# Inventory Screen
screen inventarioScreen():
    modal True  # Blocks interactions with screens below
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 600
        background "#225599"  # Dark blue like deep water
        
        vbox:
            xalign 0.5
            yalign 0.0
            xsize 780
            ysize 540
            spacing 20
            
            text "YOUR INVENTORY" size 50 color "#8CEFFD" xalign 0.5 outlines [(3, "#003366", 0, 0), (5, "#002244", 1, 1)]
            
            # Check if inventory is empty
            if len(inventario) == 0:
                text "Your inventory is empty!" size 30 color "#FF9977" xalign 0.5 outlines [(2, "#CC6644", 0, 0)]
            else:
                # Calculate how many different items are in inventory (not counting duplicates like condoms and nuts)
                $ itens_unicos = []
                $ itens_multiplos = {3: 0, 14: 0, 21: 0}  # Dictionary to count nuts (3), condoms (14) and jellyfish (21)
                
                python:
                    for item_id in inventario:
                        if item_id == 3:  # Nuts
                            itens_multiplos[3] += 1
                        elif item_id == 14:  # Condoms
                            itens_multiplos[14] += 1
                        elif item_id == 21:  # Jellyfish
                            itens_multiplos[21] += 1
                        elif item_id not in itens_unicos:
                            itens_unicos.append(item_id)
                
                # Create scrollable area for many items
                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    xsize 760
                    ysize 400
                    
                    vbox:
                        spacing 15
                        xalign 0.5
                        
                        # Show items that can have multiple units
                        if itens_multiplos[3] > 0:  # Nuts
                            frame:
                                xsize 700
                                background "#336644"  # Dark green like seaweed
                                padding (20, 10)
                                
                                vbox:
                                    spacing 5
                                    text "Nuts" size 30 color "#DDBB77" outlines [(2, "#996633", 0, 0)]
                                    text "Quantity: [itens_multiplos[3]]/10" size 25 color "#EEDDAA" outlines [(1, "#AA8844", 0, 0)]
                                    text "A nutritious and healthy snack." size 20 color "#FFFFFF" outlines [(1, "#004400", 1, 1)]
                        
                        if itens_multiplos[14] > 0:  # Condoms
                            frame:
                                xsize 700
                                background "#993366"  # Dark pink
                                padding (20, 10)
                                
                                vbox:
                                    spacing 5
                                    text "Condoms" size 30 color "#FF99CC" outlines [(2, "#CC0066", 0, 0)]
                                    text "Quantity: [itens_multiplos[14]]/5" size 25 color "#FFBBDD" outlines [(1, "#CC6699", 0, 0)]
                                    text "Protection is important for certain activities." size 20 color "#FFFFFF" outlines [(1, "#660033", 1, 1)]
                                    
                        if itens_multiplos[21] > 0:  # Captured jellyfish
                            frame:
                                xsize 700
                                background "#CC6699"  # Medium pink
                                padding (20, 10)
                                
                                vbox:
                                    spacing 5
                                    text "Captured Jellyfish" size 30 color "#FF80BF" outlines [(2, "#CC0066", 0, 0)]
                                    text "Quantity: [itens_multiplos[21]]" size 25 color "#FFBBDD" outlines [(1, "#CC6699", 0, 0)]
                                    text "Gelatinous creatures you captured. Valuable for collection or use in recipes." size 20 color "#FFFFFF" outlines [(1, "#660033", 1, 1)]
                        
                        # Show other unique items
                        for item_id in itens_unicos:
                            frame:
                                xsize 700
                                background "#336699"  # Medium blue like ocean
                                padding (20, 10)
                                
                                vbox:
                                    spacing 5
                                    # CORRECTION: Check if item_id is in itens_loja before accessing
                                    if item_id in itens_loja:
                                        text itens_loja[item_id]["nome"] size 30 color "#99CCFF" outlines [(2, "#0044AA", 0, 0)]
                                        text "Price: $[itens_loja[item_id]['preco']]" size 25 color "#AADDFF" outlines [(1, "#0066CC", 0, 0)]
                                        
                                        # Custom descriptions for items
                                        if item_id == 1:  # Cowboy Hat
                                            text "A stylish hat to look like a real cowboy." size 20 color "#FFFFFF" outlines [(1, "#003366", 1, 1)]
                                        elif item_id == 15:  # Blow-up Doll
                                            text "Companionship for lonely nights." size 20 color "#FFFFFF" outlines [(1, "#003366", 1, 1)]
                                        elif item_id == 7:  # Jellyfish Net
                                            text "Essential tool for hunting jellyfish. Allows capturing more when using the minigame." size 20 color "#FFFFFF" outlines [(1, "#003366", 1, 1)]
                                        elif item_id == 8:  # Jellyfish Jar
                                            text "A special container for storing jellyfish. Different from the ones you capture in the game." size 20 color "#FFFFFF" outlines [(1, "#003366", 1, 1)]
                                        elif item_id == 25:  # Trash Stick
                                            text "Made from 100% authentic garbage. Sold at the Cum Bucket. Used in various evil recipes." size 20 color "#FFFFFF" outlines [(1, "#003366", 1, 1)]
                                        elif item_id == 26:  # Reef Powder
                                            text "🔥 Sexual stamina enhancer! Gives +1 extra spicy action per day with any character. Crafted in Plugton's lab." size 20 color "#FF6699" outlines [(1, "#CC0033", 1, 1)]
                                        elif item_id == 27:  # Jaguar Power
                                            text "🔥🔥 Ultimate sexual enhancer! Gives +2 extra spicy actions per day with any character. Crafted in Plugton's lab." size 20 color "#FF3366" outlines [(1, "#CC0033", 1, 1)]
                                        elif item_id == 28:  # Spatula 3000
                                            text "The most advanced cooking utensil ever created. Can flip burgers at light speed with perfect precision." size 20 color "#FFCC00" outlines [(1, "#996600", 1, 1)]
                                        elif item_id == 24:  # Steroid Shots
                                            text "💪 Military-grade anabolic enhancer! Guarantees victory in physical challenges." size 20 color "#00FF00" outlines [(1, "#006600", 1, 1)]
                                        else:
                                            text "Useful item for your adventure." size 20 color "#FFFFFF" outlines [(1, "#003366", 1, 1)]
                                    # If it's the jellyfish item (ID 21) that's in the separate dictionary
                                    elif item_id == 21:
                                        text "Captured Jellyfish" size 30 color "#FF80BF" outlines [(2, "#CC0066", 0, 0)]
                                        text "Price: $25" size 25 color "#FFBBDD" outlines [(1, "#CC6699", 0, 0)]
                                        text "A glowing jellyfish you captured. Can be used in various recipes or sold." size 20 color "#FFFFFF" outlines [(1, "#660033", 1, 1)]
                                    # Fallback for any other unrecognized item
                                    else:
                                        text "Unknown Item" size 30 color "#AAAAAA" outlines [(2, "#555555", 0, 0)]
                                        text "Uncatalogued item" size 20 color "#FFFFFF" outlines [(1, "#003366", 1, 1)]
        
        # Button to close inventory - submarine bubble style
        textbutton "Close":
            action Hide("inventarioScreen")
            xalign 0.5
            yalign 0.95
            text_size 40
            text_color "#FFFFFF"
            text_hover_color "#FFFF99"
            text_outlines [(2, "#990000", 0, 0)]
            background "#DD3366"
            hover_background "#FF5588"