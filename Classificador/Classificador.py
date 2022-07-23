from base64 import decode
import os
import json
from bs4 import BeautifulSoup
config = json.load(open(os.path.join(os.getcwd(),"config.json") ))

palavrasDict =  dict()

listaDocumentos = []

path = config['PastaRaiz'] + '/Crawler'
listDir =  filter(lambda dir : os.path.isdir(os.path.join(path,dir)) , os.listdir(path))

# def classificador(pagina):
#     soup = BeautifulSoup(pagina)
#     return False

def calculaTF():         
    tf_dic = {}    
    num_palavras_doc = len(palavrasDict)     
    for palavra, contagem in palavrasDict.items():         
        tf_dic[palavra] = contagem/float(num_palavras_doc)         
    return(tf_dic)
    
for dir in listDir:
    textoDict = dict()
    for arquivo in  os.listdir( os.path.join(path,dir)):
        fullPath = os.path.join(path,dir,arquivo)
        print(fullPath)
        f = open( fullPath, mode="r", encoding="utf-8")
        soup =  BeautifulSoup(f.read())
        for script in soup(["script", "style"]):
            script.extract()   
        
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        listText = text.split("\n")

        for linha in listText:
            for palavra  in linha.split(" "):
                palavra = palavra.lower()
                if textoDict.get(palavra) is  None :
                    textoDict[palavra] = 1
                else:
                    textoDict[palavra] = palavrasDict[palavra]  + 1

        listaDocumentos.append(textoDict)
    
    
        

