# sandyfucks.rpy - Sandy Sexual Content (English)

# Animations for Sandy scenes
image sandy_peitos:
    "images/sandy_peitos.png"
    zoom 1.0
    xalign 0.5
    yalign 0.5

# Animations for handjob - Normal version
image sandy_punheta_anim:
    "images/sandy_punheta_1.png"
    pause 0.4  # Normal rhythm
    "images/sandy_punheta_2.png"
    pause 0.4
    "images/sandy_punheta_3.png"
    pause 0.4
    repeat

# Animations for handjob - Fast version (climax)
image sandy_punheta_anim_rapida:
    "images/sandy_punheta_1.png"
    pause 0.15  # Faster rhythm
    "images/sandy_punheta_2.png"
    pause 0.15
    "images/sandy_punheta_3.png"
    pause 0.15
    repeat

# Animations for blowjob - Normal version
image sandy_boquete_anim:
    "images/sandy_boquete_1.png"
    pause 0.35
    "images/sandy_boquete_2.png"
    pause 0.35
    "images/sandy_boquete_3.png"
    pause 0.35
    repeat

# Animations for blowjob - Fast version (climax)
image sandy_boquete_anim_rapida:
    "images/sandy_boquete_1.png"
    pause 0.15
    "images/sandy_boquete_2.png"
    pause 0.15
    "images/sandy_boquete_3.png"
    pause 0.15
    repeat

# Animations for pussy - Normal version
image sandy_buceta_anim:
    "images/sandy_buceta_1.png"
    pause 0.4
    "images/sandy_buceta_2.png"
    pause 0.4
    "images/sandy_buceta_3.png"
    pause 0.4
    repeat

# Animations for pussy - Fast version (climax)
image sandy_buceta_anim_rapida:
    "images/sandy_buceta_1.png"
    pause 0.2
    "images/sandy_buceta_2.png"
    pause 0.2
    "images/sandy_buceta_3.png"
    pause 0.2
    repeat

# Animations for ass - Normal version
image sandy_cuzinho_anim:
    "images/sandy_cuzinho_1.png"
    pause 0.4
    "images/sandy_cuzinho_2.png"
    pause 0.4
    "images/sandy_cuzinho_3.png"
    pause 0.4
    repeat

# Animations for ass - Fast version (climax)
image sandy_cuzinho_anim_rapida:
    "images/sandy_cuzinho_1.png"
    pause 0.18
    "images/sandy_cuzinho_2.png"
    pause 0.18
    "images/sandy_cuzinho_3.png"
    pause 0.18
    repeat

# Animations for nuts in ass - Normal version
image nozes_cuzinho_anim:
    "images/nozes_cuzinho_1.png"
    pause 0.5
    "images/nozes_cuzinho_2.png"
    pause 0.5
    "images/nozes_cuzinho_3.png"
    pause 0.5
    repeat

# Animations for nuts in ass - Fast version (climax)
image nozes_cuzinho_anim_rapida:
    "images/nozes_cuzinho_1.png"
    pause 0.25
    "images/nozes_cuzinho_2.png"
    pause 0.25
    "images/nozes_cuzinho_3.png"
    pause 0.25
    repeat

# Sound for cumshots
define audio.gozada = "audio/porra.mp3"

