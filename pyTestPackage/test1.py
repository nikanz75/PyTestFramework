from selenium import webdriver
import pytest

@pytest.fixture
def nikhil():
    global driver
    driver=webdriver.Chrome(executable_path="C:\\Users\\hp\\Desktop\\chromedriver.exe")
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    print ("this is nikhil Fixture")
    yield driver
    print ("After test case in nikhil fixture")
    driver.close()

@pytest.fixture
def sumanta():
    print ("This is sumanta fixture")


def test_1(nikhil):
    print ("Hello")

@pytest.mark.run(order=1)
def test_2(sumanta):
    print ("Bye")

@pytest.mark.run(order=2)
def test_3():
    print ("This is 3rd test case")

@pytest.mark.run(order=2)
def test_4():
    print ("This is 4th test case")

#setUp -> will run before test case

#@pytest.fixture
