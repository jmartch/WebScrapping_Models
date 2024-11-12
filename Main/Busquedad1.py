import requests  # Library to make HTTP requests
from bs4 import BeautifulSoup  # Library for parsing HTML and XML documents
from selenium import webdriver  # Browser automation tool
from selenium.webdriver.edge.service import Service as EdgeService  # Service class for Edge browser
from webdriver_manager.microsoft import EdgeChromiumDriverManager  # Manages WebDriver binaries for Edge Chromium

# URL of the webpage to scrape
URL = "https://listado.mercadolibre.com.co/_Container_full-week-aon-tecnologia#DEAL_ID=MCO13077&S=landingHubfull-envios&V=5&T=Special-withoutLabel&L=EP4TECNOLOGIA&deal_print_id=98ec9040-9fd7-11ef-bd66-6bcb9b30aa39&c_id=special-withoutlabel&c_element_order=4&c_campaign=EP4TECNOLOGIA&c_uid=98ec9040-9fd7-11ef-bd66-6bcb9b30aa39"

# Send an HTTP GET request to the URL
response = requests.get(URL)

# Configure Edge browser options
options = webdriver.EdgeOptions()

# Setting up Edge WebDriver service using the WebDriverManager
service = EdgeService(executable_path=EdgeChromiumDriverManager().install())

# Initialize WebDriver for the Edge browser with the configured options and service
driver = webdriver.Edge(service=service, options=options)

# Open the URL in the Edge browser controlled by Selenium
driver.get(URL)

# Create a BeautifulSoup object to parse the HTML content of the response
soup = BeautifulSoup(response.text, 'html.parser')

# Find all elements with the class "poly-box poly-component__title"
nombres = soup.find_all(class_="poly-box poly-component__title")

# Find all elements with the class "andes-money-amount andes-money-amount--cents-superscript"
precios = soup.find_all(class_="andes-money-amount andes-money-amount--cents-superscript")

# Find all elements with the class "andes-money-amount__discount"
descuentos = soup.find_all(class_="andes-money-amount__discount")

# Iterate over the extracted elements and print their text content
for x, y, z in zip(nombres, precios, descuentos):
    print(f'{x.text} // {y.text} // {z.text}')
