from pages.base_page import BasePage
from pages.locators import SbisMainPage

class MainPage(BasePage):
    def go_to_contacts_page(self):
        contact_button = self.browser.find_element(*SbisMainPage.CONTACT_BUTTON) # Находим контакты на главной странице
        contact_button.click()                                                   # Кликаем по контактам