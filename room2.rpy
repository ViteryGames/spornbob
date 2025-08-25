# room2.rpy - Krusty Krotch Restaurant - COM INTEGRAÇÃO DA PÉROLA

define lu = "Squirtward"
default cozinha_mensagem = False
default contador_agridoce = 0  # Counter for jellyfish milking
default molho_agridoce_desbloqueado = False  # Controls if sweet and sour sauce is unlocked
define audio.gozada = "gozada.mp3"

# VARIÁVEIS DA PÉROLA SERÃO DEFINIDAS NO ARQUIVO perola.rpy
# Aqui apenas verificamos se elas existem

# Images for jellyfish "milking" animation
image ordenha_frame1 = "images/ordenha1.png"  # Frame 1: Initial (outside)
image ordenha_frame2 = "images/ordenha2.png"  # Frame 2: Intermediate (going in)
image ordenha_frame3 = "images/ordenha3.png"  # Frame 3: Final (deeper)

# Images for "climax" animation
image gozada_frame1 = "images/gozada1.png"  # Frame 1: Initial climax
image gozada_frame2 = "images/gozada2.png"  # Frame 2: Middle climax
image gozada_frame3 = "images/gozada3.png"  # Frame 3: Final climax

# Milking sequence animation in ATL
image ordenha_sequencia:
    "ordenha_frame1"
    pause 0.05
    "ordenha_frame2"
    pause 0.3
    "ordenha_frame3" 
    pause 0.3
    "ordenha_frame2"
    pause 0.3
    "ordenha_frame1"
    pause 0.05

# Continuous animation that loops
image ordenha_anim:
    "ordenha_frame1"
    pause 0.2
    "ordenha_frame2" 
    pause 0.2
    "ordenha_frame3"
    pause 0.2
    "ordenha_frame2"
    pause 0.2
    repeat

# Images for "climax" animation
image gozada_anim:
    "gozada_frame1"
    pause 0.25
    "gozada_frame2"
    pause 0.25
    "gozada_frame3"
    pause 0.5

# If images don't exist, create placeholders
init python:
    if not renpy.loadable("images/ordenha1.png"):
        renpy.image("ordenha_frame1", Solid("#FF80BF", xsize=300, ysize=300))
    if not renpy.loadable("images/ordenha2.png"):
        renpy.image("ordenha_frame2", Solid("#FFA0CF", xsize=320, ysize=320))
    if not renpy.loadable("images/ordenha3.png"):
        renpy.image("ordenha_frame3", Solid("#FFB0DF", xsize=340, ysize=340))

# FUNÇÃO PARA VERIFICAR SE DEVE ATIVAR DESCOBERTA DA PÉROLA
init python:
    def deve_ativar_descoberta_perola():
        global dia, perola_descoberta_financeira
        return dia >= 12 and not perola_descoberta_financeira

label room2:
    # VERIFICAR SE DEVE ATIVAR A DESCOBERTA DA PÉROLA LOGO AO ENTRAR
    if deve_ativar_descoberta_perola():
        jump descoberta_financeira_perola
    
    scene kk
    "You arrive at the Krusty Krotch" 

    define k = "Mr. Krotch"
    
    show krab a at center with hpunch:
        zoom 0.75

    k "SPOOGEBOB SQUIRTPANTS!!!" 

    k "May I know where you were?"
    menu:
        "I'm not Spoogebob. The real one is tied up at home.":
            $escolha = "truth"
            jump siricas

        "Jerking off":
            $escolha = "punheta"
            jump siricas

        "Banging your mom":
            $escolha = "comituamae"
            jump siricas

        "Banging your sister":
            $escolha = "comituamae"
            jump siricas

        "My snail got sick Mr. Krotch":
            $escolha = "gary"
            jump siricas

