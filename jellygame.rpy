# jellygame.rpy - Jellyfish Hunting Minigame (English)
# Version with jellyfish jelly system and audio

# Control variables
default jogou_minigame_antes = False  # Controls if player already played at least once
default total_geleia_feita = 0  # Total jelly made throughout the game

# Screen configuration for minigame
init -10 python:
    # Jellyfish class
    class AguaViva:
        def __init__(self, x, y, velocidade, visivel=True, id=0):
            self.x = x
            self.y = y
            self.velocidade = velocidade
            self.visivel = visivel
            self.id = id
            self.som_tocado = False  # Controls if sound was already played for this jellyfish
    
    def inicializar_aguas_vivas():
        global ag_pontos, ag_tempo_restante, ag_jogo_ativo, aguas_vivas
        
        # Reset counters
        ag_pontos = 0
        ag_tempo_restante = 10.0
        ag_jogo_ativo = True
        
        # Create jellyfish
        aguas_vivas = []
        for i in range(8):
            fila = i % 4  # 4 rows for 8 jellyfish
            pos_y = 200 + (fila * 180)  # Vertical spacing
            pos_x = -150 - (renpy.random.randint(0, 3) * 150)  # Varied positions
            vel = renpy.random.randint(20, 30)  # Speeds
            aguas_vivas.append(AguaViva(pos_x, pos_y, vel, True, i))
    
    def atualizar_aguas_vivas():
        global aguas_vivas
        for q in aguas_vivas:
            if q.x > config.screen_width:
                # When it leaves screen, return to left
                q.x = -150
                q.visivel = True
                q.som_tocado = False  # Reset sound control
                q.velocidade = renpy.random.randint(20, 30)
            else:
                # Move jellyfish
                q.x += q.velocidade
    
    def clicar_agua_viva(id):
        global aguas_vivas, ag_pontos
        # Mark jellyfish as invisible
        for q in aguas_vivas:
            if q.id == id and q.visivel:
                q.visivel = False
                ag_pontos += 1
                # Play capture sound in separate channel to not interrupt jellyfish sound
                renpy.music.play("whooshnet.mp3", channel="audio", loop=False)
                break
    
    def adicionar_aguas_vivas_capturadas():
        global ag_pontos, inventario
        
        # Add captured jellyfish (ID 21) to inventory
        for i in range(ag_pontos):
            inventario.append(21)
        
        renpy.notify(f"{ag_pontos} jellyfish added to inventory!")
    
    def fazer_geleia_de_aguas_vivas(quantidade=1):
        global inventario, total_geleia_feita
        
        # Check if we have enough jellyfish and jars
        qnt_aguas_vivas = inventario.count(21)  # Jellyfish ID
        qnt_potes = inventario.count(8)  # Jar ID
        
        # Determine how many jellies we can make
        max_geleia = min(qnt_aguas_vivas, qnt_potes, quantidade)
        
        if max_geleia <= 0:
            return 0
            
        # Remove ingredients from inventory
        for i in range(max_geleia):
            inventario.remove(21)  # Remove one jellyfish
            inventario.remove(8)   # Remove one jar
            
        # Add jelly to inventory (ID 22)
        for i in range(max_geleia):
            inventario.append(22)  # Add jellyfish jelly
            
        # Update counter
        total_geleia_feita += max_geleia
        
        return max_geleia
    
    def limpar_telas_aguasvivas():
        # Function to ensure all minigame screens are hidden
        renpy.hide_screen("ag_game_screen")
        renpy.hide_screen("ag_game_info")

# Add jelly item to store dictionary
init 1 python:
    if 22 not in itens_loja:
        itens_loja[22] = {"nome": "Jellyfish Jelly", "preco": 40}

# Minigame variables (independent from main game)
default ag_pontos = 0
default ag_tempo_restante = 10.0
default ag_jogo_ativo = False
default aguas_vivas = []

# Minigame info screen (simple, text only)
screen ag_game_info():
    frame:
        xalign 1.0
        yalign 0.0
        padding (20, 20)
        margin (10, 10)
        background "#00000080"  # Semi-transparent background
        
        vbox:
            spacing 10
            text "Jellyfish: [ag_pontos]" color "#FFFFFF" outlines [(2, "#000000", 0, 0)] size 30
            text "Time: ['{:.1f}'.format(ag_tempo_restante)]s" color "#FFFFFF" outlines [(2, "#000000", 0, 0)] size 30

