p = float(input('Qual seu peso?'))
a = float(input('Qual sua altura?'))

imc = p/(a**2)
print(f'{imc:.2f}')
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso normal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 35:
    print('Obeso leve')
elif imc < 40:
    print('Obeso moderado')
elif imc >= 40:
    print('Obeso mórbido')