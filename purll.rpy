# Define Pearl character
define prl = Character("Purrl", who_color="#ff69b4")

# Variables to track Pearl's state
default conheceu_perola = False  # Track if already met Pearl
default perola_no_restaurante = False  # Track if Pearl is working at restaurant
default perola_suspeita_nivel = 0  # Pearl's suspicion level about player identity
default ultima_interacao_perola = -1  # Last day player interacted with Pearl
default perola_descoberta_financeira = False  # Track if financial discovery happened
default perola_quer_vinganca = False  # Pearl wants revenge against player
default endereco_perola_descoberto = False  # Player knows where Pearl lives
default perola_expulsa = False
# Pearl images (Available: reclavulva, pesus, perola_furiosa)
image perola_furiosa = "images/perola_furiosa.png"
image pesus = "images/pesus.png"
image reclavulva = "images/reclavulva.png"
image envelopes_dinheiro = "images/envelopes_scattered.png"

# Sound effects
define audio.porta_batendo = "porta_slam.mp3"
define audio.papeis_caindo = "papers_scatter.mp3"

# Pearl's financial discovery scene - MAIN EVENT
label descoberta_financeira_perola:
    hide screen xerequinha
    # This scene triggers automatically when entering Krusty Krotch after day 12
    scene cutkrab
    
    # Dramatic door slam
    play music "tbcdrama.mp3" volume 0.8
    play audio "soco.mp3"
    with hpunch
    
    # Pearl bursts through the door
    show reclavulva with moveinright:
        xalign -2.2
        yalign 1.2
        zoom 1.3
    
    prl "DAAAAAAAAAAD! I SAW YOUR CREDIT CARD BILLS, YOU OLD PERVERT!"

    stop music
    play music "susmusic.mp3"
    
    # Mr. Krotch comes running from his office
    show krab2 with moveinleft:
        xalign 1.5
        yalign 1.2
        zoom 0.9
    
    k "PURRL! SHIT! What are you doing here?!"
    hide reclavulva
    # Pearl waves credit card statements angrily
    show perola_furiosa with vpunch:
        xalign -2.2
        yalign 1.2
        zoom 1.3
    
    prl "YOU SPENT $400 ON WHAT?! BLOW-UP DOLLS?! YOU DISGUSTING PERVERT!"
    
    # Mr. Krotch panics and looks around nervously
    hide krab2

    show krab_talk :
        xalign 1.5
        yalign 1.2
        zoom 0.9
    
    k "Purrl! Damn! It's not exactly like that..."
    
    # Pearl gets even more furious
    prl "AND THERE ARE OTHER WEIRD PURCHASES! 'CONDOMS'?! 'ADULT BOOKS'?!"
    prl "WHAT THE HELL IS THIS, DADDY?! DID YOU BECOME A COMPLETE PERVERT?!"
    
    
    prl "EXPLAIN ALL THIS SHIT!" with vpunch
    
    # Pearl turns to look at the player suspiciously
    hide perola_furiosa
    show pesus with vpunch:
        xalign -2.2
        yalign 1.2
        zoom 1.3
    
    prl "And you, Spoogebob... did you know about all this perverted stuff?"
    
    # Player interaction menu
    menu:
        "Defend the old fart":
            $ escolha_perola = "defender"
            jump defender_krotch_grosso
            
        "Play dumb":
            $ escolha_perola = "ignorar"
            jump fingir_que_eh_burro
            
        "Mock the situation":
            $ escolha_perola = "sarcastico"
            jump zoar_perola