# Main minigame screen
screen ag_game_screen():
    # Game screen
    if ag_jogo_ativo:
        # Show only jellyfish as buttons
        for q in aguas_vivas:
            if q.visivel:
                imagebutton:
                    idle "jellyfish.png"  # Uses jellyfish.png image
                    xpos q.x
                    ypos q.y
                    action Function(clicar_agua_viva, q.id)

# Entry point for minigame
label minigame_aguasvivas:
    # Hide xerequinha screen
    hide screen xerequinha
    
    # Go to dialogue screen with Fatrick
    jump patrick_jellyfish_intro

# Fatrick asks about hunting net
label patrick_jellyfish_intro:
    # Play jellyfish fields music
    play music "hula.mp3" fadein 1.0
    
    # Fatrick scene with jellyfish background
    if renpy.has_image("jellos"):
        scene jellos
    else:
        scene bg_aguasvivas
        
    # Show Fatrick (assuming you have a "pautrick" image)
    if renpy.has_image("pautrick"):
        show patrick1
    
    p "Hey, Spoogebob Squirtpants! Want to hunt some jellyfish today?"
    
    # If not first time, offer option to make jelly first
    if jogou_minigame_antes and 21 in inventario and 8 in inventario:
        p "Hmm, I see you already have some jellyfish and jars. Want to make jelly before we start?"
        
        menu:
            "Make jelly first":
                $ qnt_aguas_vivas = inventario.count(21)
                $ qnt_potes = inventario.count(8)
                $ max_possiveis = min(qnt_aguas_vivas, qnt_potes)
                
                p "Excellent idea! We have ingredients to make [max_possiveis] jar(s) of jelly."
                p "How many jellies do you want to make?"
                
                menu:
                    "Make one jelly" if max_possiveis >= 1:
                        $ geleia_feita = fazer_geleia_de_aguas_vivas(1)
                        p "Perfect! We made [geleia_feita] jar of delicious jelly!"
                    
                    "Make three jellies" if max_possiveis >= 3:
                        $ geleia_feita = fazer_geleia_de_aguas_vivas(3)
                        p "Wow! We made [geleia_feita] jars of tasty jelly!"
                    
                    "Make all possible jellies" if max_possiveis >= 1:
                        $ geleia_feita = fazer_geleia_de_aguas_vivas(max_possiveis)
                        p "Amazing! We made [geleia_feita] jars of delicious jelly!"
                    
                    "Better not make jelly now":
                        p "Okay, let's just hunt then!"
                
                p "Now let's go hunting!"
            
            "Let's just hunt":
                p "As you wish! Let's hunt then!"
    
    p "Wait a minute... did you bring your jellyfish net?"
    
    # Check if has a net (item ID 7)
    if 7 in inventario:
        p "Ah, great! You have a net. Let's start hunting!"
        jump patrick_start_game
    else:
        p "Oh no! You don't have a hunting net. We can't hunt jellyfish like this."
        p "Go to Mr. Krack's store and buy a net. Come back when you're prepared!"
        
        # Stop music and return to main game
        stop music fadeout 1.0
        show screen xerequinha
        jump room4

# Fatrick explains how to play
label patrick_start_game:
    p "Okay buddy! Let's go! You have 10 seconds to catch as many jellyfish as you can."
    p "Just click on them when they appear on screen. Are you ready?"
    
    menu:
        "I'm ready!":
            p "Great! Let's start!"
            jump start_jellyfish_game
            
        "Wait, I need to prepare better...":
            p "Okay, come back when you're ready to hunt jellyfish!"
            $ hora_do_dia += 2
            # Stop music and return to main game
            stop music fadeout 1.0
            show screen xerequinha
            jump room4

