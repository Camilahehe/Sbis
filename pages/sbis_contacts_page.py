
from pages.base_page import BasePage
from pages.locators import SbisContactsPage
import time


class ContactsPage(BasePage):
    def go_to_tenzor_page(self):
        tenzor_button = self.browser.find_element(*SbisContactsPage.TENZOR_BUTTON)
        tenzor_button.click()

    def info_region(self):

        resp = self.browser.find_element(*SbisContactsPage.RESP_BUTTON).text
        if resp == "Республика Татарстан":
            print("Верно определилось местоположение")
        else:
            print("Ошибка")

    def info_partner(self):

        partners = self.browser.find_element(*SbisContactsPage.PARTNERS_INFO)
        assert partners != None, "Партнеры не найдены"
        print("Партнеры найдены")

    def change_region(self):

        self.browser.find_element(*SbisContactsPage.RESP_BUTTON).click()
        self.browser.find_element(*SbisContactsPage.KAMCHATKA).click()
        time.sleep(2)