# Option 1: Defend Mr. Krotch (but being dumb and rude)
label defender_krotch_grosso:
    b "Hey, you fat fucking whale, your dad is a man or what?"
    b "Every male needs some things... if you know what I mean."
    
    # Pearl gets furious with the insult
    hide pesus
    show perola_furiosa with vpunch:
        xalign -2.2
        yalign 1.2
        zoom 1.3 
    
    prl "FAT WHALE?! WHO DO YOU THINK YOU ARE, YOU PIECE OF SHIT?!"
    prl "AND WHAT THE HELL IS THIS 'EVERY MALE' CRAP?!"
    
    # Mr. Krotch tries to calm down but makes it worse
    show krab4 :
        xalign 1.5
        yalign 1.2
        zoom 0.9
    
    k "Calm down, Purrl... Spoogebob is just being... masculine..."
    
    b "Exactly, damn it! Real men don't hide these things."
    b "At least he's not picking up whores on the street, right?"
    
    # Pearl is shocked by the crude language
    hide perola_furiosa
    show reclavulva with vpunch:
        xalign -2.2
        yalign 1.2
        zoom 1.3 
    
    prl "SINCE WHEN DO YOU TALK LIKE THIS, SPOOGEBOB?!"
    prl "YOU WERE POLITE! INNOCENT!"
    prl "NOW YOU LOOK LIKE A... A... CRIMINAL!"
    
    b "Criminal my ass! I just grew up and stopped being a loser!"
    
    hide reclavulva
    show pesus with vpunch:
        xalign -2.2
        yalign 1.2
        zoom 1.3 
    
    prl "GREW UP?! OR BECAME SOMEONE ELSE?!"
    prl "I'M GONNA FIND OUT WHAT THE HELL IS HAPPENING HERE!"
    
    $ perola_suspeita_nivel += 3
    $ perola_quer_vinganca = True
    $ perola_descoberta_financeira = True
    
    jump final_descoberta_perola_grosso

# Option 2: Play dumb - ENHANCED WITH NEW OPTIONS
label fingir_que_eh_burro:
    # Player acts like a complete idiot
    b "What? What's happening? I was thinking about... uh... hamburgers..."
    b "What blow-up doll? Is it for a birthday party?"
    
    # Pearl gets irritated by the stupidity
    hide pesus
    show reclavulva with vpunch :
        xalign -2.2
        yalign 1.2
        zoom 1.3
    
    prl "BIRTHDAY PARTY?! YOU IDIOT!"
    prl "SEXUAL BLOW-UP DOLL, DAMN IT!"
    
    # NEW: Enhanced menu with additional options
    menu:
        "What is sexual? Never heard that word":
            b "Sexual? What word is that? Is it like... a type of party?"
            b "Must be like those dolls that talk when you press the button, right?"
            
            hide perola_furiosa
            hide reclavulva
            show pesus with vpunch:
                xalign -2.2
                yalign 1.2
                zoom 1.3
            
            prl "MY GOD! You really became a complete retard!"
            prl "HOW can you not know what sexual means at... how old are you again?!"
            
            b "I... don't remember. How old am I again?"
            
            prl "THIS IS TOO BIZARRE! Either you hit your head REALLY hard, or..."
            prl "... or you're NOT SPOOGEBOB!"
            
            $ perola_suspeita_nivel += 2
            
        "Blow-up doll must be like those that talk when you press":
            b "Oh yeah, must be like those dolls that when you press them they say 'mommy'!"
            b "But why would Mr. Krotch buy toys? He's not your age."
            
            hide perola_furiosa
            hide reclavulva
            show pesus with vpunch:
                xalign -2.2
                yalign 1.2
                zoom 1.3
            
            prl "TOYS?! Are you pretending to be dumb or did you really become an idiot?"
            prl "And since when do you call my dad 'Mr. Krotch' so formally?"
            prl "You always called him 'Mr. Krabs' or 'boss'!"
            
            $ perola_suspeita_nivel += 1
            
        "Your dad must be becoming a child again":
            b "Oh, I get it! Your dad must be becoming a child again!"
            b "That's why he's buying toys! It's normal in old folks."
            b "My grandma also got like this before... well, you know..."
            
            hide perola_furiosa
            hide reclavulva
            show perola_furiosa with vpunch:
                xalign -2.2
                yalign 1.2
                zoom 1.3
            
            prl "OLD FOLKS?! YOUR GRANDMA?!"
            prl "YOUR GRANDMA BOUGHT A FUCKING BLOW UP DOLL?!"
            prl "AND MY DAD ISN'T OLD! HE'S A MAN IN HIS PRIME!"
            prl "YOU'RE LYING! WHO ARE YOU?!"
            
            # This option increases suspicion considerably
            $ perola_suspeita_nivel += 4
            
        "Must be adult stuff I don't understand":
            b "Ah... must be adult stuff right..."
            b "I'm still too innocent to understand these things..."
            b "Better not know, right?"
            
            hide perola_furiosa
            hide reclavulva
            show pesus with vpunch:
                xalign -2.2
                yalign 1.2
                zoom 1.3
            
            prl "Innocent? YOU? After all these years working with adults?"
            prl "You've seen everything in that restaurant, Spoogebob!"
            prl "This sudden 'innocence' of yours is very suspicious..."
            
            $ perola_suspeita_nivel += 1

    # Mr. Krotch facepalms
    show krab4 :
        xalign 1.5
        yalign 1.2
        zoom 0.9
    
    k "Spoogebob... for Neptune's sake..."
    
    # Pearl's final reaction based on suspicion level
    if perola_suspeita_nivel >= 4:

        hide perola_furiosa
        hide pesus
        show reclavulva with vpunch:
            xalign -2.2
            yalign 1.2
            zoom 1.3
        
        prl "ENOUGH! ALL OF THIS IS TOO STRANGE!"
        prl "YOU'RE NOT THE SPOOGEBOB I KNOW!"
        prl "I'M GONNA FIND OUT WHO YOU REALLY ARE!"
        
        $ perola_quer_vinganca = True
        
    elif perola_suspeita_nivel >= 2:
        hide pesus
        show pesus with vpunch:
            xalign -2.2
            yalign 1.2
            zoom 1.3
        
        prl "Something is very wrong happening here..."
        prl "Either you became a complete mental case..."
        prl "... or there's something you're not telling me!"
        
    else:
        prl "Well... maybe you really became a bit... special."
        prl "But still, all this is very strange."
    
    $ perola_descoberta_financeira = True
    jump final_descoberta_perola_grosso

