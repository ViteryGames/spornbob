# krustykitchen.rpy - Krusty Krab Kitchen Interactions (English)

label menu_principal_siririca:
    menu:
        "Talk":
            $ escolha = "conversar"
            jump conversa_siririca
            
        "Ask for a raise":
            $ escolha = "aumento"
            # Hide krab a before going to aumento_siririca to avoid overlap
            hide krab a
            jump aumento_siririca
            
        "Ask about Squirtward":
            $ escolha = "molusco"
            # Hide krab a before going to info_molusco to avoid overlap
            hide krab a
            jump info_molusco
            
        "Mess with the secret drawer":
            $ escolha = "gaveta"
            # Hide krab a before going to gaveta_secreta to avoid overlap
            hide krab a
            jump gaveta_secreta
            
        "Go back":
            call screen lobbykk with fade

label conversa_siririca:
    # Hide any previous Mr. Krack before showing a new one
    hide krab a
    hide krab happy
    hide krab4
    
    # Show only krab4 in correct position
    show krab4:
        zoom 0.6 xpos 1000 ypos 400
    
    k "You have five seconds to say what you want. Each second costs money, boy!"
    
    jump menu_conversa_siririca

label menu_conversa_siririca:
    menu:
        "Ask about the Krusty Krotch's history":
            # Hide previous Mr. Krack to avoid overlap
            hide krab4
            show krab happy:
                zoom 0.6 xpos 1000 ypos 400
            
            k "Ah, that's an inspiring story about CAPITALISM AND MONEY!"
            
            k "I started with an old burger, a rusty pan and LOTS OF AMBITION!"
            
            k "And now I have this empire that makes me SO MUCH MONEY HAHAHA"
            
            k "Now get back to work before I change my mind and FIRE you!"
            
            jump menu_conversa_siririca
        
        "Ask about his daughter":
            # Hide any current Mr. Krack before showing another
            hide krab happy
            hide krab4
            show krab a:
                zoom 0.6 xpos 1000 ypos 400
            
            k "Wait, how do YOU know I have a daughter?"
            
            k "Have you been following Pearl around? If I find out you're hitting on her..."
            
            # Hide krab a before showing kradeath
            hide krab a
            show kradeath
            
            k "I'LL STICK THIS CRAB BURGER IN YOUR..."
            
            # Hide kradeath before showing krab a again
            hide kradeath
            show krab a:
                zoom 0.6 xpos 1000 ypos 400
            
            k "Ahem... get back to work, Spoogebob Squirtpants."
            
            jump menu_conversa_siririca
        
        "Talk about the weather":
            # Hide any current Mr. Krack before showing krab4
            hide krab a
            hide krab happy
            show krab4:
                zoom 0.6 xpos 1000 ypos 400
            
            k "The weather? TIME IS MONEY, BOY!"
            
            k "While we're here talking about NOTHING, you could be there frying burgers and MAKING ME PROFIT!"
            
            jump menu_conversa_siririca
        
        "Do something else":
            # Hide any current Mr. Krack before going back
            hide krab happy
            hide krab4
            hide krab a
            
            # Show krab a centered for main menu
            show krab a at center:
                zoom 0.75
            
            jump menu_principal_siririca
            
        "Go back":
            # Hide everything before going back to lobby
            hide krab happy
            hide krab4
            hide krab a
            call screen lobbykk with fade

# Add new default variable to track if potato promotion idea was already suggested
default sugeriu_promocao_batata = False

label aumento_siririca:
    # Hide any current Mr. Krack before showing kradeath
    hide krab a
    hide krab4
    hide krab happy
    
    # Show kradeath in appropriate position
    show kradeath
    
    k "HAHAHAHAHAHA!"
    
    # Hide kradeath before showing krab4
    hide kradeath
    show krab lsmile:
        zoom 0.6 xpos 1000 ypos 400
    
    k "That was a good one, boy. RAISE? At the Krusty Krotch?"
    
    menu:
        "Insist on the raise":
            # Hide krab4 before showing kradeath
            hide krab lsmile
            show kradeath
            
            k "LISTEN HERE YOU USELESS PIECE OF SPONGE!"
            
            k "I CAN REPLACE YOU WITH ANY OCEAN PARASITE!"
            
            k "Now get back to the kitchen before I FIRE you!"
            
            $ money -= 5
            "Mr. Krack fined you 5 dollars for insubordination!"
            
            # Hide kradeath before returning to menu
            hide kradeath
            jump menu_principal_siririca
        
        "Offer to work more hours":
            # Hide krab4 before showing krab happy
            hide krab4
            show krab happy:
                zoom 0.6 xpos 1000 ypos 400
            
            k "NOW WE'RE SPEAKING THE SAME LANGUAGE!"
            
            k "Working FOR FREE after hours? THAT'S what I call team spirit!"
            
            k "Keep it up and maybe I'll think about giving you a 0.1 raise next century!"
            
            $ money += 2
            "You earned 2 dollars as 'incentive'!"
            
            # Hide krab happy before returning to menu
            hide krab happy
            jump menu_principal_siririca
        
        # Option only appears if not suggested yet
        "Suggest a 'Bring your potato and pay 2x more' promotion" if not sugeriu_promocao_batata:
            # Hide krab4 before showing krab happy
            hide krab4
            show krab happy:
                zoom 0.6 xpos 1000 ypos 400
            
            k "MY GOD! You're a GENIUS, boy!"
            
            k "Make them bring the ingredients AND pay more? HAHAHA!"
            
            k "I'm implementing this RIGHT NOW!"
            
            $ money += 15
            "You received 15 dollars commission for the idea!"
            
            # Mark that idea was already suggested
            $ sugeriu_promocao_batata = True
            
            # Hide krab happy before returning to menu
            hide krab happy
            jump menu_principal_siririca
        
        "Do something else":
            # Hide krab4 before going back
            hide krab4
            
            # Show krab a for main menu
            show krab a at center:
                zoom 0.75
            
            jump menu_principal_siririca
            
        "Go back":
            # Hide everything before going back to lobby
            hide krab4
            call screen lobbykk with fade

