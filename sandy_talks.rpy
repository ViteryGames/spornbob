# sandy_talks.rpy - Sandy Dialogue System (English)

# Sound for cumshots - reusing existing sound
define audio.gozada = "audio/porra.mp3"

init python:
    def obter_dialogo_peitos():
        # Returns random dialogue for when Sandy shows her tits
        import random
        dialogos = [
            "You want to... see my tits? Well, I guess I can show them real quick, partner...",
            "You know that's not very scientific, right? But if you like it so much... you're different today, Spoogebob...",
            "Look what you make me do, you big head! This stays between us, okay? By all the bulls in Texas!",
            "The air here feels nice without clothes... Like what you see, cowboy? Why are you looking at me like that?",
            "Normally I'm more reserved, but with you I feel different... you're more manly today, partner..."
        ]
        return random.choice(dialogos)
    
    def obter_dialogo_punheta():
        # Returns random dialogue for when Sandy gives a handjob
        import random
        dialogos = [
            ["sd", "Hmm... Want some manual help, partner? In Texas we call this 'taming the bull'..."],
            ["sd", "You're different, Spoogebob... more rough. I like it. Let's see if you can handle the famous Texas handjob!"],
            ["sd", "Never thought I'd use my engineering skills this way... damn, you seem like a different person!"],
            ["sd", "Yeehaw! Let's see how much you can take, little sponge... by the prophet's beard, you're huge!"],
            ["sd", "In Texas, we used to call this 'milking the bull'... fuck, you're different from my usual Spoogebob!"]
        ]
        return random.choice(dialogos)
    
    def obter_dialogo_buceta():
        # Returns random dialogue for when Sandy shows her pussy
        import random
        dialogos = [
            ["sd", "Want to see my little squirrel pussy, partner? Well... I think we're intimate enough now..."],
            ["sd", "Never showed this to anyone in Bikini Bottom... You're special, Spoogebob, even being so strange..."],
            ["sd", "Holy shit! Never thought I'd show my pussy to someone, but you make me feel comfortable!"],
            ["sd", "Hope you like what you're about to see. It's a Texas treasure, as they say! What's with that perverted look?"],
            ["sd", "Want to know the wild side of a squirrel? Get ready... fuck, you're wilder than normal!"]
        ]
        return random.choice(dialogos)
    
    def obter_dialogo_cuzinho():
        # Returns random dialogue for when Sandy allows anal
        import random
        if vezes_cuzinho == 0:
            dialogos = [
                ["sd", "My cowboy ass? You want to try... that place? Never did this before, partner..."],
                ["sd", "From behind? I'm a little scared... Promise to go slow? By the devil's horns, you're different!"],
                ["sd", "This is something I never did even in Texas... Are you sure? Holy shit, you're so strange!"],
                ["sd", "Oh my God... I think we can try, but be gentle, okay? Fuck, you seem like someone else!"],
                ["sd", "This is a frontier I never explored... Yeehaw! Never saw you so... commanding before, Spoogebob!"]
            ]
        elif vezes_cuzinho == 1:
            dialogos = [
                ["sd", "Last time was a bit painful... But now I'm more prepared. Fuck, you're so good!"],
                ["sd", "Let's go slow again? In Texas they say the second ride is always better, partner!"],
                ["sd", "Hmm... I've been thinking about this since last time. Come here, cowboy! Ride me again!"],
                ["sd", "Who would've thought a Texan scientist like me would enjoy this kind of... experiment!"],
                ["sd", "This time we have to use more lubricant... It'll be better for both of us, fuck!"]
            ]
        elif vezes_cuzinho == 2:
            dialogos = [
                ["sd", "I'm getting good at this, right? Come here, let's do it again... I love this animal side of you!"],
                ["sd", "I think I found a new scientific hobby to study in depth... fuck, you changed so much!"],
                ["sd", "Who would've thought a Texan squirrel's ass would be so compatible with... your tasty dick!"],
                ["sd", "Mmm... I can barely wait. This time I want to feel everything! Holy shit, you're so good at this!"],
                ["sd", "You know, in Texas we don't talk about this, but... you became a different person, and I love it!"]
            ]
        else:
            dialogos = [
                ["sd", "Ah, my favorite cowboy arrived! You know what I want, don't you? I want to give you my ass!"],
                ["sd", "I'm already ready for you... Don't even need much preparation anymore. Yeehaw! Let's ride!"],
                ["sd", "I think I discovered my secret talent. My Texan ass loves your dick, partner!"],
                ["sd", "This became my addiction, you know? No scientific experiment gives me this much pleasure. Fuck!"],
                ["sd", "Come on, Spoogebob. My ass is throbbing... you're so much more manly now, holy shit!"]
            ]
        return random.choice(dialogos)
    
    def obter_dialogo_recusa():
        # Returns random dialogue for when Sandy refuses because already did it today
        import random
        dialogos = [
            "We already did this today, come back tomorrow you horny cowboy! By the devil's horns, you're insatiable!",
            "Hey, slow down! Even a squirrel needs rest! Holy shit, since when did you become so demanding?",
            "Hmm, someone's very eager! But you'll have to wait until tomorrow.",
            "I have other things to do... How about we get back to this tomorrow?",
            "You're insatiable, aren't you? But let's leave it for tomorrow, okay?",
            "That's enough for today, but come back tomorrow with that thick dick nice and hard for me!"
        ]
        return random.choice(dialogos)
    
    # Dialogue sequences for each sexual scene
    def obter_sequencia_peitos(vez):
        sequencias = [
            # First time
            [
                ["sd", "You really want to see my tits, Spoogebob? Damn, you're so weird today..."],
                ["sd", "Well... I guess it doesn't hurt to show them quickly... but you're different..."],
                ["sd", "Just don't tell anyone, okay?"],
                ["", "Sandy slowly removes the top of her bikini..."],
                ["sd", "So... what do you think? Why do you have that perverted look?"],
                ["sd", "I know they're not as big as the mermaids'... But they please many cowboys out there"],
                ["sd", "Are you enjoying what you see? You're drooling, Spoogebob..."],
                ["", "Sandy notices your strange and predatory gaze"],
                ["sd", "Your look is making me excited... but also a little scared, cowboy..."],
                ["", "You notice her nipples getting harder"],
                ["sd", "Ahhh... This is so... different... damn, you're so strange today..."],
                ["", "Sandy breathes deeply and closes her eyes, enjoying the sensation, but confused with the different behavior"]
            ],
            
            # Second time
            [
                ["sd", "Want to see my tits again, you naughty boy?"],
                ["sd", "I've been thinking about this since last time..."],
                ["", "Sandy removes the top of her bikini with more confidence this time"],
                ["sd", "Like what you see?"],
                ["", "Sandy shakes her Texan melons just for you"],
                ["sd", "Holy cow! You're looking like a cat at fish! Never seen you like this!"],
                ["sd", "You can squeeze a little more... wow, didn't need to be so strong, you animal!"],
                ["", "She notices your dick getting hard"],
                ["sd", "I can see your little horse is also excited!"],
                ["", "Sandy starts breathing faster"],
                ["sd", "That's enough for today cowboy"],
                ["", "Sandy puts her tits back in the bikini"]
            ],
            
            # Third time - NEW VERSION WITH VARIATIONS
            [
                # Line 1 - three variations
                [
                    ["sd", "Well, well! The cowboy came back for the rodeo, didn't he?"],
                    ["sd", "Holy cow! Never saw a man so obsessed with tits like you, Spoogebob!"],
                    ["sd", "Came back to admire the view, partner? You're more eager than a coyote in the desert!"]
                ],
                # Line 2 - three variations
                [
                    ["", "Sandy smiles while removing the top of her bikini, noticing your intense gaze"],
                    ["", "She removes the bikini with a confident movement, analyzing your reaction"],
                    ["", "Sandy takes off the bikini and shakes her breasts provocatively, testing your reaction"]
                ],
                # Line 3 - three variations
                [
                    ["sd", "Damn, Spoogebob! Your eyes are almost popping out, hell!"],
                    ["sd", "Holy cow! You're looking like a cat at fish! Never seen you like this!"],
                    ["sd", "By the horns of a wild bull! What hungry look is that, partner?"]
                ],
                # Line 4 - three variations
                [
                    ["sd", "Fuck, you're looking at me like a Texas predator looks at the last chicken thigh..."],
                    ["sd", "Wow, Spoogebob! With that look you seem like you haven't seen a woman in years!"],
                    ["sd", "Holy shit! That look of yours is hotter than the Texas sun in midsummer!"]
                ],
                # Line 5 - three variations
                [
                    ["", "You maintain a hard and serious expression, analyzing every detail of her breasts"],
                    ["", "Your eyes roam every inch of her breasts with predatory intensity"],
                    ["", "You observe coldly, without blinking, memorizing every curve of her body"]
                ],
                # Line 6 - three variations
                [
                    ["sd", "Fuck! Since when did you become so... observant? Never seen you like this before!"],
                    ["sd", "Damn! What happened to you, Spoogebob? You seem like a different man!"],
                    ["sd", "Holy cow! Who would've thought Spoogebob would look at me like this? You're too different!"]
                ],
                # Line 7 - three variations
                [
                    ["sd", "Ah, fuck! That look of yours is making me all wet! You're too different..."],
                    ["sd", "Shit, Spoogebob! You're exciting me just with that look! What did they do to you?"],
                    ["sd", "Holy shit! This way of yours is making me all shivery! Where did you learn this?"]
                ],
                # Line 8 - three variations
                [
                    ["", "She displays her breasts with pride, noticing the intensity of your gaze"],
                    ["", "Sandy adjusts her posture to better show her breasts, liking your reaction"],
                    ["", "She gets closer, displaying her breasts from a better angle for you"]
                ],
                # Line 9 - three variations
                [
                    ["sd", "By the horns of a wild bull! Like what you see, partner? Never seen you so focused!"],
                    ["sd", "Enjoying the view, cowboy? Looks like you're going to devour me just with your eyes!"],
                    ["sd", "What's this, cowboy? Looks like you never saw Texan tits before! You're hypnotized!"]
                ],
                # Line 10 - three variations
                [
                    ["", "You maintain your cold and dominating expression"],
                    ["", "Your gaze remains relentless, almost intimidating"],
                    ["", "You show no emotion, just animal desire"]
                ],
                # Line 11 - three variations
                [
                    ["sd", "Ahhh! Damn! There's something in your look that's driving me crazy! You're more... manly!"],
                    ["sd", "Fuck, Spoogebob! Just having you look at me like this I'm almost cumming! You're so... man!"],
                    ["sd", "Holy shit! That look... is making me melt completely! Never seen you so dominating!"]
                ],
                # Line 12 - three variations
                [
                    ["", "Sandy breathes deeply and closes her eyes, visibly excited just by your gaze"],
                    ["", "She bites her lower lip, her body responding intensely to your predatory gaze"],
                    ["", "Sandy shivers with pleasure, getting excited just from the intensity of your gaze"]
                ]
            ],
            
            # Repetitions after completing - NEW VERSION WITH VARIATIONS
            [
                # Line 1 - three variations
                [
                    ["sd", "Yeehaw! My tits missed your gaze, Spoogebob..."],
                    ["sd", "Well, well, look who came back! My little Texan tits were waiting for you!"],
                    ["sd", "Come on, cowboy! I know you came to admire the landscape again!"]
                ],
                # Line 2 - three variations
                [
                    ["", "She removes the top of her bikini skillfully, already used to your behavior"],
                    ["", "Sandy takes off the bikini and shakes her breasts provocatively for you"],
                    ["", "She gets rid of the bikini with a quick movement, eager to show her breasts"]
                ],
                # Line 3 - three variations
                [
                    ["sd", "Holy shit, that dick of yours is hard as a rock! Just from looking at me, huh?"],
                    ["sd", "Damn, Spoogebob! Your cock is so hard it could cut diamond! All that just from looking?"],
                    ["sd", "By the devil's horns! Look at the size of that bulge in your pants! Just from seeing me?"]
                ],
                # Line 4 - three variations
                [
                    ["sd", "Fuck, this way you look... so direct, so rough... excites me like hell!"],
                    ["sd", "Damn, Spoogebob! That hungry look of yours is making me all wet!"],
                    ["sd", "Holy shit! How do you manage to make me so excited just with that look?"]
                ],
                # Line 5 - three variations
                [
                    ["", "You observe with coldness, showing no emotion, just animal desire"],
                    ["", "Your eyes roam her body like a predator evaluating its prey"],
                    ["", "You maintain a penetrating gaze, almost violent in its intensity"]
                ],
                # Line 6 - three variations
                [
                    ["sd", "Holy mother of Texas! Keep looking like that! You're so thick in your underwear, holy shit!"],
                    ["sd", "Jesus Christ! That dick is huge! Just from looking at me you get like this, fuck!"],
                    ["sd", "Damn! Look at the size of that! You're harder than a Texan fence post!"]
                ],
                # Line 7 - three variations
                [
                    ["sd", "Sandy adjusts her breasts, displaying them better for your detailed observation"],
                    ["sd", "She massages her own breasts, offering a private show for you"],
                    ["sd", "Sandy squeezes her breasts together, creating a provocative cleavage just for your gaze"]
                ],
                # Line 8 - three variations
                [
                    ["sd", "Ahh! Your gaze is more powerful than a loaded pistol! Kills me with horniness, fuck!"],
                    ["sd", "Mmm! How do you manage to make me so excited without even touching me? You're killing me!"],
                    ["sd", "God in heaven! That look of yours is fucking me without you even touching me!"]
                ],
                # Line 9 - three variations
                [
                    ["", "She writhes under your intense gaze"],
                    ["", "Sandy starts moving sensually, responding to your dominating gaze"],
                    ["", "She breathes faster, clearly excited just by being observed by you"]
                ],
                # Line 10 - three variations
                [
                    ["sd", "Don't stop looking, you son of a bitch! So focused, so... animal!"],
                    ["sd", "Keep looking at me like that, fuck! You're driving me crazy!"],
                    ["sd", "Devour me with those eyes, shit! Never felt anything like this before!"]
                ],
                # Line 11 - three variations
                [
                    ["", "She shivers seeing the huge bulge in your pants"],
                    ["", "Sandy stares fixedly at the bulge in your pants, licking her lips"],
                    ["", "She can't take her eyes off your hard dick marking in your pants"]
                ],
                # Line 12 - three variations
                [
                    ["sd", "AHHHHH! HOLY SHIT! YES! Sandy moans, excited by your dominating gaze and your hard dick"],
                    ["sd", "FUCK! I'M CUMMING JUST FROM YOUR LOOK! You're an animal, Spoogebob!"],
                    ["sd", "BY THE DEVIL'S HORNS! YES! Never thought I'd cum just from being looked at like this!"]
                ]
            ]
        ]
        
        # If it's third time or later, we need to build a random sequence
        if vez >= 3:
            # We'll use the structure of the last sequence (index 3)
            sequencia_base = sequencias[3]
            sequencia_final = []
            
            # For each line, randomly choose one of the three variations
            import random
            for linha in sequencia_base:
                variacao_escolhida = random.choice(linha)
                sequencia_final.append(variacao_escolhida)
            
            return sequencia_final
        
        # If it's first or second time, return the original sequence
        return sequencias[vez]
    
    def obter_sequencia_punheta(vez):
        sequencias = [
            # First time
            [
                ["sd", "So... you want me to touch you? Fuck, you're so strange today, partner..."],
                ["sd", "Never did this before... guide me? Damn, why are you so anxious?"],
                ["", "Sandy approaches timidly, noticing your different expression"],
                ["sd", "Is this how it's done? Holy shit, why are you moaning like that?"],
                ["", "She starts moving her hand slowly, surprised by your exaggerated reaction"],
                ["sd", "Am I doing it right? By the devil's horns, never seen you so excited..."],
                ["", "You nod roughly, feeling the pleasure increase"],
                ["sd", "You're getting all wet, Spoogebob... is this normal for a Texas sponge?"],
                ["sd", "Should I go faster? You're shaking too much, cowboy..."],
                ["", "Your movements intensify"],
                ["you", "Ah! Sandy! Fuck, I'm going to...!"],
                ["", "You reach climax while Sandy watches fascinated and a little scared"]
            ],
            # Second time
            [
                ["sd", "Want to feel my hand again, you pervert? Fuck, you're so different now..."],
                ["sd", "I think I learned some tricks since last time..."],
                ["", "Sandy starts touching you with more confidence"],
                ["sd", "Like it when I do this? Holy shit, you don't react anything like before..."],
                ["", "She varies pressure and speed skillfully"],
                ["sd", "Mmm... you get so... strange when you're excited... you're harder than coral!"],
                ["sd", "Let's see how long you can take... son of a bitch..."],
                ["", "She suddenly accelerates the movements"],
                ["sd", "I know you're almost there... fuck, look at the thickness of this dick!!"],
                ["you", "Holy shit you mutant bitch I'm going to have to cum!!"],
                ["sd", "Go, Spoogebob! Cum for me!"],
                ["", "You have an intense orgasm in Sandy's hands, cum flew everywhere."]
            ],
            # Third time
            [
                ["sd", "Yeehaw! My little paw missed you, silly..."],
                ["sd", "I love seeing how you react to my touch..."],
                ["", "Sandy starts with slow and firm movements"],
                ["sd", "Look how hard you already are for me..."],
                ["sd", "My paws are furry but have a cold part too, don't they?"],
                ["", "She uses advanced techniques that make you dizzy with pleasure"],
                ["sd", "Enjoying it, Spoogebob? I learned this especially for you, fuck!"],
                ["", "You can barely respond, lost in sensations"],
                ["sd", "I want you to cum hard for me today... tiger"],
                ["sd", "Now, Spoogebob! Let it out!"],
                ["you", "SANDYYYYY! FUCK!"],
                ["", "You have the strongest orgasm of your life while Sandy realizes you're not who you say you are"]
            ],
            # Repetitions after completing
            [
                ["sd", "Let's see if I can beat my Texan record today, Spoogebob..."],
                ["sd", "I want to see how long you can take my special technique... you brute..."],
                ["", "Sandy envelops you with her experienced hands"],
                ["sd", "Like it when I squeeze here? And here? Holy shit, you moan so different from Spoogebob..."],
                ["", "She alternates between fast and slow movements, driving you crazy"],
                ["sd", "Your whole body is shaking, you like a good handjob huh"],
                ["sd", "Not yet, partner! I want to take you to the limit... in Texas we do it like this..."],
                ["", "You beg for relief while she controls your pleasure"],
                ["sd", "Now yes... you can cum for me... spurt everything on me!!!!"],
                ["you", "Ah! Ah! AH! SANDYYY! FUCK!"],
                ["sd", "That's it! Let it all out! Yeehaw!"],
                ["", "She smiles satisfied while you have a spectacular orgasm that almost reveals your identity"]
            ]
        ]
        
        if vez >= 3:
            return sequencias[3]
        return sequencias[vez]
    
    def obter_sequencia_buceta(vez):
        sequencias = [
            # First time
            [
                ["sd", "You really want to... see down there? By the devil's horns, you're different today..."],
                ["sd", "Nobody ever saw before... and I don't know why I feel like you never saw one either..."],
                ["", "Sandy slowly removes her shorts, with shyness"],
                ["sd", "So... what do you think, partner? Why do you have that stupid look?"],
                ["", "You look admiringly at her intimacy as if you'd never seen one"],
                ["you", "Fuck, it's beautiful, Sandy... much better than humans..."],
                ["sd", "Wow Spoogebob, you really like a Texas pussy..."],
                ["sd", "You can only look okay?"],
                ["", "You start drooling seeing that pussy all juicy staring at you"],
                ["sd", "You are..."],
                ["sd", "Drooling?!"],
                ["", "Sandy starts feeling used and decides to stop"]
            ],
            # Second time
            [
                ["sd", "Want to see my pussy again Spoogebob?"],
                ["sd", "Okay, but no funny business!"],
                ["", "Sandy removes her shorts with more confidence"],
                ["sd", "Enjoying it, partner? Your friend certainly is!"],
                ["", "Your dick gets so hard it starts throbbing"],
                ["sd", "Fuck! Your dick is even shaking hahaha"],
                ["sd", "You must be dying to fuck me right?"],
                ["", "You even try to answer but if you open your mouth you'll talk shit."],
                ["sd", "What's the problem buddy?"],
                ["sd", "Can't even see a little cowgirl pussy without losing control?"],
                ["sd", "Maybe you don't deserve to fuck me then..."],
                ["sd", "But don't think my pussy can't handle it..."]
            ],
            # Third time
            [
                ["sd", "I know I know"],
                ["sd", "Look good at it you son of a bitch!"],
                ["", "Sandy pulls her bikini down and opens her legs without hesitation"],
                ["sd", "Like what you see you dog?!"],
                ["", "Your dick hardens quickly"],
                ["sd", "Your dick grew faster than a lubricated measuring tape!"],
                ["sd", "And it's very thick too"],
                ["sd", "Keep looking at my pussy and jerk off for me"],
                ["sd", "Beat it good thinking about fucking me"],
                ["", "You masturbate in the middle of Sandy's house"],
                ["sd", "Keep beating until you feel the milk begging to come out"],
                ["sd", "My pussy is hotter than a fresh nut pie lol"]
            ],
            # Repetitions after completing
            [
                ["sd", "Don't get tired of seeing pussy huh?"],
                ["", "You immediately get hard"],
                ["sd", "Look but don't touch"],
                ["", "Your hands start shaking"],
                ["sd", "You know Spoogebob, this is getting normal for me"],
                ["sd", "Don't you think it's kind of weird to keep asking someone to show their pussy all the time?"],
                ["sd", "I certainly like it, but I'm just saying"],
                ["sd", "We've done this so many times that sometimes I show my pussy to the wall by impulse"],
                ["sd", "Oh sorry, your goal is just to jerk off"],
                ["sd", "Cum for me then you dog! I can even smell the semen already"]
            ]
        ]
        
        if vez >= 3:
            return sequencias[3]
        return sequencias[vez]
    
    def obter_sequencia_cuzinho(vez):
        sequencias = [
            # First time
            [
                ["sd", "You... want to try from behind? Holy shit, you're so perverted now, Spoogebob..."],
                ["sd", "Never did this before... be careful... fuck, I know you're too rough..."],
                ["", "Sandy turns around timidly, shaking a little"],
                ["sd", "Go really slow, okay? For God's sake, you don't seem to know how to control yourself..."],
                ["", "You start penetrating her with force and no technique"],
                ["sd", "Ow! Wait... it hurts a little... holy shit, you're too thick, you idiot!"],
                ["sd", "Maybe if we use more lubricant... fuck, you need to learn to be gentle!"],
                ["", "You try again, with a little less brutality"],
                ["sd", "Mmm... it's getting better... keep going like that... damn, don't be such an animal..."],
                ["", "You find a rhythm, still awkward"],
                ["sd", "Ah! It's different, but... it's actually good... even though you're a rough Texan..."],
                ["", "Sandy has a small orgasm, surprising herself despite your lack of skill"]
            ],
            # Second time
            [
                ["sd", "Want to try that again? Fuck, you were so clumsy last time..."],
                ["sd", "I'm a little less nervous today... but by the devil's horns, you need to be more careful..."],
                ["", "Sandy positions herself, more confident this time"],
                ["sd", "We still need to go slow... holy shit, don't be an animal like last time..."],
                ["", "You enter with less brutality this time"],
                ["sd", "Ah! That's it! It's better now! Damn, you're learning, Spoogebob..."],
                ["sd", "You can go a little deeper... but carefully, you Texan scrotum..."],
                ["", "You gradually increase the rhythm"],
                ["sd", "Spoogebob! This is... incredible! Fuck, you don't even seem like the same one anymore!"],
                ["sd", "Don't stop now! I'm enjoying it! Holy shit, who would've thought an impostor would fuck so well!"],
                ["", "You feel her contracting around you"],
                ["sd", "AHHHH! Sandy cums intensely, shaking all over"]
            ],
            # Third time
            [
                ["sd", "Spoogebob, I want to feel you inside my ass today... you tasty brute..."],
                ["sd", "I can barely wait... I'm already ready... for that 'sponge' dick of yours..."],
                ["", "Sandy positions herself anxiously"],
                ["sd", "You don't need to be so gentle this time... I already know you're an animal..."],
                ["", "You penetrate her with confidence, showing your true nature"],
                ["sd", "YES! Just like that! Harder! By the devil's horns, show who you really are!"],
                ["sd", "Fuck my ass, Spoogebob! Go deep! Holy shit!"],
                ["", "The rhythm becomes intense and wild"],
                ["sd", "I'm almost there! Don't stop! Wreck my ass!"],
                ["you", "Sandy! I'm going to cum too, fuck!"],
                ["sd", "TOGETHER! NOW! YOU DELICIOUS TEXAN!"],
                ["", "You reach climax simultaneously in an explosive orgasm"]
            ],
            # Repetitions after completing
            [
                ["sd", "Come on, cowboy. My Texan ass is impatient today..."],
                ["sd", "We don't need foreplay... stick it in without mercy!"],
                ["", "Sandy positions herself and offers herself without hesitation"],
                ["sd", "Fuck me real good today, Spoogebob... I love it..."],
                ["", "You penetrate her with force, knowing her limits well"],
                ["sd", "THAT'S IT! LIKE THAT! HARD! DAMN, YOU'RE AN ANIMAL, NOT A SPONGE!"],
                ["sd", "My God, Spoogebob! How do you make me feel this? Holy shit, you're so different now!"],
                ["", "You find the perfect rhythm you know works"],
                ["sd", "Go! Go! I'm almost there! By the devil's horns, show who you really are!"],
                ["you", "Sandy! I can't take it anymore, fuck!"],
                ["sd", "CUM INSIDE! I WANT TO FEEL IT!!"],
                ["", "You reach a mutual orgasm that seems to last forever"]
            ]
        ]
        
        if vez >= 3:
            return sequencias[3]
        return sequencias[vez]

    def obter_sequencia_boquete(vez):
        sequencias = [
            # First time
            [
                ["you", "You want to suck my dick? Come on, squirrel, show me what you know how to do."],
                ["sd", "Never did this before... but I'm curious, partner..."],
                ["", "Sandy kneels timidly in front of you"],
                ["sd", "Let me know if I do something wrong, okay? In Texas we don't usually practice this..."],
                ["", "She starts licking you gently"],
                ["you", "Fuck, what a strange sensation... but you're doing well, squirrel..."],
                ["you", "Go with more enthusiasm, squirrel, I don't have all day."],
                ["", "Sandy starts putting you in her mouth slowly"],
                ["sd", "Mmm... is this good, cowboy?"],
                ["you", "Yeah, it's getting better. Didn't know Texas squirrels sucked so well."],
                ["you", "Fuck, Sandy! This is awesome! I'm going to cum, shit!"],
                ["", "You reach climax while Sandy seems surprised, but satisfied"]
            ],
            # Second time
            [
                ["you", "Come here, squirrel, I want to feel that furry little mouth again."],
                ["sd", "I liked last time... learned some Texas tricks."],
                ["", "Sandy kneels with more confidence"],
                ["sd", "Relax there, Spoogebob. Today I'm going to give you more pleasure, partner."],
                ["", "She alternates between licks and sucks with more skill"],
                ["you", "That's it, fuck! Swallow this hard dick you whore!"],
                ["sd", "Sandy maintains eye contact while sucking you deeply"],
                ["sd", "Mmm... *slurp*... enjoying it, cowboy?"],
                ["", "She accelerates the rhythm, her mouth is so hot you go into a trance"],
                ["you", "Damn, Sandy! You're going to make me cum fast like this, fuck!"],
                ["sd", "Cum you bastard!"],
                ["", "You explode in her mouth, with your mouth open because you've lost facial control"]
            ],
            # Third time
            [
                ["you", "Bring that squirrel mouth over here again."],
                ["you", "Today I'm going to show you how to really suck."],
                ["", "Sandy kneels with an expression of desire"],
                ["sd", "Holy shit, this dick is always so clean! Doesn't even taste like piss and STDs like the ones in Texas!"],
                ["", "She starts with a perfect rhythm, knowing exactly what you like"],
                ["you", "You're lucky I live underwater because I'm not one to wash my dick..."],
                ["sd", "Sandy sucks you deeply, controlling her breathing like a professional"],
                ["sd", "Mmm... *deep throat*... *slurp*... yeehaw!"],
                ["you", "Fuck, how did a squirrel learn to do this? In prison there wasn't this..."],
                ["you", "Holy shit, Sandy! I'm going to fill your mouth, you little Texan slut!"],
                ["sd", "She seems surprised by your words, but doesn't stop sucking"],
                ["", "You cum violently in her throat, thinking about how easy it is to fool her"]
            ],
            # Repetitions after completing
            [
                ["you", "Hey squirrel, come suck my dick. I need to relax."],
                ["sd", "Right away tiger!"],
                ["", "Sandy kneels and already starts devouring you without hesitation"],
                ["sd", "Mmm... *glup*... *glup*... yeehaw, I love feeling you like this..."],
                ["", "She uses advanced techniques that make you see stars"],
                ["you", "Fuck, you got a lot better. Been sucking who?."],
                ["sd", "Sandy alternates between deep sucks and precise licks"],
                ["sd", "Mmm... I want to feel you exploding in my mouth again, cowboy..."],
                ["you", "You grab her head with force, controlling the rhythm"],
                ["you", "Holy shit! In prison this blowjob is worth more than 10 packs of cigarettes!"],
                ["sd", "Mmm... *glup*... *glup*... pris-"],
                ["", "Before she can process the sentence you flood her with cum"]
            ]
        ]
        
        if vez >= 3:
            return sequencias[3]
        return sequencias[vez]

    def obter_sequencia_foder_buceta(vez):
        sequencias = [
            # First time
            [
                ["you", "So, squirrel, how about feeling a real man inside you?"],
                ["sd", "Never did this before... but I trust you, Spoogebob... even though you're being so strange..."],
                ["", "Sandy lies down and opens her legs timidly"],
                ["sd", "I hope you're gentle, partner..."],
                ["", "You position yourself between her legs, laughing internally"],
                ["sd", "Ow! Easy, Spoogebob... go slow, by the devil's horns!"],
                ["you", "Damn, you're pretty tight huh?"],
                ["", "You find a rhythm, with you being more aggressive than Spoogebob would be"],
                ["sd", "Wow... you seem different today... more intense, fuck!"],
                ["", "The movements intensify, you don't have patience to go slow"],
                ["sd", "Spoogebob! This is... too intense! But... holy shit, I'm liking it!"],
                ["", "You cum inside her without warning, satisfied for dominating the situation"]
            ],
            # Second time
            [
                ["you", "I'm in the mood to stick it in you again."],
                ["sd", "Wow, Spoogebob... you're so... direct lately"],
                ["", "Sandy positions herself, a little surprised by your attitude"],
                ["sd", "You're very different, but I like this new energy of yours, by the devil's horns..."],
                ["", "You penetrate her without much ceremony"],
                ["you", "Fuck! Pussy is better than male ass!"],
                ["you", "Damn, Sandy! Your Texan pussy is very good!"],
                ["", "The rhythm increases, and you hit her hard"],
                ["sd", "Harder! Don't stop! Holy shit, you never fucked me like this before!"],
                ["you", "I'm going to fill this pussy with cum!"],
                ["sd", "Yes! Cum inside! Cum inside, fuck!"],
                ["", "You fill her completely, satisfied that she doesn't suspect anything"]
            ],
            # Third time
            [
                ["you", "Take off your clothes, squirrel. I'm going to fuck you now."],
                ["sd", "Wow, Spoogebob... you were never like this before... but damn, I love it, cowboy."],
                ["", "Sandy positions herself anxiously, already wet with excitement"],
                ["sd", "You know, I like this more aggressive side of you, fuck..."],
                ["", "You penetrate her with force, pulling her tail"],
                ["you", "FUCK! THAT'S IT! WRECK ME!"],
                ["you", "Swallow this whole dick, you fucking Texan squirrel!"],
                ["", "You find a wild and brutal rhythm"],
                ["sd", "Deeper! That's it! Tear me all up, by the devil's horns!"],
                ["you", "I'm going to fill you with cum, Texan!"],
                ["sd", "CUUUUM INSIDE! FLOOD ME ALL, FUCK!"],
                ["", "You have a violent orgasm, impressed how she doesn't realize you're not Spoogebob"]
            ],
            # Repetitions after completing
            [
                ["you", "Take off your clothes slut. Now."],
                ["sd", "Spoogebob, you're so bossy... holy shit, I love this dominating side of yours, cowboy."],
                ["", "Sandy positions herself on all fours, already knowing what you want"],
                ["you", "Fuck me hard, I want to feel you tearing me apart."],
                ["", "You penetrate her violently, pulling her hair"],
                ["you", "THAT'S IT! LIKE THAT! DESTROY MY LITTLE PUSSY FUUUCK!"],
                ["you", "Take this dick, slut! Spoogebob Squirtpants here is different now, fuck!"],
                ["", "You slap her ass while fucking hard"],
                ["sd", "Hit me more! Call me names! By the devil's horns, I love this!"],
                ["you", "I'm going to fill this Texan uterus with cum!"],
                ["sd", "YES! FLOOD ME WITH CUM, FUCK!"],
                ["", "You cum deeply in her, thinking about how many other women from the bottom of the sea you can fuck"]
            ]
        ]
        
        if vez >= 3:
            return sequencias[3]
        return sequencias[vez]

    def obter_sequencia_nozes_cuzinho(vez):
        sequencias = [
            # First time
            [
                ["you", "Hey, squirrel, how about shoving these nuts in your Texan ass?"],
                ["sd", "In my... what? Holy shit, that's... very strange, Spoogebob."],
                ["", "Sandy seems shocked, but also curious"],
                ["sd", "Look, I'm a Texan scientist, so... let's experiment, partner."],
                ["you", "You prepare the nuts with a malicious smile"],
                ["sd", "Is it going to hurt, fuck?"],
                ["you", "Definitely! Get on all fours now."],
                ["", "You start inserting the nuts one by one, without much care"],
                ["sd", "Ow! Easy! It's different, but... fuck, it's actually interesting."],
                ["", "While you continue, she starts moaning"],
                ["you", "Fuck, never imagined this would be so good, squirrel!"],
                ["", "Sandy has an unexpected orgasm, and you laugh at the perversion you managed to do with her"]
            ],
            # Second time or more
            [
                ["you", "Hey, brought more Texan nuts. I think your ass is hungry, squirrel."],
                ["sd", "Wow, Spoogebob... by the devil's horns, never imagined I'd like this so much."],
                ["", "Sandy positions herself anxiously on all fours"],
                ["sd", "Stick more this time, cowboy. I want to feel as much as possible, fuck!"],
                ["you", "You prepare the nuts, impressed with how perverted she became"],
                ["you", "Open your ass little squirrel!"],
                ["", "The nuts slide inside her with ease now"],
                ["sd", "That's it! Yes! Stick it deeper, holy shit!"],
                ["sd", "More! Put more! I want to feel them all inside me, for the love of Texas God!"],
                ["", "Her body trembles with each new nut inserted"],
                ["you", "Damn! This is too much, squirrel! I'm going to... going to..."],
                ["", "Sandy has an intense orgasm, and some nuts come out like projectiles, making you laugh"]
            ]
        ]
        
        if vez >= 1:
            return sequencias[1]
        return sequencias[vez]

# Define images for breast zoom sequence (after 3 times)
# These images will need to be created and placed in the game's images folder
image sandy_pes = "images/sandy/sandy_pes.png"
image sandy_pernas = "images/sandy/sandy_pernas.png"
image sandy_barriga = "images/sandy/sandy_barriga.png"
image sandy_peitos = "images/sandy/sandy_peitos.png"

# Ejaculation sound effect - this file needs to be placed in the sounds folder
define audio.porra = "audio/porra.mp3"