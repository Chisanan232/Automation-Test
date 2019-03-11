'''
The program why exists because when I studied in iii, my team's project have some data, one of data is address, but we
need pattern like address consist of longitude and latitude, and then, the trouble is the number of address at least
million, so if we want to translate address to the pattern we want efficiently, we have to use selenium with multithreding.
'''



from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as Except
from selenium.webdriver.common.by import By
from email.mime.text import MIMEText
from tomorrow import threads
import pandas as pd
import threading
import sqlite3
import smtplib
import random
import time
import csv
import os



class Parameter:
    def __init__(self, finish_path, gmail_user, gmail_password, recipient):
        self.finish_path = finish_path
        self.gmail_user = gmail_user
        self.gmail_password = gmail_password
        self.recipient = recipient


class DivideData:
    def divide_data(self, target_file, thread_num, wait_deal_file_dir):
        target_pd = pd.DataFrame(pd.read_csv(target_file))

        data_num = int(target_pd.count(axis=0))
        divide_data_num = int(data_num / thread_num)
        for num in range(thread_num):
            wait_deal_file_path_file = wait_deal_file_dir + 'thread-work-' + str('%003d' % num) + '.csv'
            target_pd['location_name'].iloc[divide_data_num * num: divide_data_num * (num + 1)].to_csv(wait_deal_file_path_file, index=False)
            print(str(divide_data_num * num) + ' ~ ' + str(divide_data_num * (num + 1)) + ' data has been divided success !!!')
        print('----------Data has been divided success.----------')


class ProtectMeasure:
    def get_header(self):
        user_agent = [
            # Samsung Galaxy S8
            'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36',
            # Samsung Galaxy S7
            'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
            # Samsung Galaxy S7 Edge
            'Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36',
            # Samsung Galaxy S6
            'Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36',
            # Samsung Galaxy S6 Edge Plus
            'Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36',
            # Sony Xperia XZ
            'Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36',
            # Sony Xperia Z5
            'Mozilla/5.0 (Linux; Android 6.0.1; E6653 Build/32.2.A.0.253) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36',
            # Apple iPhone X
            'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
            # Apple iPhone 8
            'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
            # Apple iPhone 8 Plus
            'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A5370a Safari/604.1',
            # Apple iPhone 7
            'Mozilla/5.0 (iPhone9,3; U; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1',
            # Apple iPhone 7 Plus
            'Mozilla/5.0 (iPhone9,4; U; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1',
            # Windows 10-based PC using Edge browser
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
            # Mac OS X-based computer using a Safari browser
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
            # Linux-based PC using a Firefox browser
            'Linux-based PC using a Firefox browser',
            # Windows User Agents
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
            'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 (KHTML, like Gecko) Mwendo/1.1.5 Safari/537.21'
                    ]
        header = {'User-Agent': random.choice(user_agent)}
        return header


    def get_proxy(self):
        # please CHECK your proxy can be used or not.
        proxies = [
            '5.133.27.55:3129'
                 ]
        proxy = {
            'http': 'http://' + random.choice(proxies)
            # 'https': 'https://' + random.choice(proxies)
        }
        return proxy


'''
Get some we need conditions like driver, user agent, proxy .etc to run program to get data.
'''


