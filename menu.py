import random

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
    print("Crição do personagem")
    nome = input("Digite seu nome, nobre guerreiro(a): ")
    print("Olá " + nome + ", seus atributos de vida são: 100 e " +
    "de dano são: 50 \n")

    principal = {
        'nome': nome,
        'vida': 100,
        'dano': 50
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
    while(entrada != 1 and entrada != 2):
        print("Utilize apenas os números 1 ou 2.")
        entrada = int(input())

    return entrada

def montanha(personagem_principal, personagens):
    print("E então o(a) grande Cavaleiro(a) "+ personagem_principal['nome'] +
        "decidiu seguir pelas montanhas frias e cheias de gelo do sudoeste" +
        " do Himalaia· Após muito sofrimento quando, está quase chegando ao" +
        "topo, avista um andarilho, ao aproximar-se, o mesmo o " +
        "interroga. Para aonde vai, jovem Cavaleiro(a), gostaria de um agasalho?" +
        "Você fica intrigado com a situação, várias coisas passam por sua cabeca," +
        "mas sem hesitar você:\n")
    print()
def cenario_dois():

def start():
    personagem_principal = criacao_personagem();
    get_personagens()
    print("Sua jornada inicia agora "+ personagem_principal['nome'] +". Boa sorte!\n")
    print(cenario_um())

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
