from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

options = Options()
# options.add_argument('--headless')
options.add_argument('window-size=400,800')

navegador = webdriver.Chrome(options=options)

navegador.get('https://www.airbnb.com.br')

sleep(2)

span_click = navegador.find_element(by=By.XPATH, value='//*[@id="site-content"]/div[1]/div/div/div/div/div/div/div['
                                                       '2]/div[1]/div/div[1]/div/div/div/div/div/div[1]/button/div['
                                                       '2]/div[1]')
span_click.click()

sleep(2)

input_place = navegador.find_element(by=By.TAG_NAME, value='input')
input_place.send_keys('São Paulo')
input_place.submit()

sleep(2)

next_click = navegador.find_element(by=By.XPATH, value='//*[@id="accordion-body-/homes-2"]/div[2]/footer/button[2]')
next_click.click()

click_people = navegador.find_element(by=By.XPATH, value='//*[@id="stepper-adults"]/button[2]')
click_people.click()
click_people.click()

sleep(0.5)

click_search = navegador.find_element(by=By.XPATH, value='//*[@id="vertical-tabs"]/div[3]/footer/button[2]')
click_search.click()

sleep(4)

page_content = navegador.page_source

site = BeautifulSoup(page_content, 'html.parser')
hospedagens = site.findAll('div', attrs={'itemprop': 'itemListElement'})

# print(hospedagem.prettify())

dados_hospedagem = []

for hospedagem in hospedagens:
    hospedagem_descricao = hospedagem.find('meta', attrs={'itemprop': 'name'})
    hospedagem_descricao = hospedagem_descricao['content']
    hospedagem_url = hospedagem.find('meta', attrs={'itemprop': 'url'})
    hospedagem_url = hospedagem_url['content']
    hospedagem_estrela = hospedagem.find('span', attrs={'role': 'img'})
    hospedagem_estrela = hospedagem_estrela['aria-label']
    hospedagem_valor = hospedagem.findAll('span', attrs={'class': 'a8jt5op dir dir-ltr'})[0].text

    print('Descrição: ', hospedagem_descricao)
    print('URL: ', hospedagem_url)
    print(hospedagem_estrela)
    print('Valor: ', hospedagem_valor)

    print()

    dados_hospedagem.append([hospedagem_descricao, hospedagem_url, hospedagem_estrela, hospedagem_valor])

dados = pd.DataFrame(dados_hospedagem, columns=['Descrição', 'URL', 'Avaliação', 'Valor'])

dados.to_csv('hospedagem.csv', index=False)