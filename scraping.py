from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
import requests

reque = requests.get('http://economia.awesomeapi.com.br/json/last/USD-BRL')
teste = reque.json()
print(teste['USDBRL']['high'])