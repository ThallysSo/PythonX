from random import randint
codigo = randint(1, 100)

def menu():
    print(' BEM VINDO À BIBLIOTECA!')
    resposta = input("O que deseja realizar? \n "
                     + "<I> - INSERT de um Livro \n"
                     + " <P> - SELECT de um Livro \n").upper()
    return resposta


def inserir(dicionario):
    print('Código:', codigo)
    dicionario[codigo] = [input("Qual o nome do livro: "), input('Qual o ano do livro: ')]
    return

def inserirArquivo(dicionario, codigo):
    with open('biblioteca.csv', 'a') as biblioteca:
        lista = str(dicionario.get(codigo))
        for chave, valor in dicionario.items():
            biblioteca.write(lista + ";" + valor[0] + ";" + valor[1] + ";" + '\n')
    return print('Gravado com sucesso!')


def pesquisar(dicionario):
    with open('biblioteca.csv', 'r') as biblioteca:
        print(biblioteca.read())
