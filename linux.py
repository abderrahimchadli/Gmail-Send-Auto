import csv, time, datetime
from selenium import webdriver
import getpass, os
from os.path import isdir
import random
from random import randint
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from timeit import default_timer as timer
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options = webdriver.ChromeOptions()
username = getpass.getuser()
profilnumber = 1#input('give me the profile name : ')
options.add_argument(f"user-data-dir=\\home\\{username}\\.config\\chromium\\Google\\")
options.add_argument(f"--profile-directory=Profile {profilnumber}")
fillbody = 0
fillfrom = 0
userinput = "all"#input(' Print "all" if you want to do all jobs ,\r\n Print "from" if you want to edit only the from name ,\r\n Print "body" if you want to edit only the body \r\n ')

i = 0
btcount = 0
time.sleep(randint(2, 4))
if userinput == 'all':
    fillbody = 1
    fillfrom = 1
    userinputFROM = "squ"#input('print The Offer FromName')
    body = (f'file:///home/{username}/Desktop/sendapp/impfiles/mailb.html')
else:
    if userinput == 'from':
        fillfrom = 1
        userinputFROM = input('print The Offer FromName')
    else:
        if userinput == 'body':
            fillbody = 1
            body = (f'file:///home/{username}/Desktop/sendapp/impfiles/mailb.html')
        else:
            print('bad choice')
            exit()

fromst =  os.path.join('/home',os.path.join(f'{username}'), 'Desktop', 'sendapp', 'impfiles','mailfrom//')
if not isdir(fromst):
    os.mkdir(fromst)
boites = []
mailpath =  os.path.join('/home',os.path.join(f'{username}'), 'Desktop', 'sendapp', 'impfiles','seed.csv')
with open(mailpath) as csv_file:
    mails = csv.DictReader(csv_file)
    for mail in mails:
        boites.append(mail)
        print(mail)
driverpath = os.path.join('/home',os.path.join(f'{username}'), 'Desktop', 'sendapp', 'impfiles', 'chromedriver')
driver = webdriver.Chrome(driverpath, options=options)

driver.get(str(body))
driver.maximize_window()
driver.implicitly_wait(randint(2, 4))
Window_List = driver.window_handles
driver.switch_to.window(Window_List[(-1)])
Window_List = driver.window_handles
driver.implicitly_wait(randint(2, 4))
time.sleep(randint(2, 4))

driver.find_element(By.XPATH, '/html/body').send_keys((Keys.CONTROL + 'q'))
driver.implicitly_wait(randint(2, 4))
driver.find_element(By.XPATH, '/html/body').send_keys(Keys.CONTROL + 'c')

