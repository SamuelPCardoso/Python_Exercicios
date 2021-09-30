import time

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
time.sleep(0.5)

# print('Seu nome maiúsculo é {}'.format(nome.upper()))
# print('Seu nome minúsculo é {}'.format(nome.lower()))
# print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))

print(f'Seu nome maiúsculo é {nome.upper()}.')
print(f'Seu nome minúsculo é {nome.lower()}.')
print('Seu nome tem ao todo {}.'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras.')
