import os
import json
from bs4 import BeautifulSoup
config = json.load(open('../config.json'))



arr = os.listdir(config['PastaRaiz'] + '/Crawler')

def classificador(pagina):
    soup = BeautifulSoup(pagina)
    return False

for arquivo in arr:
    fullPath = config['PastaRaiz'] + '/Crawler' + '/' + arquivo
    f = open( fullPath, "r")
    print(classificador(f.read()))
print(arr)