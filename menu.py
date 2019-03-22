import random
def batalha(personagem_principal, inimigo, chance_inimigo):

    while(personagem_principal['vida'] > 0 and inimigo['vida'] > 0):
        quem_bate = random.randrange(0,10)
        if(quem_bate > chance_inimigo):
            range_inicial_dano = (personagem_principal['dano'] * 30) / 100
            dano = random.randrange(int(range_inicial_dano), personagem_principal['dano'])
            print(personagem_principal['nome'], dano, "Dano")
            inimigo['vida'] -= dano
            print(inimigo['nome'], str(inimigo['vida']) + "/100")
        else:
            range_inicial_dano = (inimigo['dano'] * 30) / 100
            dano = random.randrange(int(range_inicial_dano), inimigo['dano'])
            print(inimigo['nome'], dano, "Dano")
            personagem_principal['vida'] -= dano
            print(personagem_principal['nome'], str(personagem_principal['vida']) + "/100")

    if(personagem_principal['vida'] > 0):
        return personagem_principal
    else:
        return inimigo

def validacao_um_e_dois(entrada):
    while(entrada != 1 and entrada != 2):
        print("Utilize apenas os números 1 ou 2.")
        entrada = int(input())

    return entrada

def get_personagens():
    arquivo = open("resources/personagens.txt", "r")
    lista_personagens = []
    for i in arquivo:
        personagem = {
            'nome' : i[:-1],
            'vida' : 100,
            'dano' : random.randrange(20,60)
        }
        lista_personagens.append(personagem)

    arquivo.close()


    return lista_personagens


def criacao_personagem():
    dano = random.randrange(40,80)
    print("Crição do personagem")
    nome = input("Digite seu nome, nobre guerreiro(a): ")
    print("Olá " + nome + ", seus atributos de vida são: 100 e " +
    "de dano são: "+ str(dano))

    principal = {
        'nome': nome,
        'vida': 100,
        'dano': dano,
        'score': 0
    }

    return principal

def cenario_um():
    print("O mundo foi devastado e agora é governardo pelo Rei Malvado.\n"+
        "Resta a você salvar o reino... Na sua jornada para a batalha,\n"+
        "há um caminho pela floresta ou pela montanha.\n" +
        "Qual a sua escolha?\n")
    print(" " * 15,"[1] FLORESTA")
    print(" " * 15,"[2] MONTANHA")
    entrada = int(input())
    entradaValida = validacao_um_e_dois(entrada)

    return entradaValida

def cenario_montanha(personagem_principal, personagens):
    print("E então o(a) grande Cavaleiro(a) "+ personagem_principal['nome'] + "\n"+
        "decidiu seguir pelas montanhas frias e cheias de gelo do sudoeste\n" +
        " do Himalaia· Após muito sofrimento quando, está quase chegando ao\n" +
        "topo, avista um andarilho, ao aproximar-se, o mesmo o \n" +
        "interroga. Para aonde vai, jovem Cavaleiro(a), gostaria de um agasalho?\n" +
        "Você fica intrigado com a situação, várias coisas passam por sua cabeca,\n" +
        "mas sem hesitar você:\n")
    print(" " * 15, "[1] Você responde a pergunta e pega o agasalho.")
    print(" " * 15, "[2] Você o ignora e segue em frente.")

    entrada = int(input())
    entradaValida = validacao_um_e_dois(entrada)
    vet = []

    if(entradaValida == 1):
        personagem_random = personagens[random.randrange(0,3)]['nome']
        print("Você pega o agasalho e fica conversando com ele(a) alguns minutos e \n"
            +" descobre que ele(a) é " + personagem_random + "\n" )
        print("Após a conversa e a descoberta, você o(a) convida para sua jornada, pedindo\n" +
            " ajuda. Sem hesitar, ele(a) aceita seu pedido e segue o caminho com você.\n"+
            " Após um longo tempo caminhando você e seu mais novo(a) amigo(a) chegam ao destino final\n"+
            "a zona de guerra.\n")
        personagem_principal['score'] += 100
    else:
        print("Você ignora o velho andarilho e segue em frente, porém, logo após andar \n"+
        "alguns minutos, você se depara com uma tremenda nevasca, o frio é intenso, sua \n"+
        "face congela, suas pernas não funcionam como antes, seus movimentos ficam lentos, \n"+
        "o sangue não circula como antes, você até tenta, mas o frio o derrota\n")
        print("Você não aguentou a tempestade, por falta de agasalho, você morreu !\n")
        personagem_random = "sozinho"
    vet.append(str(entradaValida))
    vet.append(personagem_random)

    return vet

