import datetime
import random

data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
codigo = str((random.randrange(1, 101)))



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
    arquivo = open('../Capitulo4_Dicionarios/arquivo.txt', 'r')  # abrir arquivo
    conteudo = arquivo.readlines()

    lista = usuarios.get(codigo)
    conteudo.append(str(' [ Nome: ' + lista[0] +
                        ' [ Data: ' + lista[1] +
                        ' [ Código: ' + lista[2] + ']' +
                        '\n'))
    arquivo = open('../Capitulo4_Dicionarios/arquivo.txt', 'w')
    arquivo.writelines(conteudo)
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
