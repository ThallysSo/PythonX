with open('teste.txt', 'r') as arquivo:  # 'r' forma normal de printar 'rb' printar bytes
    conteudo = arquivo.readlines()
print("Tipo de dado da variável ", type(conteudo))
print("Conteúdo do Arquivo", conteudo)
