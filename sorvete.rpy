# sorvete.rpy - Ice Cream Mini-Game System (English) - FINAL FIXED VERSION

# Ice cream mini-game variables
default ice_cream_active = False
default pedidos_corretos = 0
default pedidos_totais = 0
default pedido_atual = ""
default tempo_sorvete = 12.0  # 12 seconds per round
default ingredientes_pedido = []
default ingredientes_escolhidos = []
default trabalhos_sorvete_feitos = 0
default ultimo_dia_trabalho_sorvete = -1
default tempo_acabou = False
default lou_ja_enganou = False  # Track if Lou already tricked player

# Homemade ice cream variables
default sorvetes_caseiros = {}  # Dictionary to track homemade ice creams by day
default fazendo_sorvete_caseiro = False  # Track if making homemade ice cream

# Ice cream ingredients
default ingredientes_disponiveis = ["vanilla", "chocolate", "strawberry", "nuts", "whipped_cream", "cherry"]

# Function to check if can work at ice cream today
init python:
    def pode_trabalhar_sorvete_hoje():
        global ultimo_dia_trabalho_sorvete, dia
        return ultimo_dia_trabalho_sorvete != dia
    
    # Function to clean ice cream screens
    def limpar_telas_sorvete():
        renpy.hide_screen("sorvete_ingredientes_screen")
        renpy.hide_screen("quick_menu")
        # Force refresh
        renpy.restart_interaction()
    
    # Timer functions for ice cream mini-game (FIXED)
    def iniciar_timer_sorvete():
        global tempo_sorvete, tempo_acabou
        tempo_sorvete = 12.0
        tempo_acabou = False
    
    def atualizar_timer_sorvete():
        global tempo_sorvete, tempo_acabou
        tempo_sorvete -= 0.1
        if tempo_sorvete <= 0:
            tempo_sorvete = 0
            tempo_acabou = True
            # CRITICAL FIX: Use renpy.restart_interaction() to force screen update
            renpy.hide_screen("sorvete_ingredientes_screen")
            renpy.restart_interaction()
            # Return to main flow
            renpy.jump("sorvete_timeout_handler")
    
    # Customer messages
    def obter_mensagem_cliente():
        import random
        clientes = [
            "A muscular fish approaches the stand!",
            "A family of seahorses wants ice cream!",
            "A bodybuilder crab needs a cool treat!",
            "A group of young fish are excited for dessert!",
            "An elegant mermaid swims up to order!",
            "A hungry starfish rolls up to the counter!",
            "I don't know what the fuck that is but it wants some ice cream",
            "Your fat fucking mom is hungry for cream!",
            "A sexy looking fish is looking for some creamy goods",
            "JackSepticTide is wishing you a good morning",
            "Sharkplier wants to lick something from you",
            "Kai Seanat is hyped to taste that ice cream!",
            "A really big fish approaches the stand!",
            "Pokimane fish version opens her mouth and sticks her tongue out, ready for your goods!"
        ]
        return random.choice(clientes)
    
    # Homemade ice cream functions
    def fazer_sorvete_caseiro(tipo):
        global sorvetes_caseiros, dia
        if dia not in sorvetes_caseiros:
            sorvetes_caseiros[dia] = []
        sorvetes_caseiros[dia].append(tipo)
    
    def verificar_sorvetes_prontos():
        global sorvetes_caseiros, dia, inventario
        dia_anterior = dia - 1
        if dia_anterior in sorvetes_caseiros:
            sorvetes_prontos = sorvetes_caseiros[dia_anterior]
            for sorvete in sorvetes_prontos:
                if sorvete == "leite":
                    inventario.append(101)  # Milk ice cream ID
                elif sorvete == "manga":
                    inventario.append(102)  # Mango ice cream ID
            # Remove from pending list
            del sorvetes_caseiros[dia_anterior]
            return len(sorvetes_prontos)
        return 0

# Ice cream stand images
image batavopraia = "images/batavopraia.png"
image sorvete_area = "images/sorvete_area.png"
image lou = "images/lou.png"

# Define Lou character
define lou = Character("Lou (Angry Employee)", who_color="#8B0000")

