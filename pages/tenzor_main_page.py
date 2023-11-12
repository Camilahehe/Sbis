from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import TenzorMainPage
class TenzorPage(BasePage):
    def find_container(self):
        assert self.browser.find_element(*TenzorMainPage.STATE_PEOPLE), " Ошибка: Элемент 'Сила в людях' не найден"
        print(" Элемент 'Сила в людях' найден")

    def click_about(self):
            about = self.browser.find_element(*TenzorMainPage.ABOUT_STATE)
            self.browser.execute_script("return arguments[0].scrollIntoView(true);", about) #скроллит до нужного элемента
            about.click()

