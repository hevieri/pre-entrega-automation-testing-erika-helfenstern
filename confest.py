import pytest
from selenium import webdriver
from utils.loginpage import login

# Fixture de pytest para crear y cerrar el navegador
@pytest.fixture
def driver():
    # Configuración de opciones de Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")  # abre el navegador en modo incógnito

    # Inicializa el navegador con esas opciones
    driver = webdriver.Chrome(options=options)

    # Entrega el navegador al test que lo necesite
    yield driver

    # Cuando el test termina, se cierra el navegador
    driver.quit()


@pytest.fixture
def login_in_driver():
    login(driver)
    return driver