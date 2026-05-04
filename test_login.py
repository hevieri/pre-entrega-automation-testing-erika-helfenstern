from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
try:
    #Ingreso pagina
    driver.get("https://www.saucedemo.com/")

    #Hacer click en el botón de login
    password.send_keys(Keys.RETURN)   #Keys mayuscula, sino no lo reconoce.

    # en caso de que fuera un boton: boton.driver.find_element(By.ID, "login-button").click()

    #Verificar url
    if "/inventory.html" in driver.current_url:
        print("Pagina correcta")
    else:
        print("No es la página de inventario")

finally:
    driver.quit()