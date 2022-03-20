import undetected_chromedriver as uc
import csv, time, datetime
from random import randint
import getpass, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



username = getpass.getuser()


body = (f'file:///home/{username}/Desktop/sendapp/impfiles/mailb.html')

#password ='arzbgzik'

#username = 'vivianrivera569@gmail.com'
boite = {
  "email": "vivianrivera569@gmail.com",
  "password": "arzbgzik",
  "recoveryemail": "channel.haida01@yahoo.com",
  "sanswer": "glxovmqw"
}

datas=['cunningham68@optimum.net','yooanf@comcast.net']
subject='Re:test'






driver = uc.Chrome()
driver.delete_all_cookies()

driver.get(str(body))
driver.maximize_window()
# copy the body
driver.implicitly_wait(randint(2, 4))
Window_List = driver.window_handles
driver.switch_to.window(Window_List[(-1)])
Window_List = driver.window_handles
driver.implicitly_wait(randint(2, 4))
time.sleep(randint(2, 4))
driver.find_element(by=By.XPATH,value='/html/body').send_keys((Keys.CONTROL + 'q'))
driver.implicitly_wait(randint(2, 4))
driver.find_element(by=By.XPATH,value='/html/body').send_keys(Keys.CONTROL + 'c')
driver.implicitly_wait(4)
time.sleep(randint(2, 4))

control_string = "window.open('{0}')".format('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&hl=en&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
driver.execute_script(control_string)


#driver.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&hl=en&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

Window_List = driver.window_handles
driver.switch_to.window(Window_List[(-1)])
time.sleep(randint(2, 5))


time.sleep(randint(2, 4))
driver.find_element(By.ID,'identifierId').send_keys(boite['email'])
driver.find_element(By.ID,'identifierNext').click()

time.sleep(randint(2, 6))
driver.find_element(By.XPATH,value='//input[@type="password"]').send_keys(boite['password'])

#driver.find_element_by_xpath('//input[@type="password"]').send_keys(boite['password'])

driver.find_element(By.ID,'passwordNext').click()

time.sleep(2)
driver.get('https://mail.google.com/mail/?ui=html&zy=h')


time.sleep(2)
driver.get('https://mail.google.com/mail/u/0/h/1es4g7ty3qm0t/?v=pra')


time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="cfn"]').clear()
driver.find_element(By.XPATH,'//*[@id="cfn"]').send_keys('fdfsd')
time.sleep(2)
driver.find_element(By.XPATH,value='//input[@value="Save"]').click()
time.sleep(2)
for data in datas:
    driver.get('https://mail.google.com/mail/u/0/#inbox?compose=new')
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@name="to"]').send_keys(data)
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@name="subjectbox"]').send_keys(subject)
    time.sleep(2)
    driver.find_element(By.XPATH,'//div[@aria-label="Message Body"]').clear()
    time.sleep(2)
    
    driver.find_element(By.XPATH,'//div[@aria-label="Message Body"]').send_keys(Keys.CONTROL + 'v')
    
    time.sleep(2)
    driver.find_element(By.XPATH,'//div[@aria-label="Message Body"]').send_keys(Keys.CONTROL + Keys.ENTER)
    time.sleep(2)
