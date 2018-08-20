
# coding: utf-8

# In[ ]:


class Doctor():
    def __init__(self, name):
        self.name = name
        if name == "Papla":
            self.name = '//span[contains(text(), "Papl")]'
            self.spec = "ginekologia"
    

    
    def Check(self, user):
        global headless
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.support.ui import Select
        from selenium.webdriver.firefox.options import Options
        from selenium import webdriver
        from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
        binary = FirefoxBinary("C:\\Users\maciej-nowak\\AppData\\Local\\Mozilla Firefox\\firefox.exe")
        options = Options()
        if headless ==1:
            options.add_argument("-headless")
        import time
        from datetime import datetime
        try:
            driver = webdriver.Chrome()
        except:
            driver = webdriver.Firefox(firefox_options=options, firefox_binary=binary)
        time.sleep(3)
        driver.get("https://online.enel.pl/Visit/New")
        elem = driver.find_element_by_name("Login")
        elem.clear()
        elem.send_keys(credentials(user)[0])
        elem = driver.find_element_by_name("Password")
        elem.clear()
        elem.send_keys(credentials(user)[1])
        elem = driver.find_element_by_name("IsAcceptedRule").click()
        elem = driver.find_element_by_partial_link_text('Zalo').click()
        time.sleep(2)
        elem = driver.get("https://online.enel.pl/Visit/New")
        elem = driver.find_element_by_id("City")
        select = Select(driver.find_element_by_id("City"))
        select.select_by_visible_text("Warszawa")
        time.sleep(2)
        
        
        elem = driver.find_element_by_css_selector("#checkboxdropdown > button:nth-child(1)").click()
        elem = driver.find_element_by_css_selector(".validate > li:nth-child(1) > div:nth-child(1) > a:nth-child(1)").click()
        time.sleep(2)
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(1) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(2) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(3) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(4) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(5) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(7) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(9) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#confirmDepartment").click()
        time.sleep(2)
                
        select = Select(driver.find_element_by_id("ListOfSpecialities"))
        select.select_by_visible_text(self.spec)
        time.sleep(1)
        
        
        
        elem = driver.find_element_by_id("checkboxdropdownDoc").click()
        elem = driver.find_element_by_css_selector("#checkboxdropdownDoc > ul:nth-child(2) > li:nth-child(1) > div:nth-child(1) > a:nth-child(1)").click()
        #elem = driver.find_element_by_partial_link_text('Zazna').click()
        driver.find_element_by_xpath(self.name).click()

        elem = driver.find_element_by_css_selector("input.form-control")
        elem.clear()
        elem.send_keys("2018-08-08 - 2018-10-22")
        elem = driver.find_element_by_id("sbtn").click()
        time.sleep(8)
        driver.save_screenshot('C:\\_Research\\_Models\\'+filename+'.png')
        lol = driver.find_elements_by_xpath("//*[contains(text(), 'Nie znaleziono')]")   
        if headless ==1:
            driver.save_screenshot('C:\\_Research\\_Models\\'+filename+'.png')
            lol = driver.find_elements_by_xpath("//*[contains(text(), 'Nie znaleziono')]") 
            
            if len(lol)==0:
              MsgBox = tk.messagebox.askquestion('Question', 'Would you like to see the visits?')
              if MsgBox =='yes':
                  from PIL import Image
                  f = Image.open('C:\\_Research\\_Models\\'+filename+'.png').show()
                  MsgBox = tk.messagebox.askquestion('Question', 'Visit Found. Would you like to go to reservation?')
                  if MsgBox =='yes':
                      headless = 9
                  else:
                      driver.close()
              else:
                  driver.close()
            else:
                driver.quit()


# In[ ]:


