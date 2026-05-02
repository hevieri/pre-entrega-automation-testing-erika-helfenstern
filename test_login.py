from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
try:
    #Ingreso pagina
    driver.get("https://www.saucedemo.com/")

    #Ingresar usuario
    usuario = driver.find_element(By.ID, "user-name")

finally:
    driver.quit()