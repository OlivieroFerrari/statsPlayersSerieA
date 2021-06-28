# -*- coding: utf-8 -*-
"""
Created on Fri May  7 09:22:04 2021

@author: olife
"""

from selenium import webdriver
import json
import time 

def start_driverGenerico():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(r'--profile-directory=Default')
    driver = webdriver.Chrome(executable_path="C:\Program Files\driverWeb\chrome\chromedriver.exe", options=chrome_options)
    
    return driver

def start_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(r'--profile-directory=Default')
    driver = webdriver.Chrome(executable_path="C:\Program Files\driverWeb\chrome\chromedriver.exe", options=chrome_options)
    
    return driver


myPath=".."
driverGenerico = start_driverGenerico()
driverGenerico.get("https://www.kickest.it/it/serie-a/statistiche/giocatori/tabellone")
driver = start_driver()
time.sleep(2)
try:
    cookie = driverGenerico.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div[2]/button')
    cookie.click()
except:
    print("no cookie")
    
try:
    cookie = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div[2]/button')
    cookie.click()
except:
    print("no cookie")

try:
    close = driverGenerico.find_element_by_xpath('/html/body/div[5]/div[2]')
    close.click()
except:
    print("no ads")
numClick=0
json=""
while (numClick<37):
    for j in range (1,16,1):
        try:
            url = driverGenerico.find_element_by_xpath("/html/body/div[4]/div[5]/div/div[2]/table/tbody/tr["+str(j)+"]/td[2]")
            url = url.find_element_by_css_selector('a').get_attribute('href')
            driver.get(url)
        except:
            print("try")
        try:
            cookie = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div[2]/button')
            cookie.click()
        except:
            print("no cookie")

        try:
            stagione = driverGenerico.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/button/div/div/div').text
        except:
            print("try")
        
        squadra = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/div/div[1]/div/span[2]').text
        squadra = squadra.lower()
        nome = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/div/div[1]/div/span[1]').text
        posizione = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div/div[4]/div[2]').text
        stats = driver.find_element_by_xpath('/html/body/div[4]/div[3]/div[1]/div[2]').text
        stats = stats.replace("Generale\n", "") 
        stats = stats.replace("Goal & Tiri\n", "") 
        stats = stats.replace("Passaggi\n", "") 
        stats = stats.replace("Azioni difensive\n", "") 
        stats = stats.replace("Portiere\n", "") 
        
        
        i = 0
        json = json + "{"
        json = json + "\"Squadra\":\"" + squadra + "\","
        json = json + "\"Nome\":\"" + nome + "\","
        json = json + "\"Posizione\":\"" + posizione + "\","
        json = json + "\""
        chiave = True
        valore = False
        for lettera in stats:
            if(stats[i]=="\""):
                json = json
                i=i+1
            elif(i+1==len(stats)):
                json = json +"}"
                json = json+"\n"
                i=i+1
            elif (chiave == True and stats[i]=='\n'):
                json = json + "\""
                json = json+":"
                chiave = False
                valore = True
                i=i+1
            elif (valore == True and stats[i]=='\n'):
                json = json + ","
                json = json + "\""
                chiave = True
                valore = False
                i=i+1
            elif (chiave ==True and stats[i]!='\n'):
                json = json+stats[i]
                i=i+1
            elif (valore ==True and stats[i]!='\n'):
                json = json+stats[i]
                i=i+1        
    try:
        close = driverGenerico.find_element_by_xpath('/html/body/div[5]/div[2]')
        close.click()
    except:
        print("niente ads")
    tab = driverGenerico.find_element_by_xpath('/html/body/div[4]/div[5]/div/div[3]/div/div')
    child_elements = tab.find_elements_by_xpath('./ul/li//*')
    size = str(len(child_elements))
    avanti = driverGenerico.find_element_by_xpath('/html/body/div[4]/div[5]/div/div[3]/div/div/ul/li['+size+']')
    avanti.click()
    numClick = numClick + 1






     
text_file = open(myPath + "/calciatori.json", "w")
text_file.write(json)
text_file.close()