label siricas:
    hide krab a
    if escolha == "punheta":  
        show krab happy:
            zoom 0.6 xpos 1000 ypos 400

        k "Alright boy, no problem"

        k "I was your age once, a little jerk increases productivity"

        k "But let me know next time to avoid problems ok?! Don't be like Squirtward who spends hours in the bathroom..."

        hide patrick2
    elif escolha == "comituamae":
        show kradeath

        k "GO FUCK YOURSELF SPOOGEBOB SQUIRTPANTS!!!"

        "Game over"

        return
    elif escolha == "truth":
        show krab4:
            zoom 0.6 xpos 1000 ypos 400 

        k "Holy shit..."
    elif escolha == "gary":
        show krab4:
            zoom 0.5 xpos 1000 ypos 520 

        k "Gee boy, that's too bad..."

        show krab4:
            zoom 0.5 xpos 1000 ypos 520  

        k "How about frying some Krotch Burgers to feel better?"

label cozinha:
    # Hide xerequinha interface during kitchen
    hide screen xerequinha

    scene kitchen 

    show batavo1 at Transform(xzoom=-1):
        zoom 1.5 xpos 700 ypos 30
    
    # SE A PÉROLA ESTIVER NO RESTAURANTE, MOSTRAR ELA OBSERVANDO
    if perola_no_restaurante:
        show pesus :
         xalign -2.2
         yalign 1.2
         zoom 1.3
        "Pearl is watching your every move from the corner..."
        "Her eyes follow everything you do with suspicious intensity."
    
    while True:
        if not cozinha_mensagem:
            "This is the Krusty Krotch kitchen"  
            $ cozinha_mensagem = True 

        # MENU DA COZINHA COM OPÇÃO DA PÉROLA SE ELA ESTIVER PRESENTE
        if perola_no_restaurante:
            menu:
                "Add a secret sauce":
                    $ escolha = "gozo"
                    jump chapa_com_perola

                "Cook with jellyfish sweet and sour sauce" if 21 in inventario:
                    $ escolha = "agridoce"
                    jump ordenhar_aguaviva_com_perola

                "Cook with jellyfish jelly" if 23 in inventario:
                    $ escolha = "geleia"
                    jump chapa_geleia_com_perola
                    
                "Cook with special sauce and pineapple" if 19 in inventario:
                    $ escolha = "abacaxi"
                    jump chapa_abacaxi_com_perola

                "Cook a normal Krotch burger":
                    $ escolha = "burguer"
                    jump chapa_com_perola
                    
                "Talk to Pearl":
                    jump interagir_com_perola_cozinha
        else:
            # MENU NORMAL QUANDO PÉROLA NÃO ESTÁ PRESENTE
            menu:
                "Add a secret sauce":
                    $ escolha = "gozo"
                    jump chapa

                "Cook with jellyfish sweet and sour sauce" if 21 in inventario:
                    $ escolha = "agridoce"
                    jump ordenhar_aguaviva

                "Cook with jellyfish jelly" if 23 in inventario:
                    $ escolha = "geleia"
                    jump chapa_geleia
                    
                "Cook with special sauce and pineapple" if 19 in inventario:
                    $ escolha = "abacaxi"
                    jump chapa_abacaxi

                "Cook a normal Krotch burger":
                    $ escolha = "burguer"
                    jump chapa

# NOVA FUNÇÃO: INTERAGIR COM PÉROLA NA COZINHA
label interagir_com_perola_cozinha:
    hide pesus
    show perola_furiosa at right:
         xalign -2.2
         yalign 1.2
         zoom 1.3
         
    
    prl "Cooking something... special... Spoogebob?"
    prl "I'm watching everything you do..."
    
    menu:
        "Just normal cooking":
            prl "Normal? Nothing about you is normal anymore."
            $ perola_suspeita_nivel += 1
            
        "Mind your own business":
            prl "This IS my business now, you fake!"
            $ perola_suspeita_nivel += 1
            
        "Want to help?":
            prl "Help you? I'm here to WATCH you, not help!"
    
    prl "Continue cooking... I'll be watching."
    
    jump cozinha

