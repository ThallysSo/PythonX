from Funcoes.FuncoesArquivos import *

inventario = {}
escolha = menu()
while escolha > 0 and escolha < 4:
    if escolha == 1:
        registrar(inventario)
    elif escolha == 2:
        gravar(inventario)
    elif escolha == 3:
        resultado = exibir()
        for linha in resultado:
            lista = linha.split(";")
            print("Data.........: ", lista[1])
            print("Descrição....: ", lista[2])
            print("Departamento.: ", lista[3])
    escolha = menu()