# Animation definitions for ice cream ingredients
image sorvete_vanilla = "images/sorvete_vanilla.png"
image sorvete_chocolate = "images/sorvete_chocolate.png"  
image sorvete_strawberry = "images/sorvete_strawberry.png"
image sorvete_nuts = "images/sorvete_nuts.png"
image sorvete_whipped = "images/sorvete_whipped.png"
image sorvete_cherry = "images/sorvete_cherry.png"
image cliente_feliz = "images/cliente_feliz.png"
image cliente_bravo = "images/cliente_bravo.png"

# Homemade ice cream animations (2 frames each)
image sorvete_leite_frame1 = "images/sorvete_leite_1.png"    # Milk ice cream frame 1
image sorvete_leite_frame2 = "images/sorvete_leite_2.png"    # Milk ice cream frame 2
image sorvete_manga_frame1 = "images/sorvete_manga_1.png"    # Mango ice cream frame 1
image sorvete_manga_frame2 = "images/sorvete_manga_2.png"    # Mango ice cream frame 2

# Homemade ice cream animations (ATL)
image sorvete_leite_anim:
    "sorvete_leite_frame1"
    pause 1.0
    "sorvete_leite_frame2"
    pause 1.0
    repeat

image sorvete_manga_anim:
    "sorvete_manga_frame1"
    pause 1.0
    "sorvete_manga_frame2"
    pause 1.0
    repeat

# Ice cream area main label
label area_sorvete:
    # Clean any leftover screens
    $ limpar_telas_sorvete()
    
    scene sorvete_area
    
    
    # First time meeting Lou (he tricks the player)
    if not lou_ja_enganou:
        "You approach the ice cream stand and see an angry-looking employee."
        
        show lou at center
        
        lou "Ugh! FINALLY someone shows up!"
        lou "I've been working this damn stand all day and I'm SICK of it!"
        
        b "What's your problem, dude?"
        
        lou "My problem? I'll tell you my problem!"
        lou "The boss makes me work double shifts, customers are annoying as hell..."
        lou "And I haven't had a break in HOURS!"
        
        menu:
            "Well that's fucked up":
                lou "EXACTLY! You get it!"
                lou "You know what? You seem like a decent guy..."
                
            "I don't give a fuck!":
                lou "Oh, so you're one of THOSE people, huh?"
                lou "Well, maybe I can change your mind..."
                
            "Why don't you quit?":
                lou "Quit? With this economy? You're funny!"
                lou "But actually, I have a better idea..."
        
        lou "Listen, I'm gonna level with you here..."
        lou "How about YOU take over for me? Just for today!"
        lou "I'll split the tips with you 50/50!"
        
        menu:
            "Alright, I'll help you out":
                lou "YES! You're a lifesaver!"
                
            "What's the catch?":
                lou "No catch! Just serve some customers, make some easy money!"
                lou "It's simple work - even an idiot like you could do it!"
                
            "Go fuck yourself":
                lou "Come ON! I'm desperate here!"
                lou "Fine, fine... you can keep ALL the tips!"
                lou "Just please, PLEASE take over for a few hours!"
        
        lou "Great! just follow the customer orders and work fast!"
        lou "The customers can be real assholes if you're slow!"
        lou "Alright, I'm outta here! Good luck, sucker!"
        
        hide lou with moveoutleft
        
        "Lou quickly walks away, leaving you alone at the stand."
        "You realize you've been tricked into working for free..."
        "But the customers are already approaching!"
        
        $ lou_ja_enganou = True
        
    else:
        "You're back at the ice cream stand that Lou tricked you into working."
        "The stand is abandoned except for you..."
    
    jump menu_sorvete

# Ice cream menu (UPDATED WITH NEW OPTIONS)
label menu_sorvete:
    # Check for ready homemade ice creams from previous day
    $ sorvetes_prontos = verificar_sorvetes_prontos()
    if sorvetes_prontos > 0:
        "You found [sorvetes_prontos] homemade ice cream(s) ready from yesterday!"
        "They've been added to your inventory!"
    
    scene sorvete_area
    show batavopraia:
        xalign 2.1
        yalign 1.2
        zoom 1.2
    
    menu:
        "What do you want to do at the abandoned ice cream stand?"
        
        "Work making ice cream" if pode_trabalhar_sorvete_hoje():
            "Well, since you're here, might as well make some money..."
            "Customers are approaching - time to work!"
            jump trabalhar_sorvete_interativo
            
        "Work making ice cream (already worked today)" if not pode_trabalhar_sorvete_hoje():
            "You already worked here today. The stand needs a break too!"
            jump menu_sorvete
            
        #"Eat ice cream ($2)":
            #if money >= 2:
                #jump comer_sorvete
            #else:
                #"You don't have enough money for ice cream. You need $2."
                #jump menu_sorvete
                
        #"Make homemade ice cream":
            #jump fazer_sorvete_caseiro_menu
            
        "Go to Larry's area":
            $ limpar_telas_sorvete()
            jump area_larry
            
        "Leave ice cream area":
            $ limpar_telas_sorvete()
            jump menu_praia_principal

