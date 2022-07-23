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

config = json.load(open(os.path.join(os.getcwd(),"..","config.json") ))
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
    result = req.get(url, headers=header)
    return result.content.decode()

def getSoup(url):
    return BeautifulSoup(decodeSite(url), "html.parser")
    

def salvarArquivo(url,dominio,texto):
    guid = str(uuid.uuid4())
    path = os.path.join(config['PastaRaiz'],"Crawler",dominio)

    bancoSite.append((guid,url))
    f = open(os.path.join(path, guid + ".txt"), "w",encoding='utf8')
    f.write(str(texto.encode('utf-8')))
    f.close()

##def navegacao(paginapai, pagina, tamanhoArvore,dominio):    
    # if existeUrl(pagina):
    #     return
    # if not  existeUrl(pagina):
    #     paginaText = decodeSite(pagina)
    #     salvarArquivo(pagina,dominio,paginaText) 
    # if tamanhoArvore <= 0:
    #   return
     
    # print(paginapai,' - ',pagina,' - ',tamanhoArvore) 
     
    # soup1 = getSoup(pagina)
    # listAncora1 = soup1.find_all('a', href=True)
    # for site in listAncora1:
    #     if dominio == pegarDominio(site["href"]) and pagina != paginapai  :
    #         navegacao(paginapai,site["href"], tamanhoArvore - 1 ,dominio)
    
def navegacao2(paginapai,pagina,tamanhoArvore):
    if  len(bancoSite) > 1000:
        return
    soup1 = getSoup(pagina)
    listAncora1 = soup1.find_all('a', href=True)
    existeUrlBase = existeUrl(pagina)
    for site in listAncora1:
        url = site["href"]
        if not existeUrlBase:
            navegacao2(pagina,url,tamanhoArvore + 1)

    print(paginapai,' - ',pagina,' - ',tamanhoArvore)
    if not  existeUrlBase:
        paginaText = decodeSite(pagina)
        salvarArquivo(pagina,dominio,paginaText) 
    
def criarPasta(dominio):
    path = os.path.join(config['PastaRaiz'],"Crawler",dominio)
    if not os.path.exists(path):
        os.mkdir(path)


#os.remove( os.path.join(config['PastaRaiz'],'lista.json'))
for site in config['Paginas']:
    soup = getSoup(site)
    dominio = pegarDominio(site)
    criarPasta(dominio)

    listAncora = soup.find_all('a', href=True)
   
    for subSite in listAncora:
        if dominio == pegarDominio(subSite["href"]):
          ##  navegacao2('vazio',subSite["href"],0)
           print(subSite["href"])
    #salvarLista()

