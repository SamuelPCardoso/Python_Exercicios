from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
contador = 0

while contador <= 2:
    print('Suas opções:\n[0] Pedra\n[1] Papel\n[2] Tesoura')
    jogador = int(input('Qual é a sua jogada? '))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!')
    print('-#-' * 9)
    print(f'O Computador jogou {itens[computador]}')
    print(f'Você jogou {itens[jogador]}')
    print('-#-' * 9)

    if computador == 0:
        if jogador == 0:
            print('EMPATE!')
        elif jogador == 1:
            print('JOGADOR VENCEU!')
        elif jogador == 2:
            print('COMPUTADOR VENCEU!')
        else:
            print('Jogada Invalida!')
    elif computador == 1:
        if jogador == 0:
            print('COMPUTADOR VENCEU!')
        elif jogador == 1:
            print('EMPATE!')
        elif jogador == 2:
            print('JOGADOR VENCEU!')
        else:
            print('Jogada Invalida!')
    elif computador == 2:
        if jogador == 0:
            print('JOGADOR VENCEU!')
        elif jogador == 1:
            print('COMPUTADOR VENCEU!')
        elif jogador == 2:
            print('EMPATE!')
        else:
            print('Jogada Invalida!')
    print('-@-' * 10)
    contador += 1
