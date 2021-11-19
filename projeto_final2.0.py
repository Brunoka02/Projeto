def fim_do_jogo():
    print('''
   _____          __  __ ______    ______      ________ _____  
  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
 | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
 | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
 | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_|
                                                               
                                                               
 ''')
    print("Jogar novamente?")
    
    print("[SIM]  OU  [NÃO]")


def quebra():
    input("Aperte ENTER para continuar")

print('''
 .d8888b.          d8b          888                  8888888                                                      888                               888 
d88P  Y88b         Y8P          888                    888                                                        888                               888 
888    888                      888                    888                                                        888                               888 
888        888d888 888 88888b.  888888  8888b.         888   88888b.  .d8888b  888  888 88888b.   .d88b.  888d888 888888  8888b.  888  888  .d88b.  888 
888        888P"   888 888 "88b 888        "88b        888   888 "88b 88K      888  888 888 "88b d88""88b 888P"   888        "88b 888  888 d8P  Y8b 888 
888    888 888     888 888  888 888    .d888888        888   888  888 "Y8888b. 888  888 888  888 888  888 888     888    .d888888 Y88  88P 88888888 888 
Y88b  d88P 888     888 888 d88P Y88b.  888  888        888   888  888      X88 Y88b 888 888 d88P Y88..88P 888     Y88b.  888  888  Y8bd8P  Y8b.     888 
 "Y8888P"  888     888 88888P"   "Y888 "Y888888      8888888 888  888  88888P'  "Y88888 88888P"   "Y88P"  888      "Y888 "Y888888   Y88P    "Y8888  888 
                       888                                                              888                                                             
                       888                                                              888                                                             
                       888                                                              888                                                             
 ''')

import random
print("Cripita insuportável é um RPG de texto, nele você assumira o papel \nde um dos 3 personagens e tentara escapar de uma masmorra repleta \nde monstros, cultistas e armadilhas. Cada personagem possui 2 finais \nsendo um deles o feliz e o outro o triste, cada uma das suas \nescolhas vão influenciar no final alcançado, ou  te levar para a morte.")
print("")
print("Você está pronto?")
print("[SIM]  ou  [NÃO]")
jogador_prontidao= input().upper()
if jogador_prontidao == "NÃO" or jogador_prontidao == "NAO" :
    print("Volte quando estiver preparado...")
    SystemExit

