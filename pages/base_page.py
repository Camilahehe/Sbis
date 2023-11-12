
class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def change_window(self):
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)