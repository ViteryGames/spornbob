# plugtonlab.rpy - Plugton's Laboratory System (English) - CLEANED VERSION

# Define Plugton and Karen characters
define plug = Character("Plugton", who_color="#00ff00")
define karen = Character("Karen (Computer Wife)", who_color="#ff00ff")

# Variables to track Plugton's state
default ja_visitou_plugton = False
default pontos_relacionamento_plugton = 0
default nivel_relacionamento_plugton = 0
default palitos_lixo_comprados = 0
default laboratorio_desbloqueado = False
default karen_primeira_vez = False

# Crafting variables
default receitas_desbloqueadas = []
default ultimo_dia_craft = -1

# Images for Plugton areas
image bg_balde_lixo = "images/balde_lixo.png"
image bg_laboratorio = "images/laboratorio_plugton.png"
image plugton_normal = "images/plugton_normal.png"
image plugton_bravo = "images/plugton_bravo.png"
image plugton_feliz = "images/plugton_feliz.png"
image karen_tela = "images/karen_computer.png"

# Add new items to shop dictionary
init 1 python:
    # Add trash sticks to shop
    if 25 not in itens_loja:
        itens_loja[25] = {"nome": "Trash Stick", "preco": 8}
    
    # Add craftable items (not sold in shop)
    if 26 not in itens_loja:
        itens_loja[26] = {"nome": "Reef Powder", "preco": 0}
    if 27 not in itens_loja:
        itens_loja[27] = {"nome": "Jaguar Power", "preco": 0}
    if 28 not in itens_loja:
        itens_loja[28] = {"nome": "Mind Control Serum", "preco": 0}
    if 29 not in itens_loja:
        itens_loja[29] = {"nome": "Fake Krabby Patty Formula", "preco": 0}

# List of items that actually appear in the shop (excludes special items)
define itens_mostrados_loja = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25]

# Function to update relationship level
init python:
    def atualizar_relacionamento_plugton():
        global pontos_relacionamento_plugton, nivel_relacionamento_plugton
        nivel_relacionamento_plugton = pontos_relacionamento_plugton // 10
        if nivel_relacionamento_plugton > 10:
            nivel_relacionamento_plugton = 10
    
    def pode_craftar_hoje():
        global ultimo_dia_craft, dia
        return ultimo_dia_craft != dia
    
    def processar_craft(item_id, ingredientes_necessarios, custo_dinheiro=0):
        global inventario, money, ultimo_dia_craft
        
        # Check if has ingredients
        for ingrediente_id, quantidade in ingredientes_necessarios.items():
            if inventario.count(ingrediente_id) < quantidade:
                return False, f"You need {quantidade} {itens_loja[ingrediente_id]['nome']}"
        
        # Check money
        if money < custo_dinheiro:
            return False, f"You need ${custo_dinheiro}"
        
        # Remove ingredients
        for ingrediente_id, quantidade in ingredientes_necessarios.items():
            for i in range(quantidade):
                inventario.remove(ingrediente_id)
        
        # Remove money
        money -= custo_dinheiro
        
        # Add crafted item
        inventario.append(item_id)
        
        # Mark crafting done today
        ultimo_dia_craft = dia
        
        return True, "Item crafted successfully!"

# External exploration label
label explorar_balde_lixo:
    if hora_do_dia >= 20:
        scene insidecbs
        "The Cum Bucket is closed at night. Even evil schemes need rest."
        
        menu:
            "Go back home":
                jump room4
    else:
        scene insidecbs
        
        if not ja_visitou_plugton:
            "You arrive at the infamous Cum Bucket - Plugton's failed restaurant."
            "The place reeks of rotten food and broken dreams."
            $ ja_visitou_plugton = True
        
        menu:
            "Enter the Cum Bucket":
                jump area_plugton
                
            "Go back to map":
                call screen mapScreen