# Interactive ice cream mini-game
label trabalhar_sorvete_interativo:
    $ ultimo_dia_trabalho_sorvete = dia
    
    scene icecreamo
    show batavopraia:
        xalign 2.1
        yalign 1.2
        zoom 1.2
    
    "Time to serve some customers at this abandoned stand!"
    "You need to serve 3 customers - each one has only 12 seconds patience!"
    "Let's see if you can handle this without Lou..."
    
    # Initialize mini-game variables
    $ pedidos_corretos = 0
    $ pedidos_totais = 0
    $ ice_cream_active = True
    
    jump sorvete_minigame_loop

# FIXED: Separate timeout handler
label sorvete_timeout_handler:
    # This label handles timeout cases
    scene sorvete_area
    show batavopraia:
        xalign 2.1
        yalign 1.2
        zoom 1.2
    
    "⏰ TIME'S UP! ⏰"
    
    show cliente_bravo at left:
             xalign 0.1
             yalign 0.4
             zoom 0.5  

    "Time's up! The customer left angry!"
    "You didn't complete the order in time..."
    pause 2.0
    hide cliente_bravo
    
    # Count as wrong order
    $ pedidos_totais += 1
    
    # Continue the loop
    jump sorvete_minigame_loop

# Ice cream mini-game functions (FIXED)
init python:
    def gerar_pedido_sorvete():
        global pedido_atual, ingredientes_pedido
        import random
        
        num_ingredientes = random.randint(2, 4)
        ingredientes_pedido = random.sample(ingredientes_disponiveis, num_ingredientes)
        pedido_atual = "Customer wants: " + ", ".join(ingredientes_pedido)
        return True
    
    def verificar_pedido_sorvete():
        global pedidos_corretos, pedidos_totais, ingredientes_pedido, ingredientes_escolhidos
        
        # ALWAYS count the order attempt
        pedidos_totais += 1
        
        # Check if order is correct (exact match)
        if set(ingredientes_pedido) == set(ingredientes_escolhidos):
            pedidos_corretos += 1
            return True
        else:
            return False
    
    def reset_pedido_sorvete():
        global ingredientes_escolhidos
        ingredientes_escolhidos = []
    
    def toggle_ingrediente_sorvete(ingrediente):
        global ingredientes_escolhidos
        if ingrediente in ingredientes_escolhidos:
            ingredientes_escolhidos.remove(ingrediente)
        else:
            ingredientes_escolhidos.append(ingrediente)

# Ice cream mini-game loop (FIXED)
label sorvete_minigame_loop:
    # Check if completed 3 rounds
    if pedidos_totais >= 3:
        jump sorvete_minigame_resultado
    
    # Show new customer message
    scene sorvete_area
    show batavo sovrete :
        xalign 2.1
        yalign 1.2
        zoom 1.2
    
    $ mensagem_cliente = obter_mensagem_cliente()
    "[mensagem_cliente]"
    
    # Generate new order and reset
    $ gerar_pedido_sorvete()
    $ reset_pedido_sorvete()
    $ iniciar_timer_sorvete()
    
    "They want: [', '.join(ingredientes_pedido)]"
    "You have 12 seconds to prepare their order!"
    "Round [pedidos_totais + 1]/3 - Score: [pedidos_corretos]/[pedidos_totais]"
    
    # Show ingredient selection screen
    call screen sorvete_ingredientes_screen
    
    # If we reach here, it means player confirmed order (not timeout)
    $ limpar_telas_sorvete()
    
    # Check if it was correct
    $ resultado = verificar_pedido_sorvete()
    
    if resultado:
        show cliente_feliz at left:
             xalign 0.1
             yalign 0.4
             zoom 0.5
        "Customer is happy! Perfect order!"
        "You earned a good tip!"
        pause 1.5
        hide cliente_feliz
    else:
        show cliente_bravo at left:
             xalign 0.1
             yalign 0.4
             zoom 0.5  

        "Customer is angry! Wrong ingredients!"
        "No tip this time..."
        pause 1.5
        hide cliente_bravo
    
    jump sorvete_minigame_loop

