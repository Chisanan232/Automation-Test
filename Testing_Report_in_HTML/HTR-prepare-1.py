from selenium import webdriver
from unittest import TestCase
import HTMLTestRunner
import pyautogui
import unittest
import random
import time


class AutomaticTest(TestCase):
    def get_header(self):
        headers = [
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
        header = random.choice(headers)
        return header

    def get_driver(self):
        url = 'https://www.youtube.com/?gl=TW&hl=zh-tw'
        options = webdriver.ChromeOptions()
        options.add_argument('--user-agent=%s' % self.get_header())
        driver = webdriver.Chrome(chrome_options=options)
        driver.implicitly_wait(10)
        driver.get(url)
        return driver

    def operation(self, driver):
        msg = ['Alan Walker', 'Marshmallow', 'jay chou', 'pitbull', 'chainsmoker', 'flo rida']
        driver.find_element_by_name('search_query').send_keys(random.choice(msg))
        print('Program will sleep for 5 seconds to change to Automatic test GUI.')
        time.sleep(5)
        pyautogui.press('enter')
        time.sleep(5)

    def test_main(self):
        driver = self.get_driver()
        self.operation(driver)
        driver.quit()
        print('Test Finish')


if __name__ == '__main__':
    # unittest.main()
    # with open(r'D:\DataSource\PycharmProjects\KobeFirstProject\Automation_Test\Testing_Report_in_HTML\report_search.html', 'wb') as fp:
    #     runner = HTMLTestRunner.HTMLTestRunner(
    #         stream=fp,
    #         title='report_search',
    #         description=u'running case:'
    #     )
    #     runner.run(AutomaticTest('test_main'))

    testsuit = unittest.TestSuite()
    testsuit.addTest(AutomaticTest('test_main'))
    report = 'D:/DataSource/PycharmProjects/KobeFirstProject/Automation_Test/Testing_Report_in_HTML/report_search.html'
    with open(report, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title=u'report',
            description=u'Test_Report'
        )
        runner.run(testsuit)

