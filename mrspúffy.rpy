# Label da cena da Mrs. Puffy (versão adulta)

label mrs_puffy_visit:
    # Música de suspense
    play music "susmusic.mp3" fadein 2.0
    
    # Cena no quarto
    scene doorshutbob
    
    show batavo1 at Transform(xzoom=-1):
        zoom 1.3 xpos 1000 ypos 200
    
    # Primeiro knock knock
    play sound "soco.mp3"
    with hpunch
    "KNOCK KNOCK!"
    with fade
    
    # Pausa dramática
    pause 1.0
    
    # Segundo knock knock
    play sound "soco.mp3" volume 1.2
    with hpunch
    "KNOCK KNOCK!"
    with fade
    
    # Reação do protagonista - pensando que é polícia
    show batavo1 at Transform(xzoom=-1):
        zoom 1.5 xpos 900 ypos 150
        linear 0.1 xpos 950
        linear 0.1 xpos 900
        linear 0.1 xpos 950
        linear 0.1 xpos 900
    
    b "What the fuck..."
    b "Who's that knocking at my door?"
    b "Shit... what if it's the cops?!"
    
    with vpunch
    
    # Voz misteriosa (ele não sabe quem é ainda)
    "???" "Spoogebob! I know you're in there! Open this door!"
    
    # Reação de pânico pensando que é polícia
    show batavo1 at Transform(xzoom=-1):
        zoom 1.8 xpos 800 ypos 100
    
    with hpunch
    
    b "FUCK! IT'S THE COPS!"
    b "They found out what happened to the real Spoogebob!"
    b "I'm so fucked!!"
    
    # Menu de escolhas
    menu:
        "Ignore":
            jump ignore_mrs_puffy
            
        "Open the door":
            jump open_door_mrs_puffy
            
        "Say nobody's home":
            jump nobody_home_mrs_puffy

# Label para ignorar
label ignore_mrs_puffy:
    b "I'll just ignore whoever this is..."
    
    # Mrs. Puffy continua batendo
    play sound "soco.mp3"
    with hpunch
    "???" "Spoogebob! I can hear you in there!"
    
    # Mais batidas
    play sound "knock.mp3" volume 1.3
    with hpunch
    "???" "Don't make me use my... special teaching methods!"
    
    b "What the hell does that mean?"
    b "This definitely doesn't sound like cops..."
    
    # Ela continua insistindo
    "???" "Fine! I'll be back later with my private lesson plan!"
    
    # Som de passos se afastando
    b "Whoever that was finally left..."
    b "But what did they mean by 'special teaching methods'?"
    
    jump mrs_puffy_aftermath

# Label para abrir a porta
label open_door_mrs_puffy:
    b "Fine, let's see who this is..."
    
    # Som da porta abrindo
    play sound "door_open.mp3"
    
    scene bobdoorop
    # Mostrar Mrs. Puffy se tiver a imagem
    # show mrs_puffy at center
    show batavo1 at Transform(xzoom=-1):
        zoom 1.4 xpos 800 ypos 100
        
    show puffyhappy at left:
     zoom 0.8
    "Mrs. Puffy" "Spoogebob! There you are! You've been missing your driving..."
    

    hide puffyhappy
    # Ela para e olha para baixo
    show puffy2 at left:
     zoom 0.8
    "Mrs. Puffy" "Oh my... Spoogebob..."
    "Mrs. Puffy" "You've... grown... quite a lot since our last lesson..."
    
    # Ela fica claramente interessada
    with hpunch
    
    hide puffy2

    show puffyhappy at left:
     zoom 0.8
    "Mrs. Puffy" "I can see you've been... developing... in certain areas..."
    
    b "What the fuck are you staring at, lady?"
    
    "Mrs. Puffy" "Well... maybe traditional driving lessons aren't what you need anymore..."
    "Mrs. Puffy" "Perhaps you'd be interested in some... private tutoring?"
    
    # Tom claramente sedutor
    "Mrs. Puffy" "I have some very... hands-on teaching methods..."
    "Mrs. Puffy" "What do you say, big boy?"
    
    # Menu final
    menu:
        "Accept her offer":
            b "Well... private lessons don't sound too bad..."
            b "When do we start, Mrs. Puffy?"

            show puffyhappy
            "Mrs. Puffy" "Oh wonderful! Come by my class tomorrow..."
            "Mrs. Puffy" "Bring your... enthusiasm... for learning!"
            "Mrs. Puffy" "I'll show you things that will make your head spin!"
            
            # Ela vai embora animada
            hide puffyhappy
            b "Damn... that crazy bitch might actually be fun..."
            b "I'll check out her place later..."
            
            jump mrs_puffy_aftermath
            
        "Tell her to fuck off":
            b "Listen here, you huge fucking bitch!"
            b "Take your 'private lessons' and shove them up your old fat hole!"
            
            hide puffyhappy
            show puffymad at left:
             zoom 0.8
            # Mrs. Puffy fica chocada e irritada
            "Mrs. Puffy" "Well! I never! How dare you speak to me like that!"
            "Mrs. Puffy" "You'll regret this, you ungrateful little shit!"
            "Mrs. Puffy" "I'll remember this attitude, Spoogebob!"
            hide puffymad
            # Ela vai embora furiosa
            b "I will never answer that door again"
            
            jump mrs_puffy_aftermath

# Label para fingir que não tem ninguém
label nobody_home_mrs_puffy:
    b "Nobody's home!"
    b "Spoogebob went out!"
    
    "???" "Wait... if nobody's home, then who's talking to me?"
    "???" "That doesn't sound like Spoogebob's voice either..."
    
    # Primeira vez ficando tenso
    show closeup frank
    b "Shit, they're catching on..."
    hide closeup frank
    
    # Submenu para responder
    menu:
        "Say 'Nobody'":
            b "Uh... nobody!"
            b "You're hearing things, go back to sleep or something"
            
            "???" "I'm not stupid! Someone is definitely in there!"
            "???" "Open this door right now!"
            
            # Segunda vez ficando tenso
            show panic
            y"FUCK THEY ARE ON TO ME!"
            hide panic

            jump open_door_mrs_puffy
            
        "Say 'None of your business'":
            b "None of your fucking business, fuck head!"
            b "Mind your own damn life!"
            
            "???" "Excuse me?! That language!"
            "???" "Open this door immediately!"
            
            # Segunda vez ficando tenso
            
            jump open_door_mrs_puffy
            
        "Say 'Meow":
            b "Meow!"
            b "Meow meow!"
            
            "???" "Gary? Is that you?"
            "???" "Where's Spoogebob, Gary?"
            
            b "Meow meow... he's not here..."
            
            "???" "Wait... since when does Gary talk?!"
            "???" "And why do you sound like a grown man?!"
            
            # Segunda vez ficando tenso
            show panic
            b "Shit, I blew it..."
            hide panic 

            jump open_door_mrs_puffy

label mrs_puffy_aftermath:
    # Após ela ir embora
    scene quartobob
    show batavo1 at Transform(xzoom=-1):
        zoom 1.3 xpos 1000 ypos 200
    
    b "What a weird fucking day..."
    b "That crazy fat teacher is definitely up to something..."
    
    # Parar música de suspense
    stop music fadeout 2.0
    
    # Voltar para o gameplay normal
    jump chegada_em_casa