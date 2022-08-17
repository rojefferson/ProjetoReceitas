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
import csv


path = "C:\\Users\\jefferson-pc\\Documents\\ProjetoReceitas\\Classificador\\Receiteria"


def criaCsvInformacoes(informacoes,path):
    with open(path, mode="w", encoding="utf-8") as csvfile:
        fieldnames = ["NomeReceita", "Ingredientes", "Passos"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for informacao in informacoes:
            writer.writerow({"NomeReceita": informacao[0], "Ingredientes": informacao[1], "Passos": informacao[2]})  

for file in os.listdir(path):
    fullPaht = os.path.join(path,file)
    f = open(fullPaht, mode="r", encoding="utf-8")
    soup =  BeautifulSoup(f.read())

    
    ingredientes = soup.find("h2").find_next_siblings("ul")[0].find_all("li")
    
    textoIngredientes = " ".join(ingrediente.get_text() for ingrediente in ingredientes)
    print(textoIngredientes)
    
    passos = soup.find("h2").find_next_siblings("ol")[0].find_all("li")
    textoPassos = " ".join(passo.get_text() for passo in passos)
    print(textoPassos)

    nomeReceita = soup.find("h1").get_text()

    informacoes = [(nomeReceita, textoIngredientes, textoPassos)]

    file= "informacoes"
    criaCsvInformacoes(informacoes, "C:\\Users\\jefferson-pc\\Documents\\ProjetoReceitas\\Classificador\\Receiteria\\" + file + ".csv")


