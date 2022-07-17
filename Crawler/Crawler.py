from base64 import decode
import json
import requests as req
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

config = json.load(open('../config.json'))


def decodeSite(url):
    ua = UserAgent()
    header = {'User-Agent': str(ua.chrome)}
    result = req.get(site, headers=header)
    soup = BeautifulSoup(result.content.decode(), "html.parser")
    return soup


def navegacao(pagina, tamanhoArvore):
    ##Salvar página no disco 
    soup = decodeSite(pagina)
    listAncora = soup.find_all('a', href=True)
    for site in listAncora:
        navegacao(site,tamanhoArvore - 1)

pass

for site in config['Paginas']:
    soup = decodeSite(site)
    listAncora = soup.find_all('a', href=True)
    print(listAncora[20]["href"])
    for subSite in listAncora:
        navegacao(subSite["href"], 10)
    break