# Start game
label start_jellyfish_game:
    # Switch to game music
    play music "jellygame.mp3" fadein 1.0
    
    # Play jellyfish sound in loop during game
    play sound "jellys.mp3" loop
    
    # Hide Fatrick
    if renpy.has_image("patrick1"):
        hide patrick1
    
    # Background scene
    if renpy.has_image("jellos"):
        scene jellos
    else:
        scene bg_aguasvivas
    
    # Initialize variables
    $ inicializar_aguas_vivas()
    
    # Show game screens
    show screen ag_game_screen
    show screen ag_game_info
    
    # Main game loop
    while ag_tempo_restante > 0 and ag_jogo_ativo:
        # Update jellyfish position
        $ atualizar_aguas_vivas()
        
        # Decrease time
        $ ag_tempo_restante -= 0.05
        
        # Pause to control speed
        $ renpy.pause(0.05, hard=True)
    
    # End game
    $ ag_jogo_ativo = False
    
    # Stop jellyfish sound and game music
    stop sound
    stop music fadeout 1.0
    play music "hula.mp3" fadein 1.0
    
    # Hide info screen
    hide screen ag_game_info
    hide screen ag_game_screen
    
    # Go to final dialogue with Fatrick
    jump patrick_end_game

# Game end
label patrick_end_game:
    # Mark that player already played at least once
    $ jogou_minigame_antes = True
    
    # Show Fatrick again
    if renpy.has_image("pautrick"):
        show pautrick
    
    if ag_pontos == 0:
        p "Wow, Spoogebob Squirtpants, you didn't catch any jellyfish? Maybe you should practice a bit more."
        p "Let's go back home and try another day."
        $ hora_do_dia += 5
        # Stop music and return to main game
        stop music fadeout 1.0
        show screen xerequinha
        jump room4
        
    elif ag_pontos < 5:
        p "You only caught [ag_pontos] jellyfish... Next time try using the net"
    else:
        p "WOW! You caught [ag_pontos] jellyfish! That's incredible!"
    
    # Adding all jellyfish to inventory automatically
    $ adicionar_aguas_vivas_capturadas()
    p "I already stored all the jellyfish you captured in your inventory!"
    
    # Check if we can make jelly
    $ pode_fazer_geleia = 8 in inventario
    
    if pode_fazer_geleia:
        p "How about we make some jellyfish jelly now?"
        
        menu:
            "Make jelly":
                # Count available items
                $ qnt_aguas_vivas = inventario.count(21)
                $ qnt_potes = inventario.count(8)
                $ max_possiveis = min(qnt_aguas_vivas, qnt_potes)
                
                if max_possiveis <= 0:
                    p "Hmm, actually it seems we don't have enough jellyfish or jars. We need at least one of each."
                    p "Let's try again after getting more jellyfish or buying more jars."
                else:
                    p "Great! We have ingredients to make [max_possiveis] jar(s) of jelly."
                    
                    # Menu to choose quantity
                    menu:
                        "Make one jelly" if max_possiveis >= 1:
                            $ geleia_feita = fazer_geleia_de_aguas_vivas(1)
                            p "Perfect! We made [geleia_feita] jar of delicious jelly!"
                        
                        "Make three jellies" if max_possiveis >= 3:
                            $ geleia_feita = fazer_geleia_de_aguas_vivas(3)
                            p "Wow! We made [geleia_feita] jars of tasty jelly!"
                        
                        "Make all possible jellies" if max_possiveis >= 1:
                            $ geleia_feita = fazer_geleia_de_aguas_vivas(max_possiveis)
                            p "Amazing! We made [geleia_feita] jars of delicious jelly!"
                        
                        "Better not make jelly now":
                            p "Alright, we can make jelly later!"
            
            "I don't want to make jelly now":
                p "No problem! We can make jelly another time."
    
    p "What do you want to do now?"
    
    menu:
        "Play with the jellyfish for a bit":
            p "Ah, this is going to be fun, Spoogebob Squirtpants!"
            
            scene jellos with dissolve
            
            if renpy.has_image("pautrick"):
                show patrick1
            
            p "Look how gelatinous and pretty they are!"
            p "Be careful not to get stung!"
            
            "You and Fatrick play with the jellyfish for some time."
            "It's a fun experience and you learn more about their behavior."
            
            p "That was fun! Let's come back another time to play more."
            
        "Let's go":
            p "Okay, let's go."
            p "It was fun, but we have other things to do!"
    
    p "It was a great jellyfish hunting day! Let's go back home."
    
    # Clear screens
    $ limpar_telas_aguasvivas()
    $ hora_do_dia += 5
    
    # Stop music and return to main game
    stop music fadeout 1.0
    show screen xerequinha
    jump room4