class WebDriver(ProtectMeasure):

    '''
    Depend on what the variable input to choose what the driver we should be to start.
    '''

    def get_driver(self, web):
    # def get_driver(self, web, options):
        try:
            '''A method to get driver'''
            # if web == 'chrome':
            #     driver = webdriver.Chrome()
            #     return driver
            # # elif web == 'firefox':
            # #     driver = webdriver.Firefox()
            # #     return driver
            # # elif web == 'phantomjs':
            # #     driver = webdriver.PhantomJS()
            # #     return driver
            # elif web == 'Chrome':
            #     driver = webdriver.Chrome()
            #     return driver
            # elif web == 'cHrome':
            #     driver = webdriver.Chrome()
            #     return driver
            # elif web == 'chRome':
            #     driver = webdriver.Chrome()
            #     return driver
            # elif web == 'chrOme':
            #     driver = webdriver.Chrome()
            #     return driver
            # else:
            #     print('Not found this driver.')
            '''Second method to get driver'''
            '''
            It's a better method with second method. Because it will not be limited by number of threads. If you start
            with first method, you have to add new elif to deal with increase number of threads every time.
            '''
            web_string = str(web)
            ans = web_string[-1].isdigit()
            if ans is True:
                '''No. 1 method : use chrome'''
                driver = webdriver.Chrome()
                # driver = webdriver.Chrome(chrome_options=options)
                '''No. 2 method : use PhantomJS'''
                # driver = webdriver.PhantomJS()
                # driver = webdriver.PhantomJS(service_args=self.get_header())
                return driver
        except Exception as e:
            print('Error : ', e)

    '''
    To set user agent and proxy with driver
    '''
    def option_argument(self):
        options = webdriver.ChromeOptions()
        # header = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
        # proxy='5.133.27.55:3129'
        # options.add_argument('--user-agent=' + header)
        options.add_argument('--user-agent=%s' % self.get_header())
        # options.add_argument('--proxy-server=' + proxy)
        options.add_argument('--proxy-server=%s' % self.get_proxy())
        return options

    '''
    If this is single process, we will use this function
    '''
    def get_web(self):
        '''set proxy in selenium'''
        # chrome_options = webdriver.ChromeOptions()
        '''no.1 method'''
        # PROXY = "81.16.9.138:54174"
        # chrome_options.add_argument('--proxy-server={0}'.format(PROXY))
        '''no.2 method'''
        # chrome_options.add_argument('--proxy-server=81.16.9.138:54174')
        # chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36')
        '''no.3 method'''
        # chrome_options.add_argument('--proxy-server=%s' % get_proxy())  # 認真考慮買個可以用的穩定超級代理
        # chrome_options.add_argument('--user-agent=%s', % get_header())
        # browser = webdriver.Chrome(chrome_options=chrome_options)

        browser = webdriver.Chrome()
        return browser


'''
Here are some determine conditions functions, determine the data we crawled are we need or not, and if it is we want, 
what we will do, or if not we want, what we will do.
'''


