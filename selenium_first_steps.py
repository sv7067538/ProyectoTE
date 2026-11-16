"""
Antes de ejecutar el test, ejecutar el siguiente comando para instalar la libreria necesaria

pip install selenium webdriver-manager
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# Configuración automática del WebDriver
driver = webdriver.Chrome()

# Maximizar la ventana del navegador
driver.maximize_window()

# Abrir url en el navegador
driver.get('URL PAGINA AQUI')

# Acciones para interactuar con el navegador
driver.find_element(By.XPATH, "LOCATOR").send_keys("texto")  #send_keys() nos permite enviar texto a inputs

driver.find_element(By.XPATH, "LOCATOR").click()  #click() envía un click a un elemento

variable = driver.find_element(By.XPATH, "LOCATOR").text  # .text se debe almacenar en una variable ya que captura el texto de un elemento
print(variable)  # El texto capturado del elemento se puede imprimir


driver.quit()

print("Prueba visual completada")
