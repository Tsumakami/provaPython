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
        pass
