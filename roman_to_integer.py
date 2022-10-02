entrada = list(input("digite um numero em  romano: "))
soma =  0
aux = 0

#converter a string pra decimal
for string in range(0, len(entrada)):
    if entrada[string]== "i":
         entrada[string] = 1
    elif entrada[string] == "v":
        entrada[string] = 5
    elif entrada[string] == "x":
        entrada[string] = 10
    elif entrada[string] == "l":
        entrada[string] = 50
    elif entrada[string] == "c":
        entrada[string] = 100
    elif entrada[string] == "d":
        entrada[string] = 500
    elif entrada[string] == "m":
        entrada[string] = 1000
tam = len(entrada) + 1
entrada.append(0) #condicao pra parada e pra facilitar a comparação do ultimo algarismo

#comparar e fazer o calculo
while entrada[aux] != 0: #pra parar quando achar o primeiro zero

        # se o numero seguinte for maior q o vigente, o resultado sera =  proximo-vigente
        if entrada[aux+1]>entrada[aux]:
            soma += (entrada[aux+1]) - (entrada[aux])
            aux+=2 # pra nao fazer nenhuma operação no numero q usamos como base pra subtrair

        #se o numero atual for maior ou igual o proximo
        elif entrada[aux]>=entrada[aux+1]:
            soma += (entrada[aux])
            aux+=1 #pegar o proximo numero
print("output: ",soma)


