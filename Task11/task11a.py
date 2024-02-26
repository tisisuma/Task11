from time import sleep

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


class Task:

    def __init__(self, url):

        self.url = url

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.action = ActionChains(self.driver)

    def booting_function(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)

            return True
        except:
            print("ERROR : Unable to run the code !")
            return False

    def shutdown(self):
        self.driver.quit()

    def draganddrop(self):
        self.driver.switch_to.frame(0)
        drag_locator = "/html/body/div[1]"
        element1 = self.driver.find_element(by=By.XPATH, value=drag_locator)
        # self.action.drag_and_drop_by_offset(element1, 100, 100).perform()
        # print("Action performed")
        drop_locator = "/html/body/div[2]"
        element2 = self.driver.find_element(by=By.XPATH, value=drop_locator)
        self.action.drag_and_drop(element1, element2).perform()
        confirmmessage = element2.text
        print(confirmmessage)


url = "https://jqueryui.com/droppable/"

execute = Task(url)
execute.booting_function()
execute.draganddrop()

execute.shutdown()
