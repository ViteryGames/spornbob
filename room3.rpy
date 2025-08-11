label room3:
  "Money = [money]"
  
  scene bg room3

  "Welcome to room 3"with fade
  

  menu: 
     "Leave":
       call screen mapScreen
      
     "Work at the Chum Bucket":
       $ money += 1
       "[money]" 

  menu: 
     "Leave":
       call screen mapScreen

     "Work at the Chum Bucket":
       $ money += 2
       "[money]" 

  menu: 
     "Leave":
       call screen mapScreen  

### Jogo de Pôquer "Apostando Segredos" - Batavo Esponja ###
# Este código implementa um minijogo de pôquer simplificado onde o jogador (Batavo)
# aposta contra Plankton para ganhar segredos sobre os personagens da Fenda do Biquíni

# Definições de imagens para cartas e fundos
init python:
    # Importações necessárias
    import random

    # Definição das cartas
    NAIPES = ['copas', 'espadas', 'ouros', 'paus']
    VALORES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    # Classe para representar uma carta
    class Carta:
        def __init__(self, naipe, valor):
            self.naipe = naipe
            self.valor = valor
            
        def __str__(self):
            return f"{self.valor} de {self.naipe}"
            
        # Para comparação de cartas
        def valor_numerico(self):
            if self.valor == 'A':
                return 14
            elif self.valor == 'K':
                return 13
            elif self.valor == 'Q':
                return 12
            elif self.valor == 'J':
                return 11
            else:
                return int(self.valor)
    
    # Classe para o baralho
    class Baralho:
        def __init__(self):
            self.cartas = []
            for naipe in NAIPES:
                for valor in VALORES:
                    self.cartas.append(Carta(naipe, valor))
            self.embaralhar()
            
        def embaralhar(self):
            random.shuffle(self.cartas)
            
        def tirar_carta(self):
            if len(self.cartas) > 0:
                return self.cartas.pop()
            else:
                return None
    
    # Classe para avaliar mãos de pôquer
    class AvaliadorMao:
        @staticmethod
        def avaliar(cartas):
            # Ordenar cartas por valor
            cartas_ordenadas = sorted(cartas, key=lambda carta: carta.valor_numerico())
            
            # Verificar combinações
            if AvaliadorMao.tem_par(cartas_ordenadas):
                return 1, "Par"
            if AvaliadorMao.tem_dois_pares(cartas_ordenadas):
                return 2, "Dois Pares" 
            if AvaliadorMao.tem_trinca(cartas_ordenadas):
                return 3, "Trinca"
            if AvaliadorMao.tem_sequencia(cartas_ordenadas):
                return 4, "Sequência"
            if AvaliadorMao.tem_flush(cartas_ordenadas):
                return 5, "Flush"
            if AvaliadorMao.tem_full_house(cartas_ordenadas):
                return 6, "Full House"
            if AvaliadorMao.tem_quadra(cartas_ordenadas):
                return 7, "Quadra"
            if AvaliadorMao.tem_straight_flush(cartas_ordenadas):
                return 8, "Straight Flush"
            if AvaliadorMao.tem_royal_flush(cartas_ordenadas):
                return 9, "Royal Flush"
            
            # Se nenhuma combinação especial
            return 0, "Carta Alta"
        
        @staticmethod
        def tem_par(cartas):
            valores = [carta.valor for carta in cartas]
            for valor in VALORES:
                if valores.count(valor) >= 2:
                    return True
            return False
            
        @staticmethod
        def tem_dois_pares(cartas):
            valores = [carta.valor for carta in cartas]
            pares = 0
            for valor in VALORES:
                if valores.count(valor) >= 2:
                    pares += 1
            return pares >= 2
            
        @staticmethod
        def tem_trinca(cartas):
            valores = [carta.valor for carta in cartas]
            for valor in VALORES:
                if valores.count(valor) >= 3:
                    return True
            return False
            
        @staticmethod
        def tem_sequencia(cartas):
            valores_numericos = [carta.valor_numerico() for carta in cartas]
            valores_numericos.sort()
            
            # Verificar sequência normal
            for i in range(1, len(valores_numericos)):
                if valores_numericos[i] != valores_numericos[i-1] + 1:
                    return False
            return True
            
        @staticmethod
        def tem_flush(cartas):
            naipe = cartas[0].naipe
            for carta in cartas:
                if carta.naipe != naipe:
                    return False
            return True
            
        @staticmethod
        def tem_full_house(cartas):
            valores = [carta.valor for carta in cartas]
            tem_trinca = False
            tem_par = False
            
            for valor in VALORES:
                if valores.count(valor) == 3:
                    tem_trinca = True
                elif valores.count(valor) == 2:
                    tem_par = True
                    
            return tem_trinca and tem_par
            
        @staticmethod
        def tem_quadra(cartas):
            valores = [carta.valor for carta in cartas]
            for valor in VALORES:
                if valores.count(valor) >= 4:
                    return True
            return False
            
        @staticmethod
        def tem_straight_flush(cartas):
            return (AvaliadorMao.tem_sequencia(cartas) and 
                    AvaliadorMao.tem_flush(cartas))
                    
        @staticmethod
        def tem_royal_flush(cartas):
            if not AvaliadorMao.tem_flush(cartas):
                return False
                
            valores = [carta.valor for carta in cartas]
            return (('10' in valores) and 
                    ('J' in valores) and 
                    ('Q' in valores) and 
                    ('K' in valores) and 
                    ('A' in valores))
    
    # Sistema de trapaça
    class SistemaTrapaça:
        def __init__(self):
            self.nivel_suspeita = 0
            self.max_suspeita = 100
            
        def trocar_carta(self, baralho, carta_desejada):
            # Aumenta a suspeita
            self.nivel_suspeita += 15
            # Retorna a carta desejada
            return carta_desejada
            
        def espiar_mao_oponente(self):
            # Aumenta bastante a suspeita
            self.nivel_suspeita += 25
            return True
            
        def marcar_cartas(self):
            # Suspeita moderada
            self.nivel_suspeita += 20
            return True
            
        def resetar_suspeita(self):
            self.nivel_suspeita = 0
            
        def ser_pego(self):
            return random.random() * 100 < self.nivel_suspeita

    # Lista de segredos que podem ser apostados/ganhos
    SEGREDOS = {
        # Segredos do Sr. Siriguejo
        "siririca_1": "O Siririca esconde uma segunda cópia da fórmula em uma caixa dentro do colchão.",
        "siririca_2": "O Siririca tem um relacionamento secreto com a Sra. Puff.",
        "siririca_3": "O Siririca tem um cofre escondido sob o assoalho de seu escritório.",
        "siririca_4": "A senha do cofre do Siririca são os números do aniversário da filha dele: 2-4-7-6.",
        "siririca_5": "O Siririca tem pavor de formigas depois de um incidente em sua juventude.",
        
        # Segredos do Lula Molusco
        "lula_1": "O Lula Molusco tem uma coleção de fotos da Sandy em seu quarto.",
        "lula_2": "O Lula Molusco já tentou fugir da Fenda do Biquíni 8 vezes.",
        "lula_3": "O Lula Molusco secretamente admira o talento musical de Patrick.",
        "lula_4": "O Lula Molusco tem uma peruca escondida para ocasiões especiais.",
        "lula_5": "O verdadeiro nome do Lula Molusco é Alfredo.",
        
        # Segredos da Sandy
        "sandy_1": "A Sandy foi banida do Texas por um experimento que deu errado.",
        "sandy_2": "A Sandy mantém um diário onde admite sentir atração pelo Bob Esponja.",
        "sandy_3": "O oxigênio na cúpula da Sandy é parcialmente sintético e causa leve euforia.",
        "sandy_4": "A Sandy tem um dispositivo que pode drenar todo o oceano em 24 horas.",
        "sandy_5": "A Sandy consegue ficar sem seu capacete por até 1 hora com treinamento especial.",
        
        # Segredos do Patrick
        "patrick_1": "O Patrick é na verdade um gênio que finge ser burro.",
        "patrick_2": "O Patrick é o verdadeiro herdeiro de um reino submarino distante.",
        "patrick_3": "Sob a pedra do Patrick existe uma mansão subterrânea luxuosa.",
        "patrick_4": "O Patrick sabe exatamente onde está o verdadeiro Bob Esponja.",
        "patrick_5": "O Patrick já foi casado três vezes, mas ninguém se lembra disso.",
        
        # Segredos do próprio Plankton
        "plankton_1": "Karen não é realmente esposa do Plankton, mas sim sua carcereiro.",
        "plankton_2": "Plankton e Sr. Siriguejo já foram melhores amigos na infância.",
        "plankton_3": "Plankton já provou o Hambúrguer de Siri uma vez e não achou tão bom assim.",
        "plankton_4": "Plankton tem um clone dele mesmo que pode ativar em emergências.",
        "plankton_5": "Plankton não quer a fórmula para o negócio, mas para um experimento genético."
    }

