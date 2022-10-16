import pytest
from allure_commons.model2 import Attachment
from allure_commons.types import AttachmentType
import selenium
from selenium import webdriver
import allure
import pytest

@pytest.mark.run(order=1)
def testThree(self):
        self.driver=webdriver.Chrome(executable_path="C://Users//user//Desktop//chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        a=self.driver.title
        if a == "OrangeHRM":
            print ("Passed3")
            allure.attach(self.driver.get_screenshot_as_png(),name="TestPass",attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="TestScreen",attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False
