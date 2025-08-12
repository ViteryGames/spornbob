# larry.rpy - Larry the Pornstar Complete System (English)

# Define Larry character
define l = Character("Larry the Pornstar", who_color="#ff4400")

# Variables to track Larry's state
default ja_visitou_larry = False  # Track if already met Larry
default vitorias_arm_wrestling = 0  # Track arm wrestling wins

# Arm wrestling mini-game variables
default arm_wrestling_active = False
default player_clicks = 0
default larry_strength = 0
default game_timer = 0.0

# Larry images
image larry_normal = "images/larry_normal.png"
image larry_flexing = "images/larry_flexing.png"
image larry_angry = "images/larry_angry.png"
image larry_sweating = "images/larry_sweating.png"

# Arm wrestling animations
image arm_wrestling_neutral = "images/arm_neutral.png"
image arm_wrestling_player_winning = "images/arm_player.png"
image arm_wrestling_larry_winning = "images/larryarm.png"
image arm_wrestling_victory = "images/arm_victory.png"
image arm_wrestling_defeat = "images/arm_defeat.png"

# Larry's area
label area_larry:
    scene bg_praia_dia
    
    if not ja_visitou_larry:
        "You approach the muscular red lobster working out."
        $ ja_visitou_larry = True
    
    show larry_normal at center
    
    l "Hey there, dude! Welcome to my workout zone!"
    l "Name's Larry the Pornstar - best bodybuilder in all of Bikini Bottom!"
    
    jump menu_larry

# Larry's menu
label menu_larry:
    scene bg_praia_dia
    show larry_normal at center
    
    menu:
        "What do you want to do with Larry?"
        
        "Talk to Larry":
            jump conversar_larry
            
        "Challenge Larry to arm wrestling ($15 bet)":
            if money >= 15:
                jump desafiar_arm_wrestling
            else:
                show larry_flexing at center
                l "You need at least 15 bucks to bet, dude!"
                l "Come back when you got some real cash!"
                jump menu_larry
            
        "Ask about his nickname":
            jump perguntar_apelido
            
        "Go to ice cream area":
            jump area_sorvete
            
        "Leave Larry's area":
            jump menu_praia_principal

# Conversation with Larry
label conversar_larry:
    $ dialogo_random = renpy.random.randint(1, 4)
    
    if dialogo_random == 1:
        hide larry_normal
        show larry_flexing at center
        l "Dude, this beach is the perfect place to work out and pick up chicks!"
        l "The sand adds extra resistance to every exercise, and the babes love watching!"
        l "You should try doing some squats in the sand sometime, Spoogebob!"
        
    elif dialogo_random == 2:
        show larry_normal at center
        l "You know, Spoogebob, I never expected you to be interested in beach life."
        l "Usually you're all about those Krotch Patties and jellyfish shit!"
        l "But hey, expanding your horizons is totally radical!"
        
    elif dialogo_random == 3:
        hide larry_normal
        show larry_flexing at center
        l "The muscle-building business is booming here at Goo Lagoon!"
        l "All these fish need to stay in shape to impress the ladies!"
        l "Plus, protein shakes are the fucking best!"
        
    else:
        show larry_normal at center
        l "You seem different lately, Spoogebob. More... intense and rough."
        l "I like it! That's the spirit of a true champion!"
        l "Whatever training you're doing in that pineapple, keep it up!"
    
    jump menu_larry

# Ask about nickname
label perguntar_apelido:
    hide larry_normal
    show larry_flexing at center
    
    l "My nickname? Hah! It's because I'm a fucking stud, dude!"
    l "I've banged more fish than you can count!"
    l "The ladies can't resist these muscles and my... performance!"
    
    b "Right... that's... great for you."
    
    l "Damn right it is! Being the best takes dedication in ALL areas!"
    
    jump menu_larry

# Arm wrestling challenge
label desafiar_arm_wrestling:
    $ money -= 15
    
    scene bg_praia_dia
    show larry_flexing at center
    
    l "Alright, Spoogebob! Let's see what you've got!"
    l "This is gonna be fucking intense!"
    
    # Check if player has steroid powder for advantage
    $ tem_po_refice = 24 in inventario  # Item ID 24 for steroid powder
    
    if tem_po_refice:
        "You secretly use some steroid powder before the match..."
        "This should give you extra strength!"
        b "Let's fucking do this, lobster!"
    else:
        b "Bring it on!"
    
    "You sit across from Larry and grip his massive claw."
    "You need to click faster than Larry to win!"
    hide larry_flexing

    # Initialize arm wrestling variables
    $ player_clicks = 0
    $ larry_strength = 0
    $ game_timer = 10.0
    $ arm_wrestling_active = True
    
    # Start arm wrestling mini-game
    jump arm_wrestling_game_start

# Arm wrestling game start - SIMPLIFIED
label arm_wrestling_game_start:
    # Hide the xerequinha interface and dialogue window
    hide screen xerequinha
    window hide
    stop music
    play sound "armwrestle.mp3"
    
    # Show the arm wrestling screen
    show screen arm_wrestling_game
    
    # Wait for player interaction (they will click SHOW RESULTS when ready)
    $ ui.interact()
    
    # This point is reached when player clicks SHOW RESULTS
    # The screen hides itself and jumps to larry_resultados automatically

