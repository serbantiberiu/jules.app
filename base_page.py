from browser import Browser


class BasePage(Browser):

    def verifyUrl(self, url):
        actual_result = self.chrome.current_url
        assert actual_result == url, f"Fail: the expected url is {url} but the actual url is {actual_result}"
