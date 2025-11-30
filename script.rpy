# script.rpy - Main Script File (English Version) - SAVE COMPATIBLE VERSION

# Define sounds for typing effects - EXPANDED SYSTEM
define audio.typing_bubbles = "bubbles.mp3"     # Sound for normal characters
define audio.typing_computer = "generic.mp3"    # Sound for narration/text without character
define audio.typing_karen = "metatones.mp3"    # Special sound for Karen (computer)
define audio.typing_evil = "evil_laugh.mp3"     # Evil sound for Plugton
define audio.typing_deep = "krotch_voice.mp3"   # Deep sound for Mr. Krotch
define audio.typing_robot = "robot_voice.mp3"   # Robot sound for special characters
define audio.music_fase1 = "bobesponja.mp3"      # Dias 1-4
define audio.music_fase2 = "sua_musica_fase2.mp3"  # Dias 5-9
define audio.music_fase3 = "sua_musica_fase3.mp3"  # Dia 10+

# Adicione esta função no bloco init python do script.rpy
init python:
    def tocar_musica_por_dia():
        """Toca a música apropriada baseada no dia atual"""
        if dia < 5:
            renpy.music.play(audio.music_fase1, channel="music", fadein=2.0, if_changed=True)
        elif dia < 10:
            renpy.music.play(audio.music_fase2, channel="music", fadein=2.0, if_changed=True)
        else:
            renpy.music.play(audio.music_fase3, channel="music", fadein=2.0, if_changed=True)
            
# Code to control typing sound - SAVE COMPATIBLE VERSION
init python:
    # Global variable to control if sound is playing
    typing_sound_playing = False
    
    # ORIGINAL FUNCTION - Keep for save compatibility
    def typing_sound_callback(event, **kwargs):
        global typing_sound_playing
        
        if event == "show":
            # Start sound when text begins to show
            renpy.music.play(audio.typing_bubbles, channel="sound", loop=True)
            typing_sound_playing = True
        
        elif event == "slow_done" or event == "end":
            # Stop sound when all typing is done
            if typing_sound_playing:
                renpy.music.stop(channel="sound")
                typing_sound_playing = False
    
    # Function for narration callback (texts without character)
    def narration_sound_callback(event, **kwargs):
        global typing_sound_playing
        
        if event == "show":
            # Start sound when text begins to show
            renpy.music.play(audio.typing_computer, channel="sound", loop=True)
            typing_sound_playing = True
        
        elif event == "slow_done" or event == "end":
            # Stop sound when all typing is done
            if typing_sound_playing:
                renpy.music.stop(channel="sound")
                typing_sound_playing = False
    
    # Character-specific callbacks for different sounds
    def karen_callback(event, **kwargs):
        global typing_sound_playing
        
        if event == "show":
            renpy.music.play(audio.typing_karen, channel="sound", loop=True)
            typing_sound_playing = True
        elif event == "slow_done" or event == "end":
            if typing_sound_playing:
                renpy.music.stop(channel="sound")
                typing_sound_playing = False
    
    def deep_callback(event, **kwargs):
        global typing_sound_playing
        
        if event == "show":
            renpy.music.play(audio.typing_deep, channel="sound", loop=True)
            typing_sound_playing = True
        elif event == "slow_done" or event == "end":
            if typing_sound_playing:
                renpy.music.stop(channel="sound")
                typing_sound_playing = False

# Definindo o narrador com callback de narração
define narrator = Character(None, callback=narration_sound_callback)

# DEFINIÇÕES DE PERSONAGENS - SISTEMA DE SOM SIMPLIFICADO

# TODOS os personagens usem som padrão de bolhas (bubbles.mp3) automaticamente
# através do callback global - EXCETO Karen e Mr. Krotch que têm callbacks específicos
define p = Character("Fatrick Star")
define bs = Character("Spoogebob Squirtpants")
define sd = Character("Sandy Cunts", who_color="#ff69b4")
define prl = Character("Purrl", who_color="#ff69b4")
define l = Character("Larry the Pornstar", who_color="#ff4400")
define puff = Character("Mrs. Puffy", who_color="#ff69b4")
define lou = Character("Lou (Angry Employee)", who_color="#8B0000")
define plug = Character("Plugton", who_color="#00ff00")
define h = Character("Flying Fuckman", color="#34A65F")
define b = Character("You", who_color="#ffff00")
define you = Character("You", who_color="#ffff00") 
define y = Character("You", who_color="#ffff00")