class PreventMachinary(Parameter):
    def __init__(self, finish_path, gmail_user, gmail_password, recipient):
        super(PreventMachinary, self).__init__(finish_path=finish_path, gmail_user=gmail_user, gmail_password=gmail_password, recipient=recipient)
    
    '''
    If address data we want is error or have some problem, execute this function to save data to retry or do something 
    next time.
    '''

    def no_address(self, un_count, driver_name, address, unaddr_file, browser):
        db_obj.build_table(no_addr_table_name, connect_db, command_db)
        print('No.' + str(un_count) + ' address with ' + str(driver_name))
        print('this address just in wormhole.')
        print('-----------------------------------')
        unaddress_list = [address]
        # unaddr_file.writerow(unaddress_list)
        db_obj.insert_data(no_addr_table_name, connect_db, unaddress_list)
        if un_count % 2 == 0:
            time.sleep(1)
            browser.refresh()
            pass
        if un_count % 40 == 0:
            print('-------------------------------')
            print('Oh, no, my VPN may be locked by google server, please change your ip or VPN ASAP.')
            locked_google = 'Your IP or VPN had been locked by google server'
            self.error_email(locked_google, un_count, driver_name)
            print(str(driver_name) + ' - Lock mail has been send.')
            print('-------------------------------')
        # un_count += 1
        # continue

    '''
    Sometimes, we may got strange results like (0, 0), if our data are from USA, it's impossible, so some data kind of 
    this we call it except address, should be to do something like unknowable address.
    '''
    def except_address(self, un_count, driver_name, address, data, unaddr_file, browser):
        print('No.' + str(un_count) + ' address with ' + str(driver_name))
        print(address)
        print(data)
        print('this address is abnormal.')
        print('-----------------------------------')
        unaddress_list = [address]
        unaddr_file.writerow(unaddress_list)
        db_obj.insert_data()
        if un_count % 2 == 0:
            time.sleep(1)
            browser.refresh()
            pass
        if un_count % 40 == 0:
            print('-------------------------------')
            print('Oh, no, my VPN may be locked by google server, please change your ip or VPN ASAP.')
            locked_google = 'Your IP or VPN had been locked by google server'
            self.error_email(locked_google, un_count, driver_name)
            print(str(driver_name) + ' - Lock mail has been send.')
            print('-------------------------------')
        # un_count += 1
        # continue

    '''
    If address data we want is correct, then save data.
    '''
    def address(self, count, driver_name, address, data, data_list, addr_file, browser):
        print('No.' + str(count) + ' address with ' + str(driver_name))
        print(address)
        print(data)
        print('-----------------------------------')
        address_list = [address, data]
        data_list.append(address_list)
        if count % 30 == 0:
            for index in range(len(data_list) - 30, len(data_list)):
                addr_file.writerow(data_list[index])
            print('get ' + str(count) + ' data with ' + str(driver_name))
            print('-----------------------------------')
        if count % 105 == 0:
            time.sleep(1)
            browser.refresh()
            pass
        if count % 230 == 0:
            browser.delete_all_cookies()
            browser.refresh()
            print('Cookie have been changed.')
            print('-----------------------------------')
        # count += 1

    '''
    If we get error when program is running, setting a measure to send error message email to me to tell me error happen.
    '''
    def error_email(self, error_content, count, driver_name):
        str_error = str(error_content)
        path = str(self.finish_path)

        '''1. method that if syntax'''
        # if path[-1] == '/':
        #     error_msg = str(self.finish_path) + 'class-24-web-automatic-address-error.txt'
        # else:
        #     error_msg = str(self.finish_path) + '/class-24-web-automatic-address-error.txt'
        '''2. method that if syntax'''
        error_msg = str(self.finish_path) + 'web-automatic-address-error.txt' if path[-1] == '/' else str(self.finish_path) + '/web-automatic-address-error.txt'

        ef = open(error_msg, 'w+')
        if 'except'in error_content or 'Except'in error_content or 'exception'in error_content or 'Exception'in error_content or 'error'in error_content or 'Error' in error_content:
            ef.write(str_error)
            ef.write('\n' + 'When we get ' + str(count + 1) + 'ed data, we got error.')
            ef.write('\nPlease handle with the error situation as soon as possible !')
            ef.write('\nSend from Python3.6. class24-web-automatic-address-ver.5-fin.py')
            ef.close()
        else:
            ef.write(str_error)
            ef.write('\nWe has getting 40 unknowable address data, it may mean our crawler had been locked,')
            ef.write('\nplease change your IP or VPN as soon as possible and keep continuing to crawl data')
            ef.write('\nSend from Python3.6. class24-web-automatic-address-ver.5-fin.py')
            ef.close()

        error = open(error_msg, 'r')
        msg = MIMEText(error.read())
        error.close()
        msg['Subject'] = 'Python -web-automatic-translate-address.py- Error with %s' % driver_name
        msg['From'] = self.gmail_user
        msg['To'] = self.recipient

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(self.gmail_user, self.gmail_password)
        server.send_message(msg)
        server.quit()

    '''
    Calculate time and translate it from seconds pattern to day-hour-minute-second pattern.
    '''
    def calculate_time(self, total_time):
        second = total_time % 60
        minute = int(total_time / 60)
        hour = int(minute / 60)
        day = int(hour / 24)
        if minute >= 60:
            minute = minute % 60
            if hour >= 24:
                hour = hour % 24
            else:
                hour = hour
        else:
            minute = minute
        return second, minute, hour, day


class CreateFile(Parameter):
    def __init__(self, finish_path, gmail_user, gmail_password, recipient, target_path_dir):
        super(CreateFile, self).__init__(finish_path=finish_path, gmail_user=gmail_user, gmail_password=gmail_password, recipient=recipient)
        self.target_path_dir = target_path_dir

    '''
    Build csv files that save data we get and depend on driver name to run program.
    '''
    def open_file(self, name):

        '''
        We want to super accelerated to get the data we want with selenium, so we divide data and use thread to reach
        multiprocess to accelerate.
        '''

        ## remember change your path
        # if name == 'chrome':
        #     original_address = self.target_path
        # # elif name == 'firefox':
        # #     original_address = self.target_path
        # # elif name == 'phantomjs':
        # #     original_address = self.target_path
        # elif name == 'Chrome':
        #     original_address = self.target_path
        # elif name == 'cHrome':
        #     original_address = self.target_path
        # elif name == 'chRome':
        #     original_address = self.target_path
        # elif name == 'chrOme':
        #     original_address = self.target_path
        name_string = str(name)
        num_file = int(name_string[-3:])
        path_string = str(os.listdir(self.target_path_dir)[num_file])
        if name_string[-3:] == path_string[-7:-4]:
            original_address = os.path.join(self.target_path_dir, path_string)

        # web_id = {'chrome': '1', 'Chrome': '2', 'cHrome': '3', 'chRome': '4', 'chrOme': '5'}
        web_id = {}
        web_id[name] = name_string[-3:]

        path = str(self.finish_path)
        if path[-1] == '/':
            address_file = path + 'address-2-divide-' + str(web_id[name]) + '.csv'
            unaddress_file = path + 'unknowable-address-2-divide-' + str(web_id[name]) + '.csv'
        else:
            address_file = path + '/address-2-divide-' + str(web_id[name]) + '.csv'
            unaddress_file = path + '/unknowable-address-2-divide-' + str(web_id[name]) + '.csv'

        with open(original_address, 'r') as f1:
            line = f1.readlines()
            print('test-read')

        address_f = open(address_file, 'a+', newline='', encoding='utf-8-sig')
        addr_file = csv.writer(address_f)
        addr_file.writerow(['Address', 'Latitude,Longitude'])

        unaddress_f = open(unaddress_file, 'a+', newline='', encoding='utf-8-sig')
        unaddr_file = csv.writer(unaddress_f)
        unaddr_file.writerow(['Address'])

        return line, address_f, unaddress_f, addr_file, unaddr_file


