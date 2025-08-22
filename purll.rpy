# perola.rpy - Pearl's Financial Discovery Scene (English) - VERSÃO PALAVRÃO E GROSSERIA

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

# Pearl images
image perola_normal = "images/perola_normal.png"
image perola_furiosa = "images/perola_furiosa.png"
image perola_suspeita = "images/perola_suspeita.png"
image perola_envergonhada = "images/perola_envergonhada.png"
image perola_irritada = "images/perola_irritada.png"
image envelopes_dinheiro = "images/envelopes_scattered.png"

# Sound effects
define audio.porta_batendo = "porta_slam.mp3"
define audio.papeis_caindo = "papers_scatter.mp3"

# Pearl's financial discovery scene - MAIN EVENT
label descoberta_financeira_perola:
    # This scene triggers automatically when entering Krusty Krotch after day 12
    scene lobbykrab
    
    # Dramatic door slam
    play sound audio.porta_batendo volume 0.8
    with hpunch
    
    # Pearl bursts through the door
    show perola_furiosa at center with moveinright
    
    prl "PAI! EU VI AS CONTAS DO SEU CARTÃO, SEU VELHO TARADO!"
    
    # Mr. Krotch comes running from his office
    show krabpanico at right with moveinright
    
    k "PÉROLA! PORRA! O que você está fazendo aqui?!"
    
    # Pearl waves credit card statements angrily
    show perola_furiosa at center
    
    prl "VOCÊ GASTOU $500 EM QUÊ?! BONECAS INFLÁVEIS?! SEU PERVERTIDO NOJENTO!"
    
    # Mr. Krotch panics and looks around nervously
    hide krabpanico
    show krab nervoso at right
    
    k "Pérola! Caralho! Não é bem assim..."
    
    # Pearl gets even more furious
    prl "E AINDA TEM UMAS COMPRAS ESTRANHAS! 'CAMISINHAS'?! 'LIVROS ADULTOS'?!"
    prl "QUE PORRA É ESSA, PAI?! VOCÊ VIROU UM TARADO COMPLETO?!"
    
    # She scatters papers on the floor
    play sound audio.papeis_caindo
    show envelopes_dinheiro at center with vpunch
    
    prl "EXPLICA ESSA MERDA TODA!"
    
    # Pearl turns to look at the player suspiciously
    hide perola_furiosa
    show perola_suspeita at center
    
    prl "E você, Spoogebob... você sabia dessa putaria toda?"
    
    # Player interaction menu
    menu:
        "Defender o velho tarado":
            $ escolha_perola = "defender"
            jump defender_krotch_grosso
            
        "Fingir demência":
            $ escolha_perola = "ignorar"
            jump fingir_que_eh_burro
            
        "Zoar a situação":
            $ escolha_perola = "sarcastico"
            jump zoar_perola

# Option 1: Defend Mr. Krotch (but being dumb and rude)
label defender_krotch_grosso:
    b "Ué, sua baleia gorda, seu pai é homem ou não é?"
    b "Todo macho precisa de umas coisas... se você me entende."
    
    # Pearl gets furious with the insult
    hide perola_suspeita
    show perola_furiosa at center
    
    prl "BALEIA GORDA?! QUEM VOCÊ PENSA QUE É, SEU BOSTA?!"
    prl "E QUE PORRA É ESSA DE 'TODO MACHO'?!"
    
    # Mr. Krotch tries to calm down but makes it worse
    hide krab nervoso
    show krab sudando at right
    
    k "Calma, Pérola... o Spoogebob só está sendo... masculino..."
    
    b "Exato, poha! Homem que é homem não fica escondendo essas coisas."
    b "Pelo menos ele não tá pegando puta na rua, né?"
    
    # Pearl is shocked by the crude language
    hide perola_furiosa
    show perola_chocada at center
    
    prl "DESDE QUANDO VOCÊ FALA ASSIM, SPOOGEBOB?!"
    prl "VOCÊ ERA EDUCADO! INOCENTE!"
    prl "AGORA PARECE UM... UM... BANDIDO!"
    
    b "Bandido é o caralho! Só cresci e parei de ser otário!"
    
    hide perola_chocada
    show perola_muito_suspeita at center
    
    prl "CRESCEU?! OU VIROU OUTRA PESSOA?!"
    prl "EU VOU DESCOBRIR QUE PORRA ESTÁ ACONTECENDO AQUI!"
    
    $ perola_suspeita_nivel += 3
    $ perola_quer_vinganca = True
    $ perola_descoberta_financeira = True
    
    jump final_descoberta_perola_grosso

