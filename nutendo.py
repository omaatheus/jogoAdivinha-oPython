import random
tentativas = 0
numero = 0

print(f'Este é um jogo produzido pela nutendo corp.\n\n')
print(f'Tente adivinhar meu pensamento\n')
nivel = int(input(f'Escolha o nível de dificuldade: 3, 2, 1 '))

if(nivel == 3):
    adivinha = random.randrange(1,70)
    respNivel = 70
elif(nivel == 2):
    adivinha = random.randrange(1,35)
    respNivel = 35
else:
    adivinha = random.randrange(1,15)
    respNivel = 15

while (numero != adivinha):
    print(adivinha)
    tentativas += 1
    numero = int(input(f'Escolha um número 1 a {respNivel} '))
    
    if (numero < adivinha):
        print('Chutou baixo, tente novamente')
    elif (numero > adivinha):
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
            nivel = int(input(f'Escolha o nível de dificuldade: 3, 2, 1 '))
            if(nivel == 3):
                adivinha = random.randrange(1,70)
                respNivel = 70
            elif(nivel == 2):
                adivinha = random.randrange(1,35)
                respNivel = 35
            else:
                adivinha = random.randrange(1,15)
                respNivel = 15
            
        
