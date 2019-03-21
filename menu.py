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
    print("Olá: " + nome + " seus atributos de vida são: 100 e" +
    "de dano são: 50 ")

    principal = {
        'nome': nome,
        'vida': 100,
        'dano': 50
    }

    return principal

def start():
    personagem_principal = criacao_personagem();
    print(get_personagens())


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
    if(entrada != 1 and entrada != 0):
        print("Utilize apenas os números 1 ou 0.")
    else:
        if(entrada == 0):
            exit()
        else:
            start()

main()
