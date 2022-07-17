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

config = json.load(open(os.path.join(os.getcwd(),"config.json") ))
bancoSite = []

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
    ua = UserAgent()
    header = {'User-Agent': str(ua.chrome)}
    result = req.get(site, headers=header)
    return result.content.decode()

def getSoup(url):
    soup = BeautifulSoup(decodeSite(url), "html.parser")
    return soup

def salvarArquivo(url,dominio,texto):
    guid = str(uuid.uuid4())
    path = os.path.join(config['PastaRaiz'],"Crawler",dominio)

    bancoSite.append((guid,url))
    f = open(os.path.join(path, guid + ".txt"), "w")
    f.write(str(texto.encode('utf-8')))
    f.close()

def navegacao(pagina, tamanhoArvore,dominio):  
    paginaText = decodeSite(pagina)
    if not existeUrl(pagina):
        salvarArquivo(pagina,dominio,paginaText)
    
    if tamanhoArvore <= 0:
         return
        
    listAncora = soup.find_all('a', href=True)
    for site in listAncora:
        if dominio == pegarDominio(site["href"]):
            navegacao(site["href"], tamanhoArvore - 1,dominio)

def criarPasta(dominio):
    path = os.path.join(config['PastaRaiz'],"Crawler",dominio)
    if not os.path.exists(path):
        os.mkdir(path)

for site in config['Paginas']:
    soup = getSoup(site)
    dominio = pegarDominio(site)
    criarPasta(dominio)

    listAncora = soup.find_all('a', href=True)
   
    for subSite in listAncora:
        if dominio == pegarDominio(subSite["href"]):
            navegacao(subSite["href"], 0,dominio)
        salvarLista()

