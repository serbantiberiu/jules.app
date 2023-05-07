from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

class Browser:
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    chrome.get("https://jules.app/sign-in")
    chrome.implicitly_wait(5)

def close(self):
    self.chrome.quit()