# Variáveis do jogo de pôquer
default poker_dinheiro_jogador = 1000
default poker_dinheiro_plankton = 1000
default segredos_descobertos = []
default nivel_trapaca = 0
default suspeita_plankton = 0

# Imagens do jogo
image bg mesa_poker = "tutinha.webp"
image carta_verso = "cardsverso.png"

# Definição de personagens para o jogo de pôquer
define p = Character("Plankton", color="#00ff00")
define b = Character("Batavo", color="#ff9900")
define n = Character("Narrador", color="#ffffff")

# Tela de início do jogo de pôquer
label iniciar_jogo_poker:
    scene bg mesa_poker
    show plankton normal at right
    
    $ sistema_trapaca = SistemaTrapaça()
    $ segredo_atual = None  # O segredo sendo apostado nesta rodada
    
    p "Então você quer jogar pôquer, hein? Interessante..."
    p "Vamos tornar as coisas mais interessantes. Além de apostar dinheiro, vamos apostar... segredos."
    
    b "Segredos? Que tipo de segredos?"
    
    p "Oh, você sabe... informações que ninguém mais conhece. Coisas sobre o Siririca, Lula Molusco, Sandy..."
    p "Se você ganhar, eu revelo um segredo. Se eu ganhar, você me conta algo que eu queira saber."
    
    menu:
        "Aceitar o desafio":
            b "Parece justo. Vamos jogar."
            p "Excelente! Vamos começar então."
            jump jogo_poker_comecar
            
        "Recusar":
            b "Acho que não estou com sorte hoje. Talvez outra hora."
            p "Covarde. Sabia que você não tinha coragem."
            jump menu_plankton  # Retorna ao menu principal

