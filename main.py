import sqlite3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import time

url_login="https://www.instagram.com/"

chorme = webdriver.Chrome()

def login():
    f = open('credential.json',)
    credential = json.load(f)   
    chorme.get(url_login)
    time.sleep(4)
    usuario = chorme.find_element(By.NAME, 'username')
    usuario.send_keys(credential.get("usuario"))
    senha = chorme.find_element(By.NAME, 'password')
    senha.send_keys(credential.get("senha"))
    senha.send_keys(Keys.ENTER)
login()