from selenium import webdriver
from time import sleep


# Setting the Test Data into the Browser
def browser_testing(values_for_checking, expected):
    d = webdriver.Chrome()
    d.get("http://localhost:63342/tip_calc/index.html?_ijt=62v1m1na6vba8p143nbcipg429")
    d.find_element(by="id", value="billamt").send_keys(values_for_checking[0])
    d.find_element(by="xpath", value='//*[@id="serviceQual"]/option[3]').click()
    d.find_element(by="id", value="peopleamt").send_keys(values_for_checking[1])
    d.find_element(by="id", value="musicamt").send_keys(values_for_checking[2])
    d.find_element(by="id", value="calculate").click()
    sleep(2)

    # Getting the result

    actual = d.find_element(by="id", value="tip").text

    # testing the result
    if expected != actual:
        print("result test: failed")
    else:
        print("result test: success")

    # testing the UI
    is_visible = d.find_element(by="id", value="tip").is_displayed()
    if not is_visible:
        print("GUI test: failed")
    else:
        print("GUI test: success")


# Arrays of Tests
browser_testing(["100", "5", "2"], "6.00")
browser_testing(["100", "4", "1"], "6.00")
browser_testing(["100", "4", "3"], "8.00")


"""
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

# my_test(["100", "5"], "6.00")
"""