label info_molusco:
    # Hide any current Mr. Krack before showing krab4
    hide krab a
    hide krab happy
    
    # Show krab4 in correct position
    show krab sus:
        zoom 0.6 xpos 1000 ypos 400
    
    k "That useless jerk-off? What about him?"
    
    k "He spends all day complaining and cursing customers behind their backs!"
    
    k "But he's cheap, so I keep him around..."
    
    menu:
        "Ask where he is":
            k "Probably at the register, being rude to customers as always."
            
            k "Or hiding in the bathroom jerking... I mean, playing clarinet."
            
            jump menu_principal_siririca
        
        "Suggest firing Squirtward":
            # Hide krab4 before showing krab happy
            hide krab sus
            show krab madtalk:
                zoom 0.6 xpos 1000 ypos 400
            
            k "And pay two salaries? Are you crazy?"
            
            k "Would you do his job too?"
            
            menu:
                "Yes, I can do it":
                    k "HAHAHA, you're already accepting to do OVERTIME for free!"
                    
                    k "Now you want to do Squirtward's job too? NO WAY!"
                    
                    k "I won't fire him and hire another employee when I can exploit TWO at once!"
                    
                    # Hide krab happy before returning to menu
                    hide krab madtalk
                    jump menu_principal_siririca
                
                "No, better not":
                    k "That's what I thought. Get back to work!"
                    
                    # Hide krab happy before returning to menu
                    hide krab happy
                    jump menu_principal_siririca
        
        "Do something else":
            # Hide krab4 before going back
            hide krab4
            
            # Show krab a for main menu
            show krab a at center:
                zoom 0.75
            
            jump menu_principal_siririca
            
        "Go back":
            # Hide everything before going back to lobby
            hide krab4
            call screen lobbykk with fade

label gaveta_secreta:
    # Hide any current Mr. Krack before continuing
    hide krab a
    hide krab4
    hide krab happy
    
    "While Mr. Krack is distracted, you sneak to the office's secret drawer"
    
    menu:
        "Open the drawer":
            "You find several photos of Mr. Krack hugging money bags"
            
            "There's also a book called 'How to exploit employees and profit from it - Volume 37'"
            
            "And a small locked safe..."
            
            menu:
                "Try to open the safe":
                    "You try to turn the combination..."
                    
                    "Suddenly, an alarm goes off!"
                    
                    # Show kradeath in correct position
                    show kradeath at center with moveinright
                    
                    k "YOU LITTLE HALF-ASSED THIEF!"
                    
                    k "TRYING TO STEAL MY PRECIOUS MONEY?!"
                    
                    "Mr. Krack grabs you by the collar"
                    
                    k "I'LL THROW YOU IN THE FREEZER WITH THE LAST EMPLOYEE WHO TRIED TO ROB ME!"
                    
                    $ money = 0
                    "Mr. Krack confiscated all your money as punishment!"
                    
                    # Hide kradeath before returning to menu
                    hide kradeath
                    jump menu_principal_siririca
                
                "Close the drawer quickly":
                    "You close the drawer just in time"
                    
                    # Show krab a in correct position
                    show krab a at center with moveinright:
                        zoom 0.75
                    
                    k "What are you doing near my desk, boy?"
                    
                    menu:
                        "Just came to clean the dust, boss!":
                            # Hide krab a before showing krab happy
                            hide krab a
                            show krab happy:
                                zoom 0.6 xpos 1000 ypos 400
                            
                            k "Ah, free cleaning! That's how I like it!"
                            
                            k "Keep it up and maybe one day you'll get a half-penny raise!"
                            
                            # Hide krab happy before returning to menu
                            hide krab happy
                            jump menu_principal_siririca
                        
                        "Looking for pens for the kitchen":
                            # Hide krab a before showing krab4
                            hide krab a
                            show krab4:
                                zoom 0.6 xpos 1000 ypos 400
                            
                            k "PENS? In the kitchen?"
                            
                            k "You think PENS grow on trees? They're EXPENSIVE!"
                            
                            k "Use charcoal or squid ink like everyone else!"
                            
                            # Hide krab4 before returning to menu
                            hide krab4
                            jump menu_principal_siririca
                
                "Do something else":
                    jump menu_principal_siririca
                    
                "Go back":
                    call screen lobbykk with fade
        
        "Better not risk it":
            "You decide it's not worth risking your life out of curiosity"
            
            # Show krab a in correct position
            show krab a at center with moveinleft:
                zoom 0.75
            
            k "What are you doing standing there? TIME IS MONEY!"
            
            k "Get back to the kitchen NOW! There are customers waiting!"
            
            # Hide krab a before returning to menu
            hide krab a
            jump menu_principal_siririca
        
        "Do something else":
            # Show krab a directly in correct position
            show krab a at center:
                zoom 0.75
            
            jump menu_principal_siririca
            
        "Go back":
            call screen lobbykk with fade