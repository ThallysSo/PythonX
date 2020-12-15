# Qual o total de voos internacionais quue partiram do aeroporto de Logan no ano de 2014

with open("economic-indicators.csv", "r") as boston:
    total = 0
    for linha in boston.readlines()[1:-1]:
        total = total + float(linha.split(',')[3])  # separa pela vigula na posição 3
    print("O total de voos é: ", total)