# Option 2: Play dumb (very dumb)
label fingir_que_eh_burro:
    # Player acts like a complete idiot
    b "Que? Que tá acontecendo? Eu tava pensando em... uh... hambúrguer..."
    b "Que boneca inflável? É pra festa de aniversário?"
    
    # Pearl gets irritated by the stupidity
    hide perola_suspeita
    show perola_irritada at center
    
    prl "FESTA DE ANIVERSÁRIO?! SEU IDIOTA!"
    prl "BONECA INFLÁVEL SEXUAL, CARALHO!"
    
    b "Sexual? Que isso? Nunca ouvi falar..."
    b "Deve ser tipo aquelas bonecas que falam quando aperta, né?"
    
    # Mr. Krotch facepalms
    hide krab nervoso
    show krab vergonha at right
    
    k "Spoogebob... pelo amor de Netuno..."
    
    # Pearl realizes he's either very stupid or pretending
    hide perola_irritada
    show perola_suspeita at center
    
    prl "Ou você ficou retardado... ou está fingindo ser burro!"
    prl "O Spoogebob que eu conhecia era inocente, mas não era BURRO!"
    
    b "Eh... burro sou eu mesmo... hehe..."
    
    hide perola_suspeita
    show perola_determinada at center
    
    prl "ALGUMA COISA ESTÁ MUITO ERRADA AQUI!"
    prl "VOU INVESTIGAR ESSA MERDA TODA!"
    
    $ perola_suspeita_nivel += 2
    $ perola_quer_vinganca = True
    $ perola_descoberta_financeira = True
    
    jump final_descoberta_perola_grosso

# Option 3: Mock the situation (crude and offensive)
label zoar_perola:
    b "Relaxa aí, princesinha. Pelo menos seu pai não tá gastando com drogas."
    b "E outra, boneca inflável é mais barata que mulher de verdade."
    b "Sem falar que não enche o saco nem pede dinheiro."
    
    # Everyone is shocked by the crude response
    hide perola_suspeita
    show perola_chocada at center
    
    prl "QUE PORRA VOCÊ ACABOU DE FALAR?!"
    
    hide krab nervoso
    show krab surpreso at right
    
    k "SPOOGEBOB! QUE COMENTÁRIO FOI ESSE?!"
    
    b "Comentário de homem experiente, velhão."
    b "Sua filha que é muito inexperiente pra entender essas coisas."
    
    # Pearl gets extremely angry
    hide perola_chocada
    show perola_furiosa at center
    
    prl "INEXPERIENTE?! SEU FILHO DA PUTA!"
    prl "QUEM VOCÊ PENSA QUE É PRA FALAR COMIGO ASSIM?!"
    prl "VOCÊ NÃO É O SPOOGEBOB! O SPOOGEBOB NUNCA FALARIA ESSA MERDA!"
    
    b "Falaria sim, só que agora eu tenho culhões pra falar a verdade."
    
    hide perola_furiosa
    show perola_muito_suspeita at center
    
    prl "CULHÕES?! DESDE QUANDO VOCÊ USA ESSA PALAVRA?!"
    prl "VOCÊ PARECE UM EX-PRESIDIÁRIO, SEU DESGRAÇADO!"
    
    # Dangerous territory - too close to truth
    b "Ex-presidiário é o caralho! Só parei de ser frouxo!"
    
    hide perola_muito_suspeita
    show perola_determinada at center
    
    prl "EU VOU DESCOBRIR QUEM VOCÊ É DE VERDADE!"
    prl "E QUANDO DESCOBRIR, VOU FERRAR COM VOCÊ!"
    
    $ perola_suspeita_nivel += 4
    $ perola_quer_vinganca = True
    $ perola_descoberta_financeira = True
    
    jump final_descoberta_perola_grosso