# Ice cream ingredients selection screen (FINAL FIXED VERSION)
screen sorvete_ingredientes_screen():
    modal True
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 700
        background "#87CEEB"
        
        vbox:
            xalign 0.5
            spacing 25
            
            text "🍦 ICE CREAM ORDERS 🍦" size 35 xalign 0.5 color "#FF1493" outlines [(2, "#000080", 0, 0)]
            
            # Timer display - FIXED to prevent crashes
            if tempo_sorvete > 0:
                text ("⏰ Time: " + "{:.1f}".format(tempo_sorvete) + "s") size 30 xalign 0.5 color "#FF0000" outlines [(2, "#FFFFFF", 0, 0)]
            else:
                text "⏰ TIME'S UP!" size 30 xalign 0.5 color "#FF0000" outlines [(2, "#FFFFFF", 0, 0)]
            
            text "Customer wants: [', '.join(ingredientes_pedido)]" size 25 xalign 0.5 color "#000080"
            
            text "Selected: [', '.join(ingredientes_escolhidos) if ingredientes_escolhidos else 'None']" size 22 xalign 0.5 color "#008000"
            
            # Ingredient buttons
            grid 3 2:
                spacing 25
                xalign 0.5
                
                for ingrediente in ingredientes_disponiveis:
                    $ cor_texto = "#00FF00" if ingrediente in ingredientes_escolhidos else "#000080"
                    $ cor_fundo = "#90EE90" if ingrediente in ingredientes_escolhidos else "#F0F8FF"
                    $ emoji_map = {
                        "vanilla": "🍨", "chocolate": "🍫", "strawberry": "🍓", 
                        "nuts": "🥜", "whipped_cream": "🍶", "cherry": "🍒"
                    }
                    $ emoji = emoji_map.get(ingrediente, "🍦")
                    
                    textbutton "[emoji] [ingrediente.title()]":
                        action Function(toggle_ingrediente_sorvete, ingrediente)
                        text_color cor_texto
                        text_size 20
                        text_outlines [(1, "#FFFFFF", 0, 0)]
                        xsize 180
                        ysize 80
                        background cor_fundo
                        hover_background "#FFE4E1"
            
            hbox:
                spacing 80
                xalign 0.5
                
                textbutton "✅ Confirm Order":
                    action [Hide("sorvete_ingredientes_screen"), Return(True)]
                    text_size 25
                    text_color "#FFFFFF"
                    text_outlines [(2, "#008000", 0, 0)]
                    xsize 200
                    ysize 60
                    background "#32CD32"
                    hover_background "#228B22"
                
                textbutton "🗑️ Clear Selection":
                    action Function(reset_pedido_sorvete)
                    text_size 25
                    text_color "#FFFFFF"
                    text_outlines [(2, "#800000", 0, 0)]
                    xsize 200
                    ysize 60
                    background "#DC143C"
                    hover_background "#B22222"
    
    # Timer that counts down - ONLY if time hasn't run out
    if not tempo_acabou:
        timer 0.1 action Function(atualizar_timer_sorvete) repeat True

# Ice cream mini-game result
label sorvete_minigame_resultado:
    $ limpar_telas_sorvete()
    $ ice_cream_active = False
    

    
    # Calculate payment based on performance
    if pedidos_corretos == 3:
        show carrinvazio
        $ pagamento = renpy.random.randint(35, 40)
        "PERFECT! All 3 customers were delighted!"
        "Working alone, you managed to satisfy everyone!"
    elif pedidos_corretos == 2:
        show sovrete
        $ pagamento = renpy.random.randint(25, 32)
        "Almost there buddy! 2 out of 3 customers were happy!"
        "Not bad for working without any help!"
    elif pedidos_corretos == 1:
        show dossovretes
        $ pagamento = renpy.random.randint(18, 25)
        "Eehsh! Only 1 satisfied customer."
        "I don't think you have what it takes..."
    else:
        $ pagamento = renpy.random.randint(12, 18)
        "Rough day... No customers were satisfied."
        "Maybe Lou was right about this being harder than it looks..."
    
    "Final Score: [pedidos_corretos]/3 orders correct!"
    "You found $[pagamento] in tips that customers left!"
    
    $ money += pagamento
    $ hora_do_dia += 3
    $ trabalhos_sorvete_feitos += 1
    
    # Bonus for multiple days worked
    if trabalhos_sorvete_feitos >= 5:
        "You've become really good at running this stand alone!"
        "You found some extra tips hidden under the counter!"
        $ bonus = 8
        $ money += bonus
        "You found an extra $[bonus]!"
    
    $ quick_menu = True
    
    jump menu_sorvete

