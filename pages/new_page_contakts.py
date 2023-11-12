from pages.base_page import BasePage


class Contacts2Page(BasePage):
    def check_region(self):
         pagetitle = self.browser.title
         assert "Камчатский край" in pagetitle, "Error"
         print("Проверка названия страницы успешно пройдена")
         get_url = self.browser.current_url
         print("Текущий URL:" + str(get_url))