# Tela principal do jogo de pôquer
label jogo_poker_comecar:
    $ baralho = Baralho()
    $ mao_jogador = []
    $ mao_plankton = []
    $ pot = 0
    $ rodada = 0
    $ jogo_ativo = True
    
    # Distribuir cartas iniciais
    python:
        for i in range(5):
            mao_jogador.append(baralho.tirar_carta())
            mao_plankton.append(baralho.tirar_carta())
    
    # Selecionar um segredo para apostar
    python:
        segredos_disponiveis = [k for k in SEGREDOS.keys() if k not in segredos_descobertos]
        if segredos_disponiveis:
            segredo_atual = random.choice(segredos_disponiveis)
        else:
            segredo_atual = None
        
    jump jogo_poker_round

# Rodada de pôquer
label jogo_poker_round:
    scene bg mesa_poker
    show plankton normal at right
    
    if rodada == 0:
        p "Vou apostar um segredo muito interessante nessa rodada."
        
        if segredo_atual:
            if "siririca" in segredo_atual:
                p "É algo sobre o seu chefe, o velho Siririca. Aposto que você vai gostar de saber."
            elif "lula" in segredo_atual:
                p "É um segredinho suculento sobre seu vizinho rabugento de tentáculos."
            elif "sandy" in segredo_atual:
                p "É sobre a esquilo cientista. Coisas que ela não quer que ninguém saiba."
            elif "patrick" in segredo_atual:
                p "É sobre seu amigo rosa. Ele não é tão simples quanto parece."
            elif "plankton" in segredo_atual:
                p "Vou revelar algo sobre mim mesmo que ninguém mais sabe. É um risco, mas confio em minha habilidade."
    
    # Exibir as cartas do jogador
    n "Suas cartas:"
    python:
        for carta in mao_jogador:
            renpy.say(n, str(carta))
    
    # Avaliar a mão atual
    $ pontuacao, tipo_mao = AvaliadorMao.avaliar(mao_jogador)
    n "Você tem: [tipo_mao]"
    
    # Menu de opções de jogo
    menu:
        "Apostar $100":
            $ pot += 100
            $ poker_dinheiro_jogador -= 100
            p "Hmm, apostando. Vou cobrir."
            $ pot += 100
            $ poker_dinheiro_plankton -= 100
        
        "Verificar (não apostar)":
            p "Verificando, huh? Fraco. Vou apostar $50 então."
            $ pot += 50
            $ poker_dinheiro_plankton -= 50
            
            menu:
                "Cobrir os $50":
                    $ pot += 50
                    $ poker_dinheiro_jogador -= 50
                    p "Ao menos tem coragem de continuar."
                    
                "Desistir":
                    p "Ha! Eu sabia. Fraco demais para jogar com os grandes."
                    $ poker_dinheiro_plankton += pot
                    jump fim_jogo_poker
        
        "Desistir da mão":
            p "Desistindo já? Patético."
            $ poker_dinheiro_plankton += pot
            jump fim_jogo_poker
        
        "Menu de trapaças" if rodada < 2:
            menu:
                "Espiar as cartas do Plankton ($+25% suspeita)":
                    $ sistema_trapaca.espiar_mao_oponente()
                    n "Cartas do Plankton:"
                    python:
                        for carta in mao_plankton:
                            renpy.say(n, str(carta))
                    $ pontuacao_plankton, tipo_mao_plankton = AvaliadorMao.avaliar(mao_plankton)
                    n "Ele tem: [tipo_mao_plankton]"
                    
                "Marcar as cartas ($+20% suspeita)":
                    $ sistema_trapaca.marcar_cartas()
                    n "Você marcou sutilmente algumas cartas do baralho."
                    n "Isso lhe dará uma vantagem na troca de cartas."
                    
                "Trocar uma carta por uma específica ($+15% suspeita)":
                    n "Qual carta você quer adicionar à sua mão?"
                    menu:
                        "Ás de espadas":
                            $ carta_nova = Carta("espadas", "A")
                            $ mao_jogador.pop()  # Remove a última carta
                            $ mao_jogador.append(carta_nova)
                            $ sistema_trapaca.trocar_carta(baralho, carta_nova)
                            
                        "Rei de copas":
                            $ carta_nova = Carta("copas", "K")
                            $ mao_jogador.pop()  # Remove a última carta
                            $ mao_jogador.append(carta_nova)
                            $ sistema_trapaca.trocar_carta(baralho, carta_nova)
                            
                        "Dama de ouros":
                            $ carta_nova = Carta("ouros", "Q")
                            $ mao_jogador.pop()  # Remove a última carta
                            $ mao_jogador.append(carta_nova)
                            $ sistema_trapaca.trocar_carta(baralho, carta_nova)
                            
                        "Valete de paus":
                            $ carta_nova = Carta("paus", "J")
                            $ mao_jogador.pop()  # Remove a última carta
                            $ mao_jogador.append(carta_nova)
                            $ sistema_trapaca.trocar_carta(baralho, carta_nova)
                    
                    # Verificar se foi pego trapaceando
                    if sistema_trapaca.ser_pego():
                        p "Ei! O que você está fazendo? Você está trapaceando!"
                        p "Jogo cancelado! Fora do meu estabelecimento!"
                        jump trapaca_descoberta
                
                "Voltar":
                    pass
            
            jump jogo_poker_round
    
    # Troca de cartas (se ainda não trocou)
    if rodada == 0:
        n "Quais cartas você deseja trocar? (Você pode trocar até 3 cartas)"
        
        $ cartas_para_trocar = []
        python:
            for i in range(5):
                carta = mao_jogador[i]
                escolha = renpy.display_menu([
                    ("Trocar " + str(carta), True),
                    ("Manter " + str(carta), False)
                ])
                
                if escolha:
                    cartas_para_trocar.append(i)
                
                # Limitar a 3 cartas
                if len(cartas_para_trocar) == 3:
                    break
        
        # Substituir as cartas selecionadas
        python:
            for indice in sorted(cartas_para_trocar, reverse=True):
                mao_jogador.pop(indice)
                mao_jogador.insert(indice, baralho.tirar_carta())
        
        # Plankton também troca cartas
        $ num_cartas_plankton = random.randint(0, 3)
        p "Vou trocar [num_cartas_plankton] cartas."
        
        python:
            for i in range(num_cartas_plankton):
                indice_remover = random.randint(0, len(mao_plankton)-1)
                mao_plankton.pop(indice_remover)
                mao_plankton.insert(indice_remover, baralho.tirar_carta())
    
    # Segunda rodada de apostas
    $ rodada += 1
    
    if rodada < 2:
        jump jogo_poker_round
    
    # Mostrar resultado final
    n "Suas cartas finais:"
    python:
        for carta in mao_jogador:
            renpy.say(n, str(carta))
    
    $ pontuacao_final, tipo_mao_final = AvaliadorMao.avaliar(mao_jogador)
    n "Você tem: [tipo_mao_final]"
    
    p "Muito bem, vamos ver quem ganhou."
    p "Minhas cartas são:"
    
    python:
        for carta in mao_plankton:
            renpy.say(p, str(carta))
    
    $ pontuacao_plankton_final, tipo_mao_plankton_final = AvaliadorMao.avaliar(mao_plankton)
    p "Eu tenho: [tipo_mao_plankton_final]"
    
    # Determinar o vencedor
    if pontuacao_final > pontuacao_plankton_final:
        p "Você ganhou desta vez. Impressionante."
        $ poker_dinheiro_jogador += pot
        $ pot = 0
        
        # Revelar segredo
        if segredo_atual:
            p "Como prometido, vou revelar um segredo para você."
            $ segredo_texto = SEGREDOS[segredo_atual]
            p "[segredo_texto]"
            $ segredos_descobertos.append(segredo_atual)
            
            # Salvar o segredo no arquivo do jogador
            python:
                with open("segredos_descobertos.txt", "a") as arquivo:
                    arquivo.write(segredo_atual + ": " + segredo_texto + "\n")
    
    elif pontuacao_final < pontuacao_plankton_final:
        p "Eu ganhei! Sua mão é fraca demais para me vencer."
        $ poker_dinheiro_plankton += pot
        $ pot = 0
        
        p "Agora você me deve um segredo. Hmm, deixe-me pensar..."
        
        # Plankton pede um segredo
        $ pedido_segredo = random.choice([
            "Onde você esconde suas coisas mais valiosas na casa abacaxi?",
            "Qual é o ponto fraco do Siririca que você conhece?",
            "Você já viu o Gary fazer algo estranho ultimamente?",
            "O que aconteceu com o verdadeiro Bob Esponja? Vamos, pode me contar...",
            "Você tem algum plano para assumir o controle do Siri Cascudo?"
        ])
        
        p "[pedido_segredo]"
        
        menu:
            "Mentir descaradamente":
                $ mentira = random.choice([
                    "O Siririca tem medo de borboletas. Ele desmaia só de ver uma.",
                    "Eu guardo tudo de valor dentro do abacaxi do Gary. Ninguém suspeita.",
                    "Eu vi Gary abrindo o cofre do Siririca usando seus olhos como chaves.",
                    "O verdadeiro Bob Esponja está em uma expedição submarina.",
                    "Meu plano é colocar laxante no molho especial dos hambúrgueres."
                ])
                
                b "[mentira]"
                
                # Plankton pode suspeitar de mentira
                python:
                    if random.random() < 0.3:
                        renpy.say(p, "Hmm... isso não parece verdade. Mas vou investigar mesmo assim.")
                    else:
                        renpy.say(p, "Interessante... muito interessante.")
                
            "Revelar uma meia-verdade":
                $ meia_verdade = random.choice([
                    "O Siririca sempre conta o dinheiro três vezes antes de guardar.",
                    "Eu mantenho um diário escondido em uma lata embaixo da cama.",
                    "Gary consegue abrir fechaduras com sua gosma, é surpreendente.",
                    "O verdadeiro Bob Esponja tem um segredo que ninguém conhece...",
                    "Tenho observado a rotina do Siririca para encontrar padrões."
                ])
                
                b "[meia_verdade]"
                p "Hmm, isso parece útil. Vou guardar essa informação."
    
    else:  # Empate
        p "Parece que temos um empate. Ninguém ganha o pote."
        $ metade_pot = pot // 2
        $ poker_dinheiro_jogador += metade_pot
        $ poker_dinheiro_plankton += pot - metade_pot
        $ pot = 0
        
        p "Que tal continuarmos jogando para desempatar?"
    
    # Verificar se quer continuar jogando
    menu:
        "Jogar outra rodada":
            p "Excelente! Vamos continuar."
            $ sistema_trapaca.resetar_suspeita()
            jump jogo_poker_comecar
            
        "Parar de jogar":
            p "Já desistindo? Bem, pelo menos você teve coragem de jogar."
            jump fim_jogo_poker

