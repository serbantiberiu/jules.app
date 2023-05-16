from selenium import webdriver


class Browser:
    chrome = webdriver.Chrome("C:\\Users\\asus\\drivers\\chromedriver_win32\\chromedriver.exe")
    chrome.maximize_window()
    chrome.implicitly_wait(5)
    chrome.get("https://www.saucedemo.com/")

    def close(self):
        self.chrome.quit()