'''
Build a database and its type is sqlite currently.
This database will be used to save data in this, and than, because after data has been translated, it may be create two 
or more possible type data (for example, it is possible to translate data and be fail finally. Because it doesn't be control
and it's different if it is relative with internet. In internet, it may be happen anything. So you will get like one is 
translate successfully data, and one is fail to translate. We will get at least two type data in final result.), 
'''


class SQLDataBase:
    def connect_db(self):
        connect_sql = sqlite3.connect('lat_lon_address.sqlite')
        job_connect_sql = connect_sql.cursor()
        return connect_sql, job_connect_sql


    def build_table(self, table_name, connect_sql, job_connect_sql):
        sql_build_command = 'CREATE TABLE IF NOT EXISTS ' + table_name + ' ("address" TEXT NOT NULL, "lat_lot_address" TEXT NOT NULL)'
        job_connect_sql.execute(sql_build_command)
        connect_sql.commit()


    def insert_data(self, table_name, job_connect_sql, data_list):
        sql_insert_cmd = 'INSERT INTO ' + table_name + ' ("address", "lat_lot_address") VALUES (?, ?)'
        job_connect_sql.execute(sql_insert_cmd, data_list)


'''Main job in program'''
'''
The class AutomaticWebMainWork inherit class PreventMachinary, so the class can use the objects or functions in 
class PreventMachinary
'''
'''This is the originally program code'''