# VERSÕES DAS RECEITAS COM REAÇÕES DA PÉROLA
label chapa_com_perola:
    # REAÇÃO DA PÉROLA BASEADA NA ESCOLHA
    if escolha == "gozo":
        hide pesus
        show perola_furiosa at right:
         xalign -2.2
         yalign 1.2
         zoom 1.3
        prl "What kind of sauce is that, Spoogebob?"
        prl "It looks... weird. And smells strange too..."
        
        menu:
            "It's a new recipe I invented":
                prl "Since when do you invent recipes?!"
                prl "The old Spoogebob could barely fry a normal burger!"
                $ perola_suspeita_nivel += 2
                
            "It's a trade secret":
                prl "Trade secret? From who? What kind of trade?"
                prl "You're hiding something, I know it!"
                $ perola_suspeita_nivel += 1
                
            "Don't worry about the details":
                prl "Don't worry?! You used to explain EVERYTHING to me!"
                prl "Now you're all mysterious and secretive!"
                $ perola_suspeita_nivel += 2
    
    elif escolha == "burguer":
        
        prl "At least this looks normal..."
        prl "But your technique is different. More... aggressive."
    
    # CONTINUAR COM A RECEITA NORMAL
    jump chapa

label ordenhar_aguaviva_com_perola:
    hide pesus
    show reclavulva :
         xalign -2.2
         yalign 1.2
         zoom 1.3
    
    prl "WHAT THE HELL ARE YOU DOING TO THAT JELLYFISH?!"
    prl "That's... that's disgusting! And perverted!"
    
    b "It's just extracting the sauce, relax."
    
    prl "EXTRACTING?! IT LOOKS LIKE YOU'RE... YOU'RE..."
    prl "The old Spoogebob would NEVER do something so gross!"
    
    $ perola_suspeita_nivel += 3
    
    # CONTINUAR COM A ORDENHA NORMAL
    jump ordenhar_aguaviva

label chapa_geleia_com_perola:
    
    
    prl "Jellyfish jelly? That's actually... creative."
    prl "But since when are you so creative in the kitchen?"
    
    $ perola_suspeita_nivel += 1
    
    # CONTINUAR COM A RECEITA NORMAL
    jump chapa_geleia

label chapa_abacaxi_com_perola:
    
    
    prl "Pineapple on burgers? That's... different."
    prl "Where did you learn about these combinations?"
    
    $ perola_suspeita_nivel += 1
    
    # CONTINUAR COM A RECEITA NORMAL
    jump chapa_abacaxi

# Label for cooking with special sauce and pineapple
label chapa_abacaxi:
    play audio "grelha.mp3" fadein 2.0

    show chapa

    "You add the secret sauce and fresh pineapple slices to the burgers."
    "The sweet and sour aroma is simply irresistible!"
    
    # Remove one pineapple from inventory
    $ inventario.remove(19)
    
    pause(5)
    
    hide chapa
    
    "Six hours later" 
    $ hora_do_dia += 6
    
    pause(2)
    
    show kk night
    
    show krab happy:
        zoom 0.6 xpos 1000 ypos 400
    
    k "HOLY CRAB, Spoogebob!! These burgers are DIVINE!"
    k "The pineapple gave it a special touch... so sweet... SO PROFITABLE!"
    k "Customers are paying double just to eat more of these!"
    
    $ money += 40
    "You received 40 dollars for the pineapple burger!"
    
    stop music fadeout 3.0 
    $ hora_do_dia = 20
    
    # Show xerequinha screen before leaving
    show screen xerequinha
    
    # Exit using existing label
    jump quanaite

