from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller


def before_all(context):
    chromedriver_autoinstaller.install()
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    service = Service()
    context.browser = webdriver.Chrome(service=service, options=chrome_options)


def after_all(context):
    if context.browser:
        context.browser.quit()


def before_scenario(context, scenario):
    pass


def after_scenario(context, scenario):
    pass
