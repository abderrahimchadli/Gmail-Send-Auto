import csv, time
from selenium import webdriver
import os
from os.path import isdir
import random
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from timeit import default_timer as timer
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


fillbody=0
fillfrom=0
userinput=input(' Print "all" if you want to do all jobs ,\r\n Print "from" if you want to edit only the from name ,\r\n Print "body" if you want to edit only the body \r\n')

if userinput=="all":
    fillbody=1
    fillfrom=1
    userinputFROM=input('print The Offer FromName')
    body=input("give me the path of the body ")
elif userinput=="from":
    fillfrom=1
    userinputFROM=input('print The Offer FromName')
elif userinput=="body":
    fillbody=1
    body=input("give me the path of the body ")
else:
    print('bad choice')
    exit()

# fromemail=input("give me a from email")
fromst = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop','relayautomatic','frommaildata//',)
if not isdir(fromst):
    os.mkdir(fromst)

boites = []
mailpath=os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop','relayautomatic','testsvc.csv')
with open(mailpath) as csv_file:
    mails = csv.DictReader(csv_file)
    for mail in mails:
        boites.append(mail)
driverpath=os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop','relayautomatic','chromedriver.exe')
driver = webdriver.Chrome(driverpath)
driver.maximize_window()
i = 0
btcount = 0

driver.get(str(body))
Window_List = driver.window_handles
driver.switch_to.window(Window_List[-1])
Window_List = driver.window_handles
driver.implicitly_wait(2)
time.sleep(2)
driver.find_element_by_xpath('/html/body').send_keys(Keys.CONTROL + 'a')
driver.implicitly_wait(2)
driver.find_element_by_xpath('/html/body').send_keys(Keys.CONTROL + 'c')

# from generator



