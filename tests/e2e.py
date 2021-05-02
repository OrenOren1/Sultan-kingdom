from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


def test_scores_service(url):
    scorepage = webdriver.Chrome(executable_path="C:/Users/user/.selenium/chromedriver.exe")
    scorepage.get(f"{url}")
    """scorepage.get("http://127.0.0.1:5000/")"""
    scorepage.implicitly_wait(5)
    a = scorepage.find_element_by_css_selector("#score").text
    if 1 < int(a) < 1000:
        return True
    else:
        return False



def main_function(url):

    calltest = test_scores_service(url)
    if calltest is True:
        return 0
    else:
        return -1



score_page ='http://127.0.0.1:5000/'
OS_exit_code = main_function(score_page)
print(OS_exit_code)