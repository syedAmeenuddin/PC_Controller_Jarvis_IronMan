import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os
from jarvis import *


driver = ''
def naukri_python_bot():
    firstname=name                       #Add your LastName
    lastname=lastname                         #Add your FirstName
    joblink=[]                          #Initialized list to store links
    maxcount=25                         #Max daily apply quota for Naukri
    keywords=['python','django','developer']                    #Add you list of role you want to apply
    location = 'Bangalore'                       #Add your location/city name for within India or remote
    applied =0                          #Count of jobs applied sucessfully
    failed = 0                          #Count of Jobs failed
    applied_list={
        'passed':[],
        'failed':[]
    }                                   #Saved list of applied and failed job links for manual review

    try:
        options = webdriver.ChromeOptions() 
        options.add_argument("user-data-dir=C:\\Path") #Path to your chrome profile
        driver = webdriver.Chrome(executable_path="D:\Chrome\applications\chromedriver_win32\\chromedriver.exe", chrome_options=options)
    
    except Exception as e:
        print('Webdriver exception')
    # webbrowser.open('https://www.naukri.com/python-developer-django-jobs-in-bangalore?k=python%20developer%2C%20Django&l=Bangalore')
    time.sleep(10)
    for k in keywords:
        for i in range(5):
            if location=='':
                url = "https://www.naukri.com/"+k.lower().replace(' ','-')+"-"+str(i+1)
            else: 
                
                url = 'https://www.naukri.com/python-developer-python-django-fresher-jobs-in-bangalore-bengaluru-'+str(i+1)+'?experience=0'
                # url1 = 'https://www.naukri.com/software-developer-fresher-html-css-jobs-in-bangalore-bengaluru-'+str(i+1)+'?experience=0'
                # url = 'https://www.naukri.com/python-developer-django-python-jobs-in-bangalore?k=Python%20Developer%2C%20Django%2C%20Python&l=Bangalore&experience=0&ugTypeGid=4&ugTypeGid=9502&jobAge=3'
                # url = "https://www.naukri.com/"+k.lower().replace(' ','-')+"-jobs-in-"+location.lower().replace(' ','-')+"-"+str(i+1)
            driver.get(url)
            print(url)
            time.sleep(3)
            soup = BeautifulSoup(driver.page_source,'html.parser')
            results = soup.find(class_='list')
            job_elems = results.find_all('article',class_='jobTuple')
            for job_elem in job_elems:
                joblink.append(job_elem.find('a',class_='title ellipsis').get('href'))
            print(f'--------------joblink count  = {joblink.count}------------------------------------------');        
            print(f'joblink = {joblink}')
            print(f'joblink = {joblink}')


    for i in joblink:
        time.sleep(3)
        driver.get(i)   
        if applied <=maxcount:
            try:
                time.sleep(3)
                driver.find_element(By.XPATH,"//*[text()='Apply']").click()
                time.sleep(5)
                applied +=1
                applied_list['passed'].append(i)
                print('Applied for ',i, " Count", applied)

            except Exception as e: 
                failed+=1
                applied_list['failed'].append(i)
                # print(applied_list['failed']);
                print(e, "Failed " ,failed)
            try:    
                if driver.find_element("//*[text()='Your daily quota has been expired.']"):
                    print('MAX Limit reached closing browser')
                    driver.close()
                    return 'passed'
                if driver.find_element("//*[text()=' 1. First Name']"):
                    driver.find_element("//input[@id='CUSTOM-FIRSTNAME']").send_keys(firstname)
                if driver.find_element("//*[text()=' 2. Last Name']"):
                    driver.find_element("//input[@id='CUSTOM-LASTNAME']").send_keys(lastname);
                if driver.find_element("//*[text()='Submit and Apply']"):
                    driver.find_element("//*[text()='Submit and Apply']").click()
            except:
                pass
                
        else:
            driver.close()
            return 'passed'
    print('Completed applying closing browser saving in applied jobs csv')
    try:
        driver.close()
        return 'passed'
    except:pass
    csv_file = "naukriapplied.csv"
    final_dict= dict ([(k, pd.Series(v)) for k,v in applied_list.items()])
    df = pd.DataFrame.from_dict(final_dict)
    df.to_csv(csv_file, index = False) 
    
    