# Option 3: Mock the situation (crude and offensive)
label zoar_perola:
    b "Relax there, princess. At least your dad isn't spending on drugs."
    b "And another thing, blow-up dolls are cheaper than real women."
    b "Not to mention they don't nag or ask for money."
    
    # Everyone is shocked by the crude response
    hide pesus
    show perola_furiosa with vpunch:
        xalign -2.2
        yalign 1.2
        zoom 1.3
    
    prl "WHAT THE FUCK DID YOU JUST SAY?!"
    
    show krab4 :
        xalign 1.5
        yalign 1.2
        zoom 0.9
    
    k "SPOOGEBOB! WHAT KIND OF COMMENT WAS THAT?!"
    
    b "Comment from an experienced man, old timer."
    b "Your daughter is just too inexperienced to understand these things."
    
    # Pearl gets extremely angry
    hide perola_furiosa
    show reclavulva with vpunch:
        xalign -2.2
        yalign 1.2
        zoom 1.3
    
    prl "INEXPERIENCED?! YOU SON OF A BITCH!"
    prl "WHO DO YOU THINK YOU ARE TO TALK TO ME LIKE THAT?!"
    prl "YOU'RE NOT SPOOGEBOB! SPOOGEBOB WOULD NEVER SAY THIS SHIT!"
    
    b "He would too, just now I have the balls to speak the truth."
    
    hide reclavulva
    show pesus with vpunch:
        xalign -2.2
        yalign 1.2
        zoom 1.3
    
    prl "BALLS?! SINCE WHEN DO YOU USE THAT WORD?!"
    prl "YOU SOUND LIKE AN EX-CONVICT, YOU BASTARD!"
    
    # Dangerous territory - too close to truth
    b "Ex-convict my ass! I just stopped being a wimp!"
    
    hide pesus
    show reclavulva with vpunch:
        xalign -2.2
        yalign 1.2
        zoom 1.3
    
    prl "I'M GONNA FIND OUT WHO YOU REALLY ARE!"
    prl "AND WHEN I DO, I'M GONNA SCREW YOU OVER!"
    
    $ perola_suspeita_nivel += 4
    $ perola_quer_vinganca = True
    $ perola_descoberta_financeira = True
    
    jump final_descoberta_perola_grosso