# Main Plugton area
label area_plugton:
    scene bg_balde_lixo
    
    if not ja_visitou_plugton:
        "You enter the Cum Bucket and immediately regret it."
        "The smell hits you like a truck full of sewage."
        $ ja_visitou_plugton = True
    
    show plugton_normal :
        xalign 0.5
        yalign 0.8
        zoom 0.2
    
    plug "Well, well! If it isn't Spoogebob Squirtpants!"
    plug "Welcome to my shitty establishment! Care to try a delicious Cum Burger?"
    
    jump menu_plugton

# Plugton's main menu
label menu_plugton:
    scene bg_balde_lixo

    show plugton_normal :
        xalign 0.5
        yalign 0.8
        zoom 0.2
    
    # Show current relationship status
    "Relationship with Plugton: [pontos_relacionamento_plugton] points (Level [nivel_relacionamento_plugton])"
    
    menu:
        "What do you want to do with Plugton?"
        
        "Dialogue options":
            jump menu_dialogar_plugton
            
        "Sell items":
            jump vender_itens_plugton
            
        "Talk about creating items" if pontos_relacionamento_plugton >= 30:
            jump falar_criar_itens
            
        "Go to the laboratory" if laboratorio_desbloqueado:
            jump laboratorio_plugton
            
        "Buy trash sticks ($8 each)":
            jump comprar_palitos_lixo
            
        "Leave":
            jump sair_balde_lixo

# Dialogue submenu
label menu_dialogar_plugton:
    scene bg_balde_lixo
    show plugton_normal at center
    
    # Show current relationship status
    "Relationship with Plugton: [pontos_relacionamento_plugton] points (Level [nivel_relacionamento_plugton])"
    
    menu:
        "How do you want to talk to Plugton?"
        
        "Talk normally":
            jump conversar_plugton
            
        "Flatter him":
            jump bajular_plugton
            
        "Insult him":
            jump xingar_plugton
            
        "Provoke him":
            jump provocar_plugton
            
        "Go back":
            jump menu_plugton

# Flatter Plugton
label bajular_plugton:
    $ bajulacao_random = renpy.random.randint(1, 3)
    $ pontos_iniciais = pontos_relacionamento_plugton
    
    hide plugton_normal
    show plugton_feliz at center
    
    if bajulacao_random == 1:
        b "You're such an evil genius, Plugton! Your plans are absolutely diabolical!"
        plug "Finally! Someone who recognizes my fucking brilliance!"
        plug "You have excellent taste in evil masterminds, asshole!"
        $ pontos_relacionamento_plugton += 8
        
    elif bajulacao_random == 2:
        b "This restaurant has such... unique character! Very avant-garde!"
        plug "Avant-garde! Yes! That's exactly what I was going for!"
        plug "Not 'health code violation' like that bastard inspector said!"
        $ pontos_relacionamento_plugton += 7
        
    else:
        b "Your scientific knowledge is incredible! You could rule the world!"
        plug "RULE THE WORLD! Now you're thinking like a true fucking villain!"
        plug "With your appreciation for genius, you could be my right-hand asshole!"
        $ pontos_relacionamento_plugton += 9
    
    $ pontos_ganhos = pontos_relacionamento_plugton - pontos_iniciais
    $ atualizar_relacionamento_plugton()
    
    "You gained [pontos_ganhos] relationship points with Plugton!"
    #"Total relationship: [pontos_relacionamento_plugton] points (Level [nivel_relacionamento_plugton])"
    
    if pontos_relacionamento_plugton >= 30:
        "Plugton considers you a valuable ally! Lab access available!"
    
    jump menu_dialogar_plugton

