import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(r"C:\DriverAutomatizacion\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://test-qa.inlaze.com/auth/sign-in")
driver.maximize_window()
time.sleep(2)

baton = driver.find_element(By.XPATH,"//a[contains(text(),'Sign up')]")
baton.click()
time.sleep(1)

nombre = driver.find_element(By.XPATH,"//input[contains(@id,'full-name')]")
nombre.send_keys("miguel beltran ") # se enviara una sola palabra validando que no habilite el boton inscribirse 
time.sleep(1)

email = driver.find_element(By.XPATH,"//input[contains(@id,'email')]")
email.send_keys("tawunneunuzu-7919@yopmail.com")
time.sleep(1)

password = driver.find_element(By.XPATH,"//input[@id='password']")
password.send_keys("Miguel@1")
time.sleep(1)

confirmarPassword = driver.find_element(By.XPATH, "//input[@id='confirm-password']")
confirmarPassword.send_keys("Miguel@1")
time.sleep(1)

botonRegistrar = driver.find_element(By.XPATH, "//button[contains(text(),'Sign up')]")
botonRegistrar.click()


driver.close()