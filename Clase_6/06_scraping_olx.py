from bs4 import BeautifulSoup as BS
from selenium import webdriver
from time import sleep

# driver = webdriver.chrome ('C:/Users\groces\OneDrive - Galicia Seguros S.A\Desktop\Curso Data developer\clase 6\chromedriver.exe')
driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://www.olx.com.ar/items/q-aspiradoras-auto')

sleep(3)

script_js = """