# barg.rpy - Shop System (English) - UPDATED VERSION

label barg: 
    hide screen xerequinha
    
    scene barganinha:
      zoom 1.2

    "Welcome to Bang N Mart!"
    "You have [money] coins to spend in the shop."
    
    # Show the shop and wait for player to exit
    call screen loja
    
    # After the shop, continue the story
    "You left the shop!"
    
    # Example of using a purchased item
    if 1 in inventario:
        "You grab your Cowboy Hat and prepare for adventure!"
    else:
        "You don't have a Cowboy Hat. Maybe you should buy one..."

default inventario = []  # List of purchased items (IDs)
default pagina_atual = 1  # Controls current shop page
default agua_viva_capturadas = 0  # Counter for jellyfish caught in minigame
default mapa_piece_3_comprado = False  # NEW: Track if map piece 3 was bought

# Defining the shop items including new additions
define itens_loja = {
    1: {"nome": "Cowboy Hat", "preco": 50},
    2: {"nome": "Chocolate", "preco": 3},
    3: {"nome": "Nuts", "preco": 5},
    4: {"nome": "Screwdriver", "preco": 20},
    5: {"nome": "Seaweed Pie", "preco": 10},
    6: {"nome": "Nut Pie (Straight from Texas)", "preco": 30},
    7: {"nome": "Jellyfish Catching Net", "preco": 15},
    8: {"nome": "Jellyfish Jar", "preco": 2},
    9: {"nome": "Clarinet", "preco": 60},
    10: {"nome": "Books", "preco": 10},
    11: {"nome": "Snail Food", "preco": 5},
    12: {"nome": "Sandwich", "preco": 10},
    13: {"nome": "Burger Bun Bag", "preco": 15},
    14: {"nome": "Condom", "preco": 5},
    15: {"nome": "Blow-up Doll", "preco": 400},
    16: {"nome": "Soap Bubble", "preco": 10},
    17: {"nome": "Sleeping Pills", "preco": 25},
    18: {"nome": "Glass Bottle", "preco": 15},
    19: {"nome": "Pineapple", "preco": 8},  # UPDATED: price reduced to 8 coins
    20: {"nome": "Mysterious Item 2", "preco": 4000},
    21: {"nome": "Captured Jellyfish", "preco": 25},  # Item added for reference (not sold in shop)
    22: {"nome": "Jellyfish Jelly", "preco": 40},  # Item added for reference (not sold in shop)
    23: {"nome": "Jar with Jelly", "preco": 50},  # Item added for reference (not sold in shop)
    # NEW ITEMS ADDED - Homemade ice creams (not sold in shop)
    101: {"nome": "Homemade Milk Ice Cream", "preco": 0},  # Not sold - gift item only
    102: {"nome": "Homemade Mango Ice Cream", "preco": 0},  # Not sold - gift item only
    # NEW ITEM ADDED - Steroids (not sold in shop)
    103: {"nome": "Steroids", "preco": 0},  # Not sold - special item for Larry interactions
    # NEW ITEM ADDED - Map Piece 3
    30: {"nome": "Map Piece 3 - Mysterious Area", "preco": 200}  # NEW: Expensive map piece
}

# List of items that actually appear in the shop (excludes special items)
# UPDATED: Map Piece 3 moved to BEGINNING for easy access
define itens_mostrados_loja = [30, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20]  # Map piece FIRST in the list

