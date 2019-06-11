class Visit():
    
    
    def __init__(self,spec, name=None, kat="KONSULTACJE"):
        self.spec = spec
        self.name = name
        self.kat = kat
        
        
    def Doctor_Name(self,name=None):
        switcher = self.name
        switcher = '//span[contains(text(), "'+self.name+'")]'       
        return switcher



    
    def Check(self, user):
        global headless
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.support.ui import Select
        from selenium.webdriver.firefox.options import Options
        from selenium.webdriver.chrome.options import Options as c_Options
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium import webdriver
        from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
        login = os.path.expanduser('~')
        binary = FirefoxBinary(login+"\\AppData\\Local\\Mozilla Firefox\\firefox.exe")
        options = Options()
        c_options = c_Options()
        if headless ==1:
            options.add_argument("-headless")
            c_options.add_argument("--headless")
            c_options.add_argument("window-size=1400,600")



        import time
        from datetime import datetime
        
        def Special_Click(self, elem):
            elem = driver.execute_script("arguments[0].click();", elem)
        
        try:
            driver = webdriver.Chrome(options=c_options)
        except:
            driver = webdriver.Firefox(firefox_options=options, firefox_binary=binary)    
            
        driver.get("https://online.enel.pl/Visit/New")
        elem = driver.find_element_by_name("Login")
        elem.clear()
        elem.send_keys(credentials(user)[0])
        elem = driver.find_element_by_name("Password")
        elem.clear()
        elem.send_keys(credentials(user)[1])
        elem = driver.find_element_by_name("IsAcceptedRule").click() 
        elem = driver.find_element_by_partial_link_text('Zalo').click()
       
        wait = WebDriverWait(driver, 10)
        elem = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="visits-slot"]/div/div/div[1]/a/img')))

        elem = driver.get("https://online.enel.pl/Visit/New")
        try:
            elem = driver.find_element_by_xpath('//*[@id="NotificationPopup"]/div/div[2]/a[1]/i').click()
            time.sleep(1)

        except:
            pass
        
        #select city
        wait = WebDriverWait(driver, 100)

        elem = driver.find_element_by_xpath('//*[@id="City"]').click()
        time.sleep(1)
        elem = driver.find_element_by_xpath('//*[@id="City"]').click()

        select = Select(driver.find_element_by_xpath('//*[@id="City"]'))
        select.select_by_visible_text("Warszawa")
        
        
        
        #select locations
        elem = wait.until(EC.visibility_of_element_located((By.XPATH,'//span[contains(text(), "Wszystkie")]')))
        elem = driver.find_element_by_css_selector("#checkboxdropdown > button:nth-child(1)").click()
        elem = driver.find_element_by_css_selector(".validate > li:nth-child(1) > div:nth-child(1) > a:nth-child(1)").click()
        
        time.sleep(1)
        
        
        
        
        
        #Edit here to select which enel med locations you want to search though.
        elem = driver.find_element_by_xpath('//span[contains(text(), "Arkadia")]').click()                                        
        elem = driver.find_element_by_xpath('//span[contains(text(), "Atrium")]').click()                                        
        elem = driver.find_element_by_xpath('//span[contains(text(), "Blue")]').click()                                        
        elem = driver.find_element_by_xpath('//span[contains(text(), "Oddział Centrum")]').click() 
        elem = driver.find_element_by_xpath('//span[contains(text(), "Oddział Galeria Młociny")]').click()                                       
        elem = driver.find_element_by_xpath('//span[contains(text(), "Domaniew")]').click()                                        
        elem = driver.find_element_by_xpath('//span[contains(text(), "Post")]').click()                                        
        elem = driver.find_element_by_xpath('//span[contains(text(), "Przyoko")]').click()                                        
        elem = driver.find_element_by_xpath('//span[contains(text(), "Wilan")]').click()
        elem = driver.find_element_by_xpath('//*[@id="confirmDepartment"]')
        Special_Click(self,elem)

        time.sleep(1)
             
        
        #select type of service
        time.sleep(2)
        elem = driver.find_element_by_id("ListOfTypes").click()
        select = Select(driver.find_element_by_id("ListOfTypes"))
        select.select_by_visible_text(self.kat)
    
   
        #select specialty
        time.sleep(1)
        elem = driver.find_element_by_css_selector("#ListOfServices").click()
        select = Select(driver.find_element_by_css_selector("#ListOfServices"))
        select.select_by_visible_text(self.spec)

        elem = wait.until(EC.visibility_of_element_located((By.XPATH,'//span[contains(text(), "Wszystkie")]')))


        #select doctor 
        time.sleep(3)
        if self.name !=None:
            elem = driver.find_element_by_id("checkboxdropdownDoc").click()
            elem = driver.find_element_by_css_selector("#checkboxdropdownDoc > ul:nth-child(2) > li:nth-child(1) > div:nth-child(1) > a:nth-child(1)").click()
            driver.find_element_by_xpath(self.Doctor_Name(self.name)).click()
            driver.find_element_by_css_selector("#confirmDoctor").click()            

        #select dates
        #here we click next month 1 time and select 15th day)
        elem = driver.find_element_by_css_selector("input.form-control").click()
        time.sleep(2)
        elem = driver.find_element_by_css_selector(".dtp_input2 > div:nth-child(1) > div:nth-child(3) > table:nth-child(1) > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(3) > i:nth-child(1)")
        Special_Click(self,elem)
        elem = driver.find_element_by_css_selector(".dtp_input2 > div:nth-child(1) > div:nth-child(3) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(4) > td:nth-child(1)")
        Special_Click(self,elem)
        elem = driver.find_element_by_css_selector(".btn-success")
        Special_Click(self,elem)
        
        try:
            elem = driver.find_element_by_css_selector("#AcptRul").click()
        except:
            pass

        elem = driver.find_element_by_id("sbtn")
        Special_Click(self,elem)
        #time.sleep(5)
        elem = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="Results"]/div[1]/div[1]/div[2]/div/div')))
        

        time.sleep(1)
        if headless ==1:
            driver.save_screenshot(dir_path+filename+'.png')
            lol = driver.find_elements_by_xpath("//*[contains(text(), 'Nie znaleziono')]") 
            
            if len(lol)==0:
                Beep()           
                MsgBox = tk.messagebox.askquestion('Question', 'Would you like to see the visits?')
                if MsgBox =='yes':
                  from PIL import Image
                  f = Image.open(dir_path+filename+'.png').show()
                  MsgBox = tk.messagebox.askquestion('Question', 'Visit Found. Would you like to go to reservation?')
                  if MsgBox =='yes':
                      headless = 0
                      self.Check(user)
                  else:
                      driver.close()
                else:
                  driver.close()
            else:
                driver.quit()
                      

