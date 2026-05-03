from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
try:
    #Ingreso pagina
    driver.get("https://www.saucedemo.com/")

    #Ingresar usuario
    usuario = driver.find_element(By.ID, "user-name")
    usuario.send_keys("standard_user")

    #Ingresar contraseña
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    #Hacer click en el botón de login
    password.send_keys(keys.RETURN)

    #Verificar url
    if "/inventory.html" in driver.current_url:
        print("Pagina correcta")
    else:
        print("No es la página de inventario")

finally:
    driver.quit()