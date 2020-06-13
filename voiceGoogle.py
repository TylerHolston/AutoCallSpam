from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import os

TIMEOUT_ERROR = "THERE HAS BEEN A TIMEOUT ERROR. THE XPATH HAS NOT BEEN FOUND"
TIMEOUT_CONSTANT = 10

class GoogleVoice:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.currentDir = os.getcwd()
        print(self.currentDir)

        self.driver = webdriver.Chrome(self.currentDir + '\chromedriver.exe')
        self.driver.get("https://www.google.com/")
        self.login()
    
    def login(self):
        try:
            self.driver.get("https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f")
            self.driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
            element_present = EC.presence_of_all_elements_located((By.XPATH,'//*[@id="identifierId"]'))
            WebDriverWait(self.driver,timeout=TIMEOUT_CONSTANT).until(element_present)
            self.driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(self.username)
            self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
            element_present = EC.presence_of_all_elements_located((By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input'))
            WebDriverWait(self.driver,timeout=TIMEOUT_CONSTANT).until(element_present)
            self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(self.password)
            self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
            sleep(100)
        except TimeoutException:
            print(TIMEOUT_ERROR)

        
        

if __name__ == "__main__":
    GoogleVoice("username","password")