while jogador_prontidao == "SIM":
    print("Qual personagem você deseja jogar? \nMercenario[1] \nExorcista[2] \nAntiquário[3]")
    personagem_principal=input("Seu personagem: ")
    if personagem_principal == "1":
        print("O mercenario busca por dinheiro e redenção ao salvar a filha \nde um de seus melhores clientes. Ele está equipado com uma lanterna \ne uma pistola, que so é eficiente contra humanos, porém possui pouco conhecimento \nde seus arredores ")
        print("Deseja jogar com ele?  [SIM] OU [NÃO]")  
        desejo_de_personagem = str(input())
        if desejo_de_personagem == "NÃO" or desejo_de_personagem == "NAO" :
            continue
        if desejo_de_personagem == "SIM":
            balas = 6
            acao_porta = 0
            acao_porta2 = 0
            aux = 0
            estado = 0
            porta_celaaux = 0
            chave_estrela = 0
            conhecimeto_colecao = 0
            conhecimeto_da_verdade = 0
            print("O ano é 1989 e você, um veterano de guerra que apos sair do exercito se tornou um\nmercenario, recebe uma proposta irrecusavel de um dos seus melhores clientes. \nVocê deve encotrar a filha dele, Sara Gusmão, que sumiu durante uma viagem de férias. \nAo iniciar as investigações na casa em que ela estava um rastro de sangue te leva\naté o meio da mata, ao segui-lo você se depara com a entrada de uma caverna \ne, ao apontar a laterna para a entrada dela, você observa um colar \nque pertencia a garota, então decide adentrar na caverna para procura-la")
            print()
            print("Após dar alguns poucos passos você se depara com um corredor iluminado por tochas,\nao olha-la com atenção vc observa um lÍNGUA estranha de mais para compreender, e uma \nfechadura que parece ser mais velha que a propría caverna. O que você faz? ")
            print("Arrombar a fechadura [1]\nObservar os arredores [2]")


            acao_porta = int(input())
            if acao_porta == 1:
                print("Apesar de velha a fechadura apresenta resistencia as suas tentativas.\nContinuar a tentar [1]\nDar um tiro nela[2] \nObservar os arredores [3]")
                acao_porta2 = int(input())
                if acao_porta2 == 1:
                    print("Após muito tentar você da um tranco final e as peças \nda fechadura caem aos seus pés. Porém, antes mesmo de você \nabrir a porta, um mecanismo é acionado liberando um vapor no corredor\nalguns segundos são suficientes para você cair sem vida no chão.")
                    fim_do_jogo()
                    jogador_prontidao = str(input().upper())
                    continue
                if acao_porta2 == 2:
                    balas = balas - 1
                    print("Você da um tiro certeiro na fechadura, o som de um mecanismo \né escutado, mas um estrelo o interompe, o caminho está\nlivre, mas só restam mais {} balas no seu carregador ".format(balas))
                else: 
                    acao_porta = 2
            if acao_porta == 2:
                print("Após observar o corredor por alguns minutos você encontra um papel \ncom a mesma frase escrita na porta, e logo em baixo uma \ntentativa grosseira de tradução: para abrir a fechadura você deve \nsolucionar o enigma 'Sempre quando chego causo alívio ou tristeza, posso \nser o fim de tudo ou o começo de algo maior, falhe ao descobrir quem \neu sou e descubra minha verdadeira face' ")
                resposta = input("A resposta para o enigma é: ")
                if resposta.upper() == "MORTE":
                    print("Você escolhe, entre os diversos simbolos na fachadura o que mais \nte remete a morte, e ela se abre, o caminho esta livre")
                else:
                    print("Você procura o simbolo que maios o remete a {} entre os \npresentes na fechadura, e apos tentar forçar sua abertura ela se rompe\nPorém, antes mesmo de você abrir a porta, um mecanismo é acionado liberando \num vapor no corredor alguns segundos são suficientes para você cai sem vida no chão ".format(resposta))
                    fim_do_jogo()
                    jogador_prontidao = str(input().upper())
                    continue
            quebra()
            print("Ao passar pela porta você se depara com  entradas cada uma com seu nome\nescrito em uma placa que parece ter sido colocada a não muito tempo. \nQual voce deseja explorar primeiro?\nColeção [1]\nArquivos [2]\nO Inominável [3]\nCelas [4]\nAntessala [5]")
            as_4_salas = True
            while as_4_salas == True:
                sala_escolhida = int(input("Ir para a sala: "))
                if sala_escolhida == 1:
                    if conhecimeto_colecao == 0:
                        print("Você entra na Coleção, e encontra um segurança distraido: o que você faz ?\nConversar com ele [1]\nAtacar de surpresa- 75% [2]\nDar um tiro [3]")
                        acao_colecao = int(input())
                        if acao_colecao == 1:
                            print("Você se aproxima para perguntar sobre a garota, porém ao chegar \nmuito perto o segurança te ataca e captura. Ao recobrar a consciêcia voce está amarrado \nem uma mesa ritualistica, agora so resta torcer para que seus ultimos segundos sejam indolores.")
                            as_4_salas = False
                            continue
                        if acao_colecao == 2:
                            chance_sucessocolecao = int(random.randrange(0,5))
                            if chance_sucessocolecao == 4:
                                print("Sua tentativa não da certo, o seguranca percebe sua aproximação e atira primeiro\n Ao recobrar a consciêcia voce está amarrado \nem uma mesa ritualistica, agora so resta torcer para que seus ultimos segundos sejam indolores.")
                                as_4_salas = False
                                continue
                            if chance_sucessocolecao < 4:
                                print("Sua tentativa da certo, e com um ataque sorrateiro o segurança desmaia, deixando o caminho livre")
                        if acao_colecao == 3:
                            print("Você da um tiro certeiro no segurança, deixando o caminho livre")
                            balas = balas - 1
                        conhecimeto_colecao = 1
                    print("Dentro da coleção você encotra diversas obras de arte, mas é possivel\nperceber com certa facilidade que uma delas está em destaque, um quadro \nde um homem vestindo uma túnica, nele é possivel ler o nome 'Torvald' ")
                    print("Após algum tempo você decide retornar para a entrada das salas")
                    continue
                if sala_escolhida == 2:
                    if porta_celaaux == 0:
                        print("Você se aproxima da porta dos Arquivos e percebe um aparelho cujo nível de tecnologia\ndestoa do restante da caverna, ao se aproximar ele emite um som 'para acessar\n os arquivos voce deve informar o nome do nosso líder' ")
                        print("Caso você nao saiba o nome digite 'SAIR'")
                        porta_cela = input("Sua resposta é: ")
                        if porta_cela.upper() ==  "TORVALD":
                            porta_celaaux = 1
                        elif porta_cela.upper() == "SAIR":
                            print("Você retorna para a entrada das salas")
                            continue
                        elif porta_cela != "TORVALD":
                            print("Você erra o nome, o aparelho solta um vapor venenoso. Em alguns minutos seu corpo cai sem vida")
                            as_4_salas = False
                            continue
                    print("Ao entrar nos Arquivos você encontra diversos livros e documentos e, no\nmeio da sala, uma mesa. Ao olhar com mais atenção para a mesa você encontra uma chave\ncuja ponta tem o formato de uma estrela.")
                    chave_estrela = 1
                    print("Após olhar por algum tempo você decide retornar para a entrada das salas")
                    continue
                if sala_escolhida == 3:
                    print("Você anda por um longo corredor, e no fim dele depara com diversos destroços\nque parecem ser resultado de um desmonoramento, é possivel escutar\nsons estranhos ataves deles, mas o caminho parece instransponivel. Você retorna para as salas")
                    continue
                if sala_escolhida == 4:
                    print("Você se aproxima da entrada da porta das celas e percebe um buraco nela com um formato parecido com o de uma estrela")
                    if chave_estrela == 0:
                        print("Após algum tempo tentando abrir a porta você desiste e retorna para a entrada das salas")
                        continue
                    elif chave_estrela == 1:
                        print("Você percebe que o formato do buraco se parece muito com a chave\nque estava nos arquivos, e decide usar ela, o que ,pra sua supresa, da certo.\nO caminho para as celas está aberto")
                        quebra()
                        print("")
                        print("Dentro do local você encontra 2 carcereiros, que partem em sua \ndireção, você da dois disparos certeiros neles. Apesar do susto você está \nbem, e livre para explorar a Cela")
                        balas = balas - 2
                        print("")
                        print("Após observar o local por algum tempo você encontra o corpo de outro\num mercenario que trabalhava diretamente para o Sr. Gusmão, pai da \ngarota desaparecida, como seu mão direita.")
                        print("")
                        print("Ao chegar perto você descobre que ele está vivo, pelo menos por enquanto\ne antes que voce pudesse fazer qualquer coisa ele diz:")
                        print("'Eu conheço você, já trabalhamos juntos antes. Você caiu em uma armadilha, uma armadilha do Sr. Gusmão...'")
                        print("'Ele está trazendo pessoas para cá, para sacrificar para algum deus antigo, ou demônio'")
                        print("'Eu me opus a essa ideia e agora estou aqui, preso em uma cela, prestes a morrer")
                        print("'Ele pode estar aqui ainda, nao acredite nele'")
                        conhecimeto_da_verdade = 1
                        print("'Agora vá e termine com isso'")
                        print("Ainda confuso você retorna para as entradas das salas, e percebe que a saída está fechada\nagora sua única opção é seguir em frente")
                        continue
                if sala_escolhida == 5:
                    print("Ao avançar pela Antessala você se depara com mais 2 seguranças guardando uma porta, o que você faz?\nAtacar de supresa- 75% " + "de sucesso [1]\nDar um tiro em cada[2]\nCombate físico- 25%" +" de sucesso [3]")
                    acao_antessala = int(input ("Você ira: "))
                    chance_sucessoantessala = int(random.randrange(1,5))
                    
                    if acao_antessala == 1:
                        print("Você se aproxima de surpresa")
                        if chance_sucessoantessala < 4:
                            print("E pega um dos guardas desprevinidos, porém o outro percebe o ataque e te obriga a gastar mais uma de suas balas")
                        elif chance_sucessoantessala == 4:
                            print("Porém após derrubar o primeiro segurança o outro é mais rapido que você e te da um tiro, te matando ali mesmo")
                            print("Continuar [1]\nDesistir[2]")
                            as_4_salas = False
                            continue
                    if acao_antessala == 2:
                        print("Você da um tiro nos dois seguranças. O caminho está livre para você avançar,mas agora você tem 2 balas a menos")
                        balas = balas - 2
                    if acao_antessala == 3:
                        print("Você comeca a lutar com os proprios punhos")
                        if chance_sucessoantessala == 4: 
                            print("Surpreendentemente seu ataque é um sucesso, e agora o caminho está livre para o seu avanço ")
                        elif chance_sucessoantessala < 4:
                            print("Você até consegue derrubar um dos seguranças, mas acaba sendo atingido por um diparo que te mata ali mesmo")
                            
                            as_4_salas = False
                            continue    
                    quebra()
                    print("Você finalmente passa pela porta e se depara com varias pessoas usando tunicas, entre elas\nestá o Sr. Gusmão, sentado em uma cadeira em estado de transe")
                    if balas >= 3 and conhecimeto_da_verdade == 1:
                    
                        print("Você da um tiro no Sr. Gusmão, e com as suas outras balas mata os cultistas armados.Após\nesse ato de bravura você escapa da caverna, tendo certeza que acabou com aquele\nculto bizaro, pelo menos por enquanto.\nParabéns\nFim de jogo")
                        as_4_salas = False
                    elif balas < 3 and conhecimeto_da_verdade == 1 and balas > 0 :
                        print("Você da um tiro no Sr. Gusmão, mas nao tem balas suficientes para matar os cultistas armados. \nVocê deu um fim ao culto, mas isso custou sua vida")
                        print("Você gastou {} das suas 6 balas".format(6 - balas))
                        
                        as_4_salas = False
                    elif balas >= 3 and conhecimeto_da_verdade == 0:
                        print("Você da um tiro nos cultitas armados, e os outros correm do local. Porém, ao tentar ajudar o\nSr. Gusmão você é traido, logo apos ele sair do transe você é apunhalado pelas costas")
                        print("Algo deve estar errado...")
                        
                        as_4_salas = False
                    elif balas < 3 and conhecimeto_da_verdade == 0 and balas > 0:
                        print("Você até tenta ajudar seu chefe de um futuro terrivel, porém nao tem balas suficientes para\nmatar os cultistas armados. Após ser atingido por um golpe na cebeça você desmaia, e acorda\n amarrado em uma mesa durante um ritual, em que o sacrificio é você")
                        print("Você gastou {} das suas 6 balas".format(6 - balas))
                        
                        as_4_salas = False
                    elif balas <= 0 :
                        print("Você tenta atirar nos cultistas que começam a te perseguir, porém todas as suas 6 balas já foram\ngastas. Após um combate corpo a corpo você é amarrado ee um ritual se incia.")
                        print("Nesta noite você é o sacrificio")
                        as_4_salas = False
        print('''
   _____          __  __ ______    ______      ________ _____  
  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
 | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
 | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
 | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_|
                                                               
                                                               
 ''')
        print("Jogar novamente?")
        print("[SIM]    [NÃO]")
        jogador_prontidao = input().upper()

    #parte do exorcista
    ########################################################3
    ###########################################3###############3

    if personagem_principal == "2":
        print('''Você é um exorcista enviado pela igreja para investigar uma cripta
que, segundo um mercenario, é casa de algum demônio. Apesar da sua
avançada idade você é o melhor exorcista da região, e a única esperança
da irgreja para solucionar esse problema. Você está levando uma biblia, 
crucifixo e água benta.''' )
        print("Deseja jogar com ele?  [SIM] OU [NÃO]")  
        desejo_de_personagem = str(input()).upper()
        if desejo_de_personagem == "NÃO" or desejo_de_personagem == "NAO":
            continue
        if desejo_de_personagem == "SIM":
            agua_benta = 5
            biblia = 1
            crucifixo = 1
            expulso = 0
            print('''O ano é 1993, e você está a caminho de uma cidade do interior
que, segundo informaçôes confidenciais, possui uma caverna 
que um culto satânico usava para realizar sacrificios humanos.
Ao chegar na entrada da caverna você encontra um grupo de escavadores
que está entrando, e um deles pede uma benção antes de adentrar a caverna

Você usa sua água benta para conceder a benção, ou guarda para
um eventual problema?
[SIM]   OU   [NÃO]
            ''')
            escolha_beçao = input().upper()
            if escolha_beçao == "SIM":
                escolha_beçao = 1
                agua_benta = agua_benta - 1
            if escolha_beçao == "NÃO" or escolha_beçao == "NAO":
                escolha_beçao = 0
            print("'Muito obrigado padre'")
            print("")
            quebra()
            print('''Após esperar seu parceiro por algumas horas você decide entrar
sem ele. Ao entrar pela caverna você anda por um longo corredor
e após passar por uma porta com escritas estranhas chega a um local 
cheio de salas, mas só a que possui o nome de O Inominável está aberta
            
Você deseja entrar, ou obseravar o local antes?
[ENTRAR]   OU   [OBERVAR]''')
            entrar_ou_observar = input()
            adaga = 0
            if entrar_ou_observar.upper() == "OBSERVAR":
                print('''Você observa o local por um tempo e, perto da entrada 
de um local chamado Antessala, é possível encontrar uma 
adaga cerimonial.
                
Ela atiça sua curiosidade, mas você esqueceu sua bolsa, deseja
trocar ela por algum dos seus objetos, ou abandona-la?
Tocar pela bíblia [1]
Trocar pelo crucifixo [2]
Deixar no chão [3]
                ''')
                pegar_ou_nao = int(input())
                if pegar_ou_nao == 1:
                    biblia = 0
                    adaga = 1
                    print("Você pega a adaga e deixa sua bíblia proxima a um candelabro")
                elif pegar_ou_nao == 2:
                    crucifixo = 0
                    adaga = 1
                    print("Você pega a adaga e deixa seu crucifixo proximo a um candelabro")
                else:
                    print("Você decide deixar a adaga e continuar com seus objetos")
                print("Após fazer sua escolha você segue em direção ao corredor que está aberto")
            quebra()
            print('''Ao passar pela grande porta que guarda a entrada você se encontra
em um grande corredor, repleto de destroços de um possivel desmonoramento
e algumas ferramentas de escavação abandonadas. Após andar por alguns 
minutos você é parado por um policial fortemente armado
'Parado ai, o caminho a seguir foi barrado pelo prefeito somente pessoas
autorizadas por ele podem passar'

Conversar com ele [1]
Voltar para casa [2]
            ''')
            acao_guarda = int(input())
            if acao_guarda == 2:
                voltou = 1
                print('''Você decide voltar parao hotel, e retornar no dia seguinte, acompanhado
de seu parceiro
                ''')

                print('''Ao acordar no dia seguinte o noticiario informa que o exercito invadiu a 
caverna durante a madrugada e matou todos tabalhadores, o motivo ainda é
um misterio, e a relação do prefeito com isso está sendo investigada''')
                fim_do_jogo()
                jogador_prontidao = str(input().upper())
                continue
            if acao_guarda == 1:
                conversa = True
                while conversa == True:
                    print("Perguntar o que aconteceu ali [1]\nPerguntar o motivo de nâo poder passar [2]")
                    acao_conversa = int(input())
                    if acao_conversa == 1:
                        print("Algum acidente, não posso falar mais do que isso")
                        continue
                    elif acao_conversa == 2:
                        chance_secesso_conversa = int(random.randrange(0,4))
                        print("É uma ordem do prefeito ")
                        print('''Distrair o guarda e tentar passar escondido - 25% [1]
Abençoar o policial para ganhar a simpatia dele [2] - 75%''')
                        if biblia == 1:
                            print("Usar a bíblia para convencer ele [3]")
                        acao_conversa1 = int(input())
                        if acao_conversa1 == 1 and chance_secesso_conversa == 3:
                            print("Você se distancia e, com uma pedra, distrai o guarda, deixando o caminho livre")
                            conversa = False
                        elif acao_conversa1 == 1 and chance_secesso_conversa <3 :
                            print("Você tenta distrair o policial com uma pedra, mas quando está\nprestes a passar pela porta ele percebe sua tentativa e te expulsa")
                            expulso = 1
                            conversa = False
                            break
                        elif acao_conversa1== 2 and chance_secesso_conversa < 3:
                            print("Sua atitude comove o policial e ele decide deixar você passar")
                            conversa = False
                            agua_benta = agua_benta - 1
                        elif acao_conversa1== 2 and chance_secesso_conversa == 3:
                            print("Sua tentativa não da certo, e o policial te expulsa")
                            expulso = 1
                            break
                        elif acao_conversa1  == 3:
                            print("Você lê alguns versículos da bíblia e convence o policial a falar mais")
                            print("'Eu deixo você passar padre, mas tome muito cuidado, as pessoas que \ntrabalham aqui estão agindo muito estranhas acho que o prefeito \ntem algo a ver com tudo isso, dizem que ele fazia parte de um culto estranho alguns anos atras")
                            conversa = False
                    
                if expulso == 1:
                    print('''Você decide voltar parao hotel, e retornar no dia seguinte, acompanhado
de seu parceiro
                ''')

                    print('''Ao acordar no dia seguinte o noticiario informa que o exercito invadiu a 
caverna durante a madrugada e matou todos tabalhadores, o motivo ainda é
um misterio, e a relação do prefeito com isso está sendo investigada''')
                    fim_do_jogo()
                    jogador_prontidao = str(input().upper())
                    continue
            quebra()
            print('''Você passa pela porta e encontra os trabalhadores agindo de forma estranha
eles começam a andar em sua direção, com seus olhos compltamente pretos
Oque você faz ?
Jogar água benta neles[1]
Ir por um corredor auxiliar [2]
Fugir [3]''')   
            acao_antes_fim = int(input())
            if acao_antes_fim == 3:
                print('''Você corre para a saída e avisa as autoridades locais
                ''')

                print('''Ao acordar no dia seguinte o noticiario informa que o exercito invadiu a 
caverna durante a madrugada e matou todos tabalhadores, o motivo ainda é
um misterio, e a relação do prefeito com isso está sendo investigada''')
                fim_do_jogo()
                jogador_prontidao = str(input().upper())
                continue
            if acao_antes_fim == 1:
                print("Você joga toda a água benta restante neles, e corre em direção a uma porta com simbolos desconhecios")
                agua_benta = 0 
            if acao_antes_fim == 2:
                print("Você vai em direção a um corredor auxiliar, e após andar por alguns segundos vê um trabalhador")
                if escolha_beçao == 1:
                    print("Ao se aproximar você percebe que aquele homemem é, na verdade, o mesmo \ntrabalhador que você abençoou antes de entrar na caverna, e ele está consciente ")
                    print('''Padre, você precisa nos ajudar, o prefeito soltou algum tipo de maldição
agora todos meus colegas estão loucos, ele esta seguindo aquela porta, temos que parar ele
eu seguro a entrada para parar os outros''')
                else: 
                    print("O homem começa a caminhar em sua direção\nJogar água benta [1]")
                    if adaga == 1:
                        print("Atacar com a adaga [2]")
                    acao_homem = int(input())
                    if acao_homem == 1:
                        print("Você joga um pouco de agua benta no homem, isso é suficiente para faze-lo\nrecobrar a consciencia por um tempo e te permitir passar")
                        agua_benta = agua_benta -1
                    if acao_homem == 2: 
                        print("Você atinge o homem com a adaga e ele cai por um breve momento, deixando o caminho livre")  
            quebra()
            print('''Ao andar por alguns minutos você finalmente chega em uma grande sala, repleta de símbolos pagãos
e no meio dela é possível ver o prefeito segurando um crânio de um ser irreconhecível. Visivelmente
ele já nao tem mais conciencia de seus proprios atos, e está parado, em transe 

O que você faz?
Atacar [1]
Exorcisar [2] ''')
            acao_final = int(input())
            if acao_final == 1:
                print("Você tenta atacar o prefeito")
                if adaga == 1:
                    print('''Você usa sua adaga e da um golpe preciso no prefeito. Porém, antes que ele caia sem vida no chão
ele te da um golpe fatal, com uma força sobre humana.

Você põe um fim a maldição e salva os trabalhadores, mas isso custa sua vida. Os tra- 
balhadores informam ao exercito o que aconteceu ali, e a caverna é implodida, mas não antes
de os cientistas do governo retirarem objetos.
Fim de jogo...
''')                        
                    fim_do_jogo()
                    jogador_prontidao = str(input().upper())
                    continue                         
                else:
                    print('''Você tenta atacar o prefeito com as próprias mãos, mas o prefeito acorda brevemente 
de seu transe e te empurra com uma força sobre humana. Você bate a cabeça na parede e desmaia
Após algumas horas você acorda , no exato momento em que o exército está invadindo a caverna, é
possível escutar o barulho de tiros ao fundo. Inúmeros soldados e trabalhadores estão sendo mortos
e agora so resta torcer para que você nao seja confundido com algum daqueles mosntros amaldiçoados.

''')
                    fim_do_jogo()
                    jogador_prontidao = str(input().upper())
                    continue   
            if acao_final == 2:
                if crucifixo == 1 and agua_benta == 4:
                    print('''Você inicia o exorcismo no prefeito, utilizando seu crucifixo e água benta. Após
longos minutos você finalmente remove o dêmonio que havia assumido o controle libertando nâo só o 
prefeito como, também, os trabalhadores.
Com a ajuda do policial você prende o prefeito, e para impedir que aquela caverna venha a causar 
novos problemas, você pede para os trabalhadores implodirem ela com tudo dentro, assim, finalmente,
selando aquele demõnio para sempre
Parabéns !!!

''')
                    fim_do_jogo()
                    jogador_prontidao = str(input().upper())
                    continue
                if crucifixo != 1 or agua_benta != 4:
                    print('''Você tenta realizar o exorcismo, mas sem todos os equipamentos necessarios não é
possível se livrar do demônio, somento para-lo por um breve momento, que você utiliza para escapar ''')
                    if escolha_beçao == 1:
                         print("acompanhado do policial e do homem que você havia concedido a benção mais cedo")
                    else:
                        print("Acompanhado do policial, que ainda guardava a entrada para o local")
                    print('''Logo após saírem da caverna o exercito entra no local, inúmeras vidas são perdidas
mas ao menos você ainda está vivo. Mais tarde a caverna é implodida, mas não antes
de os cientistas do governo retirarem objetos.
Fim de jogo...''')
                    fim_do_jogo()
                    jogador_prontidao = str(input().upper())
                    continue



