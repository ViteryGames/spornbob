# storymode.rpy - Story Mode Progression (English)

define b = "You"
default day2 = False

label storymode:
    scene bg room1
        
    show patrick1:
        zoom 1.5 xpos 30 ypos 400 

    p "Hey Spoogebob, where were you?! Mr. Krack is going crazy looking for you, there are lots of customers at the Krusty Krotch"
    hide patrick1
    show batavo1 at Transform(xzoom=-1):
        zoom 1.3 xpos 900 ypos 200 
    b "Krusty Krotch?"
    
    show patrick1:
        zoom 1.5 xpos 30 ypos 400 

    p "The restaurant where you've worked for decades and value more than your own life?"
    menu: 
        "Oh yeah, I better get going. Thanks":
            $ escolha = "bob"
            jump pau1
        "Never heard of it":
            $ escolha = "tv"
            jump pau1
        "I'm not Spoogebob Squirtpants, I'm a criminal who tried to escape and ended up here somehow.":  
            $escolha = "vdd"
            jump pau1        

label pau1:
    if escolha == "crz":   
        show patrick5:
            zoom 1.5 xpos 30 ypos 400 
        p "(Poor guy, all these years have made him crazy. Must be getting senile, better stay away...)"

        p "Right Spoogebob, see ya later"

        hide patrick5
    elif escolha == "bob":
        hide patrick2    
        show patrick1:
            zoom 1.5 xpos 30 ypos 400 
        p "See ya later, square sissy"
        hide patrick2
    elif escolha == "inv":
        if vezes_investigou == 0:
            "You discover 10 dollars under the mattress."
            "Inside an envelope written: 'Last 20 years salary'."
        elif vezes_investigou == 1:
            "You discovered that today is opposite day."
            $ dia_do_contra = True 
        else:
            "Nothing more to investigate."
        $ vezes_investigou += 1
    elif escolha =="tv":
        hide patrick1   
        show patrick2:
            zoom 1.5 xpos 30 ypos 400 
        p "It's where you fry burgers for your crab boss, you know.. "

        hide patrick2
        show patrick6:
            zoom 1.5 xpos 30 ypos 400 

        p "Krotch burgers.. "

        hide patrick6
        menu: 
            "Oh yeah, I better get going. Thanks dude":
                $ escolha = "bob"
                jump pau1
            "I don't fry burgers, I'm not a loser.":
                $ escolha = "crz"
                jump pau1
    elif escolha =="vdd":
        show patrick1:
            zoom 1.5 xpos 30 ypos 400 

        p "Then why are you wearing his clothes?"   
        menu: 
            "Because I fucking want to, you pink clown son of a bitch":
                $escolha = "cuzao1"
                jump badgay
            "Because today is opposite day!":
                $escolha = "contra"
                $contrap1 = True
                jump badgay    

label badgay:
    if escolha == "cuzao1": 
        hide patrick1
        
        show patrick2:
            zoom 1.5 xpos 30 ypos 400 

        p "You don't have to talk like that..."

        p "Barnacle head!"

        hide patrick2
    elif escolha == "contra":
        hide patrick1
        show patrick aa:
            zoom 1.5 xpos 30 ypos 400 

        p "OPPOSITE DAY?! OH SNAP I HAD FORGOTTEN! THANKS BUDDY."
        
        hide patrick aa

        "Fatrick ran away"

label stry1:
    scene areia 

    menu: 
        #"Go back home":
        #jump chegada_em_casa
        "Go to the Krusty Krotch":
            jump room2 

    p "See ya later, sissy!"

label day2:
    scene areia
    
    show patrick1
    
    p "Hey buddy, how's it going?"

    p "I'm missing a good old jellyfish hunt with my best friend"

    p "I'm going to the jellyfish fields right now!!"

    p "What do you think about hunting some with me today"
    hide patrick1
    menu:
        "Hunt what?":
            $escolha = "que"
            jump oppatrick

        "Do I look like I give a fuck, you gay piece of shit?":
            $escolha = "no"
            jump oppatrick

label day3:
    scene shellfone
    
    "Your shell phone is vibrating"

    define sd = Character("Sandy Cunts")
    sd "Hi Spoogebob Squirtpants! Come visit me today at the treedome!"

    menu:
        "Visit Sandy":
            jump sandy

label oppatrick:
    if escolha == "no":  
        show patrick2:
            zoom 1.5 xpos 30 ypos 400 

        p "You don't have to talk like that..."

        p "Barnacle head!"

        hide patrick2
    elif escolha == "que":
        show patrick2:
            zoom 1.5 xpos 30 ypos 400 

        p "Hunt jellyfish in the jellyfish fields..."

        p "It's our favorite hobby, don't you remember?"
        menu:
            "No":
                call screen lobbykk

    menu:
        "Go to the Krusty Krotch":
            call screen lobbykk

label day4: 
    scene areia 

    "Flying Dutchman" "HAHAHAHAAHAHAHAH YOU SISSY SPONGE!!!"

    "THIS IS A MOTHERFUCKING MAP THAT'S GONNA FUCK YOU UP HEHEHEH KKKKKKAKAKAKAKAAKK"

    menu: 
        "Open the map":
            call screen mapScreen

return