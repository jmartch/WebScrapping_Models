from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import time
import pandas as pd

#Opciones de navegacion
options = webdriver.EdgeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service, options=options)

#Inicializar el navegagor
driver.get('https://www.eltiempo.es/')

WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a._3kalix4"))
).click()

WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input#term"))
).send_keys('Barranquilla')

WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, " input#term"))
).click()

WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "i.icon icon-sm icon-city".replace(' ' , '.')))
).click()

WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/div[8]/div[1]/div[4]/div/section[3]/section/section/ul/li[2]/h2/a'))).click()

WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/div[8]/div[1]/div[4]/div/section[3]/article/ul/li[1]')))

txt_columnas = driver.find_element(By.XPATH,'/html/body/div[8]/div[1]/div[4]/div/section[3]/article/ul/li[1]')
txt_columnas = txt_columnas.text

tiempo_hoy = txt_columnas.split('Hoy')[1].splitlines()[1:]

horas = list()
temperaturas = list()
publiometros= list()
humedad = list()
velocidad_v = list()

for i in range(0 , len(tiempo_hoy) , 5):
    horas.append(tiempo_hoy[i])
    temperaturas.append(tiempo_hoy[i+1])
    publiometros.append(tiempo_hoy[i+2])
    humedad.append(tiempo_hoy[i+3])
    velocidad_v.append(tiempo_hoy[i+4])

df = pd.DataFrame({'Horas': horas , 'Temperatura': temperaturas , 'Publiometro': publiometros , 'Humedad': humedad , 'Velocidad_v': velocidad_v})
print(df)
df.to_csv('Tiempodehoy.csv',index=False)

driver.quit()
