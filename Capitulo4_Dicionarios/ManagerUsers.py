from Funcoes import *

usuarios = {}
opcao = perguntar()
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(usuarios)
    if opcao == "P":
        pesquisar(usuarios, input("Digite o código de acesso: ").upper())
    if opcao == "E":
        excluir(usuarios, input("Digite o código de acesso:  ").upper())
    if opcao == "L":
        listar(usuarios)
    opcao = perguntar()




