
entrada = int(input('digte um numero: '))
fatores = 0
aux = 0
if entrada>1000000 :
    entrada = int(input('digte um numero ate 1000000: '))

for div in range(2, (entrada + 1), 1):  # fazer um range pra percorrer o vetor
    aux = 0
    # print("div",div) #teste
    for j in range(2, div,
                   1):  # fazer um range no divisor e ver se ele é primo
        if (
                div / j > 1 and div % j == 0):  # a condicao pra ser primo é ser nao ser divisivel duas ou mais vezes e o resto ser 0. se der uma vez e o resto for >0, como em 3%2, nao entra e o codigo da certo, ja que 3 é primo
            aux += 1
            break  # nao percorre todos os numeros se ja nao for primo
        # print("div", div, 'j',j,'aux',aux) #teste

    if aux == 0 and entrada % div == 0:  # ve se o numero é primo e se a divisao da entrada por esse numero da exata
        fatores += 1

print('{}:{}'.format(entrada, fatores))

