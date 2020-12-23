from pygeocoder import Geocoder
from Funcoes.Funcoes_JSON import ler_arquivo, gravar_arquivo

dicionario = ler_arquivo("entrada.json")
saida = {'Local': Geocoder('API').reverse_geocode(-15.8327086, -48.1108383).postal_code}
gravar_arquivo(saida, "saida.json")
