def potencial( base, expoente = 2):
    return base ** expoente

user_number = int(input('Digite o numero base:'))
user_exponte = input('Digite um expoente (default 2):')

if user_exponte:
    print(f'O resultado é: {potencial(user_number, int(user_exponte))}')

else: print(f' O resultado é:{potencial(user_number)}')