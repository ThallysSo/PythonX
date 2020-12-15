from Funcoes.FuncoesLivros import *

biblioteca = {}
escolha = menu()

while escolha == 'I' or escolha == 'P':
    if escolha == 'I':
        inserir(biblioteca)
        inserirArquivo(biblioteca)
    elif escolha == 'P':
        pesquisar(biblioteca)
    escolha = menu()