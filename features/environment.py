from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

def before_all(context):
    # Instalar automáticamente la última versión de ChromeDriver
    chromedriver_autoinstaller.install()

    # Configuración de opciones para Chrome
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Configuración del servicio de ChromeDriver
    service = Service()  # No es necesario pasar el path aquí ya que `chromedriver_autoinstaller` lo maneja
    
    # Crear una instancia del navegador Chrome
    context.browser = webdriver.Chrome(service=service, options=chrome_options)

def after_all(context):
    if context.browser:
        context.browser.quit()

def before_scenario(context, scenario):
    pass

def after_scenario(context, scenario):
    pass
