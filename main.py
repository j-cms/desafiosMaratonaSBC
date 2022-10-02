entrada = input('digte um numero: ')
tipo = type(entrada) is int
while tipo == False:
    entrada = input('digte um numero apenas: ')
    tipo = type(entrada) is int
    print(tipo)
print(entrada,"lalallaa")