class Generic():
    def __init__(self,spec):
        self.spec = spec
        
        

    def Check(self, user):
        global headless
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.support.ui import Select
        from selenium.webdriver.firefox.options import Options
        from selenium import webdriver
        from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
        binary = FirefoxBinary("C:\\Users\maciej-nowak\\AppData\\Local\\Mozilla Firefox\\firefox.exe")
        options = Options()
        if headless ==1:
            options.add_argument("-headless")
        import time
        from datetime import datetime
        try:
            driver = webdriver.Chrome()
        except:
            driver = webdriver.Firefox(firefox_options=options, firefox_binary=binary)
        time.sleep(3)
        driver.get("https://online.enel.pl/Visit/New")
        elem = driver.find_element_by_name("Login")
        elem.clear()
        elem.send_keys(credentials(user)[0])
        elem = driver.find_element_by_name("Password")
        elem.clear()
        elem.send_keys(credentials(user)[1])
        elem = driver.find_element_by_name("IsAcceptedRule").click()
        elem = driver.find_element_by_partial_link_text('Zalo').click()
        time.sleep(2)
        elem = driver.get("https://online.enel.pl/Visit/New")
        elem = driver.find_element_by_id("City")
        select = Select(driver.find_element_by_id("City"))
        select.select_by_visible_text("Warszawa")
        time.sleep(2)
        
        elem = driver.find_element_by_css_selector("#checkboxdropdown > button:nth-child(1)").click()
        elem = driver.find_element_by_css_selector(".validate > li:nth-child(1) > div:nth-child(1) > a:nth-child(1)").click()
        time.sleep(2)
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(1) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(2) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(3) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(4) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(5) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(7) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(9) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#confirmDepartment").click()
        time.sleep(2)
        
        select = Select(driver.find_element_by_id("ListOfSpecialities"))
        select.select_by_visible_text(self.spec)
        elem = driver.find_element_by_css_selector("input.form-control")
        elem.clear()
        elem.send_keys("2018-08-08 - 2018-10-22")
        try:
            elem = driver.find_element_by_css_selector("#AcptRul").click()
        except:
            pass
        time.sleep(1)

        elem = driver.find_element_by_id("sbtn").click()
        time.sleep(8)
        if headless ==1:
            driver.save_screenshot('C:\\_Research\\_Models\\'+filename+'.png')
            lol = driver.find_elements_by_xpath("//*[contains(text(), 'Nie znaleziono')]") 
            
            if len(lol)==0:
              MsgBox = tk.messagebox.askquestion('Question', 'Would you like to see the visits?')
              if MsgBox =='yes':
                  from PIL import Image
                  f = Image.open('C:\\_Research\\_Models\\'+filename+'.png').show()
                  MsgBox = tk.messagebox.askquestion('Question', 'Visit Found. Would you like to go to reservation?')
                  if MsgBox =='yes':
                      headless = 9
                  else:
                      driver.close()
              else:
                  driver.close()
            else:
                driver.quit()
        
        


# In[1]:


def credentials(user):
    f = open("C:\_Research\_Models\\"+user+".txt")
    lines = f.readlines()
    login = lines[0].split()[0]
    password = lines[1].split()[0]
    f.close()
    return login, password


def Reserve():
    pass

def Pap():
    papla = Doctor("Papla")
    papla.Check(user)
    
def higiena():
    higienistka = Generic("higiena jamy ustnej")
    higienistka.Check(user)
    
def derma():
    derma = Generic("dermatologia i wenerologia")
    derma.Check(user)
    
def endo():
    endo = Generic("endokrynologia")
    endo.Check(user)
def interna():
    interna = Generic("interna")
    interna.Check(user)
    if headless ==9:
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
filename = datetime.now().strftime("%Y%m%d-%H%M%S")

parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="filename",
                    help="write report to FILE", metavar="FILE")
parser.add_argument("-q", "--quiet",
                    action="store_true", dest="quiet", default=False,
                    help="don't print status messages to stdout")

args = parser.parse_args()

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
        ShowButtons()
    else:
        user = "Maciek"
        headless =1
        Pap()
    


root.mainloop()

