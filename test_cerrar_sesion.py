import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



service = Service(r"C:\DriverAutomatizacion\chromedriver.exe")
driver = webdriver.Chrome(service=service)  
driver.get("https://test-qa.inlaze.com/auth/sign-in")
driver.maximize_window()
time.sleep(3)

nombre = driver.find_element(By.XPATH,"//INPUT[@id='email']")
nombre.send_keys("tawunneunuzu-7919@yopmail.com")
time.sleep(2)
contras = driver.find_element(By.XPATH,"//INPUT[@id='password']")
contras.send_keys("Miguel@1")
time.sleep(2)
botón =driver.find_element(By.XPATH,"//BUTTON[@_ngcontent-ng-c1760168622=''][text()=' Sign in ']")
botón.click()

time.sleep(5)


imagen = driver.find_element(By.XPATH, "//img[@src='/assets/rengoku.webp']")
imagen.click()
time.sleep(1)
login =driver.find_element(By.XPATH, "//a[contains(.,'Logout')]")
login.click()


driver.close()
