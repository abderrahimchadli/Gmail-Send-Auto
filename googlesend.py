while True:
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
    userinputgroupe = input('if using FIRST group of emails print 1 if using SECOND group print 2 :')
    userinputprofilee = input('Print "start" if you want to start from the begin , or profile number if you want to start form specific profile')
    if userinputgroupe == '1':
        if userinputprofilee == 'start':
            if userinputgroupe == '1':
                p = 1
            else:
                if userinputgroupe == '2':
                    p = 15
                else:
                    print('bad choice type again ')
                    exit()
        else:
            if userinputprofilee.isdigit() and int(userinputprofilee) < 15 and int(userinputprofilee) > 0:
                p = str(userinputprofilee)
            else:
                print('bad choice')
                exit()
    if userinputgroupe == '2':
        if userinputprofilee == 'start':
            if userinputgroupe == '1':
                p = 1
            else:
                if userinputgroupe == '2':
                    p = 15
                else:
                    print('bad choice type again ')
                    exit()
        else:
            if userinputprofilee.isdigit() and int(userinputprofilee) < 29 and int(userinputprofilee) > 14:
                p = userinputprofilee
            else:
                print('bad choice')
                exit()
    logpath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'relayautomatic', 'logfile.text')
    print(p)
    with open(logpath, 'a+', newline='') as the_file:
        printP1 = 'profile ' + p + ' at: ' + str(datetime.datetime.now())
        the_file.write(printP1 + os.linesep)
    options = Options()
    options = webdriver.ChromeOptions()
    username = getpass.getuser()
    options.add_argument(f"user-data-dir=C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data")
    options.add_argument(f"--profile-directory=Profile {p}")
    domainpath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'relayautomatic', 'domains.csv')
    file = open(domainpath, 'r', encoding='utf8')
    domains = [line.split(',') for line in file.readlines()]
    fillbody = 0
    fillfrom = 0
    userinput = input(' Print "all" if you want to do all jobs ,\r\n Print "from" if you want to edit only the from name ,\r\n Print "body" if you want to edit only the body \r\n ')
    driverpath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'relayautomatic', 'kookoo.exe')
    dakchi = webdriver.Chrome(driverpath, options=options)
    dakchi.maximize_window()
    i = 0
    btcount = 0
    time.sleep(randint(2, 4))
    domainpath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'relayautomatic', 'domains.csv')
    file = open(domainpath, 'r', encoding='utf8')
    domains = [line.split(',') for line in file.readlines()]
    with open(domainpath, encoding='utf8') as f:
        first_line = f.readline()
    if userinput == 'all':
        fillbody = 1
        fillfrom = 1
        userinputFROM = input('print The Offer FromName')
        body = input('give me the path of the body ')
        body2 = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'relayautomatic', 'body2.html')
    else:
        if userinput == 'from':
            fillfrom = 1
            userinputFROM = input('print The Offer FromName')
        else:
            if userinput == 'body':
                fillbody = 1
                body = input('give me the path of the body ')
                body2 = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'relayautomatic', 'body2.html')
            else:
                print('bad choice')
                exit()
    fromst = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'relayautomatic', 'frommaildata//')
    if not isdir(fromst):
        os.mkdir(fromst)
    boites = []
    mailpath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'relayautomatic', 'testsvc.csv')
    with open(mailpath) as csv_file:
        while True:
            mails = csv.DictReader(csv_file)
            for mail in mails:
                boites.append(mail)
    
    Window_List = dakchi.window_handles
    dakchi.switch_to.window(Window_List[(-1)])
    Window_List = dakchi.window_handles
    dakchi.implicitly_wait(randint(2, 4))
    time.sleep(randint(2, 4))
    dakchi.find_element_by_xpath('/html/body').send_keys(Keys.CONTROL + 'a')
    dakchi.implicitly_wait(randint(2, 4))
    dakchi.find_element_by_xpath('/html/body').send_keys(Keys.CONTROL + 'c')
    dakchi.implicitly_wait(4)
    time.sleep(randint(2, 4))
    for boite in boites:
        bigtime_rand = random
        lst = ['.']
        emlParts1 = boite['email'].split('@')
        emlParts1 = emlParts1[0]
        fromrand = ''.join(('%s%s' % (x, random.choice(lst) if random.random() > 0.5 else '') for x in emlParts1[1:-1]))
        fromend = emlParts1[0] + fromrand + emlParts1[-1:]
        pathin = fromst
        with open((pathin + f"{boite['email']}.csv"), 'a+', newline='') as the_file:
            while True:
                if fromend in the_file.read():
                    fromrand = ''.join(('%s%s' % (x, random.choice(lst) if random.random() > 0.5 else '') for x in emlParts1[1:-1]))
                    fromend = emlParts1[0] + fromrand + emlParts1[-1:]  
            with open((pathin + f"{boite['email']}.csv"), 'a+', newline='') as the_file:
                the_file.write(fromend + os.linesep)
        if i == 9:
            dakchi.quit()
            p = int(p) + 1
            with open(logpath, 'a+', newline='') as the_file:
                printP2 = 'profile ' + str(p) + ' at: ' + str(datetime.datetime.now())
                the_file.write(printP2 + os.linesep)
            options = Options()
            options = webdriver.ChromeOptions()
            options.add_argument(f"user-data-dir=C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data")
            options.add_argument(f"--profile-directory=Profile {str(p)}")
            dakchi = webdriver.Chrome(driverpath, options=options)
            time.sleep(randint(3, 4))
            time.sleep(randint(2, 4))
            dakchi.implicitly_wait(randint(2, 4))
            i = 0
            btcount = 0
        if i < 9:
            with open(logpath, 'a+', newline='') as the_file:
                print1 = str(i) + ' ' + boite['email'] + ' at: ' + str(datetime.datetime.now())
                the_file.write(print1 + os.linesep)
        if fillbody == 1:
            domainpath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'relayautomatic', 'domains.csv')
            file = open(domainpath, 'r', encoding='utf8')
            domains = [line.split(',') for line in file.readlines()]
            with open(domainpath, 'r', encoding='utf8') as fin:
                data = fin.read().splitlines(True)
            with open(domainpath, 'w', encoding='utf8') as fout:
                fout.writelines(data[1:])
            with open(domainpath, encoding='utf8') as f:
                first_line = f.readline()
            body2 = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'relayautomatic', 'body2.html')
            with open((body.strip()), encoding='ISO-8859-1') as f:
                with open((body2.strip()), 'w', encoding='ISO-8859-1') as f1:
                    while True:
                        for line in f:
                            f1.write(line)  
                fin = open((body2.strip()), 'rt', encoding='ISO-8859-1')
            data = fin.read()
            data = data.replace('[domain]', str(first_line.strip()))
            fin = open((str(body2.strip())), 'wt', encoding='ISO-8859-1')
            fin.write(data)
            fin.close()
            with open(logpath, 'a+', newline='', encoding='ISO-8859-1') as the_file:
                printP2 = 'profile ' + str(p) + ' domain :' + first_line + ' at: ' + str(datetime.datetime.now())
                the_file.write(printP2 + os.linesep)
        else:
            dakchi.execute_script("window.open('');")
            time.sleep(2)
            dakchi.switch_to.window(dakchi.window_handles[(-1)])
            a = dakchi.get(body2)
            time.sleep(2)
            Window_List = dakchi.window_handles
            dakchi.switch_to.window(Window_List[(-1)])
            Window_List = dakchi.window_handles
            dakchi.switch_to.window(Window_List[(-1)])
            Window_List = dakchi.window_handles
            dakchi.implicitly_wait(randint(2, 4))
            time.sleep(randint(2, 4))
            dakchi.find_element_by_xpath('/html/body').send_keys(Keys.CONTROL + 'a')
            dakchi.implicitly_wait(randint(2, 4))
            dakchi.find_element_by_xpath('/html/body').send_keys(Keys.CONTROL + 'c')
            time.sleep(randint(3, 4))
            dakchi.implicitly_wait(randint(2, 4))
            control_string = "window.open('{0}')".format('https://accounts.google.com/AddSession?hl=en&continue=https://mail.google.com/mail&service=mail')
            dakchi.execute_script(control_string)
            Window_List = dakchi.window_handles
            dakchi.switch_to.window(Window_List[(-1)])
            time.sleep(randint(2, 5))
            dakchi.find_element_by_id('identifierId').send_keys(boite['email'])
            dakchi.implicitly_wait(randint(2, 4))
            time.sleep(randint(2, 5))
            dakchi.find_element_by_xpath('//*[@id="identifierNext"]/span/span').click()
            dakchi.implicitly_wait(randint(2, 4))
            time.sleep(randint(2, 4))
            dakchi.find_element_by_name('password').send_keys(boite['password'])
            dakchi.implicitly_wait(2)
            time.sleep(randint(2, 5))
            a = dakchi.find_element_by_xpath('//*[@id="passwordNext"]/span/span')
            dakchi.execute_script('arguments[0].click();', a)
            dakchi.implicitly_wait(2)
            time.sleep(randint(3, 5))
            if 'deniedsigninrejected' in dakchi.current_url:
                with open(logpath, 'a+', newline='') as the_file:
                    print2 = f"try with this email later {boite['email']},{boite['password']},{boite['recoveryemail']} at :{str(datetime.datetime.now())}"
                    the_file.write(print2 + os.linesep)
                i = i + 1
    else:
        while True:
            time.sleep(randint(2, 4))
            if 'sl/pwd' in dakchi.current_url:
                input('enter captcha and type enter')
            else:
                time.sleep(randint(2, 4))
                try:
                    TXT = dakchi.find_element_by_class_name('vxx8jf').text
                    b = dakchi.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div/div/form/span/section/div/div/div/ul/li[1]/div/div[2]')
                    dakchi.execute_script('arguments[0].click();', b)
                    time.sleep(randint(2, 4))
                    dakchi.implicitly_wait(2)
                    dakchi.find_element_by_xpath('//*[@id="knowledge-preregistered-email-response"]').send_keys(boite['recoveryemail'])
                    dakchi.implicitly_wait(2)
                    time.sleep(randint(2, 4))
                    dakchi.implicitly_wait(2)
                    c = dakchi.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span')
                    dakchi.execute_script("arguments[0].click('');", c)
                    dakchi.implicitly_wait(2)
                except NoSuchElementException:
                    time.sleep(randint(2, 4))
                else:
                    time.sleep(randint(2, 4))
                    if 'disabled' in dakchi.current_url:
                        with open(logpath, 'a+', newline='') as the_file:
                            print3 = boite['email'] + ' is disabled ,' + ' at: ' + str(datetime.datetime.now())
                            the_file.write(print3 + os.linesep)
                        i = i + 1   
        dakchi.implicitly_wait(4)
        time.sleep(randint(3, 6))
        if 'challenge/sq' in dakchi.current_url:
            try:
                dakchi.find_element_by_xpath('//*[@id="secret-question-response"]').send_keys(boite['sanswer'])
                dakchi.implicitly_wait(3)
                ans = dakchi.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span')
                dakchi.implicitly_wait(3)
                time.sleep(randint(3, 6))
                dakchi.execute_script("arguments[0].click('');", ans)
            except NoSuchElementException:
                input('come to see where the problem is')   
        dakchi.implicitly_wait(3)
        time.sleep(randint(3, 6))   
    if 'challenge/iap' in dakchi.current_url:
        input('fill the phone number in the browser ')
    else:
        dakchi.implicitly_wait(3)
        time.sleep(randint(3, 6))
        if fillfrom == 1:
            with open(logpath, 'a+', newline='') as the_file:
                print2 = f"  working in from  at :{str(datetime.datetime.now())}"
                the_file.write(print2 + os.linesep)
            time.sleep(randint(4, 8))
            time.sleep(randint(3, 6))
            dakchi.implicitly_wait(5)
            time.sleep(randint(2, 4))
            dakchi.get(f"https://mail.google.com/mail/u/{btcount}/#settings/accounts")
            dakchi.get(f"https://mail.google.com/mail/u/{btcount}/#settings/accounts")
            time.sleep(randint(2, 4))
            time.sleep(randint(2, 4))
            time.sleep(randint(3, 6))
            dakchi.implicitly_wait(4)
            try:
                dakchi.implicitly_wait(randint(2, 5))
                Window_List = dakchi.window_handles
                while True:
                    if 'delete' == dakchi.find_element_by_xpath(".//span[@class = 'sA' and contains(text(), 'delete')]").text:
                        dakchi.implicitly_wait(3)
                        time.sleep(randint(3, 7))
                        btns = dakchi.find_element_by_xpath(".//span[@class = 'sA' and contains(text(), 'delete')]")
                        dakchi.implicitly_wait(6)
                        time.sleep(randint(4, 8))
                        dakchi.execute_script("arguments[0].click('');", btns)
                        dakchi.implicitly_wait(3)
                        time.sleep(randint(3, 7))
                        button = dakchi.find_element_by_name('ok')
                        dakchi.implicitly_wait(4)
                        time.sleep(randint(3, 7))
                        dakchi.execute_script("arguments[0].click('');", button)
                        dakchi.implicitly_wait(randint(1, 4))
                        time.sleep(randint(2, 4))   
            except NoSuchElementException:
                time.sleep(randint(2, 4))
            else:
                time.sleep(randint(2, 4))
                dakchi.implicitly_wait(randint(2, 4))
                dakchi.implicitly_wait(randint(1, 4))
                time.sleep(5)
                dakchi.implicitly_wait(randint(4, 6))
                dakchi.implicitly_wait(randint(4, 6))
                time.sleep(randint(4, 6))
                time.sleep(randint(4, 6))
                adfv = dakchi.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div/div/div/div/div[4]/div/table/tbody/tr[3]/td[2]/table[1]/tbody/tr/td[contains(@class, "rc")]/span[contains(@class, "sA")]')
                act = ActionChains(dakchi)
                act.click(adfv).perform()
                dakchi.implicitly_wait(randint(2, 4))
                dakchi.switch_to.window(dakchi.window_handles[(-1)])
                dakchi.implicitly_wait(2)
                time.sleep(randint(2, 4))
                emlParts = boite['email'].split('@')
                email = dakchi.find_element_by_xpath('//*[@id="focus"]')
                dakchi.execute_script("arguments[0].value = '" + fromend + "@googlemail.com'; ", email)
                usn = dakchi.find_element_by_xpath('//*[@id="cfn"]')
                dakchi.execute_script(f"arguments[0].value = '{userinputFROM}'; ", usn)
                dakchi.implicitly_wait(randint(2, 4))
                time.sleep(randint(3, 6))
                addd = dakchi.find_element_by_xpath('//*[@id="bttn_sub"]')
                dakchi.execute_script('arguments[0].click();', addd)
                dakchi.implicitly_wait(randint(2, 4))
                time.sleep(randint(3, 6))
                dakchi.switch_to.window(dakchi.window_handles[(-1)])
                time.sleep(randint(3, 6))
                m_default = dakchi.find_element_by_xpath(".//span[@class = 'sA' and contains(text(), 'make default')]")
                dakchi.execute_script("arguments[0].click('');", m_default)
            if fillbody == 1:
                with open(logpath, 'a+', newline='') as the_file:
                    print2 = f"  working in BODY  at :{str(datetime.datetime.now())}"
                    the_file.write(print2 + os.linesep)
                time.sleep(randint(2, 4))
                dakchi.get(f"https://mail.google.com/mail/u/{btcount}/#settings/general")
                dakchi.implicitly_wait(randint(3, 6))
                dakchi.implicitly_wait(4)
                dakchi.find_element_by_xpath("//div[@aria-label='Vacation responder']").clear()
                dakchi.implicitly_wait(4)
                time.sleep(randint(2, 4))
                dakchi.find_element_by_xpath("//div[@aria-label='Vacation responder']").send_keys(Keys.CONTROL, 'v')
                time.sleep(randint(2, 6))
                dakchi.implicitly_wait(4)
                save = dakchi.find_element_by_xpath('//button[text()="Save Changes"]')
                dakchi.execute_script("arguments[0].click('');", save)
                time.sleep(randint(2, 6))
                dakchi.implicitly_wait(4)
        i = i + 1
        btcount = btcount + 1