# Label for milking jellyfish to make sweet and sour sauce
label ordenhar_aguaviva:
    scene kitchen
    
    "You take a jellyfish from your pocket and prepare to extract its 'sweet and sour sauce'."
    "Click 20 times on the jellyfish to extract the sauce."
    
    $ contador_agridoce = 0
    
    # Screen to click on jellyfish
    screen ordenhar_screen():
        modal True
        
        # Main frame with jellyfish 
        add "ordenha_frame1" xalign 0.5 yalign 0.5
        
        # Show animation in same position when activated
        if renpy.get_screen("ordenha_animacao"):
            add "ordenha_sequencia" xalign 0.5 yalign 0.5
        
        # Counter at top of screen
        frame:
            xalign 0.5
            yalign 0.1
            padding (20, 10)
            text "Milk: [contador_agridoce]/20" size 30 xalign 0.5
        
        # "Pump" button isolated on right side
        frame:
            xalign 0.9
            yalign 0.5
            padding (10, 10)
            
            textbutton "Pump":
                action [Play("sound", "gozada.mp3"),
                        Show("ordenha_animacao"),
                        SetVariable("contador_agridoce", contador_agridoce + 1),
                        If(contador_agridoce + 1 >= 20, 
                           Hide("ordenhar_screen"), 
                           NullAction())]
                text_size 30
                text_color "#FFFFFF"
                text_hover_color "#FF3366"
                text_outlines [(2, "#990000", 0, 0)]
                background "#DD0000"
                hover_background "#FF0000"
    
    # Screen for animation timer
    screen ordenha_animacao():
        timer 1.0 action Hide("ordenha_animacao")
    
    # Show milking screen
    show screen ordenhar_screen
    
    # Pause until player completes 20 clicks
    $ renpy.pause()
    
    # Screen for climax after completing 20 clicks
    "You're about to extract the sauce!"
    
    menu:
        "Finish":
            # Climax animation
            play sound "gozada.mp3" volume 1.0
            
            show gozada_frame1
            pause 0.3
            
            hide gozada_frame1
            show gozada_frame2
            pause 0.3
            
            hide gozada_frame2
            show gozada_frame3
            pause 0.4
            
            hide gozada_frame3
            
            # Shake effect to intensify the moment
            with hpunch
            with vpunch
            
            "YEAHHHHH!!!"
            
            "You successfully extracted the sweet and sour sauce from the jellyfish!"
            "Now let's cook with it."
    
    # Remove one jellyfish from inventory
    $ inventario.remove(21)
    
    $ escolha = "agridoce"
    $ molho_agridoce_desbloqueado = True
    jump chapa

# Label for cooking with jellyfish jelly
label chapa_geleia:
    play audio "grelha.mp3" fadein 2.0

    show chapa

    "You open the jellyfish jelly jar and spread it over the burgers."
    "The sweet and spicy aroma fills the kitchen."
    
    # Remove one jelly jar from inventory
    $ inventario.remove(23)
    
    pause(5)
    
    hide chapa
    
    "A few hours later" 
    $ hora_do_dia += 6
    
    pause(2)
    
    show kk night
    
    show krab happy:
        zoom 0.6 xpos 1000 ypos 400
    
    k "WOW, Spoogebob! These jellyfish jelly burgers were an absolute success!"
    k "Customers are crazy for them! MONEY, MONEY, MONEY!"
    
    $ money += 30
    "You received 30 dollars for excellent service with jellyfish jelly!"
    
    stop music fadeout 3.0 
    $ hora_do_dia = 20
    
    # Show xerequinha screen before leaving
    show screen xerequinha
    
    # Exit using existing label
    jump quanaite

