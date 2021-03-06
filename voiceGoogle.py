from selenium import webdriver
from time import sleep

class GoogleVoice:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.driver = webdriver.Chrome('./chromedriver')

        self.driver.get("https://voice.google.com/")
        self.login()
    
    def login(self):
        self.driver.find_element_by_xpath('//*[@id="header"]/div[2]/a[2]').click()
        self.driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(self.username)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span').click()
        sleep(100)

if __name__ == "__main__":
    GoogleVoice("username","password")