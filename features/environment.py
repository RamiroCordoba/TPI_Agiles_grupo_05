from selenium import webdriver

def before_all(context):
    context.browser = webdriver.Chrome()

def after_all(context):
    pass

def before_scenario(context, scenario):
    pass

def after_scenario(context, scenario):
    pass