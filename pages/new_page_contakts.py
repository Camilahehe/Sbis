from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class Contacts2Page(BasePage):
    def check_region(self):
         pagetitle = self.browser.title
         pageurl = self.browser.current_url
         assert "Камчатский край" in pagetitle, "Error"
         print("Проверка названия страницы успешно пройдена")
         get_url = self.browser.current_url
         print("Текущий URL:" + str(get_url))