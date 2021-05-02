from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


def test_scores_service(url):
    scorepage = webdriver.Chrome(executable_path="C:/Users/user/.selenium/chromedriver.exe")
    scorepage.get(f"{url}")
    scorepage.implicitly_wait(5)
    a = scorepage.find_element_by_id("score").text
    if  1<int(a)<1000 :
        return True
    else :
        return False

def main_function():
    url ='http://127.0.0.1:5000/'
    a=test_scores_service(url)
    print(a)