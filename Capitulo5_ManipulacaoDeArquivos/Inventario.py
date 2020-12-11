from Funcoes.FuncoesArquivos import *

inventario = {}
escolha = menu()
while escolha > 0 and escolha < 4:
    if escolha == 1:
        registrar(inventario)
    elif escolha == 2:
        gravar(inventario)
    elif escolha == 3:
        exibir()
    escolha = menu()
