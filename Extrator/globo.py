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


path = "C:\\Users\\jefferson-pc\\Documents\\ProjetoReceitas\\Classificador\\globo"

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

    ingredientes = soup.find("ul",{"class":"content-unordered-list"}).get_text()

    modoPreparo =  soup.find_all("div",{"class":"mc-column content-text active-extra-styles"})[5].get_text()

    nomeReceita = soup.find_all("h1",{"class":"content-head__title"})[0].get_text()

    print(nomeReceita)