#########################################################
#####Antiquario######################################
##################################################

    if personagem_principal== "3":
        
        print('''O antiquário explora locais antigos em busca de objetos de valor. Ele nâo tem 
nenhuma ferramenta de defesa, além de seu amuleto''')
        print("Deseja jogar com ele?  [SIM] OU [NÃO]")  
        desejo_de_personagem = str(input().upper())
        if desejo_de_personagem == "NÃO" or desejo_de_personagem == "NAO":
            continue
        if desejo_de_personagem == "SIM":
            amuleto = 1
            adaga_cerimonial = 0
            print('''O ano é 1788 é após escutar alguns boatos sobre uma caverna amaldiçoada, você
decide acompanhar uma caravana até uma cidade vizinha, com o objetivo de explorar esse local.
Em sua última parada antes de chagar ao seu destino, você encontra um vendedor ambulante
ele te oferece inúmeros objetos interessantes, entre eles uma adaga cerimonial, mas você não
tem as moedas necessarias para compra-la.
O que você faz?
Deixar ela lá [1]
Trocar pelo amuleto [2]''')
            acao_vendedor = int(input())
            if acao_vendedor == 1: 
                print("Apesar de chamar muito sua atenção, você decide deixar ela lá.")
            else:
                print('''Algo naquela adaga te atrai de forma muito estranha, e para consegui-la você
oferece seu amuleto de proteção, o que faz o vendedor aceitar prontamente.''')
                adaga_cerimonial = 1
                amuleto = 0
            quebra()
            print('''Após cavalgar por mais algumas horas você finalmente chega a entrada da caverna.
Você prontamente entra na caverna e, ao andar alguns minutos com somente a luz de sua tocha,
chega a uma porta. Nela esão ulgumas escritas bizarras, mas que não são totalmente estranhas,
você consegue ler algo parecido com 'Somente aqueles que abdicam da luz podem entrar'
O que você faz?''')
            acao_porta_tocha = "nada"
            auxiliar = True
            while auxiliar == True:
                acao_porta_tocha = input().upper()
                if acao_porta_tocha == "APAGO A TOCHA" or acao_porta_tocha =="APAGAR A TOCHA" or acao_porta_tocha =="APAGAR TOCHA":
                    auxiliar = False
                    continue
                else:
                    print("Nada acontece")
            print("Logo após a tocha apagar a porta se abre e você avança, com seu caminho iluminado por\npequenas brechas no teto e alguns cristais.")
            print("")
            quebra()
            print("Ao andar alguns minutos você se depara com dois focos de luz, que lembram muito diamantes, e\na sua esquerda uma porta.\nPara onde você vai?")
            print("Focos de luz[1]\nPorta[2]")
            acao_escuro = int(input())
            if acao_escuro == 1:
                print("Seus olhos brilham quase tanto quanto os focos de luz enquanto você se aproxima deles\nmas ao chegar perto o suficiente deles para quase tocá-los você é surpreendido.\nOs focos de luz são, na verdade, os olhos de um fera bestial, que te torna em pedaços enquanto o devora vivo")
                fim_do_jogo()
                jogador_prontidao = str(input().upper())
                continue
            print('''Você decide ir direto para porta, e ao atravessá-la chega a um longo corredor.
Visívelmente algo de estranho está acontecendo ali, e a sensação de estar sendo observado 
não saí da sua cabeça. Porém, pra confiramar sua confirmação, antes de chegar ao fim do 
corredor você é atacado por um ser com forma humanoide.
''')
            quebra()
            if amuleto == 1:
                print('''Após uma breve luta corporal ele para subtamente depois de olhar para seu amuleto
e você consegue olhar o rosto disforme daquela criatura que aparentemente já foi um humano.
Com uma voz assutadora ele te fala 'Saía daqui, já fui normal como você e a ganância me
tornou nisso. O que vive aqui não deve sair' ''')
                print("[SAIR]   OU   [CONTINUAR]")
                sair_ou_nao = input().upper()
                if sair_ou_nao == "SAIR":
                    print("Você aceita o conselho daquele ser, e foge daquele lugar")
                    print("Você está vivo.\nParabéns")
                    fim_do_jogo()
                    jogador_prontidao = str(input().upper())
                    continue
                if sair_ou_nao == "CONTINUAR":
                    print('''Você tenta empurrar a besta e continuar seu caminho, mas...
'Não vou deixar mais ninguém cometer o erro que eu cometi,nem que para isso
eu tenha sujar mais minhas mãos' ''')
                    print("A fera te ataca com fúria, e em poucos segundos você cai sem vida no chão")
                    fim_do_jogo()
                    jogador_prontidao = str(input().upper())
                    continue
            else:
                print('''Você ataca a fera com sua adaga e, mesmo no escuro, acerta o coração dela.
Ao se aproximar do corpo dela, você percebe uma certa semelhança com um humano, apesar
dass deformidades''')
                print("")
                print('''Mas, apesar do ocorrido, o caminho está livre, e você avança para o fim do corredor.
Ao chegar lá um foco de luz bate no centro da sala, e ao se aproximar dele você encontra um crânio que,
após alguns segundos, começa a falar com você''')
                quebra()
                print("'Eu espero por alguém como você há anos, junte-se a mim Torvald' ")
                print("'Aquele inútil que você acabou de por fim era um fraco'\n'Tenho certeza que você lidará bem melhor com as trevas do que ele'")
                print("'Faça um um culto em meu nome e me traga sacrifícios que te darei poder ilimitado")
                print("Você aceita ?\n[SIM]   OU   [NÃO]")
                aceitar = input().upper()
                if aceitar == "SIM":
                    print("Você faz um corte com a adaga, e com seu sangue faz um pacto com o demônio\nO poder maligno já fluí em você, assim como a sede por sangue.\nAgora você está condenado a uma vida de servidão")
                    fim_do_jogo()
                    jogador_prontidao = str(input().upper())
                    continue
                else:
                    print("Você recusa a proposta e, como forma de vingança, o demônio assume sua forma física\nque, apesar de fraca, é extremamente horrível. ")
                    print("Você o ataca com sua adaga, que não causa maiores danos a ele, porém o enfureçe o tanto \nque, em um único golpe, você é atirado longe, já sem vida.")
                    fim_do_jogo()
                    jogador_prontidao = str(input().upper())
                    continue
                