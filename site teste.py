import requests as r
from bs4 import BeautifulSoup

try:
    resultado =r.get('https://www.gov.br/pt-br')
except Exception as erro:
    print('Erro: ', erro)
else:
    resposta = resultado.text
    soup = BeautifulSoup(resposta, 'html.parser')

    print(soup.find('h2',class_="outstanding-title").prettify())