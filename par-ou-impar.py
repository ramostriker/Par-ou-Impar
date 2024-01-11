loop = 1

while (loop < 10):

numero = int(input('Informe um número de 1 a 1000 e vou te dizer se ele é Par ou Impar: '))
resultado = numero % 2
if resultado == 0:
    print(f'Você me informou o número {numero} e ele é Par!')
else:
    print(f'Você me informou o número {numero} e ele é Impar!')