# See Sandy's tits (level 1+)
label ver_peitos_sandy:
    # Check if already saw 3 times - if yes, go directly to see quickly
    if vezes_mostrou_peitos >= 3:
        # Check if already performed sexual action today
        if ultimo_dia_acao_sexual == dia:
            show sandy seducao at center
            $ dialogo = obter_dialogo_recusa()
            sd "[dialogo]"
            jump mostrar_menu_sandy
        else:
            jump ver_peitos_rapido
    
    # Check if already performed sexual action today
    if ultimo_dia_acao_sexual == dia:
        show sandy seducao at center
        $ dialogo = obter_dialogo_recusa()
        sd "[dialogo]"
        jump mostrar_menu_sandy
    
    # Mark that sexual action was performed today
    $ ultimo_dia_acao_sexual = dia
    
    # Normal sequence for first times
    # Get dialogue sequence according to progress
    $ indice = min(vezes_mostrou_peitos, 2)
    $ sequencia = obter_sequencia_peitos(indice)
    
    show sandy envergonhada at center
    
    # First dialogue (before showing tits) - only 2 lines
    $ i = 0
    while i < 2 and i < len(sequencia):
        $ item = sequencia[i]
        
        # Check if item is nested list (case of 3rd time variations)
        if isinstance(item, list) and len(item) > 0 and isinstance(item[0], list):
            # If it's a list of variations, choose first variation
            $ item = item[0]
        
        # Now process normally
        if isinstance(item, list) and len(item) >= 2:
            $ quem_fala = item[0]
            $ texto = item[1]
        else:
            $ quem_fala = "sd"
            $ texto = str(item)
        
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "you":
            you "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    # Hide Sandy with clothes
    hide sandy envergonhada
    
    # SHOW TITS - Direct and simple
    show sandynua:
        zoom 0.55
        xalign 0.48
        yalign 0.8
    
    # Pause enough to see the image
    pause 2.0
    
    # Rest of dialogue (after showing tits)
    while i < len(sequencia):
        $ item = sequencia[i]
        
        # Check if item is nested list (case of 3rd time variations)
        if isinstance(item, list) and len(item) > 0 and isinstance(item[0], list):
            # If it's a list of variations, choose first variation
            $ item = item[0]
        
        # Now process normally
        if isinstance(item, list) and len(item) >= 2:
            $ quem_fala = item[0]
            $ texto = item[1]
        else:
            $ quem_fala = "sd"
            $ texto = str(item)
        
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "you":
            you "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    # Hide tits image when dialogue ends
    hide sandynua
    
    # Return to Sandy dressed
    show sandy envergonhada at center
    
    $ vezes_mostrou_peitos += 1
    $ hora_do_dia += 2
    
    # Bonus points only on third time
    if vezes_mostrou_peitos == 3:
        "You've already seen Sandy's tits 3 times! She's much more comfortable with you now."
        $ pontos_interesse_sandy += 20
        $ atualizar_nivel_interesse()
        "Sandy's interest level increased to [nivel_interesse_sandy]!"
    
    jump finalizar_sandy  # Go to interaction end

# See tits quickly (after 3 times)
label ver_peitos_rapido:
    # Mark that sexual action was performed today
    $ ultimo_dia_acao_sexual = dia
    
    show sandy seducao at center
    sd "Want to see my tits again? Here's a quick glimpse..."
    
    # Hide dressed Sandy
    hide sandy seducao
    
    # SHOW TITS - Direct and simple
    show sandynua:
        zoom 0.55
        xalign 0.48
        yalign 0.8
    
    # Pause to see image
    pause 2.0

    # Hide tits
    hide sandynua
    
    # Return to normal scene
    scene bg casa_sandy with dissolve
    show sandy envergonhada at center
    
    sd "Enjoyed the quick view?"
    
    $ hora_do_dia += 2
    jump finalizar_sandy  # Go to interaction end

# See Sandy's pussy (level 5+ and after 3 handjobs)
label ver_buceta_sandy:
    # Check if already saw 3 times - if yes, go directly to see quickly
    if vezes_mostrou_buceta >= 3:
        # Check if already performed sexual action today
        if ultimo_dia_acao_sexual == dia:
            show sandy seducao at center
            $ dialogo = obter_dialogo_recusa()
            sd "[dialogo]"
            jump mostrar_menu_sandy
        else:
            jump ver_buceta_rapido
    
    # Check if already performed sexual action today
    if ultimo_dia_acao_sexual == dia:
        show sandy seducao at center
        $ dialogo = obter_dialogo_recusa()
        sd "[dialogo]"
        jump mostrar_menu_sandy
    
    # Mark that sexual action was performed today
    $ ultimo_dia_acao_sexual = dia
    
    # Show random dialogue before main sequence
    $ dialogo = obter_dialogo_buceta()
    $ quem_fala, texto = dialogo
    if quem_fala == "sd":
        sd "[texto]"
    
    # Show sandyxereta image right after first dialogue
    hide sandy
    show sandyxereta at center
    
    # Pause to give time to view image
    pause 2.0
    
    # Get dialogue sequence according to progress
    $ indice = min(vezes_mostrou_buceta, 2)
    $ sequencia = obter_sequencia_buceta(indice)
    
    # Show complete dialogue sequence (without options menu)
    $ i = 0
    while i < len(sequencia):
        $ quem_fala, texto = sequencia[i]
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "you":
            you "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    # Hide image
    hide sandyxereta
    
    # Return to dressed Sandy
    show sandy satisfeita at center
    
    $ hora_do_dia += 2

    # Increment counter only if hasn't reached 3 yet
    if vezes_mostrou_buceta < 3:    
        $ vezes_mostrou_buceta += 1
        
        # Bonus points only on third time
        if vezes_mostrou_buceta == 3:
            "You've already seen Sandy's pussy 3 times! Your relationship with her is getting more and more intimate."
            $ pontos_interesse_sandy += 25
            $ atualizar_nivel_interesse()
            "Sandy's interest level increased to [nivel_interesse_sandy]!"
    
    jump finalizar_sandy  # Go to interaction end

