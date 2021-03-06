


from fake_useragent import UserAgent
import requests as req
from bs4 import BeautifulSoup
import uuid
import os
import json
from urllib.parse import urlparse

config = json.load(open(os.path.join(os.getcwd(),"config.json") ))


def salvarArquivo(dominio,texto):
    guid = str(uuid.uuid4())
    path = os.path.join(config['PastaRaiz'],"Crawler",dominio)
    f = open(os.path.join(path, guid + ".txt"), "w",encoding='utf-8')
    f.write(str(texto))
    f.close()


def decodeSite(url):
    ua = UserAgent()
    header = {'User-Agent': str(ua.chrome)}
    result = req.get(url, headers=header)
    return result.content.decode("utf-8")

def pegarDominio(url):
    return urlparse(url).netloc.split(".")[0]

url = "https://vovopalmirinha.com.br/bolo-bem-casado/"

siteTexto = decodeSite(url)

salvarArquivo(pegarDominio(url),siteTexto)
