# Qual o total de voos internacionais quue partiram do aeroporto de Logan no ano de 2014

with open("economic-indicators.csv", "r") as boston:
    total = 0
    for linha in boston.readlines()[1:-1]:
        total = total + float(linha.split(',')[3])  # separa pela vigula na posição 3
    print("O total de voos é: ", total)

with open("economic-indicators.csv", "r") as boston:
    maiorPassageiros = 0
    for linha in boston.readlines()[1:-1]:
        numPassageiros = float(linha.split(',')[2])
        if numPassageiros > maiorPassageiros:
            maiorPassageiros = numPassageiros
            mes = int(linha.split(',')[1]), int(linha.split(',')[0])
    print("O mês e ano ", mes[0], '/', mes[1], "houveram ", maiorPassageiros, 'passageiros')

with open("economic-indicators.csv", "r") as boston:
    quantidadeDePassageirosQuePassaramPeloAeroporto = 0
    quantidadeDeVezesQueApareceaData = 0
    usuario = float(input('Digite o ano para saber o total de pessoas que passaram pelo aeroporto: '))
    for linha in boston.readlines()[1:-1]:
        if usuario == int(linha.split(',')[0]):
            quantidadeDeVezesQueApareceaData += 1
            quantidadeDePassageirosQuePassaramPeloAeroporto += int(linha.split(',')[2])
    print(quantidadeDeVezesQueApareceaData)
    print(quantidadeDePassageirosQuePassaramPeloAeroporto)

with open("economic-indicators.csv", "r") as boston:
    maiorMediadeDiaria = 0
    usuario = int(input('Digite o mês para saber a maior diária de um hotel: '))
    for linha in boston.readlines()[1:-1]:
        if usuario == int(linha.split(',')[1]) and maiorMediadeDiaria < float(linha.split(',')[5]):
            maiorMediadeDiaria = float(linha.split(',')[5])
    print('Maior média é: ', maiorMediadeDiaria)


