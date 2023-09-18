funcionarios = ['Ana','Marcos','Alice','Pedro','Sophia','Bruno','Melissa']

turno_dia = ['Ana','Marcos','Alice','Melissa']

turno_noite = ['Pedro','Sophia','Bruno']

tem_carro = ['Marcos','Alice','Bruno','Melissa']

func1 = set(funcionarios)


func2 = set(turno_dia)

func3 = set(turno_noite)

func4 = set(tem_carro)

print(func4 & func2)
print(func4 & func3)
print(func1 - func4)