# Quando o jogador é pego trapaceando
label trapaca_descoberta:
    p "Eu devia saber que você era desonesto. Bem, isso acaba com nosso jogo."
    p "Vai embora antes que eu chame a polícia da Fenda do Biquíni!"
    
    # Penalidade por ser pego
    $ poker_dinheiro_jogador -= 200
    python:
        if poker_dinheiro_jogador < 0:
            poker_dinheiro_jogador = 0
    
    jump menu_plankton  # Retorno ao menu principal

# Fim do jogo de pôquer
label fim_jogo_poker:
    # Resumo da sessão de jogo
    n "Sessão de pôquer finalizada."
    n "Seu dinheiro: $[poker_dinheiro_jogador]"
    n "Dinheiro do Plankton: $[poker_dinheiro_plankton]"
    n "Segredos descobertos: [len(segredos_descobertos)]/[len(SEGREDOS)]"
    
    if len(segredos_descobertos) > 0:
        n "Último segredo descoberto:"
        python:
            if segredo_atual in segredos_descobertos:
                renpy.say(n, SEGREDOS[segredo_atual])
    
    p "Podemos jogar de novo quando quiser. Eu sempre tenho mais segredos para apostar..."
    p "Ou talvez você não tenha mais coragem de enfrentar um mestre do pôquer como eu."
    
    # Retornar ao menu principal
    jump menu_plankton

# Placeholder para o menu principal
label menu_plankton:
    scene bg balde_lixo
    show plankton normal at right
    
    menu:
        "Jogar pôquer apostando segredos":
            jump iniciar_jogo_poker
        
        "Conversar com Plankton":
            p "O que você quer agora, falso Bob Esponja?"
            jump menu_plankton
        
        "Sair do Balde de Lixo":
            p "Vai embora então. Mas lembre-se que eu sei quem você realmente é..."
            jump sair_balde_lixo

# Placeholder para saída
label sair_balde_lixo:
    scene black
    "Você sai do Balde de Lixo e retorna à Fenda do Biquíni..."
    
    # Aqui retornaria ao mapa principal do jogo
    return