# See pussy quickly (after 3 times)
label ver_buceta_rapido:
    # Mark that sexual action was performed today
    $ ultimo_dia_acao_sexual = dia
    
    show sandy seducao at center
    sd "Want to see my pussy again? Here's a quick glimpse..."
    
    # Show sandyxereta image
    hide sandy seducao
    show sandyxereta at center
    
    # Pause to give time to view image
    pause 2.0
    
    # Hide image
    hide sandyxereta
    
    # Return to normal scene
    scene bg casa_sandy with dissolve
    show sandy envergonhada at center
    
    sd "Enjoyed the quick view?"
    
    $ hora_do_dia += 2
    jump finalizar_sandy  # Go to interaction end

# Ask for handjob (level 3+)
label punheta_sandy:   
    # Check if already performed sexual action today
    if ultimo_dia_acao_sexual == dia:
        show sandy seducao at center
        $ dialogo = obter_dialogo_recusa()
        sd "[dialogo]"
        jump mostrar_menu_sandy
    
    # Mark that sexual action was performed today
    $ ultimo_dia_acao_sexual = dia
    
    # Get dialogue sequence according to progress
    $ indice = min(vezes_punheta, 2)
    $ sequencia = obter_sequencia_punheta(indice)
    
    # Start with animation immediately
    scene fodasandy
    show sandy_punheta_anim
    
    # Show dialogues while animation is at normal rhythm
    $ i = 0
    while i < 5:  # First 5 dialogues
        $ quem_fala, texto = sequencia[i]
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "you":
            you "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    # Change to faster rhythm and continue dialogues
    hide sandy_punheta_anim
    show sandy_punheta_anim_rapida
    
    # Continue dialogues with faster rhythm
    while i < len(sequencia) - 2:  # -2 to stop before climax
        $ quem_fala, texto = sequencia[i]
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "you":
            you "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    # Cum option - Simplified version
    menu:
        "Cum":
            you "I'm going to cum, Sandy!"
            
            # Hide handjob animation
            hide sandy_punheta_anim_rapida
            
            # Show cum image
            show sandypohadas at center
            
            # First cum with shake and sound
            with hpunch
            play sound audio.gozada
            b "That's right, Sandy! Keep going!"
            
            # Second cum with shake and sound
            with hpunch
            play sound audio.gozada
            "Sandy continues stimulating you while you cum."
            
            # Hide cum image after some time
            $ renpy.pause(2.0)
            hide sandypohadas
    
    # Show satisfied Sandy
    show sandy envergonhada at center
    
    sd "Wow, so much milk! You really enjoyed it, huh?"

    $ vezes_punheta += 1
    $ hora_do_dia += 2

    if vezes_punheta == 3:
        "Sandy has already given you 3 handjobs! She's much more comfortable with intimacies now."
        $ pontos_interesse_sandy += 15
        $ atualizar_nivel_interesse()
        "Sandy's interest level increased to [nivel_interesse_sandy]!"
    
    jump finalizar_sandy  # Go to interaction end

