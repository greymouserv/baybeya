from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from bs4 import BeautifulSoup

chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chrome.get("https://www.kleinanzeigen.de/s-zu-verschenken/seite:1/c192")
chrome.execute_script('window.scrollTo(0, document.body.scrollHeight);')

sleep(5)

sites = chrome.page_source
bs = BeautifulSoup(sites, 'html.parser')
model = bs.find_all('a', class_='ellipsis', href=True)

titlese = open('pickres', 'w+', encoding="utf-8")
linkese = open('linkpick', 'w+', encoding="utf-8")

for mo in model:
    meow = f'{mo}'
    ebac = BeautifulSoup(meow, "lxml").text
    print(ebac)
    titlese.write(ebac + '\n')
    por = mo.get('href')
    popa = "https://www.kleinanzeigen.de"
    dopa = popa + por
    print(dopa)
    linkese.write(dopa + '\n')
titlese.close()
linkese.close()