# Arm wrestling game screen - WITH SHOW RESULTS BUTTON
screen arm_wrestling_game():
    # Show current animation based on who's winning
    if player_clicks > larry_strength + 10:
        add "arm_wrestling_player_winning" xalign 0.5 yalign 0.3
    elif larry_strength > player_clicks + 10:
        add "arm_wrestling_larry_winning" xalign 0.5 yalign 0.3
    else:
        add "arm_wrestling_neutral" xalign 0.5 yalign 0.3
    
    # Clean UI elements positioned directly on screen
    text "CLICK RAPIDLY TO WIN!" size 40 xalign 0.5 ypos 100 color "#FFFF00" outlines [(2, "#000000", 0, 0)]
    
    # Power bars and counters
    hbox:
        spacing 100
        xalign 0.5
        ypos 200
        
        vbox:
            text "Your Power: [player_clicks]" size 25 color "#00FF00" outlines [(2, "#000000", 0, 0)]
            bar value player_clicks range (max(larry_strength + 50, player_clicks + 10)):
                xsize 200
                
        vbox:
            text "Larry's Power: [larry_strength]" size 25 color "#FF0000" outlines [(2, "#000000", 0, 0)]
            bar value larry_strength range (max(player_clicks + 50, larry_strength + 10)):
                xsize 200
    
    # Timer
    text "Time: ['{:.1f}'.format(game_timer)]s" size 30 xalign 0.5 ypos 300 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
    
    # Power button (only show if game is active)
    if game_timer > 0:
        textbutton "POWER!" action Function(add_player_click):
            xalign 0.5
            ypos 400
            text_size 35
            xsize 200
            ysize 80
    
    # SHOW RESULTS button (only appears when time is up)
    if game_timer <= 0:
        textbutton "SHOW RESULTS" action [Hide("arm_wrestling_game"), Jump("larry_resultados")]:
            xalign 0.5
            ypos 400
            text_size 30
            xsize 250
            ysize 80
            background "#FF4400"
            hover_background "#FF6600"
            text_color "#FFFFFF"
    
    # Timer that updates Larry's strength and counts down (FASTER NOW)
    if game_timer > 0:
        timer 0.1 action Function(update_arm_wrestling) repeat True

# Arm wrestling functions
init python:
    def add_player_click():
        global player_clicks, tem_po_refice
        if arm_wrestling_active:
            # Check if player has steroid powder for double power
            if 24 in inventario:  # Steroid powder
                player_clicks += 2  # Double power with steroids
            else:
                player_clicks += 1  # Normal power
    
    def update_arm_wrestling():
        global larry_strength, game_timer, arm_wrestling_active
        import random
        
        if arm_wrestling_active and game_timer > 0:
            # Larry gains strength randomly (FASTER - 60% chance now)
            if random.random() < 0.6:  # 60% chance each tick (was 50%)
                larry_strength += 1
            
            # Countdown timer (FASTER)
            game_timer -= 0.1  # Faster timer tick
            
            # When timer reaches 0, just stop the game
            if game_timer <= 0:
                arm_wrestling_active = False
                game_timer = 0  # Make sure it shows exactly 0

# Results label - Simple results without interface problems
label larry_resultados:
    play music "dabeach.mp3"
    # Simple scene without complex interfaces
    scene bg_praia_dia
    show larry_normal at center
    
    # Show dialogue window again for normal dialogue
    window show
    show screen xerequinha
    
    # Check result and show simple dialogues
    if player_clicks > larry_strength:
        # VICTORY
        hide larry_normal
        show arm_victory at center
        
        # Check if used steroids
        $ tem_po_refice = 24 in inventario
        
        if tem_po_refice:
            $ inventario.remove(24)  # Consume steroid
            l "WHAT THE FUCK MAN! THAT'S IMPOSSIBLE!"
            l "Did you take something?!"
            b "Just training, you weak fag."
            l "Bullshit! Here's your fucking money!"
            "You used one Steroid Powder."
        else:
            l "Fuck dude! You actually beat me!"
            l "You're stronger than you look!"
            b "Pay me up bitch!"
            l "Here's your winnings!"
        
        $ money += 35
        $ vitorias_arm_wrestling += 1
        $ hora_do_dia += 1
        
        "You won $35!"
        
        if vitorias_arm_wrestling >= 3:
            l "You're getting really good at this!"
            l "Here's a bonus!"
            $ money += 10
            "Larry gives you an extra $10!"
    
    elif player_clicks == larry_strength:
        # TIE
        show larry_normal at center
        l "A tie! That's impressive, dude!"
        l "Here's your bet back."
        
        $ money += 15
        $ hora_do_dia += 1
        
        "You got your $15 back!"
    
    else:
        # DEFEAT
        hide larry_normal
        show larry_flexing at center
        l "GET DUNKED ON YOU FAT!!"
        l "I've been training for years!"
        l "Maybe next time, loser!"
        
        b "Damn it..."
        
        $ hora_do_dia += 1
        
        "You lost your $15 bet..."
    
    # Return to beach menu
    jump menu_praia_principal