# Conversation with Plugton
label conversar_plugton:
    $ dialogo_random = renpy.random.randint(1, 5)
    $ pontos_iniciais = pontos_relacionamento_plugton
    
    if dialogo_random == 1:
        show plugton_normal at center
        plug "You know, Spoogebob, you seem different lately..."
        plug "More... fat. Less yellow."
        b "Maybe I'm finally growing up, you anal plug?"
        plug "Growing up? You? HAHAHA! That'll be the goddamn day!"
        $ pontos_relacionamento_plugton += 2
        
    elif dialogo_random == 2:
        show plugton_feliz at center
        plug "I've been working on a new fucking plan to steal the Krabby Patty formula!"
        plug "This time it's foolproof! Well, mostly foolproof, shit!"
        b "What happened to the last 'foolproof' plan, dickhead?"
        plug "We don't talk about Plan Z-47..."
        $ pontos_relacionamento_plugton += 1
        
    elif dialogo_random == 3:
        plug "Business has been fucking terrible lately. Nobody wants to eat chum!"
        plug "I don't understand it! It's perfectly good rotted fish shit!"
        b "Maybe try adding some seasoning, you dumbass?"
        plug "Genius! Why didn't I think of that? You're smarter than you look, asshole!"
        $ pontos_relacionamento_plugton += 3

    elif dialogo_random == 4:
        b "So uh... what's up?"
        plug "What?"
        b "Just trying to make some conversation here"
        plug "Oh ok"
        plug "Not doing much right now..."
        plug "You?"
        b "Nah same"
        $ pontos_relacionamento_plugton += 1    
        
    else:
        plug "Karen's been nagging my ass about the laboratory again."
        plug "She says I need to 'upgrade my equipment' and 'stop using rusty fucking spoons'."
        b "Sounds like good advice, moron."
        plug "Whose side are you on, you piece of shit?!"
        $ pontos_relacionamento_plugton += 1
    
    $ pontos_ganhos = pontos_relacionamento_plugton - pontos_iniciais
    $ atualizar_relacionamento_plugton()
    
    "You gained [pontos_ganhos] relationship points with Plugton!"
    #"Total relationship: [pontos_relacionamento_plugton] points (Level [nivel_relacionamento_plugton])"
    
    if pontos_relacionamento_plugton == 10:
        "Plugton seems to be warming up to you!"
    elif pontos_relacionamento_plugton == 30:
        "Plugton considers you a valuable ally! Lab access available!"
    
    jump menu_dialogar_plugton

# Insult Plugton
label xingar_plugton:
    $ insulto_random = renpy.random.randint(1, 3)
    $ pontos_iniciais = pontos_relacionamento_plugton
    
    hide plugton_normal
    show plugton_bravo at center
    
    if insulto_random == 1:
        b "You're shorter than a sea cucumber's dick!"
        plug "HEY! I'll have you know I'm EVIL-sized, asshole!"
        plug "Size doesn't matter when you have FUCKING INTELLECT!"
        $ pontos_relacionamento_plugton -= 2
        
    elif insulto_random == 2:
        b "Your restaurant smells like a whale's ass after Taco Tuesday!"
        plug "That's... that's actually a compliment! Chum is SUPPOSED to smell like shit!"
        plug "Wait, no! I mean... CURSE YOU, dickwad!"
        $ pontos_relacionamento_plugton -= 1
        
    else:
        b "No wonder nobody eats here. Your food could kill bacteria!"
        plug "IT'S SUPPOSED TO BE DEADLY! That's the fucking point!"
        plug "Though the health inspector disagrees... bastard shut me down twice."
        $ pontos_relacionamento_plugton -= 3
    
    $ pontos_ganhos = pontos_relacionamento_plugton - pontos_iniciais
    $ atualizar_relacionamento_plugton()
    
    "You lost [abs(pontos_ganhos)] relationship points with Plugton!"
    #"Total relationship: [pontos_relacionamento_plugton] points (Level [nivel_relacionamento_plugton])"
    
    jump menu_dialogar_plugton