# APENAS estes dois têm callbacks específicos:
define karen = Character("Karen (Computer Wife)", who_color="#ff00ff", callback=karen_callback)
define k = Character("Mr. Krotch", callback=deep_callback)

# Imagens de fundo
image fundo_dia = "fundo_dia.jpg"
image fundo_noite = "fundo_noite.jpg"

# Função para exibir fundo
label mostrar_fundo():
    if hora_do_dia >= 6 and hora_do_dia < 18:
        show fundo_dia
    else:
        show fundo_noite
    return 

# Label de teste para sistema dia/noite
label inicio:
    call mostrar_fundo from _call_mostrar_fundo
    "It's dawn."
    
    "Do you want to wait or continue?"
    
    menu:
        "Wait":
            $ hora_do_dia += 6
            call mostrar_fundo from _call_mostrar_fundo_1
            "Now it's [hora_do_dia] o'clock."
        "Continue":
            "You moved forward."

    return

# Função para avançar tempo
label avancar_tempo():
    $ hora_do_dia += 6
    if hora_do_dia >= 24:
        $ hora_do_dia = 0
    return

# Início principal do jogo
label start:
    # Tocar música de fundo
    play music "bobesponja.mp3" fadein 2.0
    
    # Variáveis do jogo - Valores padrão
    default contrap1 = False
    default nugget = False 
    default mainmap = False
    default money = 0
    default macaca = False
    default sala_mensagem_exibida = False
    default hora_do_dia = 8
    default mapa_disponivel = False
    
    # Definições de som
    define som_opcao = "open.wav"
    
    $ money = 0 

    # Sobrescrever comportamento padrão do menu para tocar som
    init python:
        # Armazenar referência ao menu original
        original_menu = renpy.display_menu

        # Função personalizada para tocar som ao escolher
        def custom_menu(choices, *args, **kwargs):
            # Tocar som quando jogador faz escolha
            renpy.play(som_opcao, channel="sound")
            # Chamar menu original
            return original_menu(choices, *args, **kwargs)
        
        # Configure callback global APENAS para personagens sem callback específico
        # Isso fará com que todos os personagens (exceto Karen e Mr. Krotch) usem bubbles.mp3
        config.all_character_callbacks.append(typing_sound_callback)

    # Começar a cutscene principal
    jump cutscene

# Sequência principal da cutscene
label cutscene:
    # Começar com música de suspense
    scene disclaimer

    pause 2.0
    
    play music "susmusic.mp3" fadein 2.0
    play audio "bubaus.mp3" fadein 1.0

    show ingameburuba with fade

    "Uh... what?"
    show cutscene2 with fade
    
    "What is that? A pineapple?!"
    
    show cuts1

    bs "La lala lala"

    # Quando franky aparece, tocar o grito
    play audio "classicdrama.mp3"
    play audio "gritobob.mp3" volume 0.18
    show frankys with hpunch

    bs "AHHHHHHHHHHH"
    
    # Fade para tela preta depois da última imagem
    scene black with fade
    
    # Tocar som de rasgar na tela preta
    play audio "rasgazzo.mp3"
    # Esperar um pouco para o som tocar
    pause 5.0

    play audio "gritobob.mp3" volume 0.18
    bs "NO! STOP! MY CLOTHES! MY FACE! WHAT ARE YOU DOING!"
    play audio "franklaugh.mp3"
    you "SHUT THE FUCK UP!"

    scene black with fade
    play audio "fewmom.mp3"

    show fewmom

    pause 3.0
    
    show screen xerequinha 
    stop audio
    stop sound
    stop music
    stop audio

    # Jump para room4 que está definido no room4.rpy
    jump room4

# Fim do arquivo script principal