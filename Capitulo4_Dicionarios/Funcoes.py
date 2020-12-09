import datetime
import random

now = datetime.datetime.now()
codigo = str((random.randrange(1, 101)))
data = now.strftime("%d/%m/%Y %H:%M:%S")


def perguntar():
    resposta = input("O que deseja realizar? \n "
                     + "<I> - Para Inserir um usuário \n"
                     + " <P> - Para Pesquisar um usuário \n"
                     + " <E> - Para Excluir um usuário \n"''
                     + " <L> - Para Listar um usuário \n").upper()
    return resposta


def inserir(usuarios):
    print("Seu código de acesso: ", codigo)
    print("Data registrada: ", data)
    usuarios[codigo] = [input("Digite o nome: ").upper(), data, codigo]


def inserirArquivo(usuarios):
    arquivo = open('Arquivo.txt', 'w')  # abrir arquivo
    lista = usuarios.get(codigo)
    arquivo.write(str(' [ Nome: ' + lista[0] +
                      ' [ Data: ' + lista[1] +
                      ' [ Código: ' + lista[2] + ']' +
                      '\n'))
    arquivo.close()


def pesquisar(usuarios, chave):
    lista = usuarios.get(chave)
    if lista is not None:
        print("Nome...........: " + lista[0])
        print("Data...........: " + lista[1])
        print("Código.........: " + lista[2])
    else:
        print("Não há dados correspondentes!")


def excluir(usuarios, chave):
    if usuarios.get(chave) is not None:
        del usuarios[chave]
        print("Usuário deletado!")
    else:
        print("Não há dados correspondentes!")


def listar(usuarios):
    for chave, valor in usuarios.items():
        print("Código...........: " + chave)
        print("Nome.............: " + valor[0])
        print("Data e Hora......: " + valor[1])
        print('==============================')