class AutomaticWebMainWork(CreateFile, WebDriver, PreventMachinary):
    # def automatic_control_web(self, browser, address, count):
    def automatic_control_web(self, browser, address):
        Wait(browser, 5).until(Except.presence_of_all_elements_located((By.ID, 'source')))
        browser.find_element_by_css_selector('textarea#source').clear()
        browser.find_element_by_css_selector('textarea#source').send_keys(address.strip())
        browser.find_element_by_xpath('/html/body/p[4]/input').click()
        # if address.strip() == 'location_name':
        '''
        Because we change the function in js in source code (below line *****, roughly 500) to accelerate crawler so we can reduce the time 
        of sleep.
        '''
        time.sleep(1.0)
        data = browser.find_element_by_css_selector('textarea#target').get_attribute('value')
        '''get the data no.2 method'''
        # data = bowser.find_element_by_id('target').get_attribute('value')
        '''clear the data we want no.2 method'''
        # new_data = data.split()[0]
        return data

    '''
    Determine the data we got and save date in their csv files
    '''
    def main_determine_job(self, browser, driver_name, line, addr_file, unaddr_file):
        count = 1
        un_count = 1
        fail = 1
        data_list = []

        for address in line:
            try:
                # data = self.automatic_control_web(browser, address, count)
                data = self.automatic_control_web(browser, address)
                if '查無經緯度' in data:
                    self.no_address(un_count, driver_name, address, unaddr_file, browser)
                    un_count += 1
                elif '0,0' in data:
                    self.except_address(un_count, driver_name, address, data, unaddr_file, browser)
                    un_count += 1
                elif data is None:
                    time.sleep(4)
                    again_data = browser.find_element_by_css_selector('textarea#target').get_attribute('value')
                    if again_data is None:
                        continue
                    elif again_data == '查無經緯度':
                        self.no_address(un_count, driver_name, address, unaddr_file, browser)
                        un_count += 1
                    else:
                        self.address(count, driver_name, address, again_data, data_list, addr_file, browser)
                        count += 1
                else:
                    self.address(count, driver_name, address, data, data_list, addr_file, browser)
                    count += 1
            except BaseException as e:
                print(str(driver_name) + ' - BaseException : \n', e)
                self.error_email(e, count, driver_name)
                print('-----------------------------------')
                print(str(driver_name) + ' - Error email sent ! Please handle with the error situation as soon as possible !')
                print('-----------------------------------')
                fail += 1
                if fail == 4:
                    break
        return count, un_count

    '''
    The DRUG function ~~~~~ use thread to realize MULTIPROCESS,
    Remember change this variable to start multithreading.
    '''

    @threads(30)
    def thread_job(self, driver_name):
        tStart = time.time()

        url = 'http://gps.uhooamber.com/address-to-lat-lng.html'
        line, address_f, unaddress_f, addr_file, unaddr_file = self.open_file(driver_name)

        '''singal procress'''
        # browser = get_web()
        browser = self.get_driver(driver_name)

        browser.get(url)
        '''*****'''
        js_execution = 'delayedLoop = function() {addressToLatLng(split[0]);}'
        browser.execute_script(js_execution)
        count, un_count = self.main_determine_job(browser, driver_name, line, addr_file, unaddr_file)

        unaddress_f.close()
        address_f.close()
        browser.quit()

        tEnd = time.time()
        print('We get ' + str(count) + ' addresses with ' + str(driver_name))
        print('We have ' + str(un_count) + ' unknowable addresses with ' + str(driver_name))
        total_time = tEnd - tStart
        day, hour, minute, second = self.calculate_time(total_time)
        # print('Total time : ' + str(tEnd-tStart) + ' seconds with ' + str(driver_name))
        print('Total time : ' + str(day) + ' days, ' + str(hour) + ' hours, ' + str(minute) + ' minutes, ' + str(second) + ' seconds with ' + str(driver_name))
        print(str(driver_name) + ' end.')
        print('Finish')
        print('-----------------------------------')


'''
This is the second method type to realize multiple threding. Why use this? Because we 

'''


class AutomaticWebMainWorkThread(threading.Thread, WebDriver, PreventMachinary):
    def __init__(self):
        threading.Thread.__init__(self)
        super(AutomaticWebMainWorkThread, self).__init__()


    def automatic_control_web(self, browser, address):
        Wait(browser, 5).until(Except.presence_of_all_elements_located((By.ID, 'source')))
        browser.find_element_by_css_selector('textarea#source').clear()
        browser.find_element_by_css_selector('textarea#source').send_keys(address.strip())
        browser.find_element_by_xpath('/html/body/p[4]/input').click()
        # if address.strip() == 'location_name':
        '''
        Because we change the function in js in source code (below line *****, roughly 500) to accelerate crawler so we can reduce the time 
        of sleep.
        '''
        time.sleep(1.0)
        data = browser.find_element_by_css_selector('textarea#target').get_attribute('value')
        '''get the data no.2 method'''
        # data = bowser.find_element_by_id('target').get_attribute('value')
        '''clear the data we want no.2 method'''
        # new_data = data.split()[0]
        return data

    '''
    Determine the data we got and save date in their csv files
    '''
    def main_determine_job(self, browser, driver_name, line, addr_file, unaddr_file):
        count = 1
        un_count = 1
        fail = 1
        data_list = []

        for address in line:
            try:
                # data = self.automatic_control_web(browser, address, count)
                data = self.automatic_control_web(browser, address)
                if '查無經緯度' in data:
                    self.no_address(un_count, driver_name, address, unaddr_file, browser)
                    un_count += 1
                elif '0,0' in data:
                    self.except_address(un_count, driver_name, address, data, unaddr_file, browser)
                    un_count += 1
                elif data is None:
                    time.sleep(4)
                    again_data = browser.find_element_by_css_selector('textarea#target').get_attribute('value')
                    if again_data is None:
                        continue
                    elif again_data == '查無經緯度':
                        self.no_address(un_count, driver_name, address, unaddr_file, browser)
                        un_count += 1
                    else:
                        self.address(count, driver_name, address, again_data, data_list, addr_file, browser)
                        count += 1
                else:
                    self.address(count, driver_name, address, data, data_list, addr_file, browser)
                    count += 1
            except BaseException as e:
                print(str(driver_name) + ' - BaseException : \n', e)
                self.error_email(e, count, driver_name)
                print('-----------------------------------')
                print(str(driver_name) + ' - Error email sent ! Please handle with the error situation as soon as possible !')
                print('-----------------------------------')
                fail += 1
                if fail == 4:
                    break
        return count, un_count


    def run(self):
        tStart = time.time()

        url = 'http://gps.uhooamber.com/address-to-lat-lng.html'
        line, address_f, unaddress_f, addr_file, unaddr_file = self.open_file(driver_name)

        '''singal procress'''
        # browser = get_web()
        browser = self.get_driver(driver_name)

        browser.get(url)
        '''*****'''
        js_execution = 'delayedLoop = function() {addressToLatLng(split[0]);}'
        browser.execute_script(js_execution)
        count, un_count = self.main_determine_job(browser, driver_name, line, addr_file, unaddr_file)

        unaddress_f.close()
        address_f.close()
        browser.quit()

        tEnd = time.time()
        print('We get ' + str(count) + ' addresses with ' + str(driver_name))
        print('We have ' + str(un_count) + ' unknowable addresses with ' + str(driver_name))
        total_time = tEnd - tStart
        day, hour, minute, second = self.calculate_time(total_time)
        # print('Total time : ' + str(tEnd-tStart) + ' seconds with ' + str(driver_name))
        print('Total time : ' + str(day) + ' days, ' + str(hour) + ' hours, ' + str(minute) + ' minutes, ' + str(second) + ' seconds with ' + str(driver_name))
        print(str(driver_name) + ' end.')
        print('Finish')
        print('-----------------------------------')


