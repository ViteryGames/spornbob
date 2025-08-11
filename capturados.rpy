# capturados.rpy - Night Captive Scene (English)

# Initial variables for night script
default bob_desmaiado = False
default dialogo_inicial_exibido = False
default saida_quando_desmaiou = 0
default dia = 1  # New variable to count days
define y = Character("You")

label capturados:
    # Disable map during entire night scene
    $ mapa_disponivel = False
    play music "mimindo.mp3" fadein 2.0
    
    scene locker

    # Check if Spoogebob is unconscious
    if bob_desmaiado and saida <= saida_quando_desmaiou:
        "Spoogebob Squirtpants is still unconscious"
        "He breathes with difficulty, but he's alive"
        jump quanaite
    
    show bob trap night at Transform(xzoom=-1) with hpunch:
        zoom 0.9 xpos 800 ypos 450

    bs "Mmmmhhmmmm mmhm!!!!"
    
    menu:  
        "Knock him out":
            $escolha = "cu"
            jump opbob1
        
        "Talk":
            $escolha = "Talk"
            jump opbob1

        "Leave":
            jump quanaite

label opbob1:
    if escolha == "cu":
        play sound "soco.mp3"
        with hpunch
        "You knocked out Spoogebob Squirtpants"
        "He falls to the floor, unconscious"
        "There's no way to interact with him for now"
        $ bob_desmaiado = True
        $ saida_quando_desmaiou = saida
        jump quanaite
    
    elif escolha == "Talk":
        if bob_desmaiado and saida <= saida_quando_desmaiou:
            "Spoogebob Squirtpants is still unconscious on the floor"
            "Looks like he won't wake up anytime soon"
            jump quanaite
        else:
            # If saida > saida_quando_desmaiou, he woke up the next day
            $ bob_desmaiado = False
        
        # Show initial dialogue only the first time
        if not dialogo_inicial_exibido:
            "You remove the gag from Spoogebob Squirtpants' mouth"
            
            bs "Please, let me go! I didn't do anything wrong!"
            
            y "Shut the fuck up, you yellow piece of shit!"
            
            "You slap Spoogebob Squirtpants in the face"
            
            bs "Ow! Why are you doing this to me?"
            
            y "Because I fucking want to! I spent 15 years locked in a stinking hole, now it's my turn to have fun!"
            
            "Spoogebob Squirtpants trembles, his big eyes full of fear"
            
            $ dialogo_inicial_exibido = True
        
        # Conversation options menu
        jump opbob1_menu_opcoes

# Separate conversation options menu
label opbob1_menu_opcoes:
    menu:
        "What to talk about?"
        
        "Ask about Bikini Bottom":
            y "So this shit here is Bikini Bottom? What a ridiculous name!"
            
            bs "I-it's a really cool place when you get to know it... W-we have the Krusty Krab, Mrs. Puff's Boating School..."
            
            y "I don't give a shit about that crap! I want to know where there's money and where there are people for me to have fun with!"
            
            bs "B-but violence isn't the answer..."
            
            "You laugh threateningly"
            
            y "In prison, violence was the only answer, you idiot!"
            
            menu:
                "Continue talking":
                    jump opbob1_menu_opcoes
                "Go back":
                    jump quanaite
        
        "Intimidate him":
            y "You know what I did to guys like you in prison?"
            
            "You get dangerously close to Spoogebob Squirtpants"
            
            y "First I'd break all the bones in their hands... but you don't even have bones, do you? Too bad..."
            
            "Spoogebob Squirtpants tries to move away, but he's tied up"
            
            bs "P-please... have mercy..."
            
            y "Mercy? MERCY? Nobody had mercy on me when they threw me in that hell!"
            
            "Your voice echoes through the room walls"
            
            menu:
                "Continue talking":
                    jump opbob1_menu_opcoes
                "Go back":
                    jump quanaite
        
        "Tell prison stories":
            y "Let me tell you how I ripped out the eye of the last guy who looked at me wrong..."
            
            "You describe in grotesque detail a scene of extreme violence"
            
            bs "Stop, please! I don't want to hear this!"
            
            y "What? Too sensitive to hear the truth of the real world, little sponge?"
            
            "You laugh seeing the terror in Spoogebob Squirtpants' eyes"
            
            y "And that was just the beginning. Imagine what I did to the guy who stole my lunch..."
            
            menu:
                "Continue talking":
                    jump opbob1_menu_opcoes
                "Go back":
                    jump quanaite
        
        "Knock him out":
            y "I'm already tired of your stupid face!"
            play sound "soco.mp3"
            with hpunch
            
            "You hit Spoogebob Squirtpants violently in the head" with hpunch
            
            "He falls unconscious, his soft yellow form collapsing on the floor"
            
            "There's no way to interact with him for now"
            
            $ bob_desmaiado = True
            $ saida_quando_desmaiou = saida
            jump quanaite

label quanaite:
    $ mapa_disponivel = False

    # Map continues unavailable in quanaite
    scene quartobob noite 

    play music "mimindo.mp3" fadein 2.0

    show batavo1 at Transform(xzoom=-1):
        zoom 1.3 xpos 900 ypos 200 
    
    menu:  
        "Sleep":
            # Here's where we increase the day variable
            scene black with fade
            "You sleep deeply..."
            
            $ dia += 1  # Increment day variable
            $ hora_do_dia = 8      # This sets the time to 8:00 AM
            # Re-enable map when player wakes up
            
            scene quartobob with fade
            "You wake up. It's 8 AM on day [dia]."  # Shows current day
            
            jump room4
        
        "Talk to Spoogebob Squirtpants":
            jump capturados

        "Peek through window":
            jump janela

# MODIFICAÇÃO NO ARQUIVO capturados.rpy
# Substitua a seção "label janela:" por esta versão:

label janela: 
  $ mapa_disponivel = False
  # O mapa continua indisponível
  scene rua1
  
  $ renpy.pause(1)

  # Se estiver pelo menos na noite 2
  if saida >= 2:
    show rua1

    # Verifica se já viu a prostituta pela janela hoje
    if not hasattr(store, "viu_prostituta_janela_dia_{}".format(saida)):
        $ setattr(store, "viu_prostituta_janela_dia_{}".format(saida), False)
    
    $ viu_hoje = getattr(store, "viu_prostituta_janela_dia_{}".format(saida))
    
    if not viu_hoje and not getattr(store, "visitou_puta_dia_{}".format(saida), False):
        show ruap with fade

        "You see a prostitute waiting at the bus stop"
        # Marca como visto hoje
        $ setattr(store, "viu_prostituta_janela_dia_{}".format(saida), True)
        
        # Menu simples - vai direto para comcumbinas (que agora é aleatório)
        menu:
            "Whistle to call the whore":
                "You whistle loudly and wave your arms to get her attention."
                "The prostitute looks at your window and smiles wickedly"
                "She crosses the street and comes towards your house"
                scene quartobob noite
                "A few minutes later..."
                # Vai para comcumbinas (que agora escolhe aleatoriamente)
                jump comcumbinas
                
            "Go back":
                "You decide to not draw attention and go back inside"
                jump quanaite
    else:
        "Nothing to see here"
        jump quanaite
    
  # Se for antes da noite 2
  else:
    "Nothing to see here"     
  
  menu:  
    "Go back":
      jump quanaite