# Function to buy items
init python:
    def comprar_item(id_item):
        global money, inventario, mapa_piece_3_comprado
        item = itens_loja[id_item]
        
        # Check limits for special items
        if id_item == 14:  # Condom
            qnt_camisinhas = inventario.count(14)
            if qnt_camisinhas >= 5:
                renpy.notify("You already have the maximum number of condoms (5)!")
                return
                
        elif id_item == 3:  # Nuts
            qnt_nozes = inventario.count(3)
            if qnt_nozes >= 10:
                renpy.notify("You already have the maximum number of nuts (10)!")
                return
                
        elif id_item == 8:  # Jellyfish Jar
            qnt_potes = inventario.count(8)
            if qnt_potes >= 5:
                renpy.notify("You already have the maximum number of jellyfish jars (5)!")
                return
        
        elif id_item == 30:  # Map Piece 3
            if mapa_piece_3_comprado:
                renpy.notify("You already have this map piece!")
                return
        
        # Check if has enough money
        if money >= item["preco"]:
            money -= item["preco"]
            
            # For items that can be bought multiple times
            if id_item == 14:  # Condom
                inventario.append(id_item)
                renpy.notify("Condom purchased successfully!")
            elif id_item == 3:  # Nuts
                inventario.append(id_item)
                renpy.notify("Nuts purchased successfully!")
            elif id_item == 8:  # Jellyfish Jar
                inventario.append(id_item)
                renpy.notify("Jellyfish Jar purchased successfully!")
            elif id_item == 30:  # Map Piece 3 - SPECIAL HANDLING
                inventario.append(id_item)
                mapa_piece_3_comprado = True
                renpy.notify("🗺️ MAP PIECE 3 ACQUIRED! 🗺️")
                renpy.notify("New area unlocked on the map!")
                # Play special sound effect if available
                # renpy.sound.play("map_unlock.mp3")
            # For other items, check if already owns
            elif id_item not in inventario:
                inventario.append(id_item)
                renpy.notify(f"{item['nome']} purchased successfully!")
            else:
                renpy.notify("You already own this item!")
                money += item["preco"]  # Return the money
        else:
            renpy.notify("Insufficient coins!")
    
    # Function to add captured jellyfish to inventory
    def adicionar_aguas_vivas_ao_inventario(quantidade):
        global inventario, agua_viva_capturadas
        
        # Add captured jellyfish (ID 21) to inventory
        for i in range(quantidade):
            inventario.append(21)
        
        # Update total counter
        agua_viva_capturadas += quantidade
        
        renpy.notify(f"{quantidade} jellyfish added to inventory!")
    
    # Function to add special items to inventory (for homemade ice creams, steroids, etc.)
    def adicionar_item_especial(id_item, quantidade=1):
        global inventario
        for i in range(quantidade):
            inventario.append(id_item)
        
        if id_item in itens_loja:
            item_nome = itens_loja[id_item]["nome"]
            if quantidade == 1:
                renpy.notify(f"{item_nome} added to inventory!")
            else:
                renpy.notify(f"{quantidade} {item_nome} added to inventory!")
    
    # Function to check if player has specific item
    def tem_item(id_item):
        return id_item in inventario
    
    # Function to remove item from inventory
    def remover_item(id_item):
        global inventario
        if id_item in inventario:
            inventario.remove(id_item)
            return True
        return False
    
    # Function to count specific items in inventory
    def contar_item(id_item):
        return inventario.count(id_item)

# Functions to change pages
init python:
    def proxima_pagina():
        global pagina_atual
        # Calculate total pages based on number of items shown in shop
        total_paginas = (len(itens_mostrados_loja) + 5) // 6  # 6 items per page, rounding up
        if pagina_atual < total_paginas:
            pagina_atual += 1

    def pagina_anterior():
        global pagina_atual
        if pagina_atual > 1:
            pagina_atual -= 1

