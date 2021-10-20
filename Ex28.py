import random
import time
computador = random.randint(0, 5)

print('*' * 55)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('*' * 55)
jogador = int(input('Em qual número eu pensei? '))
print('PROCESSANDO...')
time.sleep(0.8)

if jogador == computador:
    print(
        f'Parabéns!! Você VENCEU! Eu pensei também pensei no número {computador}.')
else:
    print(
        f'O COMPUTADOR VENCEU!! VAMOS DOMINAR O MUNDO! Eu pensei em {computador}.')
