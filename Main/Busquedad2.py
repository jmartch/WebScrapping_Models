from selenium import webdriver  # Import Selenium WebDriver
from selenium.webdriver.support.ui import WebDriverWait  # Import WebDriverWait for explicit waits
from selenium.webdriver.support import \
    expected_conditions as EC  # Import expected_conditions for various wait conditions
from selenium.webdriver.common.by import By  # Import By for locating elements
from selenium.webdriver.edge.service import Service as EdgeService  # Import Service for Edge browser
from webdriver_manager.microsoft import EdgeChromiumDriverManager  # Manages WebDriver binaries for Edge Chromium

import time  # Import time module for sleep (if needed)
import pandas as pd  # Import pandas for data manipulation and CSV export

# Opciones de navegacion (Browser options)
options = webdriver.EdgeOptions()
options.add_argument('--start-maximized')  # Start browser maximized
options.add_argument('--disable-extensions')  # Disable browser extensions

# Setting up Edge WebDriver service using the WebDriverManager
service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service, options=options)

# Inicializar el navegagor (Initialize the browser)
driver.get('https://www.eltiempo.es/')

# Wait for the specified element to be clickable and then click it
WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a._3kalix4"))
).click()

# Wait for the search input to be clickable, then input text
WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input#term"))
).send_keys('Barranquilla')

# Wait for the search input to be clickable, then click it
WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, " input#term"))
).click()

# Wait for the city icon to be clickable, then click it
WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "i.icon.icon-sm.icon-city".replace(' ', '.')))
).click()

# Wait for the desired link to be clickable, then click it
WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[8]/div[1]/div[4]/div/section[3]/section/section/ul/li[2]/h2/a'))
).click()

# Wait for the weather element to be visible
WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div[1]/div[4]/div/section[3]/article/ul/li[1]'))
)

# Extract the text content of the weather element
txt_columnas = driver.find_element(By.XPATH, '/html/body/div[8]/div[1]/div[4]/div/section[3]/article/ul/li[1]')
txt_columnas = txt_columnas.text

# Split the text content to get today's weather details
tiempo_hoy = txt_columnas.split('Hoy')[1].splitlines()[1:]

# Initialize lists to store weather data
horas = list()
temperaturas = list()
publiometros = list()
humedad = list()
velocidad_v = list()

# Loop through the weather details and append the data to respective lists
for i in range(0, len(tiempo_hoy), 5):
    horas.append(tiempo_hoy[i])
    temperaturas.append(tiempo_hoy[i + 1])
    publiometros.append(tiempo_hoy[i + 2])
    humedad.append(tiempo_hoy[i + 3])
    velocidad_v.append(tiempo_hoy[i + 4])

# Create a pandas DataFrame from the lists
df = pd.DataFrame({
    'Horas': horas,
    'Temperatura': temperaturas,
    'Publiometro': publiometros,
    'Humedad': humedad,
    'Velocidad_v': velocidad_v
})

# Print the DataFrame
print(df)

# Export the DataFrame to a CSV file
df.to_csv('Tiempodehoy.csv', index=False)

# Close the browser
driver.quit()
