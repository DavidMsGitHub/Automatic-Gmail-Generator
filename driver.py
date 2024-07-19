from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeService
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from password_generator import PasswordGenerator
from selenium.common.exceptions import NoSuchElementException
import time

def create_password():
    pwo = PasswordGenerator()
    pwo.maxlen = 16
    pwo.minlen = 12
    pwo.minschars = 4
    pwo.excludeschars = ",*<>^.;:_+-="
    password = pwo.generate()
    return password





class GmailGenerator:
    def __init__(self):
        chrome_driver_path = "/Users/davitmirzoevi/Desktop/chromedriver"
        service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=service)


    def get_site(self):
        self.driver.get("https://accounts.google.com/lifecycle/steps/signup/name?continue=https://mail.google.com/mail&ddm=0&dsh=S1140998823:1721374670855025&ec=GAlAFw&flowEntry=SignUp&flowName=GlifWebSignIn&hl=en&service=mail&TL=ALoj5ApMEsy3iQGNqjxDM1PuaywTgh1hTgdfUsBo8KMYyRV3WBKsitCo1Gaqw5Sl")
        time.sleep(1)
        self.driver.find_element(By.TAG_NAME, "button").click()


    def filling_info(self):
        self.driver.find_element(By.NAME, "firstName").send_keys("David")
        self.driver.find_element(By.NAME, "lastName").send_keys("Davidovich")
        self.driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(0.5)
        options = self.driver.find_elements(By.TAG_NAME, "option")
        april = options[4]
        april.click()
        self.driver.find_element(By.NAME, "day").send_keys("12")
        self.driver.find_element(By.NAME, "year").send_keys("2001")
        female = options[14]
        female.click()
        time.sleep(1.5)
        self.driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(1)
        try:
            our_mail = self.driver.find_element(By.ID, "selectionc2")
            our_mail.click()
            gmail = our_mail.text
            print(gmail)
            self.driver.find_element(By.TAG_NAME, "button").click()
        except NoSuchElementException:
            print("trying other way...")
            time.sleep(4)
            self.driver.find_element(By.NAME, "Username").send_keys("workingheromonster42")
            self.driver.find_element(By.TAG_NAME, "button").click()
        else:
            print("None of the methods worked, contact developer.")


        time.sleep(1)
        # Entering Password
        password = create_password()
        self.driver.find_element(By.NAME, "Passwd").send_keys(password)
        self.driver.find_element(By.NAME, "PasswdAgain").send_keys(password)
        self.driver.find_element(By.TAG_NAME, "button").click()

        time.sleep(200)

bot = GmailGenerator()
bot.get_site()
bot.filling_info()