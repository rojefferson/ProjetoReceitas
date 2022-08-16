from base64 import decode
from importlib.resources import path
import os
import json
from bs4 import BeautifulSoup
import math

# config = json.load(open(os.path.join(os.getcwd(),"config.json") ))
listaTFDicpositivo = []
listaTFDicNegativo = []

listaIDFDicpositivo = []
listaIDFDicNegativo = []

dictPAth = dict()

dictTFIDF = dict()

dictPAth["Positivo"] =  "C:\\Users\\jefferson-pc\\Documents\\ProjetoReceitas\\ProjetoRI\\Crawler\\positivos"
dictPAth["Negativo"] = "C:\\Users\\jefferson-pc\\Documents\\ProjetoReceitas\\ProjetoRI\\Crawler\\negativos"




for key in dictPAth: 
    for file in os.listdir(dir):
        textoDict = dict()
        fullpath = os.path.join(dir,file)
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

        if key == "Positivo":
            listaTFDicpositivo.append(textoDict)
        else:
            listaTFDicNegativo.append(textoDict)




def qtdOcorrencia(listaDic,palavra):
    qtdOcorrencia = 0
    for dic in listaDic:
        if dic[palavra] > 0:
            qtdOcorrencia  =  qtdOcorrencia + 1
    


def computaIDF(palavra):
    qtdOcorrenciaPositiva = qtdOcorrencia(listaTFDicpositivo,palavra)
    qtdOcorrenciaNegativa = qtdOcorrencia(listaTFDicNegativo,palavra)

    listaIDFDicpositivo[palavra] = math.log10(200 / qtdOcorrenciaPositiva)
    listaIDFDicNegativo[palavra] = math.log10(200 / qtdOcorrenciaNegativa)