# Provoke Plugton
label provocar_plugton:
    $ provocacao_random = renpy.random.randint(1, 3)
    $ pontos_iniciais = pontos_relacionamento_plugton
    
    if provocacao_random == 1:
        b "How many times has Mr. Krotch kicked your ass this week, plug?"
        hide plugton_normal
        show plugton_bravo at center
        plug "SEVEN! But who's counting, you fucking dickhead?!"
        plug "Next time will be different! I have a NEW goddamn plan!"
        $ pontos_relacionamento_plugton += 1
        
    elif provocacao_random == 2:
        b "I bet even Patrick could run a better restaurant, you anal disaster."
        plug "PATRICK?! That pink fucking buffoon couldn't run a bath!"
        plug "Although... he did eat 47 Krabby Patties in one sitting..."
        plug "Maybe he knows something about food appeal... shit."
        $ pontos_relacionamento_plugton += 2
        
    else:
        b "What's your success rate? 0.001 percent?"
        plug "It's 0.003 percent, thank you very fucking much!"
        plug "And that's rounded UP, asshole!"
        $ pontos_relacionamento_plugton += 1
    
    $ pontos_ganhos = pontos_relacionamento_plugton - pontos_iniciais
    $ atualizar_relacionamento_plugton()
    
    "You gained [pontos_ganhos] relationship points with Plugton!"
    "Total relationship: [pontos_relacionamento_plugton] points (Level [nivel_relacionamento_plugton])"
    
    jump menu_dialogar_plugton

# Sell items to Plugton
label vender_itens_plugton:
    "What items do you want to sell to Plugton?"
    
    menu:
        "Jellyfish Net - $12 (+5 points)" if 7 in inventario:
            $ inventario.remove(7)
            $ money += 12
            plug "A jellyfish net! Ok I can do some traps with this thing."
            $ pontos_relacionamento_plugton += 5
            $ pontos_ganhos = 5
            jump vender_resultado
            
        "Captured Jellyfish - $2 (+3 points)" if 21 in inventario:
            $ inventario.remove(21)
            $ money += 2
            plug "Excellent! I can use this shit for my new chum recipe!"
            $ pontos_relacionamento_plugton += 3
            $ pontos_ganhos = 3
            jump vender_resultado
            
        "Nuts - $3 (+1 point)" if 3 in inventario:
            $ inventario.remove(3)
            $ money += 3
            plug "Nuts! Karen loves these... I mean, for EVIL fucking purposes!"
            $ pontos_relacionamento_plugton += 1
            $ pontos_ganhos = 1
            jump vender_resultado
            
        "Chocolate - $2 (+1 point)" if 2 in inventario:
            $ inventario.remove(2)
            $ money += 2
            plug "Chocolate! This will make my chum more palatable... shit!"
            $ pontos_relacionamento_plugton += 1
            $ pontos_ganhos = 1
            jump vender_resultado
            
        "Don't sell anything":
            plug "Fine! But come back when you have something useful, dickhead!"
            jump menu_plugton
    
    # If no items available
    plug "You don't have anything I want! Come back when you have something useful, dickhead!"
    jump menu_plugton

# Label for selling result
label vender_resultado:
    $ atualizar_relacionamento_plugton()
    "You sold the item to Plugton!"
    "You gained [pontos_ganhos] relationship points with Plugton!"
    "Total relationship: [pontos_relacionamento_plugton] points (Level [nivel_relacionamento_plugton])"
    
    if pontos_relacionamento_plugton >= 30:
        "Plugton considers you a valuable ally! Lab access available!"
    
    jump menu_plugton

# Buy trash sticks
label comprar_palitos_lixo:
    if money >= 8:
        $ money -= 8
        $ inventario.append(25)
        $ palitos_lixo_comprados += 1
        $ pontos_relacionamento_plugton += 1  # +1 point per trash stick
        $ atualizar_relacionamento_plugton()
        
        plug "One delicious trash stick! Made from 100 percent authentic fucking garbage!"
        plug "You've bought [palitos_lixo_comprados] so far. A loyal customer, asshole!"
        
        "You gained 1 relationship point with Plugton!"
        "Total relationship: [pontos_relacionamento_plugton] points (Level [nivel_relacionamento_plugton])"
        
        if palitos_lixo_comprados == 5:
            plug "Wait a minute... you've bought 5 fucking trash sticks!"
            plug "Either you have terrible taste, or you're up to some shit..."
            plug "I like that in a potential business partner, dickhead!"
            "Progress: You can now ask about creating items if you have 30+ relationship points!"
    else:
        plug "You need $8 for a trash stick! Come back when you're not fucking broke!"
    
    jump menu_plugton

