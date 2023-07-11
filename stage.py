
from PIL import Image
import os
import time
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip
import pyautogui
from random import randint
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument(
    "user-data-dir=C:/Users/DELL/AppData/Local/Google/Chrome/User Data")
driver = webdriver.Chrome(
    executable_path=r'C:/Users/DELL/Desktop/chromedriver.exe', options=chrome_options)

chrome_options.add_argument("--headless")

# Disable GPU acceleration (optional)
chrome_options.add_argument("--disable-gpu")
url = "https://comparatif-tarifs-bancaires.ma/fr/page/comparatif_bancaire?popup=true"
driver.get(url)
time.sleep(1)
body = driver.find_element(By.TAG_NAME,"body")
# scroll down 
body.send_keys(Keys.ARROW_DOWN)
body.send_keys(Keys.ARROW_DOWN)
time.sleep(2)
element_id = "comparatifBlock"
btn= driver.find_element(By.ID, element_id).click() #Choix comparatif bancaire
time.sleep(2)
body.send_keys(Keys.ARROW_DOWN)
body.send_keys(Keys.ARROW_DOWN)
# form of 'Selectionner Categorie'
form0 = "#form-comparatif > div.js-form-item.form-item.js-form-type-select.form-type-select.js-form-item-categorie.form-item-categorie > div > button"
driver.find_element(By.CSS_SELECTOR,form0).click()
time.sleep(2)
# first option 
form0option0="#form-comparatif > div.js-form-item.form-item.js-form-type-select.form-type-select.js-form-item-categorie.form-item-categorie > div > ul > li:nth-child(1)"
driver.find_element(By.CSS_SELECTOR,form0option0).click()
body.send_keys(Keys.ARROW_DOWN)
body.send_keys(Keys.ARROW_DOWN)
time.sleep(2)
# form of 'Choisissez votre catégorie d'opérations et de produits'
form1="#state-categorie-operation > div > div.btn-group > button"
driver.find_element(By.CSS_SELECTOR,form1).click()
time.sleep(2)
# option 0 of  is ignored  for now 
form1option1 = "#state-categorie-operation > div > div.btn-group.show > ul > li:nth-child(2)"
driver.find_element(By.CSS_SELECTOR, form1option1).click()
body.send_keys(Keys.ARROW_DOWN)
body.send_keys(Keys.ARROW_DOWN)
# form of 'Choisissez vos critères de recherche'
form2 = "#state-type-produit > div > div.btn-group > button"
driver.find_element(By.CSS_SELECTOR, form2).click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, form2).click()
time.sleep(2)
time.sleep(10)
form2option1= "#state-type-produit > div > div.btn-group.show > ul > li:nth-child(3)"
driver.find_element(By.CSS_SELECTOR, form2option1).click()
time.sleep(4)
form3 = "#form-comparatif > div.js-form-item.form-item.js-form-type-select.form-type-select.js-form-item-canal.form-item-canal > div.btn-group"
driver.find_element(By.CSS_SELECTOR, form3).click()
time.sleep(2)
#Choix du canal
form3option0= "#form-comparatif > div.js-form-item.form-item.js-form-type-select.form-type-select.js-form-item-canal.form-item-canal > div.btn-group.show > ul > li:nth-child(1)"
driver.find_element(By.CSS_SELECTOR, form3option0).click()
time.sleep(4)
# Choix du banque 


btn_Cih = ".form-item-comparatif-bancaire-banques-list-{}"
btn_ArabBank = ".form-item-comparatif-bancaire-banques-list-{}"
btn_Attijari = ".form-item-comparatif-bancaire-banques-list-{}"
btn_CreditDuMaroc = ".form-item-comparatif-bancaire-banques-list-{}"
btn_CreditAgricoleDuMaroc = ".form-item-comparatif-bancaire-banques-list-{}"
btn_Bmci = ".form-item-comparatif-bancaire-banques-list-{}"
btn_BaridBank = ".form-item-comparatif-bancaire-banques-list-{}"
btn_Bmce = ".form-item-comparatif-bancaire-banques-list-{}"
btn_Cfg = ".form-item-comparatif-bancaire-banques-list-{}"
btn_SocieteGenerale = ".form-item-comparatif-bancaire-banques-list-{}"
btn_CDG = ".form-item-comparatif-bancaire-banques-list-{}"
btn_Chaabi = ".form-item-comparatif-bancaire-banques-list-{}"

Cih_id = 3157
ArabBank_id = 37659
Attijari_id = 3167
CreditDuMaroc_id = 3155
CreditAgricoleDuMaroc_id = 12316
Bmci_id = 3161
BaridBank_id = 3162
Bmce_id = 3164
Cfg_id = 3158
SocieteGenerale_id = 3127
CDG_id = 39327
Chaabi_id = 3159

# Construct the full identifier using string formatting
btn_Cih = btn_Cih.format(Cih_id)
btn_ArabBank = btn_ArabBank.format(ArabBank_id)
btn_Attijari = btn_Attijari.format(Attijari_id)
btn_CreditDuMaroc = btn_CreditDuMaroc.format(CreditDuMaroc_id)
btn_CreditAgricoleDuMaroc = btn_CreditAgricoleDuMaroc.format(CreditAgricoleDuMaroc_id)
btn_Bmci = btn_Bmci.format(Bmci_id)
btn_BaridBank = btn_BaridBank.format(BaridBank_id)
btn_Bmce = btn_Bmce.format(Bmce_id)
btn_Cfg = btn_Cfg.format(Cfg_id)
btn_SocieteGenerale = btn_SocieteGenerale.format(SocieteGenerale_id)
btn_CDG = btn_CDG.format(CDG_id)
btn_Chaabi = btn_Chaabi.format(Chaabi_id)

#list of banks buttons 
btns = [btn_Cih, btn_ArabBank, btn_Attijari, btn_CreditDuMaroc, btn_CreditAgricoleDuMaroc, btn_Bmci, btn_BaridBank,
        btn_Bmce, btn_Cfg, btn_SocieteGenerale, btn_CDG, btn_Chaabi]
# we click on all banks
for btn in btns:
    driver.find_element(By.CSS_SELECTOR, btn).click()
body.send_keys(Keys.ARROW_DOWN)
body.send_keys(Keys.ARROW_DOWN)

# on click pour  generer les tarifs 

driver.find_element(By.ID,"edit-submit").click()
#wait for elements to load
time.sleep(10)

#identify the panel-body
element = driver.find_element(By.CLASS_NAME, "panel-body")
table = element.find_element(By.ID, "tableau_source44")
rows = table.find_elements(By.CSS_SELECTOR, 'tr[bgcolor="#FFFFFF"]')
data_dict = {}

for row in rows:
    image_place = row.find_element(By.CSS_SELECTOR, 'img')
    image_path = image_place.get_attribute('src')
    service = row.find_element(By.CSS_SELECTOR, "span.text-black-softnew").text
    data_dict[image_path] = service
print(data_dict)


time.sleep(8)