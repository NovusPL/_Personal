
class Visit():
    
    def __init__(self,spec, name=None):
        self.spec = spec
        self.name = name
        
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
        import time
        from datetime import datetime
        try:
            driver = webdriver.Chrome(chrome_options=c_options)
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
        elem = driver.find_element_by_id("City")
        select = Select(driver.find_element_by_id("City"))
        select.select_by_visible_text("Warszawa")
        elem = wait.until(EC.visibility_of_element_located((By.XPATH,'//span[contains(text(), "Wszystkie")]')))

        
        elem = driver.find_element_by_css_selector("#checkboxdropdown > button:nth-child(1)").click()
        elem = driver.find_element_by_css_selector(".validate > li:nth-child(1) > div:nth-child(1) > a:nth-child(1)").click()
        time.sleep(1)
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(1) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(2) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(3) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(4) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(5) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(7) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(9) > input:nth-child(1)").click()
        elem = driver.find_element_by_xpath('//span[contains(text(), "Wilan")]').click()                                        
        elem = driver.find_element_by_css_selector("#confirmDepartment").click()
        time.sleep(1)
                
        select = Select(driver.find_element_by_id("ListOfSpecialities"))
        select.select_by_visible_text(self.spec)
        elem = wait.until(EC.visibility_of_element_located((By.XPATH,'//span[contains(text(), "Wszystkie")]')))
        print(self.name)
        if self.name !=None:
            elem = driver.find_element_by_id("checkboxdropdownDoc").click()
            elem = driver.find_element_by_css_selector("#checkboxdropdownDoc > ul:nth-child(2) > li:nth-child(1) > div:nth-child(1) > a:nth-child(1)").click()
            driver.find_element_by_xpath(self.Doctor_Name(self.name)).click()
#here we click next month 3 times and select 25th day)
        elem = driver.find_element_by_css_selector("input.form-control").click()
        elem = driver.find_element_by_css_selector(".dtp_input2 > div:nth-child(1) > div:nth-child(3) > table:nth-child(1) > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(3) > i:nth-child(1)").click()
        elem = driver.find_element_by_css_selector(".dtp_input2 > div:nth-child(1) > div:nth-child(3) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(5) > td:nth-child(2)").click()
        elem = driver.find_element_by_css_selector(".btn-success").click()
        
        try:
            elem = driver.find_element_by_css_selector("#AcptRul").click()
        except:
            pass
        elem = driver.find_element_by_id("sbtn").click()
        elem = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[contains(text(), "terminie możesz")]')))

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

def Pap():
    papla = Visit("ginekologia","Paplicki")
    papla.Check(user)
   
def higiena():
    higienistka = Visit("higiena jamy ustnej")
    higienistka.Check(user)

    
def derma():
    derma = Visit("dermatologia i wenerologia")
    derma.Check(user)

    
def endo():
    endo = Visit("endokrynologia", "Jańczyk")
    endo.Check(user)

def interna():
    interna = Visit("interna", args.name)
    interna.Check(user)

    
def close():
    root.destroy()
    
def ShowButtons():
    global headless
    headless =1
    
    root.deiconify()
    root.title('Doctor Selector')
    frame = tk.Frame(root)
    frame.pack()
    intern = tk.Button(frame,text = 'Interna', command=interna)
    intern.pack(side = tk.RIGHT)
    button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=close)
    button.pack(side=tk.LEFT)
    slogan = tk.Button(frame,
                   text="Papla",
                   command=Pap)
    slogan.pack(side=tk.LEFT)
    dental = tk.Button(frame,text = 'Higienistka', command=higiena)
    dental.pack(side = tk.BOTTOM)
    
    dermatolog = tk.Button(frame,text = 'Dermatolog', command=derma)
    dermatolog.pack(side = tk.BOTTOM)
    
    endok = tk.Button(frame,text = 'Endokrynolog', command=endo)
    endok.pack(side = tk.BOTTOM)
    
    
    
    def sel():
        global user
        user = str(var.get())
    def click():
        global headless
        headless = v.get()

    var = StringVar(value="1")
    R1 = Radiobutton(root, text="Maciuch", variable=var, value="Maciek",
                      command=sel)
    R1.pack( anchor = W )

    R2 = Radiobutton(root, text="Donat", variable=var, value="Kasia",
                      command=sel)
    R2.pack( anchor = W )
    
    v = IntVar(value = 1)

    c = Checkbutton(root, text="HEADLESS - FOR TESTING", variable=v, onvalue = 1, offvalue = 0, command = click)
    c.pack()
   

    label = Label(root)
    label.pack()


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



root = tk.Tk()
root.geometry("300x150")
#root.iconbitmap('favicon.ico')
root.withdraw()

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
    else:
        Pap()
            


root.mainloop()
