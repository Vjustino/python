
#def par_ou_impar(num):
#    if num % 2 == 0:
#        return 'par'
#    else:
#        return 'impar'

par_ou_impar = lambda num: 'Par' if num % 2 == 0 else 'Impar'

user_number = int(input('Digite um numero:'))

print(f'O número {user_number} é {par_ou_impar(user_number)}')
