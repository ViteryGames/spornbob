# barg.rpy - Shop System (English)

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

# Defining the 20 original shop items 
# Adding item 21 (jellyfish) and 22 (jelly) and 23 (jar with jelly) so they can be referenced by inventory
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
    21: {"nome": "Captured Jellyfish", "preco": 25},  # Item added for reference
    22: {"nome": "Jellyfish Jelly", "preco": 40},  # Item added for reference
    23: {"nome": "Jar with Jelly", "preco": 50}       # Item added for reference
}

# List of items that actually appear in the shop
define itens_mostrados_loja = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Function to buy items
init python:
    def comprar_item(id_item):
        global money, inventario
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
        xsize 800
        ysize 600
        
        vbox:
            spacing 30  # Increased spacing between elements
            xalign 0.5
            
            # Title and coins
            text "Item Shop - Page [pagina_atual]" xalign 0.5 size 28  # Increased size
            text "Coins: [money]" xalign 0.5 size 24  # Increased size
            
            # Show quantity of stackable items
            $ qnt_camisinhas = inventario.count(14)
            $ qnt_nozes = inventario.count(3)
            $ qnt_potes = inventario.count(8)
            hbox:
                spacing 30
                xalign 0.5
                if qnt_camisinhas > 0:
                    text "Condoms: [qnt_camisinhas]/5" xalign 0.5 size 22 color "#00CC00"
                if qnt_nozes > 0:
                    text "Nuts: [qnt_nozes]/10" xalign 0.5 size 22 color "#00CC00"
                if qnt_potes > 0:
                    text "Jars: [qnt_potes]/5" xalign 0.5 size 22 color "#00CC00"
            
            # Item grid (3 columns x 2 rows = 6 items per page)
            grid 3 2:
                xalign 0.5
                spacing 30  # Increased spacing between items
                
                # Determine which items to show based on current page
                $ inicio = (pagina_atual - 1) * 6
                $ fim = min(pagina_atual * 6 - 1, len(itens_mostrados_loja) - 1)
                
                # Show items from current page
                for i in range(inicio, fim + 1):
                    $ id_item = itens_mostrados_loja[i]
                    # Create frame for each item
                    frame:
                        xsize 220
                        ysize 180
                        
                        vbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 15
                            
                            # Price with slightly larger font
                            text "Price: [itens_loja[id_item]['preco']]" xalign 0.5 size 18
                            
                            # Item name with even larger font
                            text itens_loja[id_item]["nome"]:
                                xalign 0.5
                                text_align 0.5
                                xmaximum 200
                                size 22  # Increased to 22
                            
                            # Status for stackable items
                            if id_item == 14:  # Condom
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
                                
                            # Buy button (disabled if reached maximum)
                            if id_item == 14 and qnt_camisinhas >= 5:
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
                            elif id_item not in inventario or id_item in [3, 8, 14]:
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
            
            # Page navigation
            hbox:
                spacing 100  # Increased spacing between buttons
                xalign 0.5
                
                # Previous page button
                textbutton "< Previous" action Function(pagina_anterior) sensitive pagina_atual > 1 xpadding 20 ypadding 10  # Increased padding
                
                # Next page button
                $ total_paginas = (len(itens_mostrados_loja) + 5) // 6  # Calculate total number of pages
                textbutton "Next >" action Function(proxima_pagina) sensitive pagina_atual < total_paginas xpadding 20 ypadding 10  # Increased padding
            
            # Button to exit shop
            textbutton "Exit Shop" action [SetVariable("hora_do_dia", hora_do_dia + 2), Show("xerequinha"), Jump("explorar_loja")] xalign 0.5 xpadding 30 ypadding 15  # Increased padding