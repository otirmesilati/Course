from selenium import webdriver
from time import sleep

from selenium.webdriver import Keys

d = webdriver.Chrome()

def my_test(values_in_check, expected):
    d.get("file:///C:/Users/otirm_2hwnj4i/Downloads/tip_calc/index.html")
    d.find_element(by="id", value="billamt").send_keys("100")
    d.find_element(by="xpath", value='//*[@id="serviceQual"]/option[3]').click()
    d.find_element(by="id", value="peopleamt").send_keys("5")
    d.find_element(by="id", value="calculate").click()
    expected = "6.00"
    actual = d.find_element(by="id", value="tip").text
    is_visible = d.find_element(by="id", value="tip").is_displayed()
    if expected != actual:
        print("different")
    else:
        print("same")
    print(is_visible)
    assert actual != expected
    assert is_visible

my_test(["100", "5"], "6.00")
