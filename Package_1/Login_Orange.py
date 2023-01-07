import time
import unittest

import self as self
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class LoginOrangeHRM(unittest.TestCase):

    # def __init__(self, methodName: str = ...):
    #     super().__init__(methodName)
    #     self.driver = None

    def setUp(self):
        serv_obj = Service("C://Users//ASUS//Wedriver_browser//Chromedriver//chromedriver_win32//chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        driver.maximize_window()

    def login(self):
        self.driver.implicitly_wait(5)
        self.username = self.driver.find_element(By.XPATH, "//input[@name='username']")
        self.username.send_keys("Admin")
        self.password = self.driver.find_element(By.XPATH, "//input[@name='password']")
        self.password.send_keys("admin123")
        self.Login_button_Click = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        self.Login_button_Click.click()
        self.assertTrue(True)

    def admin(self):
        Admin_button_Click = self.driver.find_element(By.XPATH,
                                                      "/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[1]/a[1]")
        Admin_button_Click.click()
        self.assertTrue(True)
        time.sleep(5)
        self.assertTrue(True)


if __name__ == "" "__main__":
    unittest.main()

# Current_URL = driver.current_url
# print(Current_URL)
# print(driver.title)
