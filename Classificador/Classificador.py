from base64 import decode
import os
import json
from bs4 import BeautifulSoup
import math
config = json.load(open(os.path.join(os.getcwd(),"config.json") ))

palavrasDict =  dict()

listaDocumentos = []

path = config['PastaRaiz'] + '/Crawler'
listDir =  filter(lambda dir : os.path.isdir(os.path.join(path,dir)) , os.listdir(path))

listaTFDicpositivo = []
listaTFDicNegativo = []

listaIDFDicpositivo = []
listaIDFDicNegativo = []

dictPAth = dict()

dictTFIDF = dict()

dictPAth["positivo"] =  "C:\\Users\\jefferson-pc\\Documents\\ProjetoReceitas\\ProjetoRI\\Crawler\\positivos"
dictPAth["negativo"] = "C:\\Users\\jefferson-pc\\Documents\\ProjetoReceitas\\ProjetoRI\\Crawler\\negativos"


for key in dictPAth: 
    for file in os.listdir(dictPAth[key]):
        textoDict = dict()
        fullpath = os.path.join(dictPAth[key],file)
        f = open(fullpath, mode="r", encoding="utf-8")
        soup =  BeautifulSoup(f.read())
        for script in soup(["script", "style"]):
            script.extract()   
        
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\\n'.join(chunk for chunk in chunks if chunk)
        
        listText = text.split("\\n")

        for linha in listText:
            for palavra  in linha.split(" "):
                palavra = palavra.lower()
                if textoDict.get(palavra) is  None :
                    textoDict[palavra] = 1
                else:
                    textoDict[palavra] = textoDict[palavra]  + 1

        if key == "positivo":
            listaTFDicpositivo.append(textoDict)
        else:
            listaTFDicNegativo.append(textoDict)


def pegaTFPalavrasDoc(path):
    dicTF = dict()
    f = open(path, mode="r", encoding="utf-8")
    soup =  BeautifulSoup(f.read())

    for script in soup(["script", "style"]):
        script.extract()   
    
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\\n'.join(chunk for chunk in chunks if chunk)
    
    listText = text.split("\\n")

    for linha in listText:
        for palavra  in linha.split(" "):
            palavra = palavra.lower()
            if dicTF.get(palavra) is  None :
                dicTF[palavra] = 1
            else:
                dicTF[palavra] = dicTF[palavra]  + 1
    return dicTF


for key in dictPAth: 
    for file in os.listdir(dictPAth[key]):
        textoDict = dict()
        fullpath = os.path.join(dictPAth[key],file)
        textoDict = pegaTFPalavrasDoc(fullpath)
        if key == "Positivo":
            listaTFDicpositivo.append(textoDict)
        else:
            listaTFDicNegativo.append(textoDict)

print("etapa 1")

def qtdOcorrencia(listaDic,palavra):
    qtdOcorrencia = 0
    for dic in listaDic:
        if not(dic.get(palavra) is  None):
                qtdOcorrencia  =  qtdOcorrencia + 1
    return qtdOcorrencia
    


def computaIDF(palavra,tipo):
    qtdOcorrenciaPositiva = qtdOcorrencia(listaTFDicpositivo,palavra)
    qtdOcorrenciaNegativa = qtdOcorrencia(listaTFDicNegativo,palavra)

    if (tipo == "positivo" and qtdOcorrenciaPositiva is None) or qtdOcorrenciaPositiva == 0:
        return 0
    
    if (tipo == "negativo" and qtdOcorrenciaNegativa is None) or qtdOcorrenciaNegativa == 0 :
        return 0

    if tipo == "positivo":
        return math.log10(200 / qtdOcorrenciaPositiva)
    
    return  math.log10(200 / qtdOcorrenciaNegativa)


# print("etapa2")

localPath  = "C:\\Users\\jefferson-pc\\Documents\\ProjetoReceitas\\ProjetoRI\\Crawler\\teste"
for file  in os.listdir(localPath):
    dicIdfPositivo = dict()
    dicIdfNegativo = dict()
    somapositivo = 0.01
    somanegativo = 0.01
    dicTf = pegaTFPalavrasDoc(os.path.join(localPath,file))
    for key in dicTf:
        if dicIdfPositivo.get(key) is  None:
            dicIdfPositivo[key] =  computaIDF(key,"positivo")
        if dicIdfNegativo.get(key) is  None:
            dicIdfNegativo[key] = computaIDF(key,"negativo")
    
    
    tf =  dict(sorted(dicTf.items(), key=lambda item: item[1]))
    posi =  dict(sorted(dicIdfPositivo.items(), key=lambda item: item[1]))
    nega =  dict(sorted(dicIdfNegativo.items(), key=lambda item: item[1]))
    
 











    

        
    
    
        