def credentials(user):
    f = open(dir_path+user+".txt")
    lines = f.readlines()
    login = lines[0].split()[0]
    password = lines[1].split()[0]
    f.close()
    return login, password

def Beep():
    import winsound
    duration = 700  # millisecond
    freq = 300  # Hz
    winsound.Beep(freq, duration)
    winsound.Beep(freq, duration)
    
def Reserve():
    pass

def gin():
    gin = Visit("Konsultacja ginekologiczna", name="Paplicki")
    gin.Check(user)
    
def higiena():
    higienistka = Visit("Higiena jamy ustnej", kat="STOMATOLOGIA")

    higienistka.Check(user)
    
def przeglad():
    przeglad = Visit("Przegląd stomatologiczny", kat="STOMATOLOGIA")
    przeglad.Check(user)

def derma():
    derma = Visit("Konsultacja dermatologiczna")
    derma.Check(user)
    
def endo():
    endo = Visit("Konsultacja endokrynologiczna", name="Jańczyk")
    endo.Check(user)

def interna():
    interna = Visit("Konsultacja internistyczna", args.name)
    interna.Check(user)
    
def diet():
    diet = Visit("Konsultacja dietetyka")
    diet.Check(user)
    
def orto():
    orto = Visit("Konsultacja ortopedyczna", name="Wyka")
    orto.Check(user)
    
def pulmo():
    pulmo = Visit("Konsultacja pulmonologiczna", name="Paprota")
    pulmo.Check(user)
    
def neuro():
    neuro = Visit("Konsultacja neurologiczna")
    neuro.Check(user)

def okul():
    okul = Visit("Konsultacja okulistyczna")
    okul.Check(user)
    
def USGgin():
    USGgin = Visit("USG narządu rodnego transwaginalne (TV)",kat="USG")
    USGgin.Check(user)
    
def USGpier():
    USGpier = Visit("USG piersi",kat="USG")
    USGpier.Check(user)
    
def USGtar():
    USGtar = Visit("USG tarczycy",kat="USG")
    USGtar.Check(user)
    
def close():
    root.destroy()
    



# In[3]:
    
import tkinter as tk
import sys
from tkinter import messagebox
from tkinter import *
from argparse import ArgumentParser
from datetime import datetime
global filename
import os 
global dir_path
dir_path = os.path.dirname(os.path.realpath(__file__))+"\\"
print(dir_path)
filename = datetime.now().strftime("%Y%m%d-%H%M%S")

parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="filename",
                    help="write report to FILE", metavar="FILE")
parser.add_argument("-q", "--quiet",
                    action="store_true", dest="quiet", default=False,
                    help="don't print status messages to stdout")
parser.add_argument('-s', '--spec', nargs ='?')
parser.add_argument('-n', '--name', nargs ='?')
args = parser.parse_args()
print(args.spec)
print(args.name)

if args.quiet:
    silencio = 1
else:
    silencio = 0



if __name__ == "__main__":
    print(silencio)
  
    if silencio ==0:
        headless =0
    else:
        headless =1
        
    user = "Maciek"
    if args.spec =="endo":
        endo()
    elif args.spec =="interna":
        interna()
    elif args.spec =="gin":
        gin()
    elif args.spec =="derma":
        derma()
    elif args.spec =="diet":
        diet()
    elif args.spec =="orto":
        orto()
    elif args.spec =="pulmo":
        pulmo()
    elif args.spec =="higiena":
        higiena()
    elif args.spec =="neuro":
        neuro()        
    elif args.spec =="okul":
        okul()     
    elif args.spec =="przeglad":
        przeglad()       
    elif args.spec =="USGgin":
        USGgin() 
    elif args.spec =="USGpier":
        USGpier() 
    elif args.spec =="USGtar":
        USGtar() 
    else:
        gin()
            
    


root.mainloop()