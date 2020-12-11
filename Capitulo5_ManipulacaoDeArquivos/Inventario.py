inventario = {}
escolha = int(input('Digite: \n <1> Para registrar ativo \n <2> Para gravar em arquivo \n <3> Para exibir ativos armazenados \n'))

while escolha > 1 and escolha < 4:
    if escolha == 1:
        resp = 'S'
        while resp == 'S':
            inventario[input('Digite o número patrimonial: ')] =\
                [input('Digite a data da última atualização: '),
                 input('Digite a descrição: '),
                 input('Digite o departamento: ')]
        resp = input('Digite <S> para continuar. ').upper()

    elif escolha == 2:
        with open('invetario.csv', 'a') as estoque:
            for chave, valor in inventario.items():
                estoque.write(chave + ' ; ' + valor[0] + ' ; ' + valor[1] + ' ; ' + valor[2] + '\n')
                print('Gravado com sucesso!')

    elif escolha == 3:
        with open('invetario.csv', 'r') as estoque:
            print(estoque.readlines())

    escolha = int(input('Digite: '
                        + ' <1> Para registrar ativo \n'
                        + '         <2> Para gravar em arquivo \n'
                        + '         <3> Para exibir ativos armazenados \n'))
