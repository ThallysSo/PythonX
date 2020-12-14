def menu():
    escolha = int(input('Digite: \n <1> Para registrar ativo '
                        '\n <2> Para gravar em arquivo '
                        '\n <3> Para exibir ativos armazenados \n'))
    return escolha


def registrar(dicionario):
    resp = 'S'
    while resp == 'S':
        dicionario[input('Digite o número patrimonial: ')] = [input('Digite a data da última atualização: '),
                                                              input('Digite a descrição: '),
                                                              input('Digite o departamento: ')]
        resp = input('Digite <S> para continuar. ').upper()


def gravar(dicionario):
    with open('inventario.csv', 'a') as estoque:
        for chave, valor in dicionario.items():
            estoque.write(chave + ";" + valor[0] + ";" + valor[1] + ";" + valor[2] + "")
    return print('Gravado com sucesso!')


def exibir():
    with open('inventario.csv', 'r') as estoque:
        linhas = estoque.readlines()
    return linhas
