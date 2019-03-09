
# 'Google Chrome' --remote-debugging-port=9222 --user-data-dir="/Users/chenpin/Downloads/package/seleium"

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from pyquery import PyQuery as pq
import time


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")


class nineVerifcation: 
    def __init__(self):
        self.url = 'http://127.0.0.1:8080' 
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get(self.url)

    def main(self):
    	doc = pq(self.driver.page_source)
    	target = doc('.box-num').text().replace('-','')
    	for item in target:
    		tapEle = self.driver.find_element_by_xpath('//ul[@class="clear"]/li[@num="{}"]'.format(item))
    		tapEle.click()
    		time.sleep(1)
    	
        
if __name__ == '__main__':
    yy = nineVerifcation()
    yy.main()
