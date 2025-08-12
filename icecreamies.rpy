# ice_cream_gifts.rpy - Gift System for Homemade Ice Creams

# Function to check if player has homemade ice creams
init python:
    def tem_sorvete_leite():
        return 101 in inventario
    
    def tem_sorvete_manga():
        return 102 in inventario
    
    def dar_sorvete_spoogebob(tipo):
        global inventario, money
        if tipo == "leite" and 101 in inventario:
            inventario.remove(101)
            return True
        elif tipo == "manga" and 102 in inventario:
            inventario.remove(102)
            return True
        return False
    
    def dar_sorvete_sandy(tipo):
        global inventario, money, pontos_interesse_sandy
        if tipo == "leite" and 101 in inventario:
            inventario.remove(101)
            pontos_interesse_sandy += 5
            atualizar_nivel_interesse()
            return True
        elif tipo == "manga" and 102 in inventario:
            inventario.remove(102)
            pontos_interesse_sandy += 8  # Mango gives more points (tropical theme)
            atualizar_nivel_interesse()
            return True
        return False

# Add these labels to capturados.rpy in the Spoogebob interaction menu:

# Label to give ice cream to Spoogebob (add this to capturados.rpy)
label dar_sorvete_spoogebob_menu:
    if tem_sorvete_leite() or tem_sorvete_manga():
        menu:
            "What ice cream do you want to give to Spoogebob?"
            
            "Give milk ice cream" if tem_sorvete_leite():
                $ resultado = dar_sorvete_spoogebob("leite")
                if resultado:
                    "You give the homemade milk ice cream to Spoogebob."
                    bs "Mmm! This is delicious! Thank you!"
                    bs "It tastes so much better than store-bought!"
                    "Spoogebob seems happier, but he's still tied up..."
                
            "Give mango ice cream" if tem_sorvete_manga():
                $ resultado = dar_sorvete_spoogebob("manga")
                if resultado:
                    "You give the homemade mango ice cream to Spoogebob."
                    bs "Wow! Tropical flavor! This is amazing!"
                    bs "I've never tasted anything like this!"
                    "Spoogebob's eyes light up with joy, despite his situation..."
                
            "Don't give ice cream":
                "You decide to keep the ice cream for now."
        
        jump opbob1_menu_opcoes
    else:
        "You don't have any homemade ice cream to give."
        jump opbob1_menu_opcoes

# Update the conversation menu in capturados.rpy to include ice cream option:
# Add this option to the menu in label opbob1_menu_opcoes:
#
#        "Give homemade ice cream" if tem_sorvete_leite() or tem_sorvete_manga():
#            jump dar_sorvete_spoogebob_menu

# Add these labels to sandyclaude.rpy for Sandy gifts:

# Label to give ice cream to Sandy (add this to sandyclaude.rpy in presentear_sandy)
label dar_sorvete_sandy_menu:
    if tem_sorvete_leite() or tem_sorvete_manga():
        menu:
            "What homemade ice cream do you want to give to Sandy?"
            
            "Give milk ice cream" if tem_sorvete_leite():
                $ resultado = dar_sorvete_sandy("leite")
                if resultado:
                    show sandy feliz at center
                    sd "Homemade milk ice cream? How thoughtful, Spoogebob!"
                    sd "This is so creamy and delicious! You made this yourself?"
                    sd "I'm impressed! In Texas, we appreciate good homemade treats!"
                    $ money += 3
                    "Sandy gives you $3 for the thoughtful gift!"
                    "Sandy's interest level increased!"
                
            "Give mango ice cream" if tem_sorvete_manga():
                $ resultado = dar_sorvete_sandy("manga")
                if resultado:
                    show sandy feliz at center
                    sd "Mango ice cream! Oh my stars, this is fantastic!"
                    sd "The tropical flavor is perfect for a hot day like this!"
                    sd "You really know how to make a girl happy, partner!"
                    $ money += 5
                    "Sandy gives you $5 for the amazing gift!"
                    "Sandy's interest level increased significantly!"
                
            "Don't give ice cream":
                "You decide to keep the ice cream for yourself."
        
        jump finalizar_sandy
    else:
        "You don't have any homemade ice cream to give."
        jump finalizar_sandy

# Instructions for implementation:
# 1. Add the ice cream gift option to Sandy's present menu in sandyclaude.rpy
# 2. Add the ice cream gift option to Spoogebob's interaction menu in capturados.rpy
# 3. Make sure the barg.rpy update is included so the items show in inventory