# NEW: Eat ice cream option
label comer_sorvete:
    $ money -= 2
    
    scene sorvete_area
    show batavopraia:
        xalign 2.1
        yalign 1.2
        zoom 1.2
    
    "You decide to treat yourself to some ice cream!"
    "You grab a vanilla cone from the freezer and enjoy it."
    "The cold, creamy sweetness is refreshing on this beach day."
    "It takes you about an hour to slowly savor the ice cream."
    
    $ hora_do_dia += 1
    "You feel satisfied and a bit cooler now!"
    
    jump menu_sorvete

# NEW: Homemade ice cream menu
label fazer_sorvete_caseiro_menu:
    scene sorvete_area
    show batavopraia:
        xalign 2.1
        yalign 1.2
        zoom 1.2
    
    "You decide to make some homemade ice cream using the stand's equipment."
    "You can make it with different flavors and it will be ready tomorrow!"
    "What flavor do you want to make?"
    
    menu:
        "Milk ice cream":
            jump fazer_sorvete_leite
            
        "Mango ice cream":
            jump fazer_sorvete_manga
            
        "Never mind":
            jump menu_sorvete

# NEW: Make milk ice cream
label fazer_sorvete_leite:
    scene sorvete_area
    show batavopraia:
        xalign 2.1
        yalign 1.2
        zoom 1.2
    
    "You start making delicious milk ice cream!"
    "First, you gather fresh milk and cream..."
    
    # Show first frame of animation
    show sorvete_leite_frame1 at center
    "You pour the milk into the ice cream maker..."
    pause 1.5
    
    # Show second frame of animation
    hide sorvete_leite_frame1
    show sorvete_leite_frame2 at center
    "You add sugar and vanilla, mixing everything together..."
    pause 1.5
    
    # Show animation loop for a bit
    hide sorvete_leite_frame2
    show sorvete_leite_anim at center
    "The ice cream maker churns the mixture slowly..."
    "You watch as it gradually thickens into creamy ice cream!"
    pause 3.0
    
    hide sorvete_leite_anim
    
    "You pour the mixture into a container and put it in the freezer."
    "It will be ready to collect tomorrow!"
    
    $ fazer_sorvete_caseiro("leite")
    $ hora_do_dia += 2  # Takes 2 hours to make
    
    "Homemade milk ice cream will be ready tomorrow!"
    
    jump menu_sorvete

# NEW: Make mango ice cream
label fazer_sorvete_manga:
    scene sorvete_area
    show batavopraia:
        xalign 2.1
        yalign 1.2
        zoom 1.2
    
    "You start making tropical mango ice cream!"
    "First, you gather fresh mangoes and cream..."
    
    # Show first frame of animation
    show sorvete_manga_frame1 at center
    "You blend the mangoes into a smooth puree..."
    pause 1.5
    
    # Show second frame of animation
    hide sorvete_manga_frame1
    show sorvete_manga_frame2 at center
    "You mix the mango puree with cream and sugar..."
    pause 1.5
    
    # Show animation loop for a bit
    hide sorvete_manga_frame2
    show sorvete_manga_anim at center
    "The ice cream maker churns the tropical mixture..."
    "The sweet mango scent fills the air as it thickens!"
    pause 3.0
    
    hide sorvete_manga_anim
    
    "You pour the golden mixture into a container and freeze it."
    "It will be ready to collect tomorrow!"
    
    $ fazer_sorvete_caseiro("manga")
    $ hora_do_dia += 2  # Takes 2 hours to make
    
    "Homemade mango ice cream will be ready tomorrow!"
    
    jump menu_sorvete

# Return to ice cream area from other areas
label voltar_area_sorvete:
    jump area_sorvete