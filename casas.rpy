# casas.rpy - House Selection System (English)

label casas:
    # Make sure the bobCasas screen is displayed
    call screen bobCasas

# House selection screen with xerequinha screen included
screen bobCasas:
    add "bg room1.jpg"
    
    # Add xerequinha screen to show day information
    use xerequinha
    
    # House buttons
    imagebutton:
        xpos 1300
        ypos 180
        idle "abacaxi idle.png"
        hover "abacaxi.png" 
        # Modification: check time before going home
        action Jump("verificar_horario_casa") 

    imagebutton:
        xpos 735
        ypos 195
        idle "lulah idle.png"
        hover "lulah hover.png" 
        action Show("casa_trancada_message")
        

    imagebutton:
        xpos 220
        ypos 510
        idle "preda idle.png"
        hover "preda hover.png" 
        action Jump("preda")

# New label to check time before going home
label verificar_horario_casa:
    # If it's after 8 PM, go directly to quanaite
    if hora_do_dia >= 20:
        # Disable map when entering house
        $ mapa_disponivel = False
        jump quanaite
    else:
        # During the day, go to living room normally
        jump salabob

# Message when trying to enter Squirtward's house
screen casa_trancada_message():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 300
        background "#336699"
        
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            text "The house is locked!" size 40 color "#FF9977" xalign 0.5 outlines [(2, "#CC6644", 0, 0)]
            text "Seems like Squirtward is not home\nor doesn't want to receive visitors." size 25 color "#FFFFFF" xalign 0.5 outlines [(1, "#003366", 1, 1)]
            
            textbutton "Close":
                action Hide("casa_trancada_message")
                xalign 0.5
                text_size 30
                text_color "#FFFFFF"
                text_hover_color "#FFFF99"
                text_outlines [(2, "#990000", 0, 0)]
                background "#DD3366"
                hover_background "#FF5588"

label room1: 
 call screen bobCasas 