from allure_commons.model2 import Attachment
from allure_commons.types import AttachmentType
import selenium
from selenium import webdriver
import allure
import pytest

@allure.severity(allure.severity_level.NORMAL)
class TestOneTwoThree():

    @pytest.fixture()
    def init(self):
        self.driver = webdriver.Chrome(executable_path="C://Users//user//Desktop//chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get_cookies()
        self.driver.delete_all_cookies()

    @pytest.fixture()
    def f1(self):
        print ("hello")

    def testOne(self,f1,init):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        print ("This Test Case passsed")
        a=self.driver.find_element_by_id("btnLogin").is_enabled()
        if a == True:
            assert True
            print ("Passed1")
        else:
            assert False
            print ("Failed")
            self.driver.save_screenshot("C://")
        self.driver.close()


    @pytest.mark.skip("This test case is skipped")
    def testTwo(self):
        pass

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



