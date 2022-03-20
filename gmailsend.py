while True:
    import csv, time, datetime
    from selenium import webdriver
    import pyperclip, getpass, os
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
    fillbody = 0
    fillfrom = 0
    userinput = input(' Print "all" if you want to do all jobs ,\r\n Print "from" if you want to edit only the from name ,\r\n Print "body" if you want to edit only the body \r\n ')
    driverpath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'relayautomatic', 'kookoo.exe')
    dakchi = webdriver.Chrome(driverpath, options=options)
    dakchi.maximize_window()
    i = 0
    btcount = 0
    time.sleep(randint(2, 4))
    if userinput == 'all':
        fillbody = 1
        fillfrom = 1
        userinputFROM = input('print The Offer FromName')
        body = input('give me the path of the body ')
        dakchi.get(str(body))
    else:
        if userinput == 'from':
            fillfrom = 1
            userinputFROM = input('print The Offer FromName')
        else:
            if userinput == 'body':
                fillbody = 1
                body = input('give me the path of the body ')
                dakchi.get(str(body))
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