# Blowjob (level 7)
label boquete_sandy:
    # Check if already performed sexual action today
    if ultimo_dia_acao_sexual == dia:
        show sandy seducao at center
        $ dialogo = obter_dialogo_recusa()
        sd "[dialogo]"
        jump mostrar_menu_sandy
    
    # Mark that sexual action was performed today
    $ ultimo_dia_acao_sexual = dia
    
    # Get dialogue sequence according to progress
    $ indice = min(vezes_boquete, 2)
    $ sequencia = obter_sequencia_boquete(indice)
    
    # Start with animation immediately
    scene fodasandy
    show sandy_boquete_anim
    
    # Show dialogues while animation is at normal rhythm
    $ i = 0
    while i < 5:  # First 5 dialogues
        $ quem_fala, texto = sequencia[i]
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "you":
            you "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    # Change to faster rhythm and continue dialogues
    hide sandy_boquete_anim
    show sandy_boquete_anim_rapida
    
    # Continue dialogues with faster rhythm
    while i < len(sequencia) - 2:  # -2 to stop before climax
        $ quem_fala, texto = sequencia[i]
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "you":
            you "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    # Cum option - Simplified version
    menu:
        "Cum":
            you "I'm going to cum, Sandy!"
            
            # Hide blowjob animation
            hide sandy_boquete_anim_rapida
            
            # Show cum image
            show sandypohadas at center
            
            # First cum with shake and sound
            with hpunch
            play sound audio.gozada
            b "That's right! How delicious!"
            
            # Second cum with shake and sound
            with hpunch
            play sound audio.gozada
            "You hold her head while continuing to cum."
            
            # Hide cum image after some time
            $ renpy.pause(2.0)
            hide sandypohadas
    
    # Show satisfied Sandy
    show sandy envergonhada at center
    
    sd "*Glup* *Glup* ... *Cough* *Cough*"
    sd "Wow... this is... different from what I expected."

    $ hora_do_dia += 2
    $ vezes_boquete += 1
    
    if vezes_boquete == 3:
        "Sandy has already given you 3 blowjobs! She's becoming very skilled at this."
        $ pontos_interesse_sandy += 25
        $ atualizar_nivel_interesse()
        "Sandy's interest level increased to [nivel_interesse_sandy]!"
    
    jump finalizar_sandy  # Go to interaction end

# Fuck her pussy (level 10)
label foder_buceta_sandy:
    # Check if already performed sexual action today
    if ultimo_dia_acao_sexual == dia:
        show sandy seducao at center
        $ dialogo = obter_dialogo_recusa()
        sd "[dialogo]"
        jump mostrar_menu_sandy
    
    # Mark that sexual action was performed today
    $ ultimo_dia_acao_sexual = dia
    
    # Get dialogue sequence according to progress
    $ indice = min(vezes_foder_buceta, 2)
    $ sequencia = obter_sequencia_foder_buceta(indice)
    
    # Start with animation immediately
    scene fodasandy
    show sandy_buceta_anim
    
    # Show dialogues while animation is at normal rhythm
    $ i = 0
    while i < 5:  # First 5 dialogues
        $ quem_fala, texto = sequencia[i]
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "you":
            you "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    # Change to faster rhythm and continue dialogues
    hide sandy_buceta_anim
    show sandy_buceta_anim_rapida
    
    # Continue dialogues with faster rhythm
    while i < len(sequencia) - 2:  # -2 to stop before climax
        $ quem_fala, texto = sequencia[i]
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "you":
            you "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    # Cum option - Simplified version
    menu:
        "Cum":
            you "I'm going to cum, Sandy!"
            
            # Hide sex animation
            hide sandy_buceta_anim_rapida
            
            # Show cum image
            show sandypohadas at center
            
            # First cum with shake and sound
            with hpunch
            play sound audio.gozada
            b "That's it! I'm cumming!"
            
            # Second cum with shake and sound
            with hpunch
            play sound audio.gozada
            "You continue fucking while cumming hard."
            
            # Hide cum image after some time
            $ renpy.pause(2.0)
            hide sandypohadas
    
    # Show satisfied Sandy
    show sandy satisfeita at center
    
    sd "Ahhh! I'm feeling everything inside! It's so hot!"
    "Sandy is completely satisfied."

    $ hora_do_dia += 2
    $ vezes_foder_buceta += 1
    
    if vezes_foder_buceta == 3:
        "You've already fucked Sandy's pussy 3 times! You're in perfect sync."
        $ pontos_interesse_sandy += 35
        $ atualizar_nivel_interesse()
        "Sandy's interest level increased to [nivel_interesse_sandy]!"
    
    $ pontos_interesse_sandy += 15
    $ atualizar_nivel_interesse()
    
    jump finalizar_sandy  # Go to interaction end

