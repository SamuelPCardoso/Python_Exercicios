medida = int(
    input('Digite [1] para selecionar Celsius ou [2] para selecionar Fahrenheit: '))

if medida == 1:
    c = float(input('Digite a temperatura em °C: '))
    f = 9 * c / 5 + 32
    print(f'{c:.2f}°C corresponde a {f:.2f}°F.')
else:
    fa = float(input('Digite a temperatura em °F: '))
    ca = (fa - 32) * 5 / 9
    print(f'{fa:.2f}°F corresponde a {ca:.2f}°C')