# Final scene conclusion (ENHANCED - Mr. Krotch always reveals address)
# Final scene conclusion (ENHANCED - Mr. Krotch always reveals address)
label final_descoberta_perola_grosso:
    # Mr. Krotch tries to end the confrontation
    show krab2:
        xalign 1.5
        yalign 1.2
        zoom 0.9
    
    k "Well... since we talked about all this shit..."
    k "How about you go home, Purrl?"
    
    # Purrl's reaction depends on suspicion level and revenge desire
    if perola_suspeita_nivel >= 4:
        show reclavulva with vpunch:
         xalign -2.2
         yalign 1.2
         zoom 1.3
        
        prl "GO HOME MY ASS!"
        prl "I'M GONNA STAY HERE AND FIND OUT WHAT SHIT YOU TWO ARE UP TO!"
        prl "AND YOU, YOU FAKE... I'M GONNA SCREW YOU OVER!"
        
        k "Purrl, language!"
        
        prl "LANGUAGE MY ASS, DAD!"
        prl "THAT BASTARD THERE ISN'T SPOOGEBOB!"
        prl "AND I'M GONNA PROVE IT!"
        
        # She gives player her address aggressively
        prl "YOU KNOW WHAT? COME TO MY HOUSE LATER!"
        prl "I LIVE ON WHALE STREET, NUMBER 69!"
        prl "COME THERE SO WE CAN TALK PROPERLY, YOU PIECE OF SHIT!"
        
        $ perola_no_restaurante = True
        $ conheceu_perola = True
        $ endereco_perola_descoberto = True
        
    elif perola_suspeita_nivel >= 3:
        show pesus with vpunch :
         xalign -2.2
         yalign 1.2
         zoom 1
        
        prl "Fine, I'm leaving... BUT THIS ISN'T OVER!"
        prl "I'M GONNA FIND OUT WHAT THE FUCK IS HAPPENING!"
        prl "And you, 'Spoogebob'... we're gonna have a little chat at home!"
        
        # She gives address as threat
        prl "I LIVE ON WHALE STREET, 69! SHOW UP THERE IF YOU GOT BALLS!"
        
        $ conheceu_perola = True
        $ endereco_perola_descoberto = True
        
    else:
        hide perola_furiosa
        show pesus with vpunch :
         xalign -2.2
         yalign 1.2
         zoom 1
        
        prl "Okay... sorry for yelling, dad."
        prl "But this shit was embarrassing as hell!"
        prl "Next time warn me before buying this perverted stuff!"
        
        $ conheceu_perola = True
    
    # NEW: Mr. Krotch ALWAYS gives address regardless of Pearl's suspicion level
    if not endereco_perola_descoberto:
        hide krab_talk
        hide krab2
        show krab4 at center
        
        k "Ah, Spoogebob... since you and Purrl... 'got to know each other' better today..."
        k "If you want to talk to her calmly, she lives on Whale Street, 69."
        k "But take it easy, okay? She's been kind of... temperamental."
        k "And don't mention the credit card purchases, for Neptune's sake!"
        
        $ endereco_perola_descoberto = True
        "Mr. Krotch revealed Purrl's address! You can now visit her house."
    
    # Purrl's final threat/invitation
    if endereco_perola_descoberto:
        if perola_quer_vinganca:
            prl "AND DON'T FORGET: WHALE STREET, 69!"
            prl "COME THERE SO WE CAN SETTLE ACCOUNTS!"
        elif perola_suspeita_nivel >= 2:
            prl "Whale Street, 69... don't forget."
            prl "Come there so we can talk properly about all this weirdness."
        else:
            prl "If you want to talk about this properly, look for me at home."
            prl "Whale Street, 69. But only if it's to talk like civilized people!"
    
    # Purrl exits
    if perola_no_restaurante:
        hide perola_vingativa
        hide reclavulva
        hide perola_furiosa
        show pesus :
         xalign -2.2
         yalign 1.2
         zoom 1.3
        
        "Purrl positions herself in a corner, watching you with hatred..."
        "She's planning something. This is very dangerous."
        
    else:
        hide pesus
        hide perola_envergonhada
        
        prl "BYE, DAD! BYE, 'SPOOGEBOB'!"
        
        hide perola_irritada with moveoutleft
        hide perola_envergonhada with moveoutleft
        
        "Purrl leaves, but her threats echo in the air..."
        if endereco_perola_descoberto:
            "You now know where she lives. This could be useful... or dangerous."
    
    # Mr. Krotch's reaction
    hide krab_talk
    hide krab2
    show krab4 at center
    
    k "Holy shit, Spoogebob... that was... complicated as hell."
    k "My daughter never used that kind of language... she's pissed as hell."
    
    if perola_suspeita_nivel >= 3:
        k "And be careful with Purrl. She's smart and vengeful..."
        k "If she finds out something... we're fucked."
    
    if endereco_perola_descoberto:
        k "And now she knows where to find you... or vice versa."
        k "This could be an opportunity... or a complete disaster."
        k "Good luck, boy. You're gonna need it."
    
    $ ultima_interacao_perola = dia
    
    # Return to restaurant normal flow
    jump cozinha

