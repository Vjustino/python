
rendimento = float(input('Digite o rendimento da tinta:'))

altura = int(input('Digite a altura da parede:'))

largura = int(input('Digite a largura da parede:'))

def quantidade():
    quanti = (altura * largura) / rendimento
    
    print(f'Você usara {quanti} de tinta')
    

quantidade()


