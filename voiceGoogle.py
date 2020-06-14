from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from os import getcwd
from textToSpeech import textToSpeech

TIMEOUT_ERROR_GOOGLE = "THERE HAS BEEN A TIMEOUT ERROR INSIDE GOOGLE SIGNUP. XPATH/NAME WAS NOT FOUND"
TIMEOUT_ERROR_VOICE = "THERE HAS BEEN A TIMEOUT ERROR INSIDE GOOGLE VOICE. XPATH WAS NOT FOUND"
TIMEOUT_CONSTANT = 10

class GoogleVoice:

    def __init__(self, username, password, phoneNumber, PhoneMessage):
        self.username = username
        self.password = password
        self.phoneNumber = phoneNumber
        self.phoneMessage = PhoneMessage
        self.currentDir = getcwd()

        #Bypass some browser-related notification/mic access errors
        option = Options()
        option.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 2,
            "profile.default_content_setting_values.geolocation": 1,
            "profile.default_content_setting_values.notifications": 1
        })
        self.driver = webdriver.Chrome(executable_path=self.currentDir + '\chromedriver.exe',options=option)
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
            element_present = EC.visibility_of_element_located((By.NAME,"password"))
            WebDriverWait(self.driver,timeout=TIMEOUT_CONSTANT).until(element_present)
            self.driver.find_element_by_name("password").send_keys(self.password)
            self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
            element_present = EC.visibility_of_element_located((By.XPATH,'//*[@id="content"]'))
            WebDriverWait(self.driver,timeout=TIMEOUT_CONSTANT).until(element_present)
            self.callManeuver()
        except TimeoutException:
            print(TIMEOUT_ERROR_GOOGLE)
            
    
    def callManeuver(self):
        try:
            self.driver.get("https://voice.google.com")
            element_present = EC.presence_of_all_elements_located((By.XPATH,'//*[@id="input_0"]'))
            WebDriverWait(self.driver,timeout=TIMEOUT_CONSTANT).until(element_present)
            self.driver.find_element_by_xpath('//*[@id="input_0"]').send_keys(self.phoneNumber)
            element_present = EC.element_to_be_clickable((By.XPATH,'//*[@id="gvPageRoot"]/div[2]/div[2]/gv-call-sidebar/div/gv-in-call/ng-transclude/gv-make-call-panel/div/div[1]/button'))
            WebDriverWait(self.driver,timeout=TIMEOUT_CONSTANT).until(element_present)
            self.driver.find_element_by_xpath('//*[@id="gvPageRoot"]/div[2]/div[2]/gv-call-sidebar/div/gv-in-call/ng-transclude/gv-make-call-panel/div/div[1]/button').click()
            self.monitorCall()
        except TimeoutException:
            print(TIMEOUT_ERROR_VOICE)
            
    def monitorCall(self):
        element_present = EC.presence_of_element_located((By.XPATH,'//*[@id="gvPageRoot"]/div[2]/div[2]/gv-call-sidebar/div/gv-in-call/div/div/div[1]/div[1]/div[1]/span[1]'))
        WebDriverWait(self.driver, timeout=TIMEOUT_CONSTANT).until(element_present)
        sleep(2)
        check=self.driver.find_element_by_xpath('//*[@id="gvPageRoot"]/div[2]/div[2]/gv-call-sidebar/div/gv-in-call/div/div/div[1]/div[1]/div[1]/span[1]').text
        check = str(check).strip()
        print(check)
        while("Calling …" == check):
            check=self.driver.find_element_by_xpath('//*[@id="gvPageRoot"]/div[2]/div[2]/gv-call-sidebar/div/gv-in-call/div/div/div[1]/div[1]/div[1]/span[1]').text
        self.playVoice()
    
    def playVoice(self):
        textToSpeech(self.phoneMessage).play()