def naukri_flutter_bot():
    firstname='Syed'                        #Add your LastName
    lastname='Ameenuddin'                         #Add your FirstName
    joblink=[]                          #Initialized list to store links
    maxcount=25                         #Max daily apply quota for Naukri
    keywords=['flutter','dart','developer']                    #Add you list of role you want to apply
    location = 'Bangalore'                       #Add your location/city name for within India or remote
    applied =0                          #Count of jobs applied sucessfully
    failed = 0                          #Count of Jobs failed
    applied_list={
        'passed':[],
        'failed':[]
    }                                   #Saved list of applied and failed job links for manual review

    try:
        options = webdriver.ChromeOptions() 
        options.add_argument("user-data-dir=C:\\Path") #Path to your chrome profile
        driver = webdriver.Chrome(executable_path="D:\Chrome\applications\chromedriver_win32\\chromedriver.exe", chrome_options=options)
    
    except Exception as e:
        print('Webdriver exception')
    # webbrowser.open('https://www.naukri.com/python-developer-django-jobs-in-bangalore?k=python%20developer%2C%20Django&l=Bangalore')
    time.sleep(10)
    for k in keywords:
        for i in range(3):
            if location=='':
                url = "https://www.naukri.com/"+k.lower().replace(' ','-')+"-"+str(i+1)
            else: 
                url = 'https://www.naukri.com/flutter-dart-jobs-'+str(i+1)+'?experience=0'
                # url = 'https://www.naukri.com/python-developer-python-django-fresher-jobs-in-bangalore-bengaluru-'+str(i+1)+'?experience=0'
                # url1 = 'https://www.naukri.com/software-developer-fresher-html-css-jobs-in-bangalore-bengaluru-'+str(i+1)+'?experience=0'
                # url = 'https://www.naukri.com/python-developer-django-python-jobs-in-bangalore?k=Python%20Developer%2C%20Django%2C%20Python&l=Bangalore&experience=0&ugTypeGid=4&ugTypeGid=9502&jobAge=3'
                # url = "https://www.naukri.com/"+k.lower().replace(' ','-')+"-jobs-in-"+location.lower().replace(' ','-')+"-"+str(i+1)
            driver.get(url)
            print(url)
            time.sleep(3)
            soup = BeautifulSoup(driver.page_source,'html.parser')
            results = soup.find(class_='list')
            job_elems = results.find_all('article',class_='jobTuple')
            for job_elem in job_elems:
                joblink.append(job_elem.find('a',class_='title ellipsis').get('href'))
    print(f'--------------joblink count  = {joblink.count}------------------------------------------');        
    print(f'joblink = {joblink}')


    for i in joblink:
        time.sleep(3)
        driver.get(i)   
        if applied <=maxcount:
            try:
                time.sleep(3)
                driver.find_element(By.XPATH,"//*[text()='Apply']").click()
                time.sleep(2)
                applied +=1
                applied_list['passed'].append(i)
                print('------------------------------------------------applied------------------------------')
                print('Applied for ',i, " Count", applied)
                print('-------------applied end----------------------------')

            except Exception as e: 
                failed+=1
                applied_list['failed'].append(i)
                # print(applied_list['failed']);
                print(e, "Failed " ,failed)
            try:    
                if driver.find_element("//*[text()='Your daily quota has been expired.']"):
                    print('MAX Limit reached closing browser')
                    driver.close()
                    return 'passed'
                if driver.find_element("//*[text()=' 1. First Name']"):
                    driver.find_element("//input[@id='CUSTOM-FIRSTNAME']").send_keys(firstname)
                if driver.find_element("//*[text()=' 2. Last Name']"):
                    driver.find_element("//input[@id='CUSTOM-LASTNAME']").send_keys(lastname);
                if driver.find_element("//*[text()='Submit and Apply']"):
                    driver.find_element("//*[text()='Submit and Apply']").click()
            except:
                pass
                
        else:
            driver.close()
            return 'passed'
    print('Completed applying closing browser saving in applied jobs csv')
    try:
        driver.close()
        return 'passed'
    except:pass
    csv_file = "naukriapplied.csv"
    final_dict= dict ([(k, pd.Series(v)) for k,v in applied_list.items()])
    df = pd.DataFrame.from_dict(final_dict)
    df.to_csv(csv_file, index = False)  
    
def naukriorder():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('started.. you can speak now..')
        rec_order = r.listen(source,timeout=5, phrase_time_limit=5)
        try:
            print('recognizing ur order')
            order = r.recognize_google(rec_order)
            order = order.lower()
            print(order)
            return order
        except Exception as e:
            print(e)
            print('something went wrong! say it again')
            return 'None'
        
if __name__=="__main__" :
    jarvis('Starting applying Naukri jobs')
    naukri_flutter_bot()
    jarvis('flutter task is finished')
    naukri_python_bot()
    jarvis('python task is finished')
    time.sleep(2)
    jarvis('applying task is finished')
    time.sleep(1)
    jarvis('your system will shutdown within 5 Seconds. say STOP to stop the process')
    order = naukriorder()
    if 'stop' in order or 'top' in order:
        jarvis('shutdown is canceled')
    else:
        jarvis('You have 10 second to cancel shutdown manually')
        time.sleep(10)
        jarvis('Time up. shutdowning the system') 
        os.system("taskkill /im chrome.exe /f")
        time.sleep(1)
        os.system("taskkill /im Code.exe /f")
        time.sleep(1)
        os.system('taskkill /im chrome.exe')
        time.sleep(1)
        os.system("shutdown /s /t 1")

        
    