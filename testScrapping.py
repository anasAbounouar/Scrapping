from PIL import Image
import os
import json
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
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument(
    "user-data-dir=C:/Users/DELL/AppData/Local/Google/Chrome/User Data"
)
driver = webdriver.Edge(r"msedgedriver.exe")
chrome_options.add_argument("--headless")
# Disable GPU acceleration (optional)
chrome_options.add_argument("--disable-gpu")
url = "https://comparatif-tarifs-bancaires.ma/fr/page/comparatif_bancaire?popup=true"
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

# list of banks buttons
btns = [
    btn_Cih,
    btn_ArabBank,
    btn_Attijari,
    btn_CreditDuMaroc,
    btn_CreditAgricoleDuMaroc,
    btn_Bmci,
    btn_BaridBank,
    btn_Bmce,
    btn_Cfg,
    btn_SocieteGenerale,
    btn_CDG,
    btn_Chaabi,
]
driver.get(url)
time.sleep(1)
body = driver.find_element(By.TAG_NAME, "body")
# scroll down
body.send_keys(Keys.ARROW_DOWN)
body.send_keys(Keys.ARROW_DOWN)
time.sleep(2)
element_id = "comparatifBlock"
# btn= driver.find_element(By.ID, element_id).click() #Choix comparatif bancaire
from selenium.common.exceptions import NoSuchElementException

# ...

element_id = "comparatifBlock"
timeout = 10  # Maximum time to wait in seconds
try:
    element = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.ID, element_id))
    )
except Exception as e:
    print(f"Error occurred while waiting for element: {e}")
    driver.quit()  # Quit the driver if the element is not found
else:
    # Click the element once it becomes clickable
    element.click()
# Additional actions to perform after clicking the element, if needed

time.sleep(2)
body.send_keys(Keys.ARROW_DOWN)
body.send_keys(Keys.ARROW_DOWN)
for btn in btns:
    driver.find_element(By.CSS_SELECTOR, btn).click()
time.sleep(2)
body.send_keys(Keys.ARROW_UP)
body.send_keys(Keys.ARROW_UP)
body.send_keys(Keys.ARROW_UP)
body.send_keys(Keys.ARROW_UP)
body.send_keys(Keys.ARROW_UP)
body.send_keys(Keys.ARROW_UP)
# form of 'Selectionner Categorie'
time.sleep(2)
# first option
form0 = "#form-comparatif > div.js-form-item.form-item.js-form-type-select.form-type-select.js-form-item-categorie.form-item-categorie > div > button"
form0options = driver.find_elements(
    By.CSS_SELECTOR,
    "#form-comparatif > div.js-form-item.form-item.js-form-type-select.form-type-select.js-form-item-categorie.form-item-categorie > div > ul > li",
)
S = 0
# we click on all banks
def new_func(form1options, j):
    form1options[j].click()

while S < len(form0options):
    form0options = driver.find_elements(
        By.CSS_SELECTOR,
        "#form-comparatif > div.js-form-item.form-item.js-form-type-select.form-type-select.js-form-item-categorie.form-item-categorie > div > ul > li",
    )
    form0 = "#form-comparatif > div.js-form-item.form-item.js-form-type-select.form-type-select.js-form-item-categorie.form-item-categorie > div > button"
    driver.find_element(By.CSS_SELECTOR, form0).click()
    time.sleep(2)
    for i in range(max(S - 1, 0), S + 1):
        form0options[i].click()
    time.sleep(2)
    print("form0 options is clicked")

    form1options = driver.find_elements(
        By.CSS_SELECTOR,
        "#state-categorie-operation > div > div.btn-group > ul > li",
    )
    S1 = 1
    while S1 < len(form1options):
        form1options = driver.find_elements(
            By.CSS_SELECTOR,
            "#state-categorie-operation > div > div.btn-group > ul > li",
        )
        time.sleep(2)
        form1="#state-categorie-operation > div > div.btn-group > button"
        time.sleep(2)
        driver.find_element(
            By.CSS_SELECTOR, form1
        ).click()
        time.sleep(5)
        # form1options[S1].click()
        for j in range (max(S1-1,1),S1+1):
            form1options[j].click()
        time.sleep(2)
        print ("form1 options clicked")
        time.sleep(2)
        form2 = "#state-type-produit > div > div.btn-group > button"
        driver.find_element(By.CSS_SELECTOR, form2).click()
        time.sleep(4)
        S2=2
        form2options = driver.find_elements(
        By.CSS_SELECTOR,
        "#state-type-produit > div > div.btn-group.show > ul > li",
        )
        form2 = "#state-type-produit > div > div.btn-group > button"
        while S2 < len(form2options):
            print("S2:", S2)
            print("i entrred the while")
            form2options = driver.find_elements(
        By.CSS_SELECTOR,
        "#state-type-produit > div > div.btn-group.show > ul > li",
        )
            time.sleep(2)
            
            form2 = "#state-type-produit > div > div.btn-group > button"
            driver.find_element(By.CSS_SELECTOR, form2).click()
            print("i lcicked the form2")
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, form2).click()
            time.sleep(2)
            if (S2==2):
                form2options[S2].click()
            else:
                form2options[S2-1].click()
                time.sleep(2)
                form2options[S2].click()
            # for j in range (max(S2-1,2),S2+1):
            #     form2options[j].click()
            print ("form2 options clicked")
            print(form2options)
            time.sleep(4)
            form3options = driver.find_elements(
        By.CSS_SELECTOR,
                "#form-comparatif > div.js-form-item.form-item.js-form-type-select.form-type-select.js-form-item-canal.form-item-canal > div.btn-group > ul > li",
            )
            S3 = 0
            while S3< len(form3options):
                form3 = "#form-comparatif > div.js-form-item.form-item.js-form-type-select.form-type-select.js-form-item-canal.form-item-canal > div.btn-group"
                driver.find_element(By.CSS_SELECTOR, form3).click()
                time.sleep(2)
                form3options = driver.find_elements(
        By.CSS_SELECTOR,
                "#form-comparatif > div.js-form-item.form-item.js-form-type-select.form-type-select.js-form-item-canal.form-item-canal > div.btn-group > ul > li",
            )
                # Choix du canal
                #radio 
                form3options[S3].click()
                
                time.sleep(4)
                # Choix du banque
                # on click pour  generer les tarifs

                driver.find_element(By.ID, "edit-submit").click()
                # wait for elements to load
                time.sleep(10)
                # identify the panel-body
                table = driver.find_element(By.ID, "tableau_source44")
                rows = table.find_elements(By.CSS_SELECTOR, 'tr[bgcolor="#FFFFFF"]')
                data_dict = {}
                S3+=1
                driver.back()
                time.sleep(8)
            S2+=1
            driver.back()
            time.sleep(8)
        S1 += 1

        driver.back()
        time.sleep(8)
    S+=1
    driver.back()
    time.sleep(8)
