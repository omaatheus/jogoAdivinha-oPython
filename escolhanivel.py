import random

def escolhaNivel():
    nivel = int(input(f'Escolha o nível de dificuldade: 3, 2, 1 '))

    if(nivel == 3):
        respNivel = 70
    elif(nivel == 2):
        respNivel = 35
    else:
        respNivel = 15
        
    return respNivel

def sortNumber(respNivel):
    return random.randint(1, respNivel)