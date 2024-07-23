import random
from escolhanivel import escolhaNivel, sortNumber

tentativas = 0
numero = 0

print(f'Este é um jogo produzido pela nutendo corp.\n\n')
print(f'Tente adivinhar meu pensamento\n')

respNivel = escolhaNivel()
aleatorio = sortNumber(respNivel)
print(aleatorio)

while (numero != aleatorio):
    tentativas += 1
    numero = int(input(f'Escolha um número 1 a {respNivel} '))
    
    if (numero < aleatorio):
        print('Chutou baixo, tente novamente')
    elif (numero > aleatorio):
        print('Chutou Alto, tente novamente')
    else:
        
        print(f'Você acertou em {tentativas} tentativas')
        numero = 0
        tentativas = 0
        resposta = input('Deseja continuar? (S/N) ').lower()
        if (resposta != 's'):
            print('Que pena, até mais então!')
            break #break é um método que para a operação
        else:
            
            respNivel = escolhaNivel()
            aleatorio = sortNumber(respNivel)
            print(aleatorio)
