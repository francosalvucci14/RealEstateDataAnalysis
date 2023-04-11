# from selenium import webdriver
# from bs4 import BeautifulSoup
# import pandas as pd

# driver = webdriver.Firefox()
# products=[] #List to store name of the product
# prices=[] #List to store price of the product
# ratings=[] #List to store rating of the product
# driver.get("https://francosalvucci14.github.io/bankapp/")

# content = driver.page_source
# soup = BeautifulSoup(content,"html.parser")
# for a in soup.findAll('div', attrs={'class':'container'}):
#     print("ciao")
#     name=a.find('div', attrs={'class':'author'})
#     print(name)
#     comment=a.find('div', attrs={'class':'comment'})
#     #rating=a.find('div', attrs={'class':'_3LWZlK'})
#     products.append(name.text)
#     prices.append(comment.text)
#     #ratings.append(rating.text) 
# print(products,prices,ratings)
# df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
# df.to_csv('products.csv', index=False, encoding='utf-8')

# Importare moduli
import requests
import pandas as pd
from bs4 import BeautifulSoup
import sys
import getopt
# Indirizzo sito web

for i in range(1,3):
    url = f"https://www.immobiliare.it/vendita-case/roma/centocelle/?criterio=rilevanza&pag={i}"
    print(url)
    # Eseguire richiesta GET
    response = requests.get(url)
    # Analizzare documento HTML del codice sorgente con BeautifulSoup
    html = BeautifulSoup(response.text, 'html.parser')
    # Estrarre tutte le citazioni e gli autori dal documento HTML
    locali_html = html.find_all('a', class_="in-card__title")
    price_html = html.find_all('li', class_="nd-list__item in-feat__item in-feat__item--main in-realEstateListCard__features--main")
    # Raccogliere le citazioni in un elenco
    locali = list()
    for locale in locali_html:
        locali.append(locale.text)
    # Raccogliere gli autori in un elenco
    prices = list()
    for price in price_html:
        prices.append(price.text) 
    # Per eseguire il test, combinare e visualizzare le voci di entrambi gli elenchi
    for t in zip(locali,prices):
        print(t)
    # Salvare le citazioni e gli autori in un file CSV nella directory corrente
    # Aprire il file con Excel / LibreOffice, ecc.
    # with open('./citazioni.csv', 'w') as csv_file:
    #     csv_writer = csv.writer(csv_file, dialect='excel')
    #     csv_writer.writerows(zip(quotes, authors))
    df = pd.DataFrame({'Locali':locali,'Prezzi':prices})
     
df.to_csv('Immobiliare.csv', index=False, encoding='utf-8')