capitais = {
    'Brasil':'Brasília',
    'Paris' : 'França',
    'Argentina' : 'Buenos Aires',
    'Chile' : 'Santiago',
    'Italia' : 'Roma'
}

pais_usuario = input('Digite o nome do país:')

if pais_usuario in capitais:
    print(f'A capital de {pais_usuario} é {capitais[pais_usuario]}')
else:
    ('Nao temos informaçoes desse país')