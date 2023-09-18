
numeros = [1, 2, 3,4 ,5, 6]

quadrado = lambda num: num ** 2

resultado = []

for i in numeros:
    resultado.append(quadrado(i))

print(f'Os quadrados dos numeros {numeros} são {resultado}')