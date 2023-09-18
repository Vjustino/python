
temp = int(input('Digite a temperadura da carne:'))


if temp<= 40:
    print('Deixar Assar mais')

elif temp > 40 and temp< 48:
    print('Selada')

elif temp > 54 and temp< 70:
    print('Carne ao ponto')

else:
    print('Bem passada')