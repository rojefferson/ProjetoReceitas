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



path = "C:\\Users\\jefferson-pc\\Documents\\ProjetoReceitas\\Classificador\\classificados"

for folder in os.listdir(path):
    for file in os.listdir(os.path.join(path,folder)):
        fullPaht = os.path.join(path,folder,file)
        f = open(fullPaht, mode="r", encoding="utf-8")
        soup =  BeautifulSoup(f.read())

        if(folder == "tudogostoso"):
            pass
        nomeReceita = soup.find("h1").get_text().strip()

        ingredientes = soup.find_all("ul")

        print(ingredientes)