driver.implicitly_wait(4)
time.sleep(2)
for boite in boites:
    lst = ['.']
    string = 'ijgigfds'
    emlParts1 = boite['email'].split('@')
    emlParts1=emlParts1[0]
    fromrand = ''.join('%s%s' % (x, random.choice(lst) if random.random() > 0.5 else '') for x in emlParts1[1:-1])
    fromend = (emlParts1[0] + fromrand + emlParts1[-1:])
    pathin = fromst

    with open(pathin + f'{boite["email"]}.csv', 'a+', newline='') as the_file:

        while fromend in the_file.read():
            fromrand = ''.join('%s%s' % (x, random.choice(lst) if random.random() > 0.5 else '') for x in emlParts1[1:-1])
            fromend = (emlParts1[0] + fromrand + emlParts1[-1:])

        else:
            with open(pathin + f'{boite["email"]}.csv', 'a+', newline='') as the_file:
                the_file.write(fromend + os.linesep)

    if i == 10:
        driver = webdriver.Chrome(driverpath)
        driver.get(body)
        driver.maximize_window()
        i = 0
        btcount = 0

    elif i < 10:
        # LOGING
        print(str(i) + ' ' + boite['email'])
        control_string = "window.open('{0}')".format(
            "https://accounts.google.com/AddSession?hl=en&continue=https://mail.google.com/mail&service=mail")
        driver.execute_script(control_string)
        # browser.execute_script("window.open('');")
        Window_List = driver.window_handles
        driver.switch_to.window(Window_List[-1])
        driver.find_element_by_id('identifierId').send_keys(boite['email'])
        driver.implicitly_wait(2)
        time.sleep(3)

        #driver.find_element_by_xpath('//button[text()="Next"]').click()
        driver.find_element(by=By.ID, value="identifierNext").click()
        time.sleep(3)
        driver.implicitly_wait(2)
        driver.find_element_by_name("password").send_keys(boite["password"])
        # browser.implicitly_wait(2)
        a = driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span')
        driver.execute_script("arguments[0].click();", a)
        driver.implicitly_wait(2)
        # control_string = "window.location.href='{0}';".format("")
        # driver.execute_script(control_string)
        # RECOVERY EMAIL
        time.sleep(3)
        if "deniedsigninrejected" in driver.current_url:

            print(f"try with this email later {boite['email']} ")
            i = i + 1
            continue
        time.sleep(3)
        if "sl/pwd" in driver.current_url:
            input("enter captcha and type enter")

        time.sleep(3)
        try:
            TXT = driver.find_element_by_class_name("vxx8jf").text

            b = driver.find_element_by_xpath(
                '//*[@id="view_container"]/div/div/div[2]/div/div/div/form/span/section/div/div/div/ul/li[1]/div/div[2]')
            driver.execute_script("arguments[0].click();", b)
            time.sleep(3)
            driver.implicitly_wait(2)
            driver.find_element_by_xpath('//*[@id="knowledge-preregistered-email-response"]').send_keys(
                boite['recoveryemail'])
            driver.implicitly_wait(2)
            time.sleep(3)
            driver.implicitly_wait(2)
            c = driver.find_element_by_xpath(
                '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span')
            driver.execute_script("arguments[0].click('');", c)
            driver.implicitly_wait(2)

        except NoSuchElementException:
            time.sleep(3)



        time.sleep(3)
        if "disabled" in driver.current_url:
            print(boite['email'] + ' is disabled')
            i = i + 1
            continue
        driver.implicitly_wait(4)
        time.sleep(4)
        if "challenge/sq" in  driver.current_url:

            try:
                driver.find_element_by_xpath('//*[@id="secret-question-response"]').send_keys(boite['sanswer'])
                driver.implicitly_wait(3)
                ans=driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span')
                driver.implicitly_wait(3)
                time.sleep(3)

                driver.execute_script("arguments[0].click('');", ans)

            except NoSuchElementException:
                input('come to see where the problem is')

        driver.implicitly_wait(3)
        time.sleep(3)
        if "challenge/iap" in driver.current_url:
            input("fill the phone number in the browser ")
        driver.implicitly_wait(3)
        time.sleep(3)
        driver.get(f'https://mail.google.com/mail/u/{btcount}/#settings/general')
        driver.implicitly_wait(5)
        time.sleep(5)
        Window_List = driver.window_handles
        lang1= Select(driver.find_element_by_class_name('a5p'))
        lang1.select_by_value("en")
        driver.implicitly_wait(5)
        time.sleep(2)
        save1 = driver.find_element_by_xpath('//button[@guidedhelpid="save_changes_button"]')
        driver.execute_script("arguments[0].click('');", save1)



        if fillfrom==1:
                time.sleep(2)
                driver.get(f'https://mail.google.com/mail/u/{btcount}/#settings/accounts')
                time.sleep(2)
                driver.implicitly_wait(4)
                try:
                    driver.implicitly_wait(3)
                    Window_List = driver.window_handles
                    while "delete" == driver.find_element_by_xpath(".//span[@class = 'sA' and contains(text(), 'delete')]").text:
                        driver.implicitly_wait(3)
                        time.sleep(5)
                        btns = driver.find_element_by_xpath(".//span[@class = 'sA' and contains(text(), 'delete')]")
                        driver.implicitly_wait(6)
                        time.sleep(6)
                        driver.execute_script("arguments[0].click('');", btns)
                        driver.implicitly_wait(3)
                        time.sleep(4)
                        button = driver.find_element_by_name('ok')
                        driver.implicitly_wait(4)
                        time.sleep(4)
                        driver.execute_script("arguments[0].click('');", button)
                        driver.implicitly_wait(2)
                        time.sleep(2)



                except NoSuchElementException:
                    time.sleep(3)

                # add from and fromemail 1
                driver.implicitly_wait(2)
                driver.implicitly_wait(2)
                # addadress = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div/div/div/div/div[4]/div/table/tbody/tr[3]/td[2]/table[1]/tbody/tr[3]/td/span')
                # driver.execute_script("arguments[0].click();", addadress)
                # driver.implicitly_wait(2)
                # time.sleep(5)
                adfv = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div/div/div/div/div[4]/div/table/tbody/tr[3]/td[2]/table[1]/tbody/tr/td[contains(@class, "rc")]/span[contains(@class, "sA")]')
                act = ActionChains(driver)
                # act.key_down(Keys.CONTROL)
                act.click(adfv).perform()
                # act.key_up(Keys.CONTROL)
                driver.implicitly_wait(2)
                # act.key_down(Keys.CONTROL)
                # act.send_keys(Keys.TAB)
                # act.key_up(Keys.CONTROL)
                driver.switch_to.window(driver.window_handles[-1])
                driver.implicitly_wait(2)
                # add from and fromemail 2
                time.sleep(2)
                emlParts = boite['email'].split('@')
                email = driver.find_element_by_xpath('//*[@id="focus"]')
                driver.execute_script("arguments[0].value = '" + fromend + "@googlemail.com'; ", email)
                usn = driver.find_element_by_xpath('//*[@id="cfn"]')
                driver.execute_script(f"arguments[0].value = '{userinputFROM}'; ", usn)
                driver.implicitly_wait(2)
                addd = driver.find_element_by_xpath('//*[@id="bttn_sub"]')
                driver.execute_script("arguments[0].click();", addd)
                driver.implicitly_wait(2)

                # driver.execute_script("arguments[0].click();", adfv)
                driver.switch_to.window(driver.window_handles[-1])
                # make default
                m_default = driver.find_element_by_xpath(".//span[@class = 'sA' and contains(text(), 'make default')]")
                driver.execute_script("arguments[0].click('');", m_default)

        # add body
        if fillbody==1:
            time.sleep(2)
            driver.get(f'https://mail.google.com/mail/u/{btcount}/#settings/general')
            driver.implicitly_wait(5)
            time.sleep(2)
            driver.find_element_by_xpath("//div[@aria-label='Vacation responder']").clear()
            driver.implicitly_wait(4)

            time.sleep(2)
            driver.implicitly_wait(4)
            driver.find_element_by_xpath("//div[@aria-label='Vacation responder']").send_keys(Keys.CONTROL, "v")
            time.sleep(4)
            driver.implicitly_wait(4)
            save = driver.find_element_by_xpath('//button[text()="Save Changes"]')
            driver.execute_script("arguments[0].click('');", save)

            time.sleep(2)
            driver.implicitly_wait(3)

        i = i + 1
        btcount = btcount + 1

