largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura * altura
tinta = area / 2

print(
    f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area}m².')
print(f'Para pintar está parede você precisará de {tinta}L de tinta.')