# Final scene conclusion (crude version)
label final_descoberta_perola_grosso:
    # Mr. Krotch tries to end the confrontation
    hide krab vergonha
    hide krab surpreso
    hide krab sudando
    show krab nervoso at right
    
    k "Bom... já que conversamos sobre essa merda toda..."
    k "Que tal você ir pra casa, Pérola?"
    
    # Pearl's reaction depends on suspicion level and revenge desire
    if perola_suspeita_nivel >= 4:
        hide perola_determinada
        show perola_vingativa at center
        
        prl "IR PRA CASA UMA PORRA!"
        prl "EU VOU FICAR AQUI E DESCOBRIR QUE MERDA VOCÊS ESTÃO APRONTANDO!"
        prl "E VOCÊ, SEU FALSO... EU VOU TE FODER!"
        
        k "Pérola, linguagem!"
        
        prl "LINGUAGEM O CARALHO, PAI!"
        prl "ESSE DESGRAÇADO AÍ NÃO É O SPOOGEBOB!"
        prl "E EU VOU PROVAR ISSO!"
        
        # She gives player her address aggressively
        prl "SABE DE UMA COISA? VEM NA MINHA CASA DEPOIS!"
        prl "EU MORO NA RUA DAS BALEIAS, NÚMERO 69!"
        prl "VEM LÁ PRA GENTE CONVERSAR DIREITO, SEU BOSTA!"
        
        $ perola_no_restaurante = True
        $ conheceu_perola = True
        $ endereco_perola_descoberto = True
        
    elif perola_suspeita_nivel >= 3:
        hide perola_determinada
        show perola_irritada at center
        
        prl "Tá bom, vou embora... MAS ISSO NÃO VAI FICAR ASSIM!"
        prl "EU VOU DESCOBRIR QUE PORRA ESTÁ ACONTECENDO!"
        prl "E você, 'Spoogebob'... a gente vai ter uma conversinha em casa!"
        
        # She gives address as threat
        prl "EU MORO NA RUA DAS BALEIAS, 69! APARECE LÁ SE TIVER CULHÕES!"
        
        $ conheceu_perola = True
        $ endereco_perola_descoberto = True
        
    else:
        hide perola_irritada
        show perola_envergonhada at center
        
        prl "Tá... desculpa ter gritado, pai."
        prl "Mas essa merda foi constrangedora pra caralho!"
        prl "Da próxima vez avisa antes de comprar essas putarias!"
        
        $ conheceu_perola = True
    
    # Pearl's final threat/invitation
    if endereco_perola_descoberto:
        if perola_quer_vinganca:
            prl "E NÃO ESQUECE: RUA DAS BALEIAS, 69!"
            prl "VEM LÁ PRA GENTE ACERTAR AS CONTAS!"
        else:
            prl "Se quiser conversar sobre isso direito, me procura em casa."
            prl "Rua das Baleias, 69. Mas só se for pra conversar como gente civilizada!"
    
    # Pearl exits
    if perola_no_restaurante:
        hide perola_vingativa
        show perola_observando at left
        
        "Pearl positions herself in a corner, watching you with hatred..."
        "She's planning something. This is very dangerous."
        
    else:
        hide perola_irritada
        hide perola_envergonhada
        
        prl "TCHAU, PAI! TCHAU, 'SPOOGEBOB'!"
        
        hide perola_irritada with moveoutleft
        hide perola_envergonhada with moveoutleft
        
        "Pearl leaves, but her threats echo in the air..."
        if endereco_perola_descoberto:
            "You now know where she lives. This could be useful... or dangerous."
    
    # Mr. Krotch's reaction
    hide krab nervoso
    show krab preocupado at center
    
    k "Puta merda, Spoogebob... isso foi... complicado pra caralho."
    k "Minha filha nunca teve essa linguagem... ela tá puta da vida."
    
    if perola_suspeita_nivel >= 3:
        k "E cuidado com a Pérola. Ela é esperta e vingativa..."
        k "Se ela descobrir alguma coisa... a gente tá fodido."
    
    if endereco_perola_descoberto:
        k "E ela te deu o endereço... isso pode ser uma armadilha."
        k "Ou uma oportunidade, sei lá... você que sabe."
    
    $ ultima_interacao_perola = dia
    
    # Return to restaurant normal flow
    jump cozinha

# Pearl interaction menu (if she stays in restaurant)
label interagir_com_perola:
    if not perola_no_restaurante:
        "Pearl is not here right now."
        jump cozinha
    
    scene lobbykrab
    show perola_observando at left
    
    prl "E aí, seu merda? Vamos conversar?"
    
    menu:
        "Sobre o quê, baleia?":
            jump conversa_perola_agressiva
            
        "Não tenho tempo pra suas babaquices":
            jump evitar_perola_grosso
            
        "Para de me encher o saco":
            jump confrontar_perola_grosso

# Aggressive conversation with Pearl
label conversa_perola_agressiva:
    prl "BALEIA?! SEU FILHO DA PUTA!"
    prl "SOBRE O FATO DE VOCÊ SER UM IMPOSTOR, DESGRAÇADO!"
    
    menu:
        "Impostor é o caralho":
            prl "ENTÃO PROVE QUE VOCÊ É O SPOOGEBOB MESMO!"
            jump teste_identidade_perola_grosso
            
        "Você tá louca, garota":
            prl "LOUCA É A PUTA QUE TE PARIU!"
            prl "EU SEI QUE TEM ALGO ERRADO!"
            $ perola_suspeita_nivel += 1
            
        "Quer parar de frescura?":
            prl "FRESCURA?! EU VOU TE MOSTRAR FRESCURA!"
            prl "VEM NA MINHA CASA PRA GENTE RESOLVER ISSO!"
            $ perola_suspeita_nivel += 1
    
    jump final_conversa_perola_grosso

