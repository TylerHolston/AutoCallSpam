from selenium import webdriver
from time import sleep
import os


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
        self.driver.get("https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f")
        self.driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
        self.driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(self.username)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(100)
        

if __name__ == "__main__":
    GoogleVoice("username","password")