from selenium import webdriver
driver = webdriver.Chrome()
try:
    driver.get("https://www.saucedemo.com/")

#Ingresar usuario

finally:
    driver.quit()