# Avoid Pearl (rude version)
label evitar_perola_grosso:
    prl "FUGINDO DE MIM, SEU COVARDE?!"
    prl "O SPOOGEBOB VERDADEIRO NUNCA FUGIRIA DE UMA CONVERSA!"
    
    b "Fugindo uma merda! Só não tenho tempo pra suas paranóias!"
    
    prl "PARANÓIAS?! EU VOU TE MOSTRAR PARANÓIA!"
    prl "APARECE NA MINHA CASA SE TIVER PEITO!"
    
    $ perola_suspeita_nivel += 1
    $ endereco_perola_descoberto = True
    
    jump final_conversa_perola_grosso

# Confront Pearl (very rude)
label confrontar_perola_grosso:
    prl "PARA DE ME ENCHER O SACO?!"
    prl "QUEM TÁ ENCHENDO O SACO É VOCÊ, SEU FALSO!"
    
    b "Falso é o caralho! Você que tá criando caso!"
    
    prl "ENTÃO PROVE QUE VOCÊ É O SPOOGEBOB!"
    prl "VEM NA MINHA CASA E PROVA!"
    
    menu:
        "Beleza, vou na sua casa sim":
            prl "ÓTIMO! RUA DAS BALEIAS, 69!"
            prl "VEM LÁ PRA GENTE RESOLVER ESSA MERDA!"
            $ endereco_perola_descoberto = True
            
        "Não vou na casa de maluca":
            prl "MALUCA?! SEU BOSTA!"
            prl "ENTÃO EU VOU TORNAR SUA VIDA UM INFERNO AQUI!"
            $ perola_suspeita_nivel += 2
            
        "Só se for pra outras coisas...":
            prl "OUTRAS COISAS?! QUE PORRA VOCÊ TÁ INSINUANDO?!"
            prl "SEU TARADO NOJENTO!"
            $ perola_suspeita_nivel += 2
    
    jump final_conversa_perola_grosso

# Identity test (crude version)
label teste_identidade_perola_grosso:
    prl "BELEZA, RESPONDE ISSO: QUAL É O NOME DO MEU PEIXINHO DE ESTIMAÇÃO?"
    
    menu:
        "Que peixinho, porra?":
            prl "COMO ASSIM 'QUE PEIXINHO'?! SEU MENTIROSO!"
            prl "VOCÊ CONVERSOU COMIGO SOBRE ELE SEMANA PASSADA!"
            $ perola_suspeita_nivel += 2
            
        "Sei lá... Gary?":
            prl "GARY É SEU, SEU IDIOTA!"
            prl "MEU PEIXE SE CHAMA ALGERNON!"
            $ perola_suspeita_nivel += 2
            
        "Não lembro dessa merda":
            prl "NÃO LEMBRA?! COMO NÃO LEMBRA?!"
            prl "SEU IMPOSTOR DE MERDA!"
            $ perola_suspeita_nivel += 2
    
    prl "EU SABIA! VOCÊ NÃO É O SPOOGEBOB!"
    prl "VEM NA MINHA CASA PRA GENTE ACERTAR ISSO!"
    
    $ endereco_perola_descoberto = True
    
    jump final_conversa_perola_grosso

# Final conversation (crude version)
label final_conversa_perola_grosso:
    if perola_suspeita_nivel >= 6:
        hide perola_observando
        show perola_determinada at left
        
        prl "EU TENHO CERTEZA! VOCÊ NÃO É O SPOOGEBOB!"
        prl "EU VOU DESCOBRIR QUEM VOCÊ É E FODER COM VOCÊ!"
        prl "RUA DAS BALEIAS, 69! NÃO ESQUECE!"
        
        "EXTREME DANGER! Pearl is convinced you're an impostor!"
        "She wants revenge and knows where you 'live'. This is very bad."
        
    elif perola_suspeita_nivel >= 4:
        hide perola_observando
        show perola_suspeita at left
        
        prl "TEM ALGO MUITO ERRADO AQUI..."
        prl "EU VOU FICAR DE OLHO EM VOCÊ, SEU MERDA."
        prl "E SE EU DESCOBRIR QUE VOCÊ TÁ ME ENGANANDO..."
        
        "Pearl is very suspicious and planning something."
        
    else:
        prl "Bom... talvez eu esteja sendo paranóica mesmo..."
        prl "Mas você ainda tá estranho pra caralho."
    
    if endereco_perola_descoberto and not perola_quer_vinganca:
        prl "Se quiser conversar direito, aparece lá em casa."
        prl "Rua das Baleias, 69. Mas sem sacanagem!"
    
    $ ultima_interacao_perola = dia
    jump cozinha

# Function to check if Pearl discovery should trigger
init python:
    def deve_ativar_descoberta_perola():
        global dia, perola_descoberta_financeira
        return dia >= 12 and not perola_descoberta_financeira