# Shop interface with items in grid
screen loja():
    frame:
        xalign 0.5
        yalign 0.5
        xsize 760  # Reduced from 800 to prevent overflow
        ysize 580  # Reduced from 600 to prevent overflow
        
        vbox:
            spacing 30  # Increased spacing between elements
            xalign 0.5
            
            # Title and coins with improved styling
            frame:
                background "#000000"  # Black background
                xalign 0.5
                padding (20, 15)
                
                vbox:
                    spacing 10
                    xalign 0.5
                    
                    text "🏪 ITEM SHOP 🏪" xalign 0.5 size 32 color "#FFCC00" outlines [(3, "#CC6600", 0, 0)]
                    text "Page [pagina_atual]" xalign 0.5 size 24 color "#00CCFF" outlines [(2, "#003366", 0, 0)]
                    text "💰 Coins: [money]" xalign 0.5 size 26 color "#00FF00" outlines [(2, "#006600", 0, 0)]
            
            # Show quantity of stackable items with improved styling
            $ qnt_camisinhas = inventario.count(14)
            $ qnt_nozes = inventario.count(3)
            $ qnt_potes = inventario.count(8)
            
            if qnt_camisinhas > 0 or qnt_nozes > 0 or qnt_potes > 0:
                frame:
                    background "#000000"  # Black background
                    xalign 0.5
                    padding (15, 10)
                    
                    hbox:
                        spacing 40
                        xalign 0.5
                        if qnt_camisinhas > 0:
                            text "🔞 Condoms: [qnt_camisinhas]/5" size 20 color "#FF69B4" outlines [(2, "#CC0066", 0, 0)]
                        if qnt_nozes > 0:
                            text "🥜 Nuts: [qnt_nozes]/10" size 20 color "#DEB887" outlines [(2, "#8B7355", 0, 0)]
                        if qnt_potes > 0:
                            text "🏺 Jars: [qnt_potes]/5" size 20 color "#87CEEB" outlines [(2, "#4682B4", 0, 0)]
            
            # Item grid (3 columns x 2 rows = 6 items per page) - FIXED LAYOUT
            grid 3 2:
                xalign 0.5
                spacing 20  # Reduced spacing to prevent overflow
                xsize 720  # Fixed width to prevent overflow
                
                # Determine which items to show based on current page
                $ inicio = (pagina_atual - 1) * 6
                $ fim = min(pagina_atual * 6 - 1, len(itens_mostrados_loja) - 1)
                
                # Show items from current page
                for i in range(inicio, fim + 1):
                    if i < len(itens_mostrados_loja):  # Safety check
                        $ id_item = itens_mostrados_loja[i]
                        # Create frame for each item - FIXED SIZE
                        frame:
                            xsize 200  # Reduced from 220
                            ysize 160  # Reduced from 180
                            xalign 0.5
                            
                            # Special styling for Map Piece 3
                            if id_item == 30:
                                background "#FFD700"  # Gold background for special item
                            
                            vbox:
                                xalign 0.5
                                yalign 0.5
                                spacing 15
                                
                                # Price with slightly larger font - special color for map piece
                                if id_item == 30:
                                    text "🗺️ Price: [itens_loja[id_item]['preco']] 🗺️" xalign 0.5 size 18 color "#8B0000"
                                else:
                                    text "Price: [itens_loja[id_item]['preco']]" xalign 0.5 size 18
                                
                                # Item name with even larger font - special color for map piece
                                if id_item == 30:
                                    text itens_loja[id_item]["nome"]:
                                        xalign 0.5
                                        text_align 0.5
                                        xmaximum 180  # Reduced from 200
                                        size 18  # Reduced font size
                                        color "#8B0000"  # Dark red for map piece
                                else:
                                    text itens_loja[id_item]["nome"]:
                                        xalign 0.5
                                        text_align 0.5
                                        xmaximum 180  # Reduced from 200
                                        size 20  # Reduced font size
                                
                                # Special description for Map Piece 3
                                if id_item == 30:
                                    if mapa_piece_3_comprado:
                                        text "✅ ALREADY OWNED" xalign 0.5 size 14 color "#006600"
                                    else:
                                        text "🔓 Unlocks new area!" xalign 0.5 size 14 color "#8B0000"
                                
                                # Status for stackable items
                                elif id_item == 14:  # Condom
                                    if qnt_camisinhas >= 5:
                                        text "Maximum reached!" xalign 0.5 size 16 color "#CC0000"
                                    else:
                                        text "Owns: [qnt_camisinhas]/5" xalign 0.5 size 16 color "#0066CC"
                                elif id_item == 3:  # Nuts
                                    if qnt_nozes >= 10:
                                        text "Maximum reached!" xalign 0.5 size 16 color "#CC0000"
                                    else:
                                        text "Owns: [qnt_nozes]/10" xalign 0.5 size 16 color "#0066CC"
                                elif id_item == 8:  # Jellyfish Jar
                                    if qnt_potes >= 5:
                                        text "Maximum reached!" xalign 0.5 size 16 color "#CC0000"
                                    else:
                                        text "Owns: [qnt_potes]/5" xalign 0.5 size 16 color "#0066CC"
                                elif id_item in inventario and id_item not in [3, 8, 14]:  # Other items
                                    text "Already own" xalign 0.5 size 16 color "#CC0000"
                                    
                                # Buy button (disabled if reached maximum or already owned)
                                if id_item == 30 and mapa_piece_3_comprado:  # Map piece already bought
                                    textbutton "✅ OWNED":
                                        action NullAction()
                                        xalign 0.5
                                        text_size 12
                                        text_color "#FFFFFF"
                                        background "#006600"
                                        sensitive False
                                elif id_item == 14 and qnt_camisinhas >= 5:
                                    textbutton "Buy":
                                        action NullAction()
                                        xalign 0.5
                                        text_size 12
                                        sensitive False
                                elif id_item == 3 and qnt_nozes >= 10:
                                    textbutton "Buy":
                                        action NullAction()
                                        xalign 0.5
                                        text_size 12
                                        sensitive False
                                elif id_item == 8 and qnt_potes >= 5:
                                    textbutton "Buy":
                                        action NullAction()
                                        xalign 0.5
                                        text_size 12
                                        sensitive False
                                elif id_item not in inventario or id_item in [3, 8, 14, 30]:
                                    # Special button styling for Map Piece 3
                                    if id_item == 30:
                                        textbutton "🗺️ BUY MAP 🗺️":
                                            action Function(comprar_item, id_item)
                                            xalign 0.5
                                            text_size 10
                                            text_color "#FFFFFF"
                                            background "#8B0000"
                                            hover_background "#CD5C5C"
                                    else:
                                        textbutton "Buy":
                                            action Function(comprar_item, id_item)
                                            xalign 0.5
                                            text_size 12
                                else:
                                    textbutton "Buy":
                                        action NullAction()
                                        xalign 0.5
                                        text_size 12
                                        sensitive False
            
            # Page navigation with improved styling
            frame:
                background "#000000"  # Black background like item frames
                xalign 0.5
                padding (20, 15)
                
                hbox:
                    spacing 80  # Good spacing between buttons
                    xalign 0.5
                    
                    # Previous page button with fixed conditional styling
                    $ cor_texto_anterior = "#00CCFF" if pagina_atual > 1 else "#666666"
                    $ cor_hover_anterior = "#FFFFFF" if pagina_atual > 1 else "#666666"
                    $ cor_fundo_anterior = "#003366" if pagina_atual > 1 else "#222222"
                    $ cor_hover_fundo_anterior = "#0066CC" if pagina_atual > 1 else "#222222"
                    
                    textbutton "◀ Previous":
                        action Function(pagina_anterior) 
                        sensitive pagina_atual > 1
                        text_size 22
                        text_color cor_texto_anterior
                        text_hover_color cor_hover_anterior
                        text_outlines [(2, "#003366", 0, 0)]
                        background cor_fundo_anterior
                        hover_background cor_hover_fundo_anterior
                        xpadding 25
                        ypadding 12
                    
                    # Page indicator
                    text "Page [pagina_atual]/[((len(itens_mostrados_loja) + 5) // 6)]":
                        size 20
                        color "#00CCFF"
                        outlines [(2, "#003366", 0, 0)]
                        yalign 0.5
                    
                    # Next page button with fixed conditional styling
                    $ total_paginas = (len(itens_mostrados_loja) + 5) // 6
                    $ cor_texto_proximo = "#00CCFF" if pagina_atual < total_paginas else "#666666"
                    $ cor_hover_proximo = "#FFFFFF" if pagina_atual < total_paginas else "#666666"
                    $ cor_fundo_proximo = "#003366" if pagina_atual < total_paginas else "#222222"
                    $ cor_hover_fundo_proximo = "#0066CC" if pagina_atual < total_paginas else "#222222"
                    
                    textbutton "Next ▶":
                        action Function(proxima_pagina) 
                        sensitive pagina_atual < total_paginas
                        text_size 22
                        text_color cor_texto_proximo
                        text_hover_color cor_hover_proximo
                        text_outlines [(2, "#003366", 0, 0)]
                        background cor_fundo_proximo
                        hover_background cor_hover_fundo_proximo
                        xpadding 25
                        ypadding 12
            
            # Exit button with improved styling
            frame:
                background "#000000"  # Black background
                xalign 0.5
                padding (15, 10)
                
                textbutton "🚪 Exit Shop":
                    action [SetVariable("hora_do_dia", hora_do_dia + 2), Show("xerequinha"), Jump("explorar_loja")]
                    text_size 26
                    text_color "#FFCC00"  # Gold color for exit
                    text_hover_color "#FFFFFF"
                    text_outlines [(2, "#CC6600", 0, 0)]
                    background "#CC6600"
                    hover_background "#FF9900"
                    xpadding 40
                    ypadding 15