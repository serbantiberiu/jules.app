from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Browser:
    chrome = webdriver.Chrome("C:\\Users\\asus\\drivers\\chromedriver_win32\\chromedriver.exe")
    chrome.maximize_window()
    chrome.get("https://jules.app")
    chrome.implicitly_wait(5)

    def close(self):
        self.chrome.quit()