# Purrl interaction menu (if she stays in restaurant)
label interagir_com_perola:
    if not perola_no_restaurante or perola_expulsa:
        "Purrl is not here right now."
        jump cozinha
    
    scene lobbykrab
    
    show pesus :
        xalign -2.2
        yalign 1.2
        zoom 1.3
    
    prl "What's up, you piece of shit? Wanna talk?"
    
    menu:
        "About what, whale?":
            jump conversa_perola_agressiva
            
        "I don't have time for your bullshit":
            jump evitar_perola_grosso
            
        "Stop bugging me":
            jump confrontar_perola_grosso
            
        "GET THE FUCK OUT OF HERE!" if perola_no_restaurante:
            jump expulsar_perola_grosso

# Aggressive conversation with Purrl
label conversa_perola_agressiva:
    prl "WHALE?! YOU SON OF A BITCH!"
    prl "ABOUT THE FACT THAT YOU'RE AN IMPOSTOR, ASSHOLE!"
    
    menu:
        "Impostor my ass":
            prl "THEN PROVE THAT YOU'RE REALLY SPOOGEBOB!"
            jump teste_identidade_perola_grosso
            
        "You're crazy, girl":
            prl "CRAZY IS THE WHORE WHO GAVE BIRTH TO YOU!"
            prl "I KNOW SOMETHING'S WRONG!"
            $ perola_suspeita_nivel += 1
            
        "Wanna stop the drama?":
            prl "DRAMA?! I'LL SHOW YOU DRAMA!"
            prl "COME TO MY HOUSE SO WE CAN SOLVE THIS!"
            $ perola_suspeita_nivel += 1
    
    jump final_conversa_perola_grosso

# Avoid Purrl (rude version)
label evitar_perola_grosso:
    prl "RUNNING FROM ME, YOU COWARD?!"
    prl "THE REAL SPOOGEBOB WOULD NEVER RUN FROM A CONVERSATION!"
    
    b "Running my ass! I just don't have time for your paranoia!"
    
    prl "PARANOIA?! I'LL SHOW YOU PARANOIA!"
    prl "SHOW UP AT MY HOUSE IF YOU GOT GUTS!"
    
    $ perola_suspeita_nivel += 1
    $ endereco_perola_descoberto = True
    
    jump final_conversa_perola_grosso

# Confront Purrl (very rude)
label confrontar_perola_grosso:
    prl "STOP BUGGING ME?!"
    prl "YOU'RE THE ONE BUGGING ME, YOU FAKE!"
    
    b "Fake my ass! You're the one making trouble!"
    
    prl "THEN PROVE YOU'RE SPOOGEBOB!"
    prl "COME TO MY HOUSE AND PROVE IT!"
    
    menu:
        "Alright, I'll come to your house":
            prl "GREAT! WHALE STREET, 69!"
            prl "COME THERE SO WE CAN SOLVE THIS SHIT!"
            $ endereco_perola_descoberto = True
            
        "I'm not going to a crazy person's house":
            prl "CRAZY?! YOU PIECE OF SHIT!"
            prl "THEN I'LL MAKE YOUR LIFE HELL HERE!"
            $ perola_suspeita_nivel += 2
            
        "Only if it's for other things...":
            prl "OTHER THINGS?! WHAT THE FUCK ARE YOU IMPLYING?!"
            prl "YOU DISGUSTING PERVERT!"
            $ perola_suspeita_nivel += 2
    
    jump final_conversa_perola_grosso

# Identity test (crude version)
label teste_identidade_perola_grosso:
    prl "ALRIGHT, ANSWER THIS: WHAT'S THE NAME OF MY PET FISH?"
    
    menu:
        "What fish, damn?":
            prl "WHAT DO YOU MEAN 'WHAT FISH'?! YOU LIAR!"
            prl "YOU TALKED TO ME ABOUT HIM LAST WEEK!"
            $ perola_suspeita_nivel += 2
            
        "I dunno... Gary?":
            prl "GARY IS YOURS, YOU IDIOT!"
            prl "MY FISH IS NAMED ALGERNON!"
            $ perola_suspeita_nivel += 2
            
        "I don't remember that shit":
            prl "DON'T REMEMBER?! HOW CAN YOU NOT REMEMBER?!"
            prl "YOU FUCKING IMPOSTOR!"
            $ perola_suspeita_nivel += 2
    
    prl "I KNEW IT! YOU'RE NOT SPOOGEBOB!"
    prl "COME TO MY HOUSE SO WE CAN SETTLE THIS!"
    
    $ endereco_perola_descoberto = True
    
    jump final_conversa_perola_grosso

