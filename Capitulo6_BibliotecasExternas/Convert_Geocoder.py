from pygeocoder import Geocoder
# from Funcoes.Funcoes_JSON import ler_arquivo, gravar_arquivo

# dicionario = ler_arquivo("entrada.json")

endereco = 'QNN 22 conjunto I'
saida = Geocoder('AIzaSyDMNTWTw53ctTCocc5lYjAF7EGLxWTt1Rs').geocode(endereco).postal_code
print(saida)


# gravar_arquivo(saida, "saida.json")
