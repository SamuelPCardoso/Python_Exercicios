import math

oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Compimento do cateto adjacente: '))
hipotenusa = math.hypot(oposto, adjacente)

print(f'A hipotenusa vai medir {hipotenusa:.2f}.')


# oposto = float(input('Comprimento do cateto oposto: '))
# adjacente = float(input('Compimento do cateto adjacente: '))
# hipotenusa = (oposto ** 2 + adjacente ** 2) ** (1 / 2)
#
# print(f'A hipotenusa vai medir {hipotenusa:.2f}.')
