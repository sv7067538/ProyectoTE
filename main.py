from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuración automática del WebDriver
driver = webdriver.Chrome()

# Maximizar la ventana del navegador
driver.maximize_window()

# Abrir URL en el navegador
driver.get('https://www.random-name-generator.com/es/generador-de-nombres-aleatorios')
driver.find_element(By.XPATH, "(//div[@role = 'combobox' and @aria-autocomplete = 'list'])[1]").click()
time.sleep(2)
argentina = driver.find_element(By.XPATH, "//div[contains(@class, 'choices__list--dropdown')]//div[@data-value = '/es/argentina']")
argentina.click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@value = '3']").clear()
driver.find_element(By.XPATH, "//input[@value = '3']").send_keys("1")
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class = 'choices__item choices__placeholder choices__item--selectable']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@data-value = 'male']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@class = 'btn btn-success btn-lg btn-generate']").click()
time.sleep(2)
nombre = driver.find_element(By.XPATH, "//dd[@class = 'h4 col-12']").text
driver.get('https://www.facebook.com/reg/')
driver.find_element(By.XPATH, "(//input[@dir = 'ltr'])[1]").send_keys(nombre)
time.sleep(2)
driver.find_element(By.XPATH, "(//input[@dir = 'ltr'])[2]").send_keys("Prueba")
time.sleep(2)
driver.find_element(By.XPATH, "(//div[@aria-haspopup = 'listbox'])[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[text() = '28']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@aria-controls = '_r_a_']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[text() = 'enero']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@aria-controls = '_r_g_']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[text() = '2002']").click()
time.sleep(2)
driver.quit()

print("Prueba visual completada")