# Talk about creating items
label falar_criar_itens:
    if pontos_relacionamento_plugton < 30:
        plug "Create items? Why would I help YOU with that shit?"
        plug "We're not exactly fucking friends, you know!"
        plug "You need at least 30 relationship points to access my lab, asshole!"
        "Current relationship: [pontos_relacionamento_plugton]/30 points"
        jump menu_plugton
    
    plug "Hmm, creating items, you say? Interesting as fuck..."
    plug "I suppose my laboratory could use a test subject... I mean, assistant, asshole!"
    
    menu:
        "I want to learn evil science!":
            plug "EVIL SCIENCE! Now you're speaking my fucking language!"
            plug "Very well! I'll grant you access to my secret laboratory, dickhead!"
            $ laboratorio_desbloqueado = True
            $ pontos_relacionamento_plugton += 10
            $ atualizar_relacionamento_plugton()
            "You gained 10 relationship points with Plugton!"
            
        "I just want to make useful stuff":
            plug "Useful? How fucking boring! But... I suppose evil and useful can overlap."
            plug "Fine! You can use my lab, but only for EVIL fucking purposes!"
            $ laboratorio_desbloqueado = True
            $ pontos_relacionamento_plugton += 5
            $ atualizar_relacionamento_plugton()
            "You gained 5 relationship points with Plugton!"
            
        "Never mind":
            plug "Coward! Come back when you're ready for REAL fucking science!"
    
    if laboratorio_desbloqueado:
        "LABORATORY ACCESS UNLOCKED!"
        "You can now access Plugton's secret laboratory!"
        "Total relationship: [pontos_relacionamento_plugton] points (Level [nivel_relacionamento_plugton])"
    
    jump menu_plugton

# Plugton's Laboratory
label laboratorio_plugton:
    scene bg_laboratorio
    
    if not karen_primeira_vez:
        "You enter Plugton's secret laboratory hidden beneath the Chum Bucket."
        "The room is filled with bubbling beakers, strange machines, and blinking computers."
        
        show karen_tela at right
        karen "Well, well. What do we have here?"
        karen "Another one of Plugton's 'brilliant' fucking schemes, I suppose?"
        
        plug "Karen! Meet my new... business associate, bitch!"
        plug "He's going to help us with our evil experiments!"
        
        karen "Oh great. Another test subject for your half-baked shit inventions."
        karen "Try not to blow up the lab again, you pathetic plug."
        
        $ karen_primeira_vez = True
    else:
        show karen_tela at right
        karen "Back again? I suppose you didn't learn your fucking lesson last time."
    
    jump menu_laboratorio

# Laboratory menu
label menu_laboratorio:
    scene bg_laboratorio
    show karen_tela at right
    
    menu:
        "What do you want to do in the laboratory?"
        
        "Talk to Karen":
            jump conversar_karen
            
        "Craft items" if pode_craftar_hoje():
            jump menu_craft
            
        "Craft items (already crafted today)" if not pode_craftar_hoje():
            karen "The laboratory equipment is cooling down. Come back tomorrow."
            jump menu_laboratorio
            
        "Learn about recipes":
            jump aprender_receitas
            
        "Go back to Chum Bucket":
            jump menu_plugton

# Exit Chum Bucket
label sair_balde_lixo:
    plug "Leaving so fucking soon? Come back anytime! My door is always open!"
    plug "Mainly because the lock is broken, but still, asshole!"
    
    scene black with dissolve
    "You leave the smelly Chum Bucket..."
    
    jump explorar_balde_lixo