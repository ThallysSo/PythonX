from datetime import datetime
from random import randrange

def perguntar():
    resposta = input("O que deseja realizar? \n "
                     + "<I> - Para Inserir um usuário \n"
                     + " <P> - Para Pesquisar um usuário \n"
                     + " <E> - Para Excluir um usuário \n"
                     + " <L> - Para Listar um usuário: ").upper()
    return resposta


def inserir(usuarios):
    now = datetime.now
    codigo = str((randrange(1, 101)))
    data = now.strftime("%d/%m/%Y %H:%M:%S")

    arquivo = open('arquivo.txt', 'r') #abrir arquivo
    conteudo = arquivo.readlines()

    print("Seu código de acesso: ", codigo)
    print("Data registrada: ", data)

    usuarios[codigo] = [input("Digite o nome: ").upper(), data, codigo]

    lista = usuarios.get(codigo)
    conteudo.append(str(' [ Nome: ' + lista[0] +
                        ' [ Data: ' + lista[1] +
                        ' [ Código: ' + lista[2] +
                        '\n'))  # inserindo conteudo
    arquivo = open('arquivo.txt', 'w')  # abre o arquivo novamente (escreve)
    arquivo.writelines(conteudo)  # escreva o conteúdo criado
    arquivo.close()

def pesquisar(usuarios, chave):
    lista = usuarios.get(chave)
    if lista is not None:
        print("Nome...........: " + lista[0])
        print("Último acesso..: " + lista[1])
        print("Última estação.: " + lista[2])


def excluir(usuarios, chave):
    if usuarios.get(chave) is not None:
        del usuarios[chave]
    print("Objeto Eliminado")


def listar(usuarios):
    for chave, valor in usuarios.items():
        print("Objeto......")
        print("Login: ", chave)
        print("Dados: ", valor)