'''
Give the EntryPoint to start this program
'''
if __name__ == '__main__':
    ans = input('Do you open the authorization to let this python program send gmail ? \
                 \nIf you need assistant, you can click the url below to check this. \
                 \nThe url of Google email about authorization setting: https://myaccount.google.com/security#activity \
                 \nPlease enter any key to start this program...')
    '''
    In this variable, number of threads (number_thread) means we have to divide what number of file, and we will open 
    the number of web drivers.
    '''
    number_thread = 30

    '''
    Our file we target to do something where its path.
    '''
    target_file_path = 'The path where you target divide to smaller size file to do something conveniently.'

    '''
    Save all of file's path where it is in this list.
    The path (should be a folder is better) where save the data has been divided success and can begin to deal the data 
    to be the data we want finally.
    '''
    deal_data_file_dir = 'The path save data you got'

    deal_data = DivideData()
    deal_data.divide_data(target_file_path, number_thread, deal_data_file_dir)

    '''
    We finish and got the data we want, we save the files it should be in its path.
    '''
    finish_path_dir = 'The path save all finish data file and error message text'
    gmail_user = 'Your email user'
    gmail_password = 'Your email password'
    recipient = 'The email of recipient, if error happen, who you want to send'

    '''This is multithreading method with tomorrow package: '''

    work = AutomaticWebMainWork(finish_path=finish_path_dir,
                                gmail_user=gmail_user,
                                gmail_password=gmail_password,
                                recipient=recipient,
                                target_path_dir=deal_data_file_dir)

    '''version 1 method'''
    # web_name = ['firefox', 'chrome', 'phantomjs']
    '''version 2 method'''
    # web_name = ['chrome', 'Chrome', 'cHrome', 'chRome', 'chrOme']
    '''version 3 - No.1 method'''
    web_name = []
    for j in range(number_thread):
        web_name.append('chrome-' + str('%003d' % j))
    '''version 3 - No.2 method'''
    # web_name = [('chrome-' + str('%003d' % j)) for j in range(number_thread)]
    for i in web_name:
        work.thread_job(i)


    '''End here.'''

    '''This is the multithreading method with threading package: '''

    db_obj = SQLDataBase()
    connect_db, command_db = db_obj.connect_db()
    no_addr_table_name = 'non_address_table'
    addr_table_name = 'address_table'
    db_obj.build_table(no_addr_table_name, connect_db, command_db)
    db_obj.build_table(addr_table_name, connect_db, command_db)

    threads_list = []
    for j in range(number_thread):
        threads_list.append(AutomaticWebMainWorkThread(finish_path=finish_path_dir,
                                                       gmail_user=gmail_user,
                                                       gmail_password=gmail_password,
                                                       recipient=recipient,
                                                       target_path_dir=deal_data_file_dir))
