m = float(input('Digite uma distância em metros: '))
mm = m * 1000
cm = m * 100
dm = m * 10
dam = m / 10
hm = m / 100
km = m / 1000

print(f'A medida de {m:.2f} corresponde a:')
print(f'{mm}mm')
print(f'{cm}cm')
print(f'{dm}dm')
print(f'{dam}dam')
print(f'{hm}hm')
print(f'{km}km')