label chapa:
    play audio "grelha.mp3" fadein 2.0

    show chapa

    if escolha == "burguer":  
        pause(5)

        hide chapa

        "A few hours later" 
        $ hora_do_dia += 6 

        pause(2)

        show kk night

        show krab happy:
            zoom 0.6 xpos 1000 ypos 400

        k "Go home boy, and try harder tomorrow, customers are complaining the taste is crap."
        
        k "Not that I care about that if it's once in a while, but if you keep this pace I'll lose MONEY- I mean my beloved customers."
        
        # Show xerequinha screen before leaving
        show screen xerequinha
        
        # Use existing label
        jump quanaite

    elif escolha == "gozo":
        show molho

        pause(2)

        show molho2

        pause(2)

        show molho3
        
        "You added the SECRET SAUCE to all the Krotch Burgers"

        pause(2)

        "A few hours later"
        $ hora_do_dia += 6  

        stop audio fadeout 2.0

        show kk night

        show krab happy:
            zoom 0.6 xpos 1000 ypos 400

        k "Go home boy, and keep this new recipe, customers are loving it!"

        # Generate random reward between 8 and 15 for secret sauce
        $ recompensa = renpy.random.randint(8, 15)
        $ money += recompensa
        "You received [recompensa] dollars for great service!"
        
        stop music fadeout 3.0 
        $ hora_do_dia = 20
        
        # Show xerequinha screen before leaving
        show screen xerequinha
        
        # Exit using existing label
        jump quanaite

    elif escolha == "agridoce":
        show gozojam1

        pause(2)

        show gozojam2

        pause(2)

        show gozojam3
        
        "You added the JELLYFISH SWEET AND SOUR SAUCE to all the crab burgers"

        pause(2)

        "A few hours later"
        $ hora_do_dia += 6  

        stop audio fadeout 2.0

        show kk night

        show krab happy:
            zoom 0.6 xpos 1000 ypos 400

        k "Damn, Spoogebob! This jellyfish sweet and sour sauce is fantastic!"
        k "Customers are asking for more! Keep it up and I'll get rich... I mean, we'll get rich together!"

        # Generate random reward between 8 and 25 for sweet and sour sauce
        $ recompensa = renpy.random.randint(8, 25)
        $ money += recompensa
        "You received [recompensa] dollars for service with sweet and sour sauce!"
        
        stop music fadeout 3.0 
        $ hora_do_dia = 20
        
        # Show xerequinha screen before leaving
        show screen xerequinha
        
        # Exit using existing label
        jump quanaite

    if nugget: 
        k "I see someone ate your ass boy..."

    menu: 
        "Leave":
            # Show xerequinha screen before leaving
            show screen xerequinha
            call screen mapScreen

label caixakk:
    scene caixa kk lula

    lu "Well, I guess since I'm the only being with positive IQ in this hellhole of a city, I'll have to ask"
    
    show lula com vc

    lu "Who are you and where is that little square sissy?"

    menu:
        "I don't know what you're talking about, I am him!":
            $ escolha = "mentiu"
            jump luleta

        "Ignore (screw it, it's Squirtward)":
            $ escolha = "mentiu"
            jump luleta

label luleta:              
    if escolha == "mentiu":  
        pause(3)

        show caixa kk lula
        lu "Whatever, I only come here to use the gloryhole anyway"
        jump cozinha

# LOBBY SEM A VERIFICAÇÃO DA PÉROLA (já foi movida para room2)
label lobbykk: 
    play music "siricracudo.mp3" fadein 2.0

    screen lobbykk: 
        add "lobbykrab.png"  
        on "show" action Play("music", "siricracudo.mp3", fadein=2.0)
        use xerequinha 

        imagebutton:
            xpos 920
            ypos 230
            idle "barco pirusco idle.png"
            hover "barco pirusco.png" 
            action Jump("caixakk")  

        imagebutton:
            xpos 1170
            ypos 200
            idle "porta kk idle.png"
            hover "porta kk hover.png" 
            action Jump("cozinha")     

        imagebutton:
            xpos 263
            ypos 200
            idle "porta kk idle.png"
            hover "porta kk hover.png" 
            action Jump("sala_siririca")
            
        # NOVO BOTÃO PARA INTERAGIR COM A PÉROLA (só aparece se ela estiver no restaurante)
        if perola_no_restaurante:
            imagebutton:
                xpos 20
                ypos 300
                idle "perola_button_idle.png"
                hover "perola_button_idle.png"
                action Jump("interagir_com_perola")

label banheirao: 
    scene banheirao 

    k "My d*** is soft today damn.."

    menu: 
        "Go back":
            call screen lobbykk with fade

default visitou_sala_siririca = False

label sala_siririca:
    scene tutinha
    play music "siricracudo.mp3" fadein 2.0
    
    if not visitou_sala_siririca:
        "You enter Mr. Krotch's office"
        
        show krab a at center with fade:
            zoom 0.75
        
        k "What do you want now boy? Can't you see I'm BUSY COUNTING MY MONEY... I mean, doing the restaurant's accounting!"
        $ visitou_sala_siririca = True
    else:
        show krab fine at center with fade:
            zoom 0.75

    jump menu_principal_siririca