# Stick nuts in ass (level 15)
label nozes_cuzinho_sandy:
    # Check if already performed sexual action today
    if ultimo_dia_acao_sexual == dia:
        show sandy seducao at center
        $ dialogo = obter_dialogo_recusa()
        sd "[dialogo]"
        jump mostrar_menu_sandy
    
    # Mark that sexual action was performed today
    $ ultimo_dia_acao_sexual = dia
    
    # Get dialogue sequence according to time
    $ indice = min(vezes_nozes_cuzinho, 0)
    $ sequencia = obter_sequencia_nozes_cuzinho(indice)
    
    # Start with animation immediately
    scene bg casa_sandy
    show nozes_cuzinho_anim
    
    # Show dialogues while animation is at normal rhythm
    $ i = 0
    while i < 5:  # First 5 dialogues
        $ quem_fala, texto = sequencia[i]
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "you":
            you "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    # Change to faster rhythm and continue dialogues
    hide nozes_cuzinho_anim
    show nozes_cuzinho_anim_rapida
    
    # Continue dialogues with faster rhythm
    while i < len(sequencia) - 2:  # -2 to stop before climax
        $ quem_fala, texto = sequencia[i]
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "you":
            you "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    # Climax options
    menu:
        "Cum":
            "You masturbate furiously while inserting the nuts."
            
            # Hide nuts animation
            hide nozes_cuzinho_anim_rapida
            
            # Show cum image
            show sandypohadas at center
            
            # First cum with shake and sound
            with hpunch
            play sound audio.gozada
            b "That's it, Sandy! Cum with those nuts in your ass!"
            
            # Second cum with shake and sound
            with hpunch
            play sound audio.gozada
            "You continue masturbating while watching the nuts going into her."
            
            # Complete with last dialogues
            $ i = len(sequencia) - 2
            while i < len(sequencia):
                $ quem_fala, texto = sequencia[i]
                if quem_fala == "sd":
                    sd "[texto]"
                elif quem_fala == "you":
                    you "[texto]"
                else:
                    "[texto]"
                $ i += 1
            
            # Hide cum image after some time
            $ renpy.pause(2.0)
            hide sandypohadas
    
    # Show satisfied Sandy
    show sandy satisfeita at center
    
    $ hora_do_dia += 2
    $ vezes_nozes_cuzinho += 1
    
    # Remove one nut from inventory
    $ inventario.remove(3)
    $ pontos_interesse_sandy += 20
    $ atualizar_nivel_interesse()
    
    if vezes_nozes_cuzinho == 1:
        "Sandy is exploring new pleasures with you!"
        "Sandy's interest level increased to [nivel_interesse_sandy]!"
    
    jump finalizar_sandy  # Go to interaction end

# Fuck Sandy's ass (level 20)
label comer_cuzinho:
    # Check if already performed sexual action today
    if ultimo_dia_acao_sexual == dia:
        show sandy seducao at center
        $ dialogo = obter_dialogo_recusa()
        sd "[dialogo]"
        jump mostrar_menu_sandy
    
    # Mark that sexual action was performed today
    $ ultimo_dia_acao_sexual = dia
    
    # Get dialogue sequence according to progress
    $ indice = min(vezes_cuzinho, 2)
    $ sequencia = obter_sequencia_cuzinho(indice)
    
    # Start with animation immediately
    scene fodasandy
    show sandy_cuzinho_anim
    
    # Show dialogues while animation is at normal rhythm
    $ i = 0
    while i < 5:  # First 5 dialogues
        $ quem_fala, texto = sequencia[i]
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "you":
            you "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    # Change to faster rhythm and continue dialogues
    hide sandy_cuzinho_anim
    show sandy_cuzinho_anim_rapida
    
    # Continue dialogues with faster rhythm
    while i < len(sequencia) - 2:  # -2 to stop before climax
        $ quem_fala, texto = sequencia[i]
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "you":
            you "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    # Cum option - Simplified version
    menu:
        "Cum":
            you "I'm going to cum, Sandy!"
            
            # Hide ass animation
            hide sandy_cuzinho_anim_rapida
            
            # Show cum image
            show sandypohadas at center
            
            # First cum with shake and sound
            with hpunch
            play sound audio.gozada
            b "Take this! I'm cumming a lot!"
            
            # Second cum with shake and sound
            with hpunch
            play sound audio.gozada
            "You continue fucking while releasing jets and more jets."
            
            sd "Ahhhh! It's so hot! How delicious!"
            
            # Hide cum image after some time
            $ renpy.pause(2.0)
            hide sandypohadas
    
    # Show satisfied Sandy
    show sandy satisfeita at center
    
    $ hora_do_dia += 2
    $ vezes_cuzinho += 1
    
    if vezes_cuzinho == 3:
        "You've already fucked Sandy's ass 3 times! Your relationship has reached maximum intimacy level."
        $ pontos_interesse_sandy += 30
        $ atualizar_nivel_interesse()
        "Sandy's interest level increased to [nivel_interesse_sandy]!"
    
    $ pontos_interesse_sandy += 15
    $ atualizar_nivel_interesse()
    
    jump finalizar_sandy  # Go to interaction end