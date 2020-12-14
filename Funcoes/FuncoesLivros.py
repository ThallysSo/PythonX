from random import randint


def menu():
    print(' BEM VINDO À BIBLIOTECA!')
    resposta = input("O que deseja realizar? \n "
                     + "<I> - INSERT de um Livro \n"
                     + " <P> - SELECT de um Livro \n").upper()
    return resposta


def inserir(dicionario):
    dicionario[str(randint(1, 10))] = [input("Qual o nome do livro: "), input('Qual o ano do livro: ')]


def inserirArquivo(dicionario):
    with open('biblioteca.csv', 'a') as biblioteca:
        for chave, valor in dicionario.items():
            biblioteca.write(chave + ";" + valor[0] + ";" + valor[1] + ";" + '\n')
    return print('Gravado com sucesso!')


def pesquisar(dicionario):
    with open('biblioteca.csv', 'r') as biblioteca:
        print(biblioteca.read())
