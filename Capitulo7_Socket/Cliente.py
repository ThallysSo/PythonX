from socket import *

servidor = "127.0.0.1"
porta = 43210

print('Digite SAIR pra fechar o chat.')
while True:
    obj_socket = socket(AF_INET, SOCK_STREAM)
    obj_socket.connect((servidor, porta))
    msg = bytes(input("Sua mensagem: "), 'utf-8')
    if str(msg)[2:-1] == 'SAIR':
        print('Saindo da conversa...')
        obj_socket.send(msg)
        break
    obj_socket.send(msg)
    resposta = obj_socket.recv(1024)
    print("Resposta do Servidor: ", str(resposta)[2:-1])

obj_socket.close()
