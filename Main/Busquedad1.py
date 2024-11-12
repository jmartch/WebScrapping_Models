import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

URL = "https://listado.mercadolibre.com.co/_Container_full-week-aon-tecnologia#DEAL_ID=MCO13077&S=landingHubfull-envios&V=5&T=Special-withoutLabel&L=EP4TECNOLOGIA&deal_print_id=98ec9040-9fd7-11ef-bd66-6bcb9b30aa39&c_id=special-withoutlabel&c_element_order=4&c_campaign=EP4TECNOLOGIA&c_uid=98ec9040-9fd7-11ef-bd66-6bcb9b30aa39"
response = requests.get(URL)

options = webdriver.EdgeOptions()
service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service, options=options)
driver.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

nombres = soup.find_all(class_="poly-box poly-component__title")
precios = soup.find_all(class_="andes-money-amount andes-money-amount--cents-superscript")
descuentos = soup.find_all(class_="andes-money-amount__discount")

for x,y,z in zip(nombres,precios,descuentos):
    print(f'{x.text} // {y.text} //{z.text}')