def cenario_floresta(personagem_principal, personagens):
    print("E então o(a) grande Cavaleiro(a) "+ personagem_principal['nome'] + "\n"+
        "decidiu seguir pela floresta, as árvores fazem barulho durante todo o percurso,\n"+
        " no fim do caminho, alguém surge por trás delas oferecendo alimento. \n" +
        "\n")
    print("Você vê a sua frente uma jovem criança com um capuz vermelho,\n"+
            " lhe oferecendo uma maçã. O que você faz?\n")
    print(" " * 15, "[1] Você aceita e come a maçã.")
    print(" " * 15, "[2] Você o ignora e segue em frente.")
    entrada = int(input())
    entradaValida = validacao_um_e_dois(entrada)

    if(entradaValida == 1):
        print("O(A) " + personagem_principal['nome'] + " comeu a maça...\n" +
            "Aos poucos foi percebendo que estava ficando fraco, a visão distorcida \n"+
            "e então percebeu que a maçã estava envenenada.\n"+
            "Mas foi tarde demais...")
        print("você morreu!")
        print("GAME OVER")
    else:
        print("Você ignora a pequena criança, segue sua jornada caminhando por mais alguns \n"+
        "minutos, então finalmente você chega no seu objetivo final, a zona de guerra!")
        personagem_principal['score'] += 100

    return entradaValida

def cenario_final(personagem_principal, personagens, amigo):
    print("Na zona de guerra o(a) "+ personagem_principal['nome']+ " avista apenas \n"+
        "destruição e caos a sua frente, juntamente de 4 pessoas misteriosas.\n")
    print("Rapidamente sem pensar duas vezes "+ personagem_principal['nome']+ " \n"+
    " avança na direção das 4 pessoas, e durante seu avanço uma das pessoas corre \n"+
    "em sua direção e ali começam uma das maiores batalhas do século!")
    inimigos = []
    if(amigo != "sozinho"):
        for i in personagens:
            if(i['nome'] != amigo):
                inimigos.append(i)

        index = random.randrange(0,3)
        inimigo = inimigos[index]
        del(inimigos[index])
        print(inimigos)
        print("Entre "+ personagem_principal['nome'] + " vs " + inimigo['nome'])
        vencedor = batalha(personagem_principal, inimigo, 2)
        if(vencedor['nome'] == inimigo['nome']):
            print("Você foi morto com honra em uma batalha!")
            print("GAME OVER")
        else:
            print("Após derrotar o", inimigo['nome'])

def start():
    personagem_principal = criacao_personagem();
    personagens = get_personagens()
    print("Sua jornada inicia agora "+ personagem_principal['nome'] +". Boa sorte!\n")
    resposta_cenario_um = cenario_um()
    if(resposta_cenario_um == 2):
        saida = cenario_montanha(personagem_principal, personagens)
        decisao_tomada = saida[0]
        amigo = saida[1]
        if(int(saida[0]) == 1):
            cenario_final(personagem_principal, personagens, amigo)
        else:
            print("GAME OVER")
    else:
        saida = cenario_floresta(personagem_principal, personagens)
        if(saida == 2):
            cenario_final(personagem_principal, personagens, "sozinho")
        else:
            print("GAME OVER")

def main():
    print("##########################################################")
    print("***           Bem vindo ao jogo da Aventura            ***")
    print("***           Preparado para a sua jornada?            ***")
    print("##########################################################\n")
    print("Escolha uma das opções abaixo, digitando o número que está")
    print(" " * 15,"entre colchetes.\n")
    print(" " * 15,"[1] INICIAR")
    print(" " * 15, "[0] SAIR")

    entrada = int(input());
    while(entrada != 1 and entrada != 0):
        print("Utilize apenas os números 1 ou 0.")
        entrada = int(input())
    if(entrada == 0):
        exit()
    else:
        start()

main()
