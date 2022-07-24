from ast import For
from base64 import decode
from genericpath import exists
import json
from re import sub
import requests as req
from bs4 import BeautifulSoup
import uuid
from urllib.parse import urlparse
from fake_useragent import UserAgent
import os
import re

config = json.load(open(os.path.join(os.getcwd(),"config.json") ))
bancoSite = []

tentativasSite = 5

def salvarLista():
    with open( os.path.join(config['PastaRaiz'],'lista.json'), 'w') as filehandle:
        json.dump(bancoSite, filehandle)

def existeUrl(url):
    for item in bancoSite:
        if(item[1] == url ):     
            return True
    return False

def pegarDominio(url):
    return urlparse(url).netloc.split(".")[0]

def decodeSite(url):
    if url == "#primary":
        return ""
    try:
        ua = UserAgent()
        header = {'User-Agent': str(ua.chrome)}
        retorno  =""      
        for t in range(tentativasSite):
         result = req.get(url, headers=header)
         if result.status_code == 200: 
            retorno = result.content.decode()
            break

        return retorno
    except:
        return ""

def getSoup(url):
    return BeautifulSoup(decodeSite(url), "html.parser")


def salvarArquivo(url,dominio,texto):
    guid = str(uuid.uuid4())
    path = os.path.join(config['PastaRaiz'],"Crawler",dominio)

    bancoSite.append((guid,url))
    f = open(os.path.join(path, guid + ".txt"), "w",encoding='utf8')
    f.write(str(texto.encode('utf-8')))
    f.close()


def navegacao2(paginapai,pagina):
   
    if paginapai == pagina or pagina == "#primary" or  len(bancoSite) > 1000 or existeUrl(pagina):
        return 

    paginaText = decodeSite(pagina)
    salvarArquivo(pagina,dominio,paginaText) 

    print(str(len(bancoSite)) + " - " + paginapai + " - " + pagina)

    soup1 = BeautifulSoup(paginaText, "html.parser")
    listAncora1 = soup1.find_all('a', href=True)
    
    for site in listAncora1:
        url = site["href"]
        if  pegarDominio(url) == pegarDominio(paginapai):
            navegacao2(pagina,url)
                 
    
def criarPasta(dominio):
    path = os.path.join(config['PastaRaiz'],"Crawler",dominio)
    if not os.path.exists(path):
        os.mkdir(path)

def is_valid_url(url):
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url is not None and regex.search(url)

#os.remove( os.path.join(config['PastaRaiz'],'lista.json'))
for site in config['Paginas']:
    soup = getSoup(site)
    dominio = pegarDominio(site)
   ## criarPasta(dominio)

    listAncora =  filter(lambda x: is_valid_url(x["href"]), soup.find_all('a', href=True))
   
    for subSite in listAncora:
        if dominio == pegarDominio(subSite["href"]):
            navegacao2(site,subSite["href"])
    
    print(bancoSite)
    
    #salvarLista()