# Final conversation (crude version)
label final_conversa_perola_grosso:
    if perola_suspeita_nivel >= 6:
        hide perola_observando
        show reclavulva with vpunch :
         xalign -2.2
         yalign 1.2
         zoom 1
        
        prl "I'M SURE OF IT! YOU'RE NOT SPOOGEBOB!"
        prl "I'M GONNA FIND OUT WHO YOU ARE AND FUCK YOU OVER!"
        prl "WHALE STREET, 69! DON'T FORGET!"
        
        "EXTREME DANGER! Purrl is convinced you're an impostor!"
        "She wants revenge and knows where you 'live'. This is very bad."
        
    elif perola_suspeita_nivel >= 4:
        hide perola_observando
        show perola_suspeita at left
        
        prl "SOMETHING'S VERY WRONG HERE..."
        prl "I'M GONNA KEEP AN EYE ON YOU, YOU BASTARD."
        prl "AND IF I FIND OUT YOU'RE FOOLING ME..."
        
        "Purrl is very suspicious and planning something."
        
    else:
        prl "Well... maybe I'm being paranoid..."
        prl "But you're still weird as hell."
    
    if endereco_perola_descoberto and not perola_quer_vinganca:
        prl "If you want to talk properly, show up at my house."
        prl "Whale Street, 69. But no funny business!"
    
    $ ultima_interacao_perola = dia
    jump cozinha

# NEW: Option to kick out Purrl (violent and permanent)
label expulsar_perola_grosso:
    b "GET THE FUCK OUT OF HERE, YOU FAT WHALE!"
    b "THIS IS A WORKPLACE, NOT A DAYCARE!"
    b "NOBODY WANTS TO HEAR YOUR BULLSHIT!"
    
    # Purrl is shocked by the aggressive response
    hide pesus
    show perola_furiosa with vpunch:
        xalign -2.2
        yalign 1.2
        zoom 1.3
    
    prl "WHAT?! YOU CAN'T KICK ME OUT!"
    prl "THIS IS MY DAD'S RESTAURANT!"
    
    b "I DON'T GIVE A SHIT WHOSE DAUGHTER YOU ARE!"
    b "GET OUT BEFORE I DRAG YOU OUT MYSELF!"
    
    # Mr. Krotch intervenes, torn between sides
    show krab4:
        xalign 1.5
        yalign 1.2
        zoom 0.9
    
    k "Spoogebob! What the hell are you doing?!"
    k "That's my daughter!"
    
    b "Your daughter is a pain in the ass, boss!"
    b "She's disturbing the customers and causing problems!"
    b "Either she leaves or I quit!"
    
    # Mr. Krotch has to choose between money and family
    k "Shit... Purrl, maybe you should go home for today..."
    k "We'll talk about this later at home."
    
    # Purrl is furious but has to leave
    hide perola_furiosa
    show reclavulva with vpunch:
        xalign -2.2
        yalign 1.2
        zoom 1.3
    
    prl "FINE! BUT THIS ISN'T OVER!"
    prl "I'LL REMEMBER THIS, YOU BASTARD!"
    prl "AND DAD... WE'LL HAVE A SERIOUS TALK AT HOME!"
    
    # Dramatic exit
    prl "YOU'LL PAY FOR THIS HUMILIATION!"
    
    hide reclavulva with moveoutleft
    play audio porta_batendo
    
    # Consequences
    $ perola_expulsa = True
    $ perola_no_restaurante = False
    $ perola_suspeita_nivel += 3
    $ perola_quer_vinganca = True
    
    # Mr. Krotch's reaction
    k "Holy fuck Spoogebob... what have you done?"
    k "She's never gonna forgive this..."
    k "And neither will I, probably..."
    k "But... work comes first, I guess..."
    
    "You kicked Purrl out! She won't appear in the restaurant anymore."
    "But this will have consequences... She's planning revenge."
    "Your relationship with Mr. Krotch has also been damaged."
    
    if not endereco_perola_descoberto:
        k "If you want to apologize... she lives on Whale Street, 69."
        k "But I don't think she'll want to see you after this..."
        $ endereco_perola_descoberto = True
    
    $ ultima_interacao_perola = dia
    jump cozinha

# Function to check if Purrl discovery should trigger
init python:
    def deve_ativar_descoberta_perola():
        global dia, perola_descoberta_financeira
        return dia >= 12 and not perola_descoberta_financeira