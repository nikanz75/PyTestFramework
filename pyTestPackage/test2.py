from selenium import webdriver
import pytest
import time
import allure

from selenium.common.exceptions import NoSuchElementException

class Test_sample:

    @pytest.fixture
    def setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="C://Users//user//Desktop//chromedriver.exe")

    @pytest.mark.run(order=5)
    def test_1(self,setup):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        print (driver.title)

    @pytest.mark.regression
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("username,password",[("Admin","admin123"),("Admin123","admin111"),("Admin111","abc111")])
    def test_login(self,username,password):
        try:
            global driver
            driver = webdriver.Chrome(executable_path="C://Users//user//Desktop//chromedriver.exe")
            driver.maximize_window()
            driver.implicitly_wait(5)
            driver.get("https://opensource-demo.orangehrmlive.com/")
            driver.find_element_by_id("txtUsername").send_keys(username)
            time.sleep(2)
            driver.find_element_by_id("txtPassword").send_keys(password)
            time.sleep(2)
            driver.find_element_by_id("btnLogin").click()
            driver.find_element_by_id("menu_admin_viewAdminModule").click()
        except NoSuchElementException as e:
            print ("Test Case Passed")
            print (e)

    @pytest.mark.regression
    @pytest.mark.run(order=2)
    def test_3(self,setup):
        driver.get("http://www.google.com")
        assert "Google" in driver.title


    def test_4(self):
        assert 10*2 == 20
        print("Run Test case 4")

    @pytest.mark.regression
    @pytest.mark.sanity
    @pytest.mark.run(order = 1)
    def test_5(self,setup):
        assert "hello" in "hello123"
        print ("Run Test case 5")

    @pytest.fixture
    def setup2(self):
        print ("Hello")

    @pytest.mark.regression
    def test_7(self,setup):
        driver.get("